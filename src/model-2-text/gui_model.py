"""
GUI Model Classes (Pure Python)
Dataclasses for representing GUI models without BESSER dependency
"""

"""GUI model with Python 2/3 compatibility.
Tries to use dataclasses (Python 3.7+). Falls back to classic classes for Python 2.
"""

try:
    from dataclasses import dataclass, field
    from typing import Set, Dict

    @dataclass
    class Screen:
        name: str
        x_dpi: str = "xdpi"
        y_dpi: str = "ydpi"
        screen_size: str = "Medium"
        view_elements: Set = field(default_factory=set)
        is_main_page: bool = False

        def __hash__(self):
            return hash(self.name)

    @dataclass
    class Module:
        name: str
        screens: Set[Screen] = field(default_factory=set)

        def __hash__(self):
            return hash(self.name)

    @dataclass
    class GUIModel:
        name: str
        package: str
        versionCode: str
        versionName: str
        description: str = ""
        screenCompatibility: bool = True
        modules: Set[Module] = field(default_factory=set)
        features: Dict[str, bool] = field(default_factory=dict)
        theme: Dict[str, str] = field(default_factory=dict)

        def get_all_screens(self):
            screens = []
            for module in self.modules:
                screens.extend(module.screens)
            return screens

except Exception:
    # Python 2 fallback without dataclasses/typing
    class Screen(object):
        def __init__(self, name, x_dpi="xdpi", y_dpi="ydpi", screen_size="Medium", view_elements=None, is_main_page=False):
            self.name = name
            self.x_dpi = x_dpi
            self.y_dpi = y_dpi
            self.screen_size = screen_size
            self.view_elements = view_elements or set()
            self.is_main_page = is_main_page

        def __hash__(self):
            return hash(self.name)

    class Module(object):
        def __init__(self, name, screens=None):
            self.name = name
            self.screens = screens or set()

        def __hash__(self):
            return hash(self.name)

    class GUIModel(object):
        def __init__(self, name, package, versionCode, versionName, description="", screenCompatibility=True, modules=None, features=None, theme=None):
            self.name = name
            self.package = package
            self.versionCode = versionCode
            self.versionName = versionName
            self.description = description
            self.screenCompatibility = screenCompatibility
            self.modules = modules or set()
            self.features = features or {}
            self.theme = theme or {}

        def get_all_screens(self):
            screens = []
            for module in self.modules:
                screens.extend(list(module.screens))
            return screens
