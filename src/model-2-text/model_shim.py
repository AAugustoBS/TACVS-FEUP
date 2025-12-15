import sys
import types


def _ensure_besser_stub():
    if 'besser' in sys.modules:
        return

    besser = types.ModuleType('besser')
    BUML = types.ModuleType('besser.BUML')
    metamodel = types.ModuleType('besser.BUML.metamodel')
    gui_mod = types.ModuleType('besser.BUML.metamodel.gui')

    class _Base(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    class GUIModel(_Base):
        pass

    class Module(_Base):
        pass

    class Screen(_Base):
        pass

    class Button(_Base):
        pass

    class InputField(_Base):
        pass

    class DataList(_Base):
        pass

    class DataSourceElement(_Base):
        pass

    class ViewComponent(_Base):
        pass

    class ButtonType:
        TextButton = 'TextButton'
        RaisedButton = 'RaisedButton'
        IconButton = 'IconButton'

    class ButtonActionType:
        Navigate = 'Navigate'
        OpenForm = 'OpenForm'

    class InputFieldType:
        Text = 'Text'
        Number = 'Number'
        Date = 'Date'
        Search = 'Search'

    gui_mod.GUIModel = GUIModel
    gui_mod.Module = Module
    gui_mod.Screen = Screen
    gui_mod.Button = Button
    gui_mod.InputField = InputField
    gui_mod.DataList = DataList
    gui_mod.DataSourceElement = DataSourceElement
    gui_mod.ViewComponent = ViewComponent
    gui_mod.ButtonType = ButtonType
    gui_mod.ButtonActionType = ButtonActionType
    gui_mod.InputFieldType = InputFieldType

    sys.modules['besser'] = besser
    sys.modules['besser.BUML'] = BUML
    sys.modules['besser.BUML.metamodel'] = metamodel
    sys.modules['besser.BUML.metamodel.gui'] = gui_mod


def _to_local_gui(stub_gui):
    from gui_model import GUIModel as LocalGUIModel, Module as LocalModule, Screen as LocalScreen

    name = getattr(stub_gui, 'name', 'App')
    package = getattr(stub_gui, 'package', 'com.example.app')
    versionCode = getattr(stub_gui, 'versionCode', '1')
    versionName = getattr(stub_gui, 'versionName', '1.0')
    description = getattr(stub_gui, 'description', '')
    screenCompatibility = getattr(stub_gui, 'screenCompatibility', True)

    local_modules = set()
    for m in getattr(stub_gui, 'modules', set()):
        local_screens = set()
        for s in getattr(m, 'screens', set()):
            local_screens.add(LocalScreen(
                name=getattr(s, 'name', 'Screen'),
                is_main_page=getattr(s, 'is_main_page', False)
            ))
        local_modules.add(LocalModule(name=getattr(m, 'name', 'Module'), screens=local_screens))

    return LocalGUIModel(
        name=name,
        package=package,
        versionCode=versionCode,
        versionName=versionName,
        description=description,
        screenCompatibility=screenCompatibility,
        modules=local_modules,
    )


def create_gui_model():
    _ensure_besser_stub()
    import importlib
    mod = importlib.import_module('generate_from_besser_gui')

    if hasattr(mod, 'create_sample_gui_model'):
        stub_gui = mod.create_sample_gui_model()
    elif hasattr(mod, 'build_generated_gui_model'):
        stub_gui = mod.build_generated_gui_model()
    elif hasattr(mod, 'community_gui_model'):
        stub_gui = mod.community_gui_model
    else:
        raise AttributeError("generate_from_besser_gui.py must define 'build_generated_gui_model()', 'create_sample_gui_model()', or 'community_gui_model'")

    return _to_local_gui(stub_gui)


# Optional: expose 'gui' lazily only if accessed via create_gui_model()
# Keep module lightweight to avoid import-time errors
