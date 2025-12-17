"""
generated_gui_model.py

FULL generated GUI model (Python) from M2M (pruning-only).
"""

from __future__ import annotations
import inspect
from typing import Set, Optional

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen, Button, InputField, DataList,
    DataSourceElement, ViewComponent,
    ButtonType, ButtonActionType, InputFieldType
)

import structural_community_platform as st

def _accepted_kwargs(cls, provided: dict) -> dict:
    sig = inspect.signature(cls.__init__)
    params = set(sig.parameters.keys())
    params.discard('self')
    return {k: v for k, v in provided.items() if k in params}

def _get_prop(cls_obj, prop_name: str):
    attrs = getattr(cls_obj, 'attributes', None) or set()
    if isinstance(attrs, list):
        attrs = set(attrs)
    for a in attrs:
        if getattr(a, 'name', None) == prop_name:
            return a
    return None

def mk_screen(*, name: str, description: str, is_main: bool = False) -> Screen:
    base = {
        'name': name, 'description': description,
        'x_dpi': 'x_dpi', 'y_dpi': 'y_dpi',
        'screen_size': 'Medium', 'view_elements': set(),
        'is_main_page': is_main,
    }
    return Screen(**_accepted_kwargs(Screen, base))

def mk_datasource(*, name: str, dataSourceClass, fields: Set) -> DataSourceElement:
    base = {'name': name, 'dataSourceClass': dataSourceClass, 'fields': set(fields)}
    return DataSourceElement(**_accepted_kwargs(DataSourceElement, base))

def mk_input(*, name: str, description: str, field_type=InputFieldType.Text, validation_rules: str = '') -> InputField:
    base = {'name': name, 'description': description}
    p = inspect.signature(InputField.__init__).parameters
    if 'validationRules' in p: base['validationRules'] = validation_rules
    elif 'validation' in p: base['validation'] = validation_rules
    elif 'validation_rules' in p: base['validation_rules'] = validation_rules
    if 'field_type' in p: base['field_type'] = field_type
    elif 'type' in p: base['type'] = field_type
    elif 'inputFieldType' in p: base['inputFieldType'] = field_type
    elif 'fieldType' in p: base['fieldType'] = field_type
    return InputField(**_accepted_kwargs(InputField, base))

def mk_button(*, name: str, description: str, label: str,
              button_type=ButtonType.TextButton,
              action_type=ButtonActionType.Navigate,
              target: Optional[Screen] = None) -> Button:
    p = inspect.signature(Button.__init__).parameters
    base = {'name': name, 'description': description, 'label': label}
    if 'buttonType' in p: base['buttonType'] = button_type
    elif 'button_type' in p: base['button_type'] = button_type
    ctor_action = action_type
    if action_type == ButtonActionType.Navigate and target is None:
        ctor_action = ButtonActionType.OpenForm
    if 'actionType' in p: base['actionType'] = ctor_action
    elif 'action_type' in p: base['action_type'] = ctor_action
    if target is not None and 'targetScreen' in p: base['targetScreen'] = target
    b = Button(**_accepted_kwargs(Button, base))
    if hasattr(b, 'buttonType'):
        try: b.buttonType = button_type
        except Exception: pass
    if hasattr(b, 'targetScreen'):
        try: b.targetScreen = target
        except Exception: pass
    if hasattr(b, 'actionType'):
        try: b.actionType = action_type
        except Exception: pass
    return b

def mk_datalist(*, name: str, description: str, sources: Set[DataSourceElement]) -> DataList:
    p = inspect.signature(DataList.__init__).parameters
    base = {'name': name, 'description': description}
    if 'list_sources' in p: base['list_sources'] = set(sources)
    elif 'listSources' in p: base['listSources'] = set(sources)
    elif 'sources' in p: base['sources'] = set(sources)
    return DataList(**_accepted_kwargs(DataList, base))

def mk_module(*, name: str, screens: Set[Screen]) -> Module:
    base = {'name': name, 'screens': set(screens)}
    return Module(**_accepted_kwargs(Module, base))

