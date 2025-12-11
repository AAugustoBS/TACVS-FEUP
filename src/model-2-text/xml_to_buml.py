"""
XML GUI Model to BESSER B-UML Converter
Converts XML/XMI GUI models to BESSER's B-UML structural metamodel
"""

import xml.etree.ElementTree as ET
from typing import Dict, List, Optional
from besser.BUML.metamodel.structural import DomainModel, Class, Property, PrimitiveDataType


class XMLToBAMLConverter:
    """Converts XML GUI model to BESSER B-UML Domain Model"""
    
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        self.namespaces = {
            'xmi': 'http://www.omg.org/XMI',
            'gui': 'http://www.example.org/gui'
        }
        
    def convert(self) -> DomainModel:
        """Convert XML GUI model to B-UML Domain Model"""
        app_name = self.root.get('appName', 'WebApp')
        model = DomainModel(name=f"{app_name}_Model")
        
        # Extract GUI structure
        gui_data = self._extract_gui_structure()
        
        # Create B-UML classes for GUI components
        self._create_app_class(model, gui_data)
        self._create_theme_class(model, gui_data)
        self._create_screen_classes(model, gui_data)
        
        return model, gui_data
    
    def _extract_gui_structure(self) -> Dict:
        """Extract GUI structure from XML"""
        gui_data = {
            'appName': self.root.get('appName', 'WebApp'),
            'theme': self._extract_theme(),
            'screens': self._extract_screens()
        }
        return gui_data
    
    def _extract_theme(self) -> Optional[Dict]:
        """Extract theme configuration"""
        theme_elem = self.root.find('gui:theme', self.namespaces)
        if theme_elem is None:
            theme_elem = self.root.find('theme')
        
        if theme_elem is not None:
            return {
                'primaryColor': theme_elem.get('primaryColor', '#2196F3'),
                'secondaryColor': theme_elem.get('secondaryColor', '#FFC107'),
                'logoUrl': theme_elem.get('logoUrl', '')
            }
        return None
    
    def _extract_screens(self) -> List[Dict]:
        """Extract all screens from XML"""
        screens = []
        screen_elems = self.root.findall('gui:screens', self.namespaces)
        if not screen_elems:
            screen_elems = self.root.findall('screens')
        
        for screen_elem in screen_elems:
            screen_data = {
                'id': screen_elem.get('{http://www.omg.org/XMI}id', ''),
                'name': screen_elem.get('name', 'Screen'),
                'path': screen_elem.get('path', '/'),
                'type': screen_elem.get('type', 'DEFAULT'),
                'title': screen_elem.get('title', 'Page'),
                'components': self._extract_components(screen_elem)
            }
            screens.append(screen_data)
        
        return screens
    
    def _extract_components(self, screen_elem: ET.Element) -> List[Dict]:
        """Extract components from a screen"""
        components = []
        comp_elems = screen_elem.findall('gui:components', self.namespaces)
        if not comp_elems:
            comp_elems = screen_elem.findall('components')
        
        for comp_elem in comp_elems:
            comp_type = comp_elem.get('{http://www.omg.org/XMI}type', '')
            if not comp_type:
                comp_type = comp_elem.tag.split('}')[-1]
            
            # Remove namespace prefix
            comp_type_name = comp_type.split(':')[-1]
            
            comp_data = {
                'id': comp_elem.get('{http://www.omg.org/XMI}id', ''),
                'type': comp_type_name,
                'htmlId': comp_elem.get('id', ''),
                'order': int(comp_elem.get('order', 0)),
                'attributes': dict(comp_elem.attrib)
            }
            
            # Extract specific component attributes
            if comp_type_name == 'ListView':
                comp_data.update({
                    'entity': comp_elem.get('entity', 'Item'),
                    'showImage': comp_elem.get('showImage', 'false') == 'true',
                    'showPrice': comp_elem.get('showPrice', 'false') == 'true',
                    'showLocation': comp_elem.get('showLocation', 'false') == 'true',
                    'showRating': comp_elem.get('showRating', 'false') == 'true'
                })
            elif comp_type_name == 'DetailView':
                comp_data.update({
                    'entity': comp_elem.get('entity', 'Item')
                })
            elif comp_type_name == 'ActionButton':
                comp_data.update({
                    'label': comp_elem.get('label', 'Action'),
                    'icon': comp_elem.get('icon', ''),
                    'actionType': comp_elem.get('actionType', 'NAVIGATE'),
                    'targetPath': comp_elem.get('targetPath', '')
                })
            
            components.append(comp_data)
        
        # Sort components by order
        components.sort(key=lambda c: c['order'])
        return components
    
    def _create_app_class(self, model: DomainModel, gui_data: Dict):
        """Create Application class in B-UML"""
        app_class = Class(name="Application", model=model)
        
        # Add properties
        Property(name="appName", type=PrimitiveDataType("str"), 
                owner=app_class, multiplicity=(1, 1))
        Property(name="screens", type=PrimitiveDataType("list"), 
                owner=app_class, multiplicity=(0, "*"))
        
        model.types.append(app_class)
    
    def _create_theme_class(self, model: DomainModel, gui_data: Dict):
        """Create Theme class in B-UML"""
        theme_class = Class(name="Theme", model=model)
        
        Property(name="primaryColor", type=PrimitiveDataType("str"), 
                owner=theme_class, multiplicity=(1, 1))
        Property(name="secondaryColor", type=PrimitiveDataType("str"), 
                owner=theme_class, multiplicity=(1, 1))
        Property(name="logoUrl", type=PrimitiveDataType("str"), 
                owner=theme_class, multiplicity=(0, 1))
        
        model.types.append(theme_class)
    
    def _create_screen_classes(self, model: DomainModel, gui_data: Dict):
        """Create Screen and Component classes in B-UML"""
        screen_class = Class(name="Screen", model=model)
        
        Property(name="name", type=PrimitiveDataType("str"), 
                owner=screen_class, multiplicity=(1, 1))
        Property(name="path", type=PrimitiveDataType("str"), 
                owner=screen_class, multiplicity=(1, 1))
        Property(name="type", type=PrimitiveDataType("str"), 
                owner=screen_class, multiplicity=(1, 1))
        Property(name="title", type=PrimitiveDataType("str"), 
                owner=screen_class, multiplicity=(1, 1))
        Property(name="components", type=PrimitiveDataType("list"), 
                owner=screen_class, multiplicity=(0, "*"))
        
        model.types.append(screen_class)
        
        # Create Component base class
        component_class = Class(name="Component", model=model)
        Property(name="id", type=PrimitiveDataType("str"), 
                owner=component_class, multiplicity=(1, 1))
        Property(name="type", type=PrimitiveDataType("str"), 
                owner=component_class, multiplicity=(1, 1))
        Property(name="order", type=PrimitiveDataType("int"), 
                owner=component_class, multiplicity=(1, 1))
        
        model.types.append(component_class)
