"""
generated_gui_model.py

FULL generated GUI model (Python) from M2M.
"""

from __future__ import annotations
import inspect
from typing import Set, Optional

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen, Button, InputField, DataList,
    DataSourceElement, ViewComponent,
    ButtonType, ButtonActionType, InputFieldType
)

from structural_community_platform import (
    Community,
    Community_name,
    Item,
    Item_description,
    Item_price,
    Item_publicationDate,
    Item_status,
    Item_title,
    Item_transactionType,
    Review,
    Review_comment,
    Review_rating,
    Review_reviewDate,
    Tag,
    Tag_name,
)

def _accepted_kwargs(cls, provided: dict) -> dict:
    sig = inspect.signature(cls.__init__)
    params = set(sig.parameters.keys())
    params.discard('self')
    return {k: v for k, v in provided.items() if k in params}

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
    if target is not None:
        base['targetScreen'] = target
    return b

def mk_datalist(*, name: str, description: str, sources: Set[DataSourceElement]) -> DataList:
    p = inspect.signature(DataList.__init__).parameters
    base = {'name': name, 'description': description}
    if 'list_sources' in p: base['list_sources'] = set(sources)
    elif 'listSources' in p: base['listSources'] = set(sources)
    elif 'sources' in p: base['sources'] = set(sources)
    base = {'name': name, 'description': description, 'list_sources': list(sources)}
    return DataList(**_accepted_kwargs(DataList, base))
    #return DataList(**_accepted_kwargs(DataList, base))

def mk_module(*, name: str, screens: Set[Screen]) -> Module:
    base = {'name': name, 'screens': set(screens)}
    return Module(**_accepted_kwargs(Module, base))

