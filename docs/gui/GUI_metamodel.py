####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
InputFieldType: Enumeration = Enumeration(
    name="InputFieldType",
    literals={
            EnumerationLiteral(name="URL"),
			EnumerationLiteral(name="Search"),
			EnumerationLiteral(name="Checkbox"),
			EnumerationLiteral(name="Select"),
			EnumerationLiteral(name="RichText"),
			EnumerationLiteral(name="MultiSelect"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Number"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Password"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="File")
    }
)

ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="RaisedButton"),
			EnumerationLiteral(name="TextButton"),
			EnumerationLiteral(name="OutlinedButton"),
			EnumerationLiteral(name="IconButton"),
			EnumerationLiteral(name="FloatingActionButton"),
			EnumerationLiteral(name="DropdownButton"),
			EnumerationLiteral(name="ToggleButtons")
    }
)

ButtonActionType: Enumeration = Enumeration(
    name="ButtonActionType",
    literals={
            EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="ShowList"),
			EnumerationLiteral(name="OpenForm"),
			EnumerationLiteral(name="SubmitForm"),
			EnumerationLiteral(name="Cancel"),
			EnumerationLiteral(name="Save"),
			EnumerationLiteral(name="Delete"),
			EnumerationLiteral(name="Confirm"),
			EnumerationLiteral(name="Navigate"),
			EnumerationLiteral(name="Search"),
			EnumerationLiteral(name="Filter"),
			EnumerationLiteral(name="Sort"),
			EnumerationLiteral(name="Send"),
			EnumerationLiteral(name="Settings"),
			EnumerationLiteral(name="Login"),
			EnumerationLiteral(name="Logout"),
			EnumerationLiteral(name="Back"),
			EnumerationLiteral(name="Next"),
			EnumerationLiteral(name="View"),
			EnumerationLiteral(name="Edit")
    }
)

FileSourceType: Enumeration = Enumeration(
    name="FileSourceType",
    literals={
            EnumerationLiteral(name="FileSystem"),
			EnumerationLiteral(name="LocalStorage"),
			EnumerationLiteral(name="Database")
    }
)

CollectionSourceType: Enumeration = Enumeration(
    name="CollectionSourceType",
    literals={
            EnumerationLiteral(name="List"),
			EnumerationLiteral(name="Table"),
			EnumerationLiteral(name="Tree"),
			EnumerationLiteral(name="Grid"),
			EnumerationLiteral(name="Array"),
			EnumerationLiteral(name="Stack")
    }
)

TransitionType: Enumeration = Enumeration(
    name="TransitionType",
    literals={
            EnumerationLiteral(name="Navigate"),
			EnumerationLiteral(name="Back"),
			EnumerationLiteral(name="Replace"),
			EnumerationLiteral(name="Reload"),
			EnumerationLiteral(name="OpenModal")
    }
)

