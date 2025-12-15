"""
Generate Web UI from a user-provided .py model file.
The .py must define either:
 - variable: gui (instance of GUIModel), or
 - function: create_model() returning GUIModel
"""

import os
import sys

from besser_web_ui_generator import WebUIGenerator

try:
    # Try to import from BESSER if installed
    from besser.BUML.metamodel.gui import GUIModel as BESSERGUIModel
    GUIModel = BESSERGUIModel
    USING_BESSER = True
except ImportError:
    # Fallback to local gui_model
    from gui_model import GUIModel
    USING_BESSER = False


def _load_module_py2(py_path, module_name):
    # Fallback loader for Python 2
    import imp
    with open(py_path, 'r') as f:
        return imp.load_source(module_name, py_path, f)


def _load_module(py_path):
    # Prefer Python 3 importlib.util when available
    try:
        import importlib.util
        module_name = os.path.splitext(os.path.basename(py_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, py_path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        return module
    except Exception:
        # Fallback to Python 2 loader
        module_name = os.path.splitext(os.path.basename(py_path))[0]
        return _load_module_py2(py_path, module_name)


def load_model(py_path):
    if not os.path.exists(py_path):
        raise IOError("Model file not found: " + py_path)

    module = _load_module(py_path)

    # 1) Direct variable 'gui'
    if hasattr(module, 'gui') and isinstance(module.gui, GUIModel):
        print("✓ Found 'gui' variable")
        return module.gui
    
    # 2) Direct variable 'community_gui_model' (from M2M output)
    if hasattr(module, 'community_gui_model'):
        model = module.community_gui_model
        if isinstance(model, GUIModel):
            print("✓ Found 'community_gui_model' variable")
            return model
    
    # 3) Function 'build_generated_gui_model()' (from M2M output)
    if hasattr(module, 'build_generated_gui_model'):
        model = module.build_generated_gui_model()
        if isinstance(model, GUIModel):
            print("✓ Built model from 'build_generated_gui_model()'")
            return model
        raise TypeError("build_generated_gui_model() did not return GUIModel")
    
    # 4) Factory 'create_model()'
    if hasattr(module, 'create_model'):
        model = module.create_model()
        if isinstance(model, GUIModel):
            print("✓ Built model from 'create_model()'")
            return model
        raise TypeError("create_model() did not return GUIModel")
    
    # 5) Common sample factory 'create_sample_gui_model()'
    if hasattr(module, 'create_sample_gui_model'):
        model = module.create_sample_gui_model()
        if isinstance(model, GUIModel):
            print("✓ Built model from 'create_sample_gui_model()'")
            return model
        raise TypeError("create_sample_gui_model() did not return GUIModel")
    
    # 6) Alternate factory name 'create_gui_model()'
    if hasattr(module, 'create_gui_model'):
        model = module.create_gui_model()
        if isinstance(model, GUIModel):
            print("✓ Built model from 'create_gui_model()'")
            return model
        raise TypeError("create_gui_model() did not return GUIModel")

    raise AttributeError("Model file must define one of: 'gui', 'community_gui_model', 'build_generated_gui_model()', 'create_model()', 'create_sample_gui_model()', 'create_gui_model()' returning GUIModel")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_app.py <path_to_model.py> [output_dir]")
        if USING_BESSER:
            print("Using BESSER GUI metamodel classes")
        else:
            print("Using local GUI model classes (BESSER not found)")
        sys.exit(1)

    model_py = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output_besser"

    print("Loading model from:", model_py)
    if USING_BESSER:
        print("✓ Using official BESSER framework")
    
    gui_model = load_model(model_py)

    # Ensure features dict exists (for template compatibility)
    if not hasattr(gui_model, 'features'):
        gui_model.features = {}
    
    # Defaults for features if missing
    if not gui_model.features:
        gui_model.features = {
            'show_mbway': True,
            'show_multibanco': True,
            'show_logout': True,
            'show_profile': True
        }
    else:
        # Fill in missing features
        gui_model.features.setdefault('show_mbway', True)
        gui_model.features.setdefault('show_multibanco', True)
        gui_model.features.setdefault('show_logout', True)
        gui_model.features.setdefault('show_profile', True)
    
    # Ensure theme dict exists
    if not hasattr(gui_model, 'theme'):
        gui_model.theme = {}

    generator = WebUIGenerator(model=gui_model, output_dir=output_dir)
    generator.generate()
    print("\n✓ Website ready at:", output_dir)


if __name__ == '__main__':
    main()
