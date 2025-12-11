"""
Web UI Generator extending BESSER CodeGenerator
Generates HTML+CSS+Vanilla JS from GUI models using Jinja2 templates
"""

import os
from pathlib import Path
from typing import Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape

from besser.generators import CodeGenerator

from gui_metamodel import GUIApplication, build_gui_application
from xml_to_buml import XMLToBAMLConverter


class WebUIGenerator(CodeGenerator):
    """
    BESSER Code Generator for Web UI (HTML+CSS+Vanilla JS)
    Extends BESSER's CodeGenerator to leverage the framework's infrastructure
    """
    
    def __init__(self, model_path: str, output_dir: str = "./output"):
        """
        Initialize the Web UI Generator
        
        Args:
            model_path: Path to XML GUI model file
            output_dir: Output directory for generated code
        """
        # BESSER CodeGenerator initialization
        super().__init__(model=None, output_dir=output_dir)
        
        self.model_path = model_path
        self.gui_app: Optional[GUIApplication] = None
        
        # Setup Jinja2 environment
        template_dir = Path(__file__).parent / "templates"
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Add custom Jinja2 filters
        self._register_filters()
    
    def _register_filters(self):
        """Register custom Jinja2 filters"""
        
        def snake_case(text: str) -> str:
            """Convert text to snake_case"""
            import re
            text = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
        
        def kebab_case(text: str) -> str:
            """Convert text to kebab-case"""
            return snake_case(text).replace('_', '-')
        
        def camel_case(text: str) -> str:
            """Convert text to camelCase"""
            words = text.replace('-', '_').split('_')
            return words[0].lower() + ''.join(w.capitalize() for w in words[1:])
        
        def pascal_case(text: str) -> str:
            """Convert text to PascalCase"""
            words = text.replace('-', '_').split('_')
            return ''.join(w.capitalize() for w in words)
        
        self.jinja_env.filters['snake_case'] = snake_case
        self.jinja_env.filters['kebab_case'] = kebab_case
        self.jinja_env.filters['camel_case'] = camel_case
        self.jinja_env.filters['pascal_case'] = pascal_case
    
    def generate(self):
        """
        Main generation method (BESSER CodeGenerator interface)
        Orchestrates the complete code generation process
        """
        print(f"🚀 Starting Web UI generation from {self.model_path}")
        
        # Step 1: Convert XML to B-UML and extract GUI data
        print("📦 Converting XML to BESSER B-UML model...")
        converter = XMLToBAMLConverter(self.model_path)
        buml_model, gui_data = converter.convert()
        self.model = buml_model  # Set BESSER model
        
        # Step 2: Build GUI application object
        print("🏗️  Building GUI application structure...")
        self.gui_app = build_gui_application(gui_data)
        
        # Step 3: Generate code files
        print("✨ Generating web application files...")
        self._generate_html()
        self._generate_css()
        self._generate_javascript()
        self._generate_assets()
        
        print(f"✅ Generation complete! Output in {self.output_dir}")
    
    def _generate_html(self):
        """Generate HTML files"""
        print("  📄 Generating index.html...")
        
        template = self.jinja_env.get_template('index.html.j2')
        content = template.render(app=self.gui_app)
        
        output_path = Path(self.output_dir) / "index.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
    
    def _generate_css(self):
        """Generate CSS files"""
        css_dir = Path(self.output_dir) / "css"
        css_dir.mkdir(parents=True, exist_ok=True)
        
        # Main styles
        print("  🎨 Generating styles.css...")
        template = self.jinja_env.get_template('styles.css.j2')
        content = template.render(app=self.gui_app)
        (css_dir / "styles.css").write_text(content, encoding='utf-8')
        
        # Component styles
        print("  🎨 Generating components.css...")
        template = self.jinja_env.get_template('components.css.j2')
        content = template.render(app=self.gui_app)
        (css_dir / "components.css").write_text(content, encoding='utf-8')
    
    def _generate_javascript(self):
        """Generate JavaScript files"""
        js_dir = Path(self.output_dir) / "js"
        js_dir.mkdir(parents=True, exist_ok=True)
        
        # Main app.js
        print("  ⚡ Generating app.js...")
        template = self.jinja_env.get_template('app.js.j2')
        content = template.render(app=self.gui_app)
        (js_dir / "app.js").write_text(content, encoding='utf-8')
        
        # Router
        print("  🗺️  Generating router.js...")
        template = self.jinja_env.get_template('router.js.j2')
        content = template.render(app=self.gui_app)
        (js_dir / "router.js").write_text(content, encoding='utf-8')
        
        # Components
        print("  🧩 Generating components.js...")
        template = self.jinja_env.get_template('components.js.j2')
        content = template.render(app=self.gui_app)
        (js_dir / "components.js").write_text(content, encoding='utf-8')
        
        # API service
        print("  🌐 Generating api.js...")
        template = self.jinja_env.get_template('api.js.j2')
        content = template.render(app=self.gui_app)
        (js_dir / "api.js").write_text(content, encoding='utf-8')
        
        # Page-specific JavaScript
        pages_dir = js_dir / "pages"
        pages_dir.mkdir(parents=True, exist_ok=True)
        
        for screen in self.gui_app.screens:
            print(f"  📃 Generating {screen.get_page_filename()}...")
            template = self.jinja_env.get_template('page.js.j2')
            content = template.render(screen=screen, app=self.gui_app)
            (pages_dir / screen.get_page_filename()).write_text(content, encoding='utf-8')
    
    def _generate_assets(self):
        """Generate additional assets and configuration files"""
        # README
        print("  📖 Generating README.md...")
        template = self.jinja_env.get_template('README.md.j2')
        content = template.render(app=self.gui_app)
        (Path(self.output_dir) / "README.md").write_text(content, encoding='utf-8')
        
        # .gitignore
        print("  🙈 Generating .gitignore...")
        gitignore_content = """# Dependencies
node_modules/

# Environment
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Build
dist/
build/
"""
        (Path(self.output_dir) / ".gitignore").write_text(gitignore_content, encoding='utf-8')


# Convenience function for direct usage
def generate_web_ui(xml_model_path: str, output_dir: str = "./output"):
    """
    Generate web UI from XML GUI model
    
    Args:
        xml_model_path: Path to XML GUI model file
        output_dir: Output directory for generated files
    """
    generator = WebUIGenerator(model_path=xml_model_path, output_dir=output_dir)
    generator.generate()
    return generator
