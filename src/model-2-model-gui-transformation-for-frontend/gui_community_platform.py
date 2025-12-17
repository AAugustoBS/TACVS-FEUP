"""
gui_community_platform.py

FULL baseline GUI model (canonical template)
Sincronizado com o Structural Model (PlantUML):
- Rating em vez de Review
- Offer incluído
- Atributos: uid, state, amount, fullName
"""

from __future__ import annotations
import inspect
from typing import Set, Optional

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen, Button, InputField, DataList,
    DataSourceElement, ViewComponent,
    ButtonType, ButtonActionType, InputFieldType
)

def _accepted_kwargs(cls, provided: dict) -> dict:
    sig = inspect.signature(cls.__init__)
    params = set(sig.parameters.keys())
    params.discard("self")
    return {k: v for k, v in provided.items() if k in params}

def mk_input(*, name: str, description: str, field_type=InputFieldType.Text, validation_rules: str = "") -> InputField:
    base = {"name": name, "description": description}
    sig = inspect.signature(InputField.__init__)
    p = sig.parameters
    if "validationRules" in p: base["validationRules"] = validation_rules
    elif "validation_rules" in p: base["validation_rules"] = validation_rules
    if "field_type" in p: base["field_type"] = field_type
    elif "type" in p: base["type"] = field_type
    return InputField(**_accepted_kwargs(InputField, base))

def mk_button(*, name: str, description: str, label: str, button_type=ButtonType.TextButton, action_type=ButtonActionType.Navigate, target: Optional[Screen] = None) -> Button:
    sig = inspect.signature(Button.__init__)
    p = sig.parameters
    base = {"name": name, "description": description, "label": label}
    if "buttonType" in p: base["buttonType"] = button_type
    if target is not None and "targetScreen" in p: base["targetScreen"] = target
    if "actionType" in p: base["actionType"] = action_type
    b = Button(**_accepted_kwargs(Button, base))
    if target is not None and hasattr(b, "targetScreen"):
        try: b.targetScreen = target
        except Exception: pass
    return b

def mk_datalist(*, name: str, description: str, sources: Set[DataSourceElement]) -> DataList:
    sig = inspect.signature(DataList.__init__)
    p = sig.parameters
    base = {"name": name, "description": description}
    if "list_sources" in p: base["list_sources"] = set(sources)
    elif "sources" in p: base["sources"] = set(sources)
    return DataList(**_accepted_kwargs(DataList, base))

def mk_screen(*, name: str, description: str, is_main: bool = False) -> Screen:
    base = {"name": name, "description": description, "x_dpi": "x_dpi", "y_dpi": "y_dpi", "screen_size": "Medium", "view_elements": set(), "is_main_page": is_main}
    return Screen(**_accepted_kwargs(Screen, base))

def mk_module(*, name: str, screens: Set[Screen]) -> Module:
    return Module(**_accepted_kwargs(Module, {"name": name, "screens": set(screens)}))

def mk_datasource(*, name: str, dataSourceClass: str, fields: Set) -> DataSourceElement:
    return DataSourceElement(**_accepted_kwargs(DataSourceElement, {"name": name, "dataSourceClass": dataSourceClass, "fields": set(fields)}))

# ----------------------------
# 1. FULL baseline screens
# ----------------------------
ItemListScreen = mk_screen(name="ItemListScreen", description="Browse items", is_main=True)
ItemDetailsScreen = mk_screen(name="ItemDetailsScreen", description="View item details")
LoginScreen = mk_screen(name="LoginScreen", description="Authentication")
ChatScreen = mk_screen(name="ChatScreen", description="Chat with users")
PaymentScreen = mk_screen(name="PaymentScreen", description="Payment checkout")
RatingsListScreen = mk_screen(name="RatingsListScreen", description="Review list")
SubcommunitySelectorScreen = mk_screen(name="SubcommunitySelectorScreen", description="Select area")
BlankScreen = mk_screen(name="BlankScreen", description="Placeholder")

# ----------------------------
# 2. FULL baseline datasources (Sincronizado com Structural)
# ----------------------------
ItemsDataSource = mk_datasource(name="ItemsDataSource", dataSourceClass="Item", fields=set())
TagsDataSource = mk_datasource(name="TagsDataSource", dataSourceClass="Tag", fields=set())
RatingsDataSource = mk_datasource(name="RatingsDataSource", dataSourceClass="Rating", fields=set())
MessagesDataSource = mk_datasource(name="MessagesDataSource", dataSourceClass="Message", fields=set())
ConversationsDataSource = mk_datasource(name="ConversationsDataSource", dataSourceClass="Conversation", fields=set())
CommunitiesDataSource = mk_datasource(name="CommunitiesDataSource", dataSourceClass="Community", fields=set())
OffersDataSource = mk_datasource(name="OffersDataSource", dataSourceClass="Offer", fields=set())

