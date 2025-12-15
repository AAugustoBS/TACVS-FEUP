# Shim model file to adapt existing generator file without modifying it
# Exposes create_gui_model() for generate_app.py

from generate_from_besser_gui import create_sample_gui_model


def create_gui_model():
    return create_sample_gui_model()

# Also expose 'gui' for broader compatibility
try:
    gui = create_sample_gui_model()
except Exception:
    pass
