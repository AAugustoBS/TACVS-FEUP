"""
Web UI Generator extending BESSER CodeGenerator
Generates HTML+CSS+Vanilla JS from GUI models using Jinja2 templates
"""

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

# BESSER-inspired base class (no external dependency needed)
class CodeGenerator:
    """Base code generator class inspired by BESSER framework"""
    def __init__(self, model=None, output_dir="./output"):
        self.model = model
        self.output_dir = output_dir
    
    def generate(self):
        """Override this method in subclasses"""
        raise NotImplementedError("Subclasses must implement generate()")


from gui_metamodel import GUIApplication, build_gui_application
from xml_to_buml import XMLToBAMLConverter


class WebUIGenerator(CodeGenerator):
    """
    BESSER Code Generator for Web UI (HTML+CSS+Vanilla JS)
    Extends BESSER's CodeGenerator to leverage the framework's infrastructure
    """
    
    def __init__(self, model_path, output_dir="./output"):
        """
        Initialize the Web UI Generator
        
        Args:
            model_path: Path to XML GUI model file
            output_dir: Output directory for generated code
        """
        # BESSER CodeGenerator initialization
        super(WebUIGenerator, self).__init__(model=None, output_dir=output_dir)
        
        self.model_path = model_path
        self.gui_app = None
        
        # Setup Jinja2 environment
        template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Add custom Jinja2 filters
        self._register_filters()
    
    def _register_filters(self):
        """Register custom Jinja2 filters"""
        
        def snake_case(text):
            """Convert text to snake_case"""
            import re
            text = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
        
        def kebab_case(text):
            """Convert text to kebab-case"""
            return snake_case(text).replace('_', '-')
        
        def camel_case(text):
            """Convert text to camelCase"""
            words = text.replace('-', '_').split('_')
            return words[0].lower() + ''.join(w.capitalize() for w in words[1:])
        
        def pascal_case(text):
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
        print("Starting Web UI generation from " + self.model_path)
        
        # Step 1: Convert XML to B-UML and extract GUI data
        print("Converting XML to BESSER B-UML model...")
        converter = XMLToBAMLConverter(self.model_path)
        buml_model, gui_data = converter.convert()
        self.model = buml_model  # Set BESSER model
        
        # Step 2: Build GUI application object
        print("Building GUI application structure...")
        self.gui_app = build_gui_application(gui_data)
        
        # Step 3: Generate code files
        print("Generating web application files...")
        self._generate_html()
        self._generate_css()
        self._generate_javascript()
        self._generate_assets()
        
        print("Generation complete! Output in " + self.output_dir)
    
    def _generate_html(self):
        """Generate HTML files"""
        print("  Generating index.html...")
        
        template = self.jinja_env.get_template('index.html.j2')
        content = template.render(app=self.gui_app)
        
        output_path = os.path.join(self.output_dir, "index.html")
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else self.output_dir, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(content)
    
    def _generate_css(self):
        """Generate CSS files"""
        css_dir = os.path.join(self.output_dir, "css")
        if not os.path.exists(css_dir):
            os.makedirs(css_dir)
        
        # Main styles
        print("  Generating styles.css...")
        template = self.jinja_env.get_template('styles.css.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(css_dir, "styles.css"), 'w') as f:
            f.write(content)
        
        # Component styles
        print("  Generating components.css...")
        template = self.jinja_env.get_template('components.css.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(css_dir, "components.css"), 'w') as f:
            f.write(content)
    
    def _generate_javascript(self):
        """Generate JavaScript files"""
        js_dir = os.path.join(self.output_dir, "js")
        if not os.path.exists(js_dir):
            os.makedirs(js_dir)
        
        # Main app.js
        print("  Generating app.js...")
        template = self.jinja_env.get_template('app.js.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(js_dir, "app.js"), 'w') as f:
            f.write(content)
        
        # Router
        print("  Generating router.js...")
        template = self.jinja_env.get_template('router.js.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(js_dir, "router.js"), 'w') as f:
            f.write(content)
        
        # Components
        print("  Generating components.js...")
        template = self.jinja_env.get_template('components.js.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(js_dir, "components.js"), 'w') as f:
            f.write(content)
        
        # API service
        print("  Generating api.js...")
        template = self.jinja_env.get_template('api.js.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(js_dir, "api.js"), 'w') as f:
            f.write(content)
        
        # Page-specific JavaScript
        pages_dir = os.path.join(js_dir, "pages")
        if not os.path.exists(pages_dir):
            os.makedirs(pages_dir)
        
        for screen in self.gui_app.screens:
            print("  Generating " + screen.get_page_filename() + "...")
            template = self.jinja_env.get_template('page.js.j2')
            content = template.render(screen=screen, app=self.gui_app)
            with open(os.path.join(pages_dir, screen.get_page_filename()), 'w') as f:
                f.write(content)
    
    def _generate_assets(self):
        """Generate additional assets and configuration files"""
        # README
        print("  Generating README.md...")
        template = self.jinja_env.get_template('README.md.j2')
        content = template.render(app=self.gui_app)
        with open(os.path.join(self.output_dir, "README.md"), 'w') as f:
            f.write(content)
        
        # .gitignore
        print("  Generating .gitignore...")
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
        with open(os.path.join(self.output_dir, ".gitignore"), 'w') as f:
            f.write(gitignore_content)


# Convenience function for direct usage
def generate_web_ui(xml_model_path, output_dir="./output"):
    """
    Generate web UI from XML GUI model
    
    Args:
        xml_model_path: Path to XML GUI model file
        output_dir: Output directory for generated files
    """
    generator = WebUIGenerator(model_path=xml_model_path, output_dir=output_dir)
    generator.generate()
    return generator
