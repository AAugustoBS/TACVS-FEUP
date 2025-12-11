"""
GUI Metamodel Extension for BESSER
Extends BESSER's structural metamodel with GUI-specific elements
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class GUITheme:
    """Represents GUI theme configuration"""
    primary_color: str = "#2196F3"
    secondary_color: str = "#FFC107"
    logo_url: str = ""
    
    def to_css_vars(self) -> Dict[str, str]:
        """Convert theme to CSS custom properties"""
        return {
            '--primary-color': self.primary_color,
            '--secondary-color': self.secondary_color
        }


@dataclass
class GUIComponent:
    """Base class for GUI components"""
    id: str
    html_id: str
    type: str
    order: int
    attributes: Dict = field(default_factory=dict)
    
    def get_html_class(self) -> str:
        """Get CSS class for component"""
        return f"component-{self.type.lower()}"


@dataclass
class ListView(GUIComponent):
    """List view component for displaying collections"""
    entity: str = "Item"
    show_image: bool = True
    show_price: bool = True
    show_location: bool = False
    show_rating: bool = False
    
    def __post_init__(self):
        self.type = "ListView"
    
    def get_visible_fields(self) -> List[str]:
        """Get list of fields to display"""
        fields = []
        if self.show_image:
            fields.append('image')
        if self.show_price:
            fields.append('price')
        if self.show_location:
            fields.append('location')
        if self.show_rating:
            fields.append('rating')
        return fields


@dataclass
class DetailView(GUIComponent):
    """Detail view component for displaying single entity"""
    entity: str = "Item"
    
    def __post_init__(self):
        self.type = "DetailView"


@dataclass
class ActionButton(GUIComponent):
    """Action button component"""
    label: str = "Action"
    icon: str = ""
    action_type: str = "NAVIGATE"
    target_path: str = ""
    
    def __post_init__(self):
        self.type = "ActionButton"
    
    def get_action_handler(self) -> str:
        """Get JavaScript action handler name"""
        if self.action_type == "NAVIGATE":
            return "navigateTo"
        elif self.action_type == "SUBMIT":
            return "submitForm"
        return "handleAction"


@dataclass
class ChatComponent(GUIComponent):
    """Chat component for messaging"""
    conversation_id: str = ""
    
    def __post_init__(self):
        self.type = "ChatComponent"


@dataclass
class GUIScreen:
    """Represents a screen/page in the application"""
    id: str
    name: str
    path: str
    type: str
    title: str
    components: List[GUIComponent] = field(default_factory=list)
    
    def get_route_params(self) -> List[str]:
        """Extract route parameters from path"""
        import re
        return re.findall(r':(\w+)', self.path)
    
    def get_page_filename(self) -> str:
        """Get filename for page JavaScript file"""
        return f"{self.name.lower()}.js"
    
    def has_component_type(self, comp_type: str) -> bool:
        """Check if screen has a component of specific type"""
        return any(comp.type == comp_type for comp in self.components)


@dataclass
class GUIApplication:
    """Represents the complete GUI application"""
    app_name: str
    theme: Optional[GUITheme] = None
    screens: List[GUIScreen] = field(default_factory=list)
    
    def get_routes(self) -> List[Dict[str, str]]:
        """Get all routes for the router"""
        return [
            {
                'path': screen.path,
                'name': screen.name,
                'title': screen.title,
                'handler': f"{screen.name.lower()}Page"
            }
            for screen in self.screens
        ]
    
    def get_app_filename(self) -> str:
        """Get safe filename for application"""
        return self.app_name.lower().replace(' ', '-')
    
    def get_home_screen(self) -> Optional[GUIScreen]:
        """Get home/landing screen"""
        home_screens = [s for s in self.screens if s.type == "HOME" or s.path == "/"]
        return home_screens[0] if home_screens else None


def component_factory(comp_data: Dict) -> GUIComponent:
    """Factory function to create appropriate component instance"""
    comp_type = comp_data.get('type', 'Component')
    
    if comp_type == 'ListView':
        return ListView(
            id=comp_data.get('id', ''),
            html_id=comp_data.get('htmlId', ''),
            type=comp_type,
            order=comp_data.get('order', 0),
            entity=comp_data.get('entity', 'Item'),
            show_image=comp_data.get('showImage', True),
            show_price=comp_data.get('showPrice', True),
            show_location=comp_data.get('showLocation', False),
            show_rating=comp_data.get('showRating', False),
            attributes=comp_data.get('attributes', {})
        )
    elif comp_type == 'DetailView':
        return DetailView(
            id=comp_data.get('id', ''),
            html_id=comp_data.get('htmlId', ''),
            type=comp_type,
            order=comp_data.get('order', 0),
            entity=comp_data.get('entity', 'Item'),
            attributes=comp_data.get('attributes', {})
        )
    elif comp_type == 'ActionButton':
        return ActionButton(
            id=comp_data.get('id', ''),
            html_id=comp_data.get('htmlId', ''),
            type=comp_type,
            order=comp_data.get('order', 0),
            label=comp_data.get('label', 'Action'),
            icon=comp_data.get('icon', ''),
            action_type=comp_data.get('actionType', 'NAVIGATE'),
            target_path=comp_data.get('targetPath', ''),
            attributes=comp_data.get('attributes', {})
        )
    elif comp_type == 'ChatComponent':
        return ChatComponent(
            id=comp_data.get('id', ''),
            html_id=comp_data.get('htmlId', ''),
            type=comp_type,
            order=comp_data.get('order', 0),
            attributes=comp_data.get('attributes', {})
        )
    else:
        return GUIComponent(
            id=comp_data.get('id', ''),
            html_id=comp_data.get('htmlId', ''),
            type=comp_type,
            order=comp_data.get('order', 0),
            attributes=comp_data.get('attributes', {})
        )


def build_gui_application(gui_data: Dict) -> GUIApplication:
    """Build GUIApplication object from extracted data"""
    # Create theme
    theme = None
    if gui_data.get('theme'):
        theme_data = gui_data['theme']
        theme = GUITheme(
            primary_color=theme_data.get('primaryColor', '#2196F3'),
            secondary_color=theme_data.get('secondaryColor', '#FFC107'),
            logo_url=theme_data.get('logoUrl', '')
        )
    
    # Create screens with components
    screens = []
    for screen_data in gui_data.get('screens', []):
        components = [component_factory(comp) for comp in screen_data.get('components', [])]
        
        screen = GUIScreen(
            id=screen_data.get('id', ''),
            name=screen_data.get('name', 'Screen'),
            path=screen_data.get('path', '/'),
            type=screen_data.get('type', 'DEFAULT'),
            title=screen_data.get('title', 'Page'),
            components=components
        )
        screens.append(screen)
    
    # Create application
    app = GUIApplication(
        app_name=gui_data.get('appName', 'WebApp'),
        theme=theme,
        screens=screens
    )
    
    return app