ScreenType: Enumeration = Enumeration(
    name="ScreenType",
    literals={
            EnumerationLiteral(name="Small"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Large"),
			EnumerationLiteral(name="xLarge")
    }
)

# Classes
Model = Class(name="Model")
NamedElement = Class(name="NamedElement")
GUIModel = Class(name="GUIModel")
Module = Class(name="Module")
Screen = Class(name="Screen")
ViewElement = Class(name="ViewElement")
ViewContainer = Class(name="ViewContainer")
ViewComponent = Class(name="ViewComponent")
Menu = Class(name="Menu")
Form = Class(name="Form")
InputField = Class(name="InputField")
DataList = Class(name="DataList")
Button = Class(name="Button")
Image = Class(name="Image")
DataSource = Class(name="DataSource")
File = Class(name="File")
Collection = Class(name="Collection")
MenuItem = Class(name="MenuItem")
DataSourceElement = Class(name="DataSourceElement")
NavigationAction = Class(name="NavigationAction")
Binding = Class(name="Binding")
Class_var = Class(name="Class_")
Property_var = Class(name="Property_")
MapView = Class(name="MapView")

# Model class attributes and methods

# NamedElement class attributes and methods
NamedElement_name: Property = Property(name="name", type=StringType)
NamedElement.attributes={NamedElement_name}

# GUIModel class attributes and methods
GUIModel_package: Property = Property(name="package", type=StringType)
GUIModel_versionCode: Property = Property(name="versionCode", type=StringType)
GUIModel_versionName: Property = Property(name="versionName", type=StringType)
GUIModel_description: Property = Property(name="description", type=StringType)
GUIModel_screenCompatibility: Property = Property(name="screenCompatibility", type=BooleanType)
GUIModel.attributes={GUIModel_versionName, GUIModel_description, GUIModel_versionCode, GUIModel_screenCompatibility, GUIModel_package}

# Module class attributes and methods

# Screen class attributes and methods
Screen_x_dpi: Property = Property(name="x_dpi", type=IntegerType)
Screen_y_dpi: Property = Property(name="y_dpi", type=IntegerType)
Screen_screen_size: Property = Property(name="screen_size", type=ScreenType)
Screen_is_main_page: Property = Property(name="is_main_page", type=BooleanType)
Screen.attributes={Screen_is_main_page, Screen_y_dpi, Screen_screen_size, Screen_x_dpi}

# ViewElement class attributes and methods
ViewElement_description: Property = Property(name="description", type=StringType)
ViewElement_visibleIf: Property = Property(name="visibleIf", type=StringType)
ViewElement.attributes={ViewElement_description, ViewElement_visibleIf}

# ViewContainer class attributes and methods

# ViewComponent class attributes and methods

# Menu class attributes and methods

# Form class attributes and methods
Form_validationRules: Property = Property(name="validationRules", type=StringType)
Form.attributes={Form_validationRules}

# InputField class attributes and methods
InputField_type: Property = Property(name="type", type=InputFieldType)
InputField_validationRules: Property = Property(name="validationRules", type=StringType)
InputField.attributes={InputField_type, InputField_validationRules}

# DataList class attributes and methods

# Button class attributes and methods
Button_label: Property = Property(name="label", type=StringType)
Button_buttonType: Property = Property(name="buttonType", type=ButtonType)
Button_actionType: Property = Property(name="actionType", type=ButtonActionType)
Button.attributes={Button_label, Button_actionType, Button_buttonType}

# Image class attributes and methods

# DataSource class attributes and methods
DataSource_name: Property = Property(name="name", type=StringType)
DataSource.attributes={DataSource_name}

# File class attributes and methods
File_type: Property = Property(name="type", type=FileSourceType)
File.attributes={File_type}

# Collection class attributes and methods
Collection_type: Property = Property(name="type", type=CollectionSourceType)
Collection.attributes={Collection_type}

# MenuItem class attributes and methods
MenuItem_label: Property = Property(name="label", type=StringType)
MenuItem.attributes={MenuItem_label}

# DataSourceElement class attributes and methods

# NavigationAction class attributes and methods
NavigationAction_transitionType: Property = Property(name="transitionType", type=TransitionType)
NavigationAction_condition: Property = Property(name="condition", type=StringType)
NavigationAction_parameters: Property = Property(name="parameters", type=StringType)
NavigationAction.attributes={NavigationAction_parameters, NavigationAction_transitionType, NavigationAction_condition}

# Binding class attributes and methods
Binding_exp: Property = Property(name="exp", type=StringType)
Binding.attributes={Binding_exp}

# Class_ class attributes and methods

# Property_ class attributes and methods

# MapView class attributes and methods
MapView_interactive: Property = Property(name="interactive", type=BooleanType)
MapView_zoom: Property = Property(name="zoom", type=IntegerType)
MapView.attributes={MapView_zoom, MapView_interactive}

# Relationships
Screen_Module: BinaryAssociation = BinaryAssociation(
    name="Screen_Module",
    ends={
        Property(name="screens", type=Screen, multiplicity=Multiplicity(0, 9999)),
        Property(name="module", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ViewElement_ViewContainer: BinaryAssociation = BinaryAssociation(
    name="ViewElement_ViewContainer",
    ends={
        Property(name="viewelement", type=ViewElement, multiplicity=Multiplicity(0, 9999)),
        Property(name="viewcontainer", type=ViewContainer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Module_GUIModel: BinaryAssociation = BinaryAssociation(
    name="Module_GUIModel",
    ends={
        Property(name="modules", type=Module, multiplicity=Multiplicity(0, 9999)),
        Property(name="guimodel", type=GUIModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Screen_ViewElement: BinaryAssociation = BinaryAssociation(
    name="Screen_ViewElement",
    ends={
        Property(name="screen", type=Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="view_elements", type=ViewElement, multiplicity=Multiplicity(0, 9999))
    }
)
NavigationAction_Button: BinaryAssociation = BinaryAssociation(
    name="NavigationAction_Button",
    ends={
        Property(name="navigation_actions", type=NavigationAction, multiplicity=Multiplicity(0, 9999)),
        Property(name="button", type=Button, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MenuItem_Menu: BinaryAssociation = BinaryAssociation(
    name="MenuItem_Menu",
    ends={
        Property(name="menu_items", type=MenuItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="menu", type=Menu, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NavigationAction_Screen: BinaryAssociation = BinaryAssociation(
    name="NavigationAction_Screen",
    ends={
        Property(name="navigationaction", type=NavigationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="screen_1", type=Screen, multiplicity=Multiplicity(1, 1))
    }
)
InputField_Form: BinaryAssociation = BinaryAssociation(
    name="InputField_Form",
    ends={
        Property(name="input_fields", type=InputField, multiplicity=Multiplicity(0, 9999)),
        Property(name="form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ViewElement_Binding: BinaryAssociation = BinaryAssociation(
    name="ViewElement_Binding",
    ends={
        Property(name="viewelement_1", type=ViewElement, multiplicity=Multiplicity(0, 1)),
        Property(name="binding", type=Binding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DataSource_DataList: BinaryAssociation = BinaryAssociation(
    name="DataSource_DataList",
    ends={
        Property(name="list_sources", type=DataSource, multiplicity=Multiplicity(1, 9999)),
        Property(name="datalist", type=DataList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Binding_Class_: BinaryAssociation = BinaryAssociation(
    name="Binding_Class_",
    ends={
        Property(name="binding_1", type=Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="classRef", type=Class_var, multiplicity=Multiplicity(0, 1))
    }
)
Binding_Property_: BinaryAssociation = BinaryAssociation(
    name="Binding_Property_",
    ends={
        Property(name="binding_2", type=Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="props", type=Property_var, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_GUIModel_Model = Generalization(general=Model, specific=GUIModel)
gen_Module_NamedElement = Generalization(general=NamedElement, specific=Module)
gen_ViewElement_NamedElement = Generalization(general=NamedElement, specific=ViewElement)
gen_ViewComponent_ViewElement = Generalization(general=ViewElement, specific=ViewComponent)
gen_ViewContainer_ViewElement = Generalization(general=ViewElement, specific=ViewContainer)
gen_Form_ViewContainer = Generalization(general=ViewContainer, specific=Form)
gen_DataList_ViewContainer = Generalization(general=ViewContainer, specific=DataList)
gen_Menu_ViewContainer = Generalization(general=ViewContainer, specific=Menu)
gen_Image_ViewComponent = Generalization(general=ViewComponent, specific=Image)
gen_Button_ViewComponent = Generalization(general=ViewComponent, specific=Button)
gen_Screen_NamedElement = Generalization(general=NamedElement, specific=Screen)
gen_InputField_ViewComponent = Generalization(general=ViewComponent, specific=InputField)
gen_File_DataSource = Generalization(general=DataSource, specific=File)
gen_Collection_DataSource = Generalization(general=DataSource, specific=Collection)
gen_DataSourceElement_DataSource = Generalization(general=DataSource, specific=DataSourceElement)
gen_MapView_ViewComponent = Generalization(general=ViewComponent, specific=MapView)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Model, NamedElement, GUIModel, Module, Screen, ViewElement, ViewContainer, ViewComponent, Menu, Form, InputField, DataList, Button, Image, DataSource, File, Collection, MenuItem, DataSourceElement, NavigationAction, Binding, Class_var, Property_var, MapView, InputFieldType, ButtonType, ButtonActionType, FileSourceType, CollectionSourceType, TransitionType, ScreenType},
    associations={Screen_Module, ViewElement_ViewContainer, Module_GUIModel, Screen_ViewElement, NavigationAction_Button, MenuItem_Menu, NavigationAction_Screen, InputField_Form, ViewElement_Binding, DataSource_DataList, Binding_Class_, Binding_Property_},
    generalizations={gen_GUIModel_Model, gen_Module_NamedElement, gen_ViewElement_NamedElement, gen_ViewComponent_ViewElement, gen_ViewContainer_ViewElement, gen_Form_ViewContainer, gen_DataList_ViewContainer, gen_Menu_ViewContainer, gen_Image_ViewComponent, gen_Button_ViewComponent, gen_Screen_NamedElement, gen_InputField_ViewComponent, gen_File_DataSource, gen_Collection_DataSource, gen_DataSourceElement_DataSource, gen_MapView_ViewComponent}
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="New project")
project = Project(
    name="metamodelGUI",
    models=[domain_model],
    owner="Krsto",
    metadata=metadata
)
