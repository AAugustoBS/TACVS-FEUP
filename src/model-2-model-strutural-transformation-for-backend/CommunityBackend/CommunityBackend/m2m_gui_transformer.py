"""
m2m_dsml_to_gui.py

DSML -> GUI M2M transformer (Python / Besser)
Implements the transformation rules document (Option C: DSML -> GUI Model).

Outputs:
  - gui_model (an instance of GUIModel)
  - optionally writes "generated_gui.xmi" using Besser's XMI exporter
"""

from typing import Optional
import logging

#import custom_dsml

# XMI loader (pyecore) - used only to read AppConfig XMI.
try:
    from pyecore.resources import ResourceSet
except Exception:
    ResourceSet = None

# Besser GUI metamodel classes - assumed available as in your project
from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen, Button, InputField, DataList,
    DataSourceElement, ViewComponent, ButtonType, ButtonActionType,
    InputFieldType
)

from besser.BUML.metamodel.structural import (Property, NamedElement, PrimitiveDataType, Type,
                                              StringType, 
    IntegerType, 
    FloatType, 
    BooleanType)

try:
    from besser.BUML.export.xmi_export import XMIExporter
    have_xmi_exporter = True
except Exception:
    XMIExporter = None
    have_xmi_exporter = False

log = logging.getLogger("m2m_dsml_to_gui")
log.setLevel(logging.INFO)


# ----------------------------
# Helper: load DSML (AppConfig)
# ----------------------------
def load_dsml_appconfig(xmi_path: str, ecore_path: str):
    """
    Loads AppConfig instance from an XMI file.
    Returns a simple python object with attributes matching Ecore AppConfig structure:
      - appName, shortName, logoUrl, primaryColor, secondaryColor
      - accounts (object with localLogin, oauthLogin, phoneVerification, moderators)
      - listings (object with products, services, priceMode, exchangeMode, donationMode, expiry, variants, currency, minPrice, maxPrice)
      - messaging (object with chat, imagesInChat)
      - ratings (object with simple, bidirectional)
      - payments (object with mbway, multibanco, paypal, none, publicKey, secretRef)
      - logistics (object with inPerson, mail, locker)
      - subcommunities (object with enabled)
      - accessPolicies (object with anonymousBrowse, anonymousMessages)
    If pyecore is not available, the function will attempt a naive XML parse to extract attributes.
    """
    if ResourceSet is None:
        raise RuntimeError("pyecore is required to load DSML XMI. Install pyecore or provide the model object directly.")
    
    rset = ResourceSet()

    # Load metamodel
    ecore_resource = rset.get_resource(ecore_path)
    metamodel_root = ecore_resource.contents[0]

    # Register metamodel by its nsURI
    rset.metamodel_registry[metamodel_root.nsURI] = metamodel_root

    # Load XMI instance
    xmi_resource = rset.get_resource(xmi_path)
    root = xmi_resource.contents[0]

    return root


