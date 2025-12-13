# -*- coding: utf-8 -*-
"""
BESSER Web UI Generator - Main Script
Template-Based Model-to-Text Generator using BESSER Framework + Jinja2

Usage:
    python generate.py <path_to_xml_model> [output_directory]

Example:
    python generate.py ../example.gui.xmi ./output/ballet-swap
"""

from __future__ import print_function
import sys
import os

# Add current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from web_ui_generator import WebUIGenerator


def print_banner():
    """Print generator banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║           BESSER Web UI Generator                         ║
    ║           Model-to-Text with Jinja2                       ║
    ║                                                           ║
    ║           Generate HTML+CSS+Vanilla JS                    ║
    ║           from DSML GUI Models                            ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_usage():
    """Print usage instructions"""
    usage = """
    Usage:
        python generate.py <path_to_xml_model> [output_directory]
    
    Arguments:
        path_to_xml_model    Path to XML/XMI GUI model file (required)
        output_directory     Output directory for generated code (optional)
                            Default: ./output
    
    Examples:
        python generate.py example.gui.xmi
        python generate.py ../models/app.xmi ./generated/app
        python generate.py C:/models/gui.xmi C:/output/webapp
    
    The generator will create:
        - index.html          Main HTML file
        - css/                Stylesheets
        - js/                 JavaScript modules
        - README.md           Documentation
    """
    print(usage)


def validate_model_file(model_path):
    """Validate that model file exists and has correct extension"""
    if not os.path.exists(model_path):
        print("Error: Model file not found: " + model_path)
        return False
    
    if not model_path.endswith(('.xml', '.xmi')):
        print("Warning: Model file should have .xml or .xmi extension")
        try:
            response = raw_input("Continue anyway? (y/n): ")
        except NameError:
            response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return False
    
    return True


def main():
    """Main entry point"""
    print_banner()
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Error: Missing required argument")
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)
    
    model_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output"
    
    # Validate model file
    if not validate_model_file(model_path):
        sys.exit(1)
    
    # Print configuration
    print("Configuration:")
    print("   Model:  " + os.path.abspath(model_path))
    print("   Output: " + os.path.abspath(output_dir))
    print()
    
    # Confirm generation
    try:
        response = raw_input("Start generation? (y/n): ")
    except NameError:
        response = input("Start generation? (y/n): ")
    if response.lower() != 'y':
        print("Generation cancelled")
        sys.exit(0)
    
    print()
    
    try:
        # Run generator
        generator = WebUIGenerator(
            model_path=model_path,
            output_dir=output_dir
        )
        generator.generate()
        
        print()
        print("=" * 60)
        print("Generation completed successfully!")
        print("=" * 60)
        print()
        print("Generated files in: " + os.path.abspath(output_dir))
        print()
        print("Next steps:")
        print("   1. cd " + output_dir)
        print("   2. python -m http.server 8000")
        print("   3. Open http://localhost:8000 in your browser")
        print()
        print("Read README.md for more information")
        print()
        
    except Exception as e:
        print()
        print("=" * 60)
        print("Generation failed!")
        print("=" * 60)
        print()
        print("Error: " + str(e))
        print()
        
        import traceback
        print("Traceback:")
        traceback.print_exc()
        
        sys.exit(1)


if __name__ == "__main__":
    main()