def build_generated_gui_model() -> GUIModel:
    gui_name = 'appName'
    gui_pkg  = 'com.example.shortName'
    vcode    = '1'
    vname    = '1.0'
    gdesc    = 'GUI generated from baseline + DSML pruning for appName'
    compat   = False

    # Screens
    BlankScreen = mk_screen(name='BlankScreen', description='Placeholder', is_main=False)
    ItemDetailsScreen = mk_screen(name='ItemDetailsScreen', description='View item details', is_main=False)
    ItemListScreen = mk_screen(name='ItemListScreen', description='Browse items', is_main=True)
    PaymentScreen = mk_screen(name='PaymentScreen', description='Payment checkout', is_main=False)
    RatingsListScreen = mk_screen(name='RatingsListScreen', description='Review list', is_main=False)
    SubcommunitySelectorScreen = mk_screen(name='SubcommunitySelectorScreen', description='Select area', is_main=False)

    # DataSources
    CommunitiesDataSource = mk_datasource(name='CommunitiesDataSource', dataSourceClass=getattr(st, 'Community'), fields={ _get_prop(getattr(st, 'Community'), 'name') })
    ItemsDataSource = mk_datasource(name='ItemsDataSource', dataSourceClass=getattr(st, 'Item'), fields={ _get_prop(getattr(st, 'Item'), 'condition'), _get_prop(getattr(st, 'Item'), 'createdAt'), _get_prop(getattr(st, 'Item'), 'description'), _get_prop(getattr(st, 'Item'), 'kind'), _get_prop(getattr(st, 'Item'), 'state'), _get_prop(getattr(st, 'Item'), 'title') })
    OffersDataSource = mk_datasource(name='OffersDataSource', dataSourceClass=getattr(st, 'Offer'), fields=set())
    RatingsDataSource = mk_datasource(name='RatingsDataSource', dataSourceClass=getattr(st, 'Rating'), fields={ _get_prop(getattr(st, 'Rating'), 'comment'), _get_prop(getattr(st, 'Rating'), 'createdAt'), _get_prop(getattr(st, 'Rating'), 'stars') })
    TagsDataSource = mk_datasource(name='TagsDataSource', dataSourceClass=getattr(st, 'Category'), fields={ _get_prop(getattr(st, 'Category'), 'name') })

    # View elements per screen
    # Elements for BlankScreen
    # no elements in BlankScreen

    # Elements for ItemDetailsScreen
    ItemDetailsScreen_ItemConditionField = mk_input(name='ItemConditionField', description='condition', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemCreatedAt = mk_input(name='ItemCreatedAt', description='createdAt', field_type=InputFieldType.Date, validation_rules='')
    ItemDetailsScreen_ItemDesc = mk_input(name='ItemDesc', description='description', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemPrice = mk_input(name='ItemPrice', description='minExchangeValue.amount', field_type=InputFieldType.Number, validation_rules='')
    ItemDetailsScreen_ItemRatingsList = mk_datalist(name='ItemRatingsList', description='Ratings', sources={ RatingsDataSource })
    ItemDetailsScreen_ItemStateField = mk_input(name='ItemStateField', description='state', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemTagsList = mk_datalist(name='ItemTagsList', description='Tags', sources={ TagsDataSource })
    ItemDetailsScreen_ItemTitle = mk_input(name='ItemTitle', description='title', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_OfferBtn = mk_button(name='OfferBtn', description='Make Offer', label='Offer', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    ItemDetailsScreen_PayBtn = mk_button(name='PayBtn', description='Pay', label='Pay Now', button_type=ButtonType.TextButton, action_type=ButtonActionType.Navigate, target=PaymentScreen)
    ItemDetailsScreen.view_elements.update({ItemDetailsScreen_ItemConditionField, ItemDetailsScreen_ItemCreatedAt, ItemDetailsScreen_ItemDesc, ItemDetailsScreen_ItemPrice, ItemDetailsScreen_ItemRatingsList, ItemDetailsScreen_ItemStateField, ItemDetailsScreen_ItemTagsList, ItemDetailsScreen_ItemTitle, ItemDetailsScreen_OfferBtn, ItemDetailsScreen_PayBtn})

    # Elements for ItemListScreen
    ItemListScreen_ItemsList = mk_datalist(name='ItemsList', description='Items list', sources={ ItemsDataSource })
    ItemListScreen_SearchField = mk_input(name='SearchField', description='Search by title', field_type=InputFieldType.Search, validation_rules='')
    ItemListScreen_ViewItemBtn = mk_button(name='ViewItemBtn', description='Go to details', label='Details', button_type=ButtonType.TextButton, action_type=ButtonActionType.Navigate, target=ItemDetailsScreen)
    ItemListScreen.view_elements.update({ItemListScreen_ItemsList, ItemListScreen_SearchField, ItemListScreen_ViewItemBtn})

    # Elements for PaymentScreen
    PaymentScreen_MBWayBtn = mk_button(name='MBWayBtn', description='MBWay', label='MBWay', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen_MultibancoBtn = mk_button(name='MultibancoBtn', description='Multibanco', label='Multibanco', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen_PayPalBtn = mk_button(name='PayPalBtn', description='PayPal', label='PayPal', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen.view_elements.update({PaymentScreen_MBWayBtn, PaymentScreen_MultibancoBtn, PaymentScreen_PayPalBtn})

    # Elements for RatingsListScreen
    # no elements in RatingsListScreen

    # Elements for SubcommunitySelectorScreen
    # no elements in SubcommunitySelectorScreen

    vc = ViewComponent(name='CommunityPlatformView', description='Canonical Baseline')

    modules = set()
    Module_MainModule = mk_module(name='MainModule', screens={ BlankScreen, ItemDetailsScreen, ItemListScreen, PaymentScreen, RatingsListScreen, SubcommunitySelectorScreen })
    modules.add(Module_MainModule)

    gui = GUIModel(**_accepted_kwargs(GUIModel, {
        'name': gui_name,
        'package': gui_pkg,
        'versionCode': vcode,
        'versionName': vname,
        'description': gdesc,
        'screenCompatibility': compat,
        'modules': modules,
    }))
    if vc is not None: gui.viewComponent = vc
    gui.data_sources = { CommunitiesDataSource, ItemsDataSource, OffersDataSource, RatingsDataSource, TagsDataSource }
    return gui

community_gui_model = build_generated_gui_model()