# ----------------------------
# M2M transformer main function
# ----------------------------
def generate_gui_from_dsml(
    dsml_xmi_path: Optional[str] = None,
    dsml_obj = None,
    output_xmi_path: Optional[str] = "generated_gui.xmi",
    write_xmi: bool = True
) -> GUIModel:
    """
    Main transformation: DSML -> GUIModel.

    Provide either dsml_xmi_path (XMI file) OR dsml_obj (already-loaded AppConfig-like object).
    If write_xmi=True and BESSER XMI exporter is available, the function writes the generated GUI model to output_xmi_path.

    Returns: generated GUIModel instance.
    """
    # 1) load dsml
    if dsml_obj is None:
        if dsml_xmi_path is None:
            raise ValueError("Provide either dsml_xmi_path or dsml_obj")
        dsml = load_dsml_appconfig(dsml_xmi_path)
    else:
        dsml = dsml_obj

    # 2) Create root GUIModel and base pieces
    gui_name = dsml.appName if getattr(dsml, "appName", None) else "GeneratedApp"
    short = dsml.shortName if getattr(dsml, "shortName", None) else "generatedapp"
    gui_model = GUIModel(
        name=gui_name,
        package=f"com.example.{short}",
        versionCode="1",
        versionName="1.0",
        description=f"GUI generated from DSML for {gui_name}",
        screenCompatibility=True,
        modules=set()
    )

    # viewComponent
    vc = ViewComponent(name=f"{gui_name}ViewComponent", description=f"View component for {gui_name}")
    gui_model.viewComponent = vc

    # create main module
    main_module = Module(name="MainModule", screens=set())
    gui_model.modules.add(main_module)

    # Helper factories for common elements (to avoid duplicates)
    # Basic InputFields and Buttons used across screens
    def make_input_field(name, desc, ftype=InputFieldType.Text, validation=None):
        return InputField(name=name, description=desc, type=ftype, validationRules=(validation or ""))

    def make_button(name, label, btype=ButtonType.TextButton, action=ButtonActionType.Navigate, target=None):
        btn = Button(name=name, description=label, label=label, buttonType=btype, actionType=action)
        if action == ButtonActionType.Navigate and target is not None:
            btn.targetScreen = target
        return btn

    # Create screens B1 mandatory screens
    # Item Details Screen
    # create placeholders first (we will add view elements to them later)
    ItemDetailsScreen = Screen(
        name="ItemDetailsScreen",
        description="View details of a selected item",
        x_dpi="x_dpi",
        y_dpi="y_dpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    ItemListScreen = Screen(
        name="ItemListScreen",
        description="Browse items available in the community",
        x_dpi="x_dpi",
        y_dpi="y_dpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=True
    )

    # Blank screen
    BlankScreen = Screen(
        name="BlankScreen",
        description="Placeholder",
        x_dpi="x_dpi",
        y_dpi="y_dpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )

    # Login screen (conditionally created)
    LoginScreen = None
    if (dsml.accounts and (dsml.accounts.localLogin or dsml.accounts.oauthLogin or dsml.accounts.phoneVerification)):
        LoginScreen = Screen(
            name="LoginScreen",
            description="User authentication screen",
            x_dpi="x_dpi",
            y_dpi="y_dpi",
            screen_size="Medium",
            view_elements=set(),
            is_main_page=False
        )

    # Chat screen (conditionally created)
    ChatScreen = None
    if dsml.messaging and getattr(dsml.messaging, "chat", False):
        ChatScreen = Screen(
            name="ChatScreen",
            description="Community chat",
            x_dpi="x_dpi",
            y_dpi="y_dpi",
            screen_size="Medium",
            view_elements=set(),
            is_main_page=False
        )

    # Ratings screen (conditionally created)
    RatingsListScreen = None
    if dsml.ratings and (getattr(dsml.ratings, "simple", False) or getattr(dsml.ratings, "bidirectional", False)):
        RatingsListScreen = Screen(
            name="RatingsListScreen",
            description="List and create ratings / reviews",
            x_dpi="x_dpi",
            y_dpi="y_dpi",
            screen_size="Medium",
            view_elements=set(),
            is_main_page=False
        )

    # Payment screen(s)
    any_payment = False
    payments = dsml.payments if getattr(dsml, "payments", None) else None
    if payments and (getattr(payments, "mbway", False) or getattr(payments, "multibanco", False) or getattr(payments, "paypal", False)):
        any_payment = True
        PaymentScreen = Screen(
            name="PaymentScreen",
            description="Payment options and checkout",
            x_dpi="x_dpi",
            y_dpi="y_dpi",
            screen_size="Medium",
            view_elements=set(),
            is_main_page=False
        )
    else:
        PaymentScreen = None

    # Subcommunity selector
    SubcommunityScreen = None
    if dsml.subcommunities and getattr(dsml.subcommunities, "enabled", False):
        SubcommunityScreen = Screen(
            name="SubcommunitySelectorScreen",
            description="Select subcommunity",
            x_dpi="x_dpi",
            y_dpi="y_dpi",
            screen_size="Medium",
            view_elements=set(),
            is_main_page=False
        )

    # ======= Build reusable view elements =======

    item_fields = {
        Property(name="title", type=StringType),
        Property(name="description", type=StringType),
        Property(name="price", type=FloatType), # Using FloatType for price
        Property(name="status", type=StringType),
        Property(name="publicationDate", type=StringType),
        Property(name="transactionType", type=StringType),
    }

    tag_fields = {
        Property(name="name", type=StringType)
    }

    review_fields = {
        Property(name="rating", type=IntegerType), # Using IntegerType for rating
        Property(name="comment", type=StringType),
        Property(name="reviewDate", type=StringType)
    }

    # DataSources
    ItemsDataSource = DataSourceElement(
        name="ItemsDataSource",
        dataSourceClass="Item",
        fields=item_fields # Pass the set of Property objects
    )
    TagsDataSource = DataSourceElement(
        name="TagsDataSource",
        dataSourceClass="Tag",
        fields=tag_fields # Pass the set of Property objects
    )
    ReviewsDataSource = DataSourceElement(
        name="ReviewsDataSource",
        dataSourceClass="Review",
        fields=review_fields # Pass the set of Property objects
    )
    gui_model.data_sources = {ItemsDataSource, TagsDataSource, ReviewsDataSource}

    # --- Item details elements ---
    ItemTitleField = make_input_field("ItemTitleField", "Title of the item.", InputFieldType.Text, "required")
    ItemDescriptionField = make_input_field("ItemDescriptionField", "Detailed description of the item.", InputFieldType.Text)
    ItemPriceField = make_input_field("ItemPriceField", "Price of the item (for sale).", InputFieldType.Number)
    ItemStatusField = make_input_field("ItemStatusField", "Current status of the item", InputFieldType.Text)
    ItemTransactionTypeField = make_input_field("ItemTransactionTypeField", "Transaction type (Donation/Sale/Exchange).", InputFieldType.Text)
    ItemCommunityField = make_input_field("ItemCommunityField", "Community where the item is listed.", InputFieldType.Text)
    ItemPublicationDateField = make_input_field("ItemPublicationDateField", "Date when the item was published.", InputFieldType.Date)

    ItemTagsList = DataList(name="ItemTagsList", description="Tags for this item", list_sources={TagsDataSource})
    ItemReviewsList = DataList(name="ItemReviewsList", description="Reviews for this item", list_sources={ReviewsDataSource})

    # Buttons for details
    ContactSellerButton = Button(name="ContactSellerButton", description="Start a conversation", label="Contact Seller", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
    StartOrderButton = Button(name="StartOrderButton", description="Create an order", label="Start Order", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)
    SuggestExchangeButton = Button(name="SuggestExchangeButton", description="Suggest an exchange", label="Suggest Exchange", buttonType=ButtonType.TextButton, actionType=ButtonActionType.OpenForm)
    AddReviewButton = Button(name="AddReviewButton", description="Write a review", label="Add Review", buttonType=ButtonType.TextButton, actionType=ButtonActionType.OpenForm)
    BackToItemListButton = Button(name="BackToItemListButton", description="Back to items list", label="Back to Items", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

    # --- Item list elements ---
    ItemsList = DataList(name="ItemsList", description="List of available items", list_sources={ItemsDataSource})
    ViewItemDetailsButton = Button(name="ViewItemDetailsButton", description="Open selected item details", label="View Details", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=ItemDetailsScreen)
    ProfileButton = Button(name="ProfileButton", description="Open user profile", label="Profile", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Navigate, targetScreen=BlankScreen)
    RegisterButton = Button(name="RegisterButton", description="Go to registration", label="Sign up", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=BlankScreen)

    SearchItemsField = make_input_field("SearchItemsField", "Search items", InputFieldType.Search)
    CommunityFilterField = make_input_field("CommunityFilterField", "Filter items by community", InputFieldType.Text)
    StatusFilterField = make_input_field("StatusFilterField", "Filter items by status", InputFieldType.Text)
    TagFilterField = make_input_field("TagFilterField", "Filter items by tag", InputFieldType.Text)
    TransactionTypeFilterField = make_input_field("TransactionTypeFilterField", "Filter by transaction type", InputFieldType.Text)

    # --- Login elements ---
    PhoneLoginButton = Button(name="PhoneLoginButton", description="Sign in with phone", label="Sign in with phone", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Navigate, targetScreen=BlankScreen)
    OAuthLoginButton = Button(name="OAuthLoginButton", description="Sign in with Google", label="Sign in with Google", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Navigate, targetScreen=BlankScreen)
    SubmitLoginButton = Button(name="SubmitLoginButton", description="Submit login", label="Sign in", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)
    EmailFieldLogin = make_input_field("EmailFieldLogin", "Email address used for authentication.", InputFieldType.Email, "required;format:email")
    PasswordFieldLogin = make_input_field("PasswordFieldLogin", "Password", InputFieldType.Password, "required;minLength:8")

    # --- Chat elements ---
    SendImageButton = Button(name="SendImageButton", description="Send image in chat", label="Send Image", buttonType=ButtonType.IconButton, actionType=ButtonActionType.OpenForm)
    OpenChatButton = None

    # --- Payment buttons (created conditionally) ---
    MBWayButton = Button(name="MBWayButton", description="Pay with MBWay", label="Pay with MBWay", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)
    MultibancoButton = Button(name="MultibancoButton", description="Pay with Multibanco", label="Pay with Multibanco", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)
    PayPalButton = Button(name="PayPalButton", description="Pay with PayPal", label="Pay with PayPal", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)

    # ====== Apply DSML rules (add elements to screens) ========
    # Base: ItemDetailsScreen always has title/desc; add price only if priceMode true
    ItemDetailsScreen.view_elements.update({
        ItemTitleField, ItemDescriptionField, ItemStatusField, ItemCommunityField, ItemPublicationDateField, ItemTransactionTypeField,
        ItemTagsList, ItemReviewsList, ContactSellerButton, StartOrderButton, AddReviewButton
    })

    if dsml.listings and getattr(dsml.listings, "priceMode", False):
        ItemDetailsScreen.view_elements.add(ItemPriceField)

    # exchange mode
    if dsml.listings and getattr(dsml.listings, "exchangeMode", False):
        ItemDetailsScreen.view_elements.add(SuggestExchangeButton)

    # donation mode (we will show a badge or field; represented as a simple InputField)
    if dsml.listings and getattr(dsml.listings, "donationMode", False):
        DonationBadge = make_input_field("DonationBadge", "Donation", InputFieldType.Text)
        ItemDetailsScreen.view_elements.add(DonationBadge)

    # expiry
    if dsml.listings and getattr(dsml.listings, "expiry", False):
        ExpiryFilterField = make_input_field("ExpiryFilterField", "Filter by expiry", InputFieldType.Text)
        ItemListScreen.view_elements.add(ExpiryFilterField)

    # variants
    if dsml.listings and getattr(dsml.listings, "variants", False):
        VariantSelector = make_input_field("VariantSelector", "Choose variant", InputFieldType.Text)
        ItemDetailsScreen.view_elements.add(VariantSelector)

    # Add list & list controls to ItemListScreen
    ItemListScreen.view_elements.update({
        ItemsList, ViewItemDetailsButton, ProfileButton, RegisterButton,
        SearchItemsField, StatusFilterField, TagFilterField, TransactionTypeFilterField
    })

    # Community filter presence depends on subcommunities.enabled OR DSML requires it
    if dsml.subcommunities and getattr(dsml.subcommunities, "enabled", False):
        ItemListScreen.view_elements.add(CommunityFilterField)
        # create subcommunity screen
        SubcommunitySelector = SubcommunityScreen
        if SubcommunitySelector:
            # add a sample selector input field
            SubcommunitySelector.view_elements.add(make_input_field("SubcommunitySelectorField", "Select subcommunity", InputFieldType.Text))
    else:
        # no subcommunities -> keep community filter optional if access policy requests it
        if getattr(dsml.accessPolicies, "anonymousBrowse", False) is False:
            ItemListScreen.view_elements.add(CommunityFilterField)

    # Ratings
    if dsml.ratings and (getattr(dsml.ratings, "simple", False) or getattr(dsml.ratings, "bidirectional", False)):
        # add reviews list and add-review button
        ItemDetailsScreen.view_elements.add(AddReviewButton)
        if RatingsListScreen:
            RatingsListScreen.view_elements.add(ItemReviewsList)

    # Messaging: create chat screen + contact seller button
    if dsml.messaging and getattr(dsml.messaging, "chat", False):
        # Add Chat related components
        ChatScreen.view_elements.add(make_input_field("ChatInput", "Type message", InputFieldType.Text))
        if getattr(dsml.messaging, "imagesInChat", False):
            ChatScreen.view_elements.add(SendImageButton)

        # Ensure ContactSellerButton navigates to ChatScreen
        ContactSellerButton.targetScreen = ChatScreen
        ContactSellerButton.actionType = ButtonActionType.Navigate

        OpenChatButton = Button(name="OpenChatButton", description="Open chat with seller", label="Chat", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=ChatScreen)

        # Add OpenChatButton to ItemDetails as well
        ItemDetailsScreen.view_elements.add(OpenChatButton)

    else:
        # If chat disabled, remove contact/open chat buttons
        if ContactSellerButton in ItemDetailsScreen.view_elements:
            ItemDetailsScreen.view_elements.discard(ContactSellerButton)
        if OpenChatButton in ItemDetailsScreen.view_elements:
            ItemDetailsScreen.view_elements.discard(OpenChatButton)

    # Accounts/Login
    login_enabled = dsml.accounts and (getattr(dsml.accounts, "localLogin", False) or getattr(dsml.accounts, "oauthLogin", False) or getattr(dsml.accounts, "phoneVerification", False))
    if login_enabled:
        # add appropriate fields/buttons to LoginScreen
        if dsml.accounts.localLogin:
            LoginScreen.view_elements.update({EmailFieldLogin, PasswordFieldLogin, SubmitLoginButton})
        if dsml.accounts.oauthLogin:
            LoginScreen.view_elements.add(OAuthLoginButton)
        if dsml.accounts.phoneVerification:
            LoginScreen.view_elements.add(PhoneLoginButton)
        # Add LoginButton to item list navigation
        LoginButton = Button(name="LoginButton", description="Open login screen", label="Login", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=LoginScreen)
        ItemListScreen.view_elements.add(LoginButton)
    else:
        # no login methods: if anonymousBrowse false, we still create login? We follow DSML: if anonymousBrowse true -> don't add login
        if not getattr(dsml.accessPolicies, "anonymousBrowse", False):
            # create minimal login if required
            LoginButton = Button(name="LoginButton", description="Open login screen", label="Login", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=BlankScreen)
            ItemListScreen.view_elements.add(LoginButton)

    # Payments: add PaymentScreen and buttons if payment methods enabled
    if PaymentScreen:
        if dsml.payments.mbway:
            PaymentScreen.view_elements.add(MBWayButton)
        if dsml.payments.multibanco:
            PaymentScreen.view_elements.add(MultibancoButton)
        if dsml.payments.paypal:
            PaymentScreen.view_elements.add(PayPalButton)
        # Add a "Pay" button in item details if priceMode true and any payment enabled
        if dsml.listings and getattr(dsml.listings, "priceMode", False):
            ItemDetailsScreen.view_elements.add(Button(name="PayNowButton", description="Pay now", label="Pay Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, targetScreen=PaymentScreen))

    # Logistics options (represent as InputField choices in ItemDetails)
    if dsml.logistics:
        if getattr(dsml.logistics, "inPerson", False):
            ItemDetailsScreen.view_elements.add(make_input_field("LogisticsInPersonOption", "Meet in person", InputFieldType.Text))
        if getattr(dsml.logistics, "mail", False):
            ItemDetailsScreen.view_elements.add(make_input_field("LogisticsMailOption", "Ship item", InputFieldType.Text))
        if getattr(dsml.logistics, "locker", False):
            ItemDetailsScreen.view_elements.add(make_input_field("LogisticsLockerOption", "Use locker", InputFieldType.Text))

    # AccessPolicies: anonymousBrowse and anonymousMessages
    if getattr(dsml.accessPolicies, "anonymousBrowse", False):
        # remove login button if present
        to_remove = [e for e in ItemListScreen.view_elements if isinstance(e, Button) and e.name == "LoginButton"]
        for r in to_remove:
            ItemListScreen.view_elements.discard(r)

    if getattr(dsml.accessPolicies, "anonymousMessages", False):
        # only meaningful if chat enabled
        if dsml.messaging and getattr(dsml.messaging, "chat", False):
            # mark chat as allowing anonymous messages using an ad-hoc field (property)
            # If GUI metamodel supports it, set attribute; else add a note element
            ChatScreen.view_elements.add(make_input_field("ChatAnonymousAllowedNote", "Anonymous messages allowed", InputFieldType.Text))

    # Theme & branding: apply to the viewComponent (if structure allows)
    if dsml.primaryColor:
        # place in viewComponent metadata - best-effort
        try:
            vc.primaryColor = dsml.primaryColor
        except Exception:
            # if field not present, add a small theme descriptor as InputField in the main module
            ThemeNote = make_input_field("ThemeNote", f"Theme: primary={dsml.primaryColor} secondary={dsml.secondaryColor}", InputFieldType.Text)
            ItemListScreen.view_elements.add(ThemeNote)

    # Add screens to module (in appropriate order)
    main_module.screens.add(ItemListScreen)
    main_module.screens.add(ItemDetailsScreen)
    main_module.screens.add(BlankScreen)
    if LoginScreen:
        main_module.screens.add(LoginScreen)
    if ChatScreen:
        main_module.screens.add(ChatScreen)
    if RatingsListScreen:
        main_module.screens.add(RatingsListScreen)
    if PaymentScreen:
        main_module.screens.add(PaymentScreen)
    if SubcommunityScreen:
        main_module.screens.add(SubcommunityScreen)


    # 3) Optionally write to XMI (using BESSER exporter if present)
    if write_xmi:
        if have_xmi_exporter:
            try:
                exporter = XMIExporter()
                exporter.export(gui_model, output_xmi_path)
                log.info(f"Wrote generated GUI XMI to {output_xmi_path}")
            except Exception as e:
                log.error("Failed to write XMI via XMIExporter: %s", e)
        else:
            # fallback: try to use pyecore resource save if GUIModel is an EMF object; otherwise skip
            try:
                # If GUIModel is an EMF object, we can use ResourceSet; otherwise skip
                from pyecore.resources import ResourceSet
                rset = ResourceSet()
                res = rset.create_resource(output_xmi_path)
                res.append(gui_model)
                res.save()
                log.info(f"Wrote generated GUI XMI using pyecore to {output_xmi_path}")
            except Exception:
                log.warning("No XMI exporter available and gui_model is not an EMF resource; skipping XMI write.")

    return gui_model

def write_gui_model_as_python(gui_model: GUIModel, output_path: str):
    """
    Writes a Python file that reconstructs the GUIModel.
    """
    with open(output_path, "w") as f:
        f.write("# Auto-generated GUI model (temporary M2T)\n")
        f.write("from besser.BUML.metamodel.gui import *\n\n")

        f.write(f'gui = GUIModel(\n')
        f.write(f'    name="{gui_model.name}",\n')
        f.write(f'    package="{gui_model.package}",\n')
        f.write(f'    versionCode="{gui_model.versionCode}",\n')
        f.write(f'    versionName="{gui_model.versionName}",\n')
        f.write(f'    description="{gui_model.description}",\n')
        f.write(f'    screenCompatibility={gui_model.screenCompatibility},\n')
        f.write(f'    modules=set()\n')
        f.write(")\n\n")

        for module in gui_model.modules:
            f.write(f'{module.name} = Module(name="{module.name}", screens=set())\n')
            f.write(f'gui.modules.add({module.name})\n\n')

            for screen in module.screens:
                f.write(
                    f'{screen.name} = Screen('
                    f'name="{screen.name}", '
                    f'x_dpi="{screen.x_dpi}", '
                    f'y_dpi="{screen.y_dpi}", '
                    f'screen_size="{screen.screen_size}", '
                    f'view_elements=set(), '
                    f'is_main_page={screen.is_main_page}'
                    f')\n'
                )
                f.write(f'{module.name}.screens.add({screen.name})\n')

                for element in screen.view_elements:
                    f.write(f'# Element: {element}\n')

                f.write("\n")

        f.write("\n# End of generated model\n")



if __name__ == "__main__":
    import sys
    dsml_ecore = "dsml_metamodel.ecore"
    dsml_xmi = "test_custom.xmi"

    dsml_obj = load_dsml_appconfig(dsml_xmi, dsml_ecore)

    gui = generate_gui_from_dsml(
        dsml_obj=dsml_obj,
        write_xmi=True
    )

    write_gui_model_as_python(gui, "generated_gui.py")
    print("generated_gui.py written successfully")

    print(gui)

    print("Generated GUIModel:", gui.name)