# ----------------------------
# 3. View Elements
# ----------------------------

# --- Item List Screen ---
ItemsList = mk_datalist(name="ItemsList", description="Items list", sources={ItemsDataSource})
SearchField = mk_input(name="SearchField", description="Search by title", field_type=InputFieldType.Search)
ViewItemBtn = mk_button(name="ViewItemBtn", description="Go to details", label="Details", target=ItemDetailsScreen)
ItemListScreen.view_elements.update({ItemsList, SearchField, ViewItemBtn})

# --- Item Details Screen ---
ItemTitle = mk_input(name="ItemTitle", description="title", field_type=InputFieldType.Text)
ItemDesc = mk_input(name="ItemDesc", description="description", field_type=InputFieldType.Text)
ItemPrice = mk_input(name="ItemPrice", description="minExchangeValue.amount", field_type=InputFieldType.Number)
ItemStateField = mk_input(name="ItemStateField", description="state", field_type=InputFieldType.Text)
ItemConditionField = mk_input(name="ItemConditionField", description="condition", field_type=InputFieldType.Text)
ItemCreatedAt = mk_input(name="ItemCreatedAt", description="createdAt", field_type=InputFieldType.Date)

ItemRatingsList = mk_datalist(name="ItemRatingsList", description="Ratings", sources={RatingsDataSource})
ItemTagsList = mk_datalist(name="ItemTagsList", description="Tags", sources={TagsDataSource})

ContactBtn = mk_button(name="ContactBtn", description="Contact", label="Contact", target=ChatScreen)
PayBtn = mk_button(name="PayBtn", description="Pay", label="Pay Now", target=PaymentScreen)
OfferBtn = mk_button(name="OfferBtn", description="Make Offer", label="Offer", action_type=ButtonActionType.OpenForm)

ItemDetailsScreen.view_elements.update({
    ItemTitle, ItemDesc, ItemPrice, ItemStateField, ItemConditionField, 
    ItemCreatedAt, ItemRatingsList, ItemTagsList, ContactBtn, PayBtn, OfferBtn
})

# --- Login Screen ---
UsernameInput = mk_input(name="UsernameInput", description="username", field_type=InputFieldType.Text)
EmailInput = mk_input(name="EmailInput", description="email", field_type=InputFieldType.Email)
LoginSubmitBtn = mk_button(name="LoginSubmitBtn", description="Login", label="Sign In", action_type=ButtonActionType.OpenForm)
LoginScreen.view_elements.update({UsernameInput, EmailInput, LoginSubmitBtn})

# --- Chat Screen ---
ChatMsgInput = mk_input(name="ChatMsgInput", description="content", field_type=InputFieldType.Text)
MessagesList = mk_datalist(name="MessagesList", description="History", sources={MessagesDataSource})
ChatScreen.view_elements.update({ChatMsgInput, MessagesList})

# --- Payment Screen ---
MBWayBtn = mk_button(name="MBWayBtn", description="MBWay", label="MBWay", action_type=ButtonActionType.OpenForm)
MultibancoBtn = mk_button(name="MultibancoBtn", description="Multibanco", label="Multibanco", action_type=ButtonActionType.OpenForm)
PayPalBtn = mk_button(name="PayPalBtn", description="PayPal", label="PayPal", action_type=ButtonActionType.OpenForm)
PaymentScreen.view_elements.update({MBWayBtn, MultibancoBtn, PayPalBtn})

# ----------------------------
# 4. GUIModel root
# ----------------------------
vc = ViewComponent(name="CommunityPlatformView", description="Canonical Baseline")

main_module = mk_module(
    name="MainModule",
    screens={
        ItemListScreen, ItemDetailsScreen, LoginScreen, ChatScreen, 
        PaymentScreen, RatingsListScreen, SubcommunitySelectorScreen, BlankScreen
    }
)

community_gui_model = GUIModel(
    name="CommunityPlatform",
    package="com.example.platform",
    versionCode="1",
    versionName="1.0",
    description="Baseline FULL GUI compatible with PlantUML structure",
    modules={main_module}
)

community_gui_model.viewComponent = vc
community_gui_model.data_sources = {
    ItemsDataSource, TagsDataSource, RatingsDataSource, 
    MessagesDataSource, ConversationsDataSource, CommunitiesDataSource, OffersDataSource
}