"""
GUI Model Classes (Pure Python)
Dataclasses for representing GUI models without BESSER dependency
"""

from dataclasses import dataclass, field
from typing import Set, Optional


@dataclass
class Screen:
    """Represents a screen in the GUI"""
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
    """Represents a module containing screens"""
    name: str
    screens: Set[Screen] = field(default_factory=set)
    
    def __hash__(self):
        return hash(self.name)


@dataclass
class GUIModel:
    """Represents the complete GUI application model"""
    name: str
    package: str
    versionCode: str
    versionName: str
    description: str = ""
    screenCompatibility: bool = True
    modules: Set[Module] = field(default_factory=set)
    
    def get_all_screens(self):
        """Get all screens from all modules"""
        screens = []
        for module in self.modules:
            screens.extend(module.screens)
        return screens