def build_generated_gui_model() -> GUIModel:
    gui_name = 'appName'
    gui_pkg  = 'com.example.shortName'
    vcode    = '1'
    vname    = '1.0'
    gdesc    = 'GUI generated from baseline + DSML pruning for appName'
    compat   = True

    # Screens
    BlankScreen = mk_screen(name='BlankScreen', description='Placeholder', is_main=False)
    ItemDetailsScreen = mk_screen(name='ItemDetailsScreen', description='View details of a selected item', is_main=False)
    ItemListScreen = mk_screen(name='ItemListScreen', description='Browse items available in the community', is_main=True)
    PaymentScreen = mk_screen(name='PaymentScreen', description='Payment options and checkout', is_main=False)
    RatingsListScreen = mk_screen(name='RatingsListScreen', description='List and create ratings / reviews', is_main=False)
    SubcommunitySelectorScreen = mk_screen(name='SubcommunitySelectorScreen', description='Select subcommunity', is_main=False)

    # DataSources
    CommunitiesDataSource = mk_datasource(name='CommunitiesDataSource', dataSourceClass=Community, fields={ Community_name })
    ItemsDataSource = mk_datasource(name='ItemsDataSource', dataSourceClass=Item, fields={ Item_description, Item_price, Item_publicationDate, Item_status, Item_title, Item_transactionType })
    ReviewsDataSource = mk_datasource(name='ReviewsDataSource', dataSourceClass=Review, fields={ Review_comment, Review_rating, Review_reviewDate })
    TagsDataSource = mk_datasource(name='TagsDataSource', dataSourceClass=Tag, fields={ Tag_name })

    # View elements per screen
    # Elements for BlankScreen
    # no elements in BlankScreen

    # Elements for ItemDetailsScreen
    ItemDetailsScreen_AddReviewButton = mk_button(name='AddReviewButton', description='Write a review', label='Add Review', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    ItemDetailsScreen_ContactSellerButton = mk_button(name='ContactSellerButton', description='Start a conversation', label='Contact Seller', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.OpenForm, target=None)
    ItemDetailsScreen_DonationBadge = mk_input(name='DonationBadge', description='Donation', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemCommunityField = mk_input(name='ItemCommunityField', description='Community where the item is listed.', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemDescriptionField = mk_input(name='ItemDescriptionField', description='Detailed description of the item.', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemPriceField = mk_input(name='ItemPriceField', description='Price of the item (for sale).', field_type=InputFieldType.Number, validation_rules='')
    ItemDetailsScreen_ItemPublicationDateField = mk_input(name='ItemPublicationDateField', description='Date when the item was published.', field_type=InputFieldType.Date, validation_rules='')
    ItemDetailsScreen_ItemReviewsList = mk_datalist(name='ItemReviewsList', description='Reviews for this item', sources={ ReviewsDataSource })
    ItemDetailsScreen_ItemStatusField = mk_input(name='ItemStatusField', description='Current status of the item', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_ItemTagsList = mk_datalist(name='ItemTagsList', description='Tags for this item', sources={ TagsDataSource })
    ItemDetailsScreen_ItemTitleField = mk_input(name='ItemTitleField', description='Title of the item.', field_type=InputFieldType.Text, validation_rules='required')
    ItemDetailsScreen_ItemTransactionTypeField = mk_input(name='ItemTransactionTypeField', description='Transaction type (Donation/Sale/Exchange).', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen_PayNowButton = mk_button(name='PayNowButton', description='Pay now', label='Pay Now', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.Navigate, target=PaymentScreen)
    ItemDetailsScreen_StartOrderButton = mk_button(name='StartOrderButton', description='Create an order', label='Start Order', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.OpenForm, target=None)
    ItemDetailsScreen_SuggestExchangeButton = mk_button(name='SuggestExchangeButton', description='Suggest an exchange', label='Suggest Exchange', button_type=ButtonType.TextButton, action_type=ButtonActionType.OpenForm, target=None)
    ItemDetailsScreen_VariantSelector = mk_input(name='VariantSelector', description='Choose variant', field_type=InputFieldType.Text, validation_rules='')
    ItemDetailsScreen.view_elements.update({ItemDetailsScreen_AddReviewButton, ItemDetailsScreen_ContactSellerButton, ItemDetailsScreen_DonationBadge, ItemDetailsScreen_ItemCommunityField, ItemDetailsScreen_ItemDescriptionField, ItemDetailsScreen_ItemPriceField, ItemDetailsScreen_ItemPublicationDateField, ItemDetailsScreen_ItemReviewsList, ItemDetailsScreen_ItemStatusField, ItemDetailsScreen_ItemTagsList, ItemDetailsScreen_ItemTitleField, ItemDetailsScreen_ItemTransactionTypeField, ItemDetailsScreen_PayNowButton, ItemDetailsScreen_StartOrderButton, ItemDetailsScreen_SuggestExchangeButton, ItemDetailsScreen_VariantSelector})

    # Elements for ItemListScreen
    ItemListScreen_CommunityFilterField = mk_input(name='CommunityFilterField', description='Filter items by community', field_type=InputFieldType.Text, validation_rules='')
    ItemListScreen_ExpiryFilterField = mk_input(name='ExpiryFilterField', description='Filter by expiry', field_type=InputFieldType.Text, validation_rules='')
    ItemListScreen_ItemsList = mk_datalist(name='ItemsList', description='List of available items', sources={ ItemsDataSource })
    ItemListScreen_ProfileButton = mk_button(name='ProfileButton', description='Open user profile', label='Profile', button_type=ButtonType.IconButton, action_type=ButtonActionType.Navigate, target=BlankScreen)
    ItemListScreen_RegisterButton = mk_button(name='RegisterButton', description='Go to registration', label='Sign up', button_type=ButtonType.TextButton, action_type=ButtonActionType.Navigate, target=BlankScreen)
    ItemListScreen_SearchItemsField = mk_input(name='SearchItemsField', description='Search items', field_type=InputFieldType.Search, validation_rules='')
    ItemListScreen_StatusFilterField = mk_input(name='StatusFilterField', description='Filter items by status', field_type=InputFieldType.Text, validation_rules='')
    ItemListScreen_TagFilterField = mk_input(name='TagFilterField', description='Filter items by tag', field_type=InputFieldType.Text, validation_rules='')
    ItemListScreen_TransactionTypeFilterField = mk_input(name='TransactionTypeFilterField', description='Filter by transaction type', field_type=InputFieldType.Text, validation_rules='')
    ItemListScreen_ViewItemDetailsButton = mk_button(name='ViewItemDetailsButton', description='Open selected item details', label='View Details', button_type=ButtonType.TextButton, action_type=ButtonActionType.Navigate, target=ItemDetailsScreen)
    ItemListScreen.view_elements.update({ItemListScreen_CommunityFilterField, ItemListScreen_ExpiryFilterField, ItemListScreen_ItemsList, ItemListScreen_ProfileButton, ItemListScreen_RegisterButton, ItemListScreen_SearchItemsField, ItemListScreen_StatusFilterField, ItemListScreen_TagFilterField, ItemListScreen_TransactionTypeFilterField, ItemListScreen_ViewItemDetailsButton})

    # Elements for PaymentScreen
    PaymentScreen_MBWayButton = mk_button(name='MBWayButton', description='Pay with MBWay', label='Pay with MBWay', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen_MultibancoButton = mk_button(name='MultibancoButton', description='Pay with Multibanco', label='Pay with Multibanco', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen_PayPalButton = mk_button(name='PayPalButton', description='Pay with PayPal', label='Pay with PayPal', button_type=ButtonType.RaisedButton, action_type=ButtonActionType.OpenForm, target=None)
    PaymentScreen.view_elements.update({PaymentScreen_MBWayButton, PaymentScreen_MultibancoButton, PaymentScreen_PayPalButton})

    # Elements for RatingsListScreen
    RatingsListScreen_ItemReviewsList = mk_datalist(name='ItemReviewsList', description='Reviews for this item', sources={ ReviewsDataSource })
    RatingsListScreen.view_elements.update({RatingsListScreen_ItemReviewsList})

    # Elements for SubcommunitySelectorScreen
    SubcommunitySelectorScreen_SubcommunitySelectorField = mk_input(name='SubcommunitySelectorField', description='Select subcommunity', field_type=InputFieldType.Text, validation_rules='')
    SubcommunitySelectorScreen.view_elements.update({SubcommunitySelectorScreen_SubcommunitySelectorField})

    vc = ViewComponent(name='CommunityPlatformViewComponent', description='Baseline view component')

    # Modules
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
    gui.data_sources = { CommunitiesDataSource, ItemsDataSource, ReviewsDataSource, TagsDataSource }
    return gui

community_gui_model = build_generated_gui_model()
