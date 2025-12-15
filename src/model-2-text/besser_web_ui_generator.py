"""
BESSER Web UI Generator
Generates HTML+CSS+Vanilla JS from BESSER GUI models using Jinja2 templates
Using the official BESSER GeneratorInterface
"""

import os
from jinja2 import Environment, FileSystemLoader

try:
    # Try to import the official BESSER GeneratorInterface
    from besser.generators import GeneratorInterface
    BESSER_AVAILABLE = True
except ImportError:
    # Fallback to minimal interface if BESSER not installed
    BESSER_AVAILABLE = False
    class GeneratorInterface:
        """Minimal GeneratorInterface fallback"""
        def __init__(self, model, output_dir=None):
            self.model = model
            self.output_dir = output_dir or "./output"
        
        def build_generation_path(self, file_name):
            """Build file path for generated code"""
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            return os.path.join(self.output_dir, file_name)


class WebUIGenerator(GeneratorInterface):
    """
    WebUIGenerator is a class that implements the GeneratorInterface and is responsible
    for generating HTML+CSS+JavaScript web applications based on the BESSER GUI model.

    Args:
        model (GUIModel): An instance of the GUIModel class representing the B-UML GUI model.
        output_dir (str, optional): The output directory where the generated code will be 
            saved. Defaults to None.
    """
    
    def __init__(self, model, output_dir=None):
        super().__init__(model, output_dir)
        
        # Setup Jinja2 environment
        templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
        self.env = Environment(
            loader=FileSystemLoader(templates_path),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Add custom filters
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
        
        self.env.filters['snake_case'] = snake_case
        self.env.filters['kebab_case'] = kebab_case
        self.env.filters['camel_case'] = camel_case
        self.env.filters['pascal_case'] = pascal_case
    

    
    def generate(self, *args):
        """
        Generates HTML+CSS+JavaScript code based on the provided BESSER GUI model 
        and saves it to the specified output directory.

        Returns:
            None, but stores the generated code as files in the output directory
        """
        print("Starting Web UI generation from GUI model: " + self.model.name)
        
        # Generate HTML
        self._generate_html()
        
        # Generate CSS
        self._generate_css()
        
        # Generate JavaScript
        self._generate_javascript()
        
        # Generate additional assets
        self._generate_assets()
        
        print("Code generated successfully in: " + self.output_dir)
    
    def _generate_html(self):
        """Generate HTML file from template"""
        print("  Generating index.html...")
        
        template = self.env.get_template('index.html.j2')
        file_path = self.build_generation_path("index.html")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
    
    def _generate_css(self):
        """Generate CSS files"""
        # Create css directory
        css_dir = self.build_generation_path("css")
        if not os.path.exists(css_dir):
            os.makedirs(css_dir)
        
        # Main styles
        print("  Generating styles.css...")
        template = self.env.get_template('styles.css.j2')
        file_path = os.path.join(css_dir, "styles.css")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
        
        # Component styles
        print("  Generating components.css...")
        template = self.env.get_template('components.css.j2')
        file_path = os.path.join(css_dir, "components.css")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
    
    def _generate_javascript(self):
        """Generate JavaScript files"""
        # Create js directory
        js_dir = self.build_generation_path("js")
        if not os.path.exists(js_dir):
            os.makedirs(js_dir)
        
        # App.js
        print("  Generating app.js...")
        template = self.env.get_template('app.js.j2')
        file_path = os.path.join(js_dir, "app.js")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
        
        # Router.js
        print("  Generating router.js...")
        template = self.env.get_template('router.js.j2')
        file_path = os.path.join(js_dir, "router.js")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model, screens=self._get_screens())
            f.write(content)
        
        # Components.js
        print("  Generating components.js...")
        template = self.env.get_template('components.js.j2')
        file_path = os.path.join(js_dir, "components.js")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
        
        # API.js
        print("  Generating api.js...")
        template = self.env.get_template('api.js.j2')
        file_path = os.path.join(js_dir, "api.js")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
            f.write(content)
        
        # Generate page-specific JavaScript
        pages_dir = os.path.join(js_dir, "pages")
        if not os.path.exists(pages_dir):
            os.makedirs(pages_dir)
        
        screens = self._get_screens()
        for screen in screens:
            filename = screen.name.lower() + ".js"
            print("  Generating " + filename + "...")
            template = self.env.get_template('page.js.j2')
            file_path = os.path.join(pages_dir, filename)
            
            with open(file_path, mode="w", encoding='utf-8') as f:
                content = template.render(screen=screen, gui=self.model)
                f.write(content)
    
    def _generate_assets(self):
        """Generate additional assets like README and gitignore"""
        # README.md
        print("  Generating README.md...")
        template = self.env.get_template('README.md.j2')
        file_path = self.build_generation_path("README.md")
        
        with open(file_path, mode="w", encoding='utf-8') as f:
            content = template.render(gui=self.model)
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
        file_path = self.build_generation_path(".gitignore")
        with open(file_path, mode="w", encoding='utf-8') as f:
            f.write(gitignore_content)
    
    def _get_screens(self):
        """Extract all screens from the GUI model"""
        screens = []
        if hasattr(self.model, 'modules'):
            for module in self.model.modules:
                if hasattr(module, 'screens'):
                    screens.extend(module.screens)
        return screens
