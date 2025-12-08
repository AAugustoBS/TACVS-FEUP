# mypy: ignore-errors
from besser.BUML.metamodel.gui import *  

from structural_community_platform import *

##################################
#      View component            #
##################################

viewComponent: ViewComponent = ViewComponent(
    name="LocalSwapViewComponent",
    description="Local community item exchange app"
)


##################################
#      DATA SOURCE ELEMENTI      #
##################################

# Data source za listu predmeta
ItemsDataSource: DataSourceElement = DataSourceElement(
    name="ItemsDataSource",
    dataSourceClass=Item,
    fields=[
        Item_title,
        Item_description,
        Item_price,
        Item_status,
        Item_publicationDate,
        Item_transactionType
    ] # type: ignore
)

# Data source za tagove
TagsDataSource: DataSourceElement = DataSourceElement(
    name="TagsDataSource",
    dataSourceClass=Tag,
    fields=[
        Tag_name
    ] # type: ignore
)

# Data source za recenzije
ReviewsDataSource: DataSourceElement = DataSourceElement(
    name="ReviewsDataSource",
    dataSourceClass=Review,
    fields=[
        Review_rating,
        Review_comment,
        Review_reviewDate
    ] # type: ignore
)


BlankScreen: Screen = Screen(
    name="BlankScree",
    description="",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    view_elements=set(),
    is_main_page=False
)

# --- Item details screen ---
ContactSellerButton: Button = Button(
    name="ContactSellerButton",
    description="Start a conversation with the seller",
    label="Contact Seller",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.OpenForm
)

StartOrderButton: Button = Button(
    name="StartOrderButton",
    description="Create an order for this item",
    label="Start Order",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.OpenForm
)

SuggestExchangeButton: Button = Button(
    name="SuggestExchangeButton",
    description="Suggest an exchange for this item",
    label="Suggest Exchange",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
)

AddReviewButton: Button = Button(
    name="AddReviewButton",
    description="Write a new review for this item",
    label="Add Review",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
)

BackToItemListButton: Button = Button(
    name="BackToItemListButton",
    description="Return to items list",
    label="Back to Items",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
)

ItemTitleField: InputField = InputField(
    name="ItemTitleField",
    description="Title of the item.",
    type=InputFieldType.Text,
    validationRules="required"
)

ItemDescriptionField: InputField = InputField(
    name="ItemDescriptionField",
    description="Detailed description of the item.",
    type=InputFieldType.Text
)

ItemPriceField: InputField = InputField(
    name="ItemPriceField",
    description="Price of the item (applicable for sale transactions only).",
    type=InputFieldType.Number
)

ItemStatusField: InputField = InputField(
    name="ItemStatusField",
    description="Current status of the item (Available, Sold, Donated, Exchanged, Paused).",
    type=InputFieldType.Text
)

ItemTransactionTypeField: InputField = InputField(
    name="ItemTransactionTypeField",
    description="Transaction type assigned to the item (Donation, Sale, Exchange).",
    type=InputFieldType.Text
)

ItemCommunityField: InputField = InputField(
    name="ItemCommunityField",
    description="Community in which the item is listed or published.",
    type=InputFieldType.Text
)

ItemPublicationDateField: InputField = InputField(
    name="ItemPublicationDateField",
    description="Date when the item was published.",
    type=InputFieldType.Date
)

ItemTagsList: DataList = DataList(
    name="ItemTagsList",
    description="Tags for this item",
    list_sources={TagsDataSource}
)

ItemReviewsList: DataList = DataList(
    name="ItemReviewsList",
    description="Reviews for this item",
    list_sources={ReviewsDataSource}
)

'''
ItemDetailsImage: ImageElement = ImageElement(
    name="ItemDetailsImage",
    description="Main image or preview image for selected item",
    imagePath="assets/images/item_detail.png",
    width=350,
    height=220
)
'''

ItemDetailsScreen: Screen = Screen(
    name="ItemDetailsScreen",
    description="View details of a selected item",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    view_elements={
        ItemTagsList,
        ItemReviewsList,
        ContactSellerButton,
        StartOrderButton,
        SuggestExchangeButton,
        AddReviewButton,
        #BackToItemListButton,
        ItemTitleField, 
        ItemDescriptionField, 
        ItemPriceField, 
        ItemStatusField, 
        ItemCommunityField, 
        ItemPublicationDateField,
        ItemTransactionTypeField,
        #ItemDetailsImage

    },
    is_main_page=False
)


# --- Item list screen ---

ViewItemDetailsButton: Button = Button(
    name="ViewItemDetailsButton",
    description="Open selected item details",
    label="View Details",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate,
    targetScreen=ItemDetailsScreen
)

ProfileButton: Button = Button(
    name="ProfileButton",
    description="Open user profile",
    label="Profile",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Navigate,
    targetScreen=BlankScreen
)

RegisterButton: Button = Button(
    name="RegisterButton",
    description="Go to registration screen",
    label="Sign up",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate,
    targetScreen=BlankScreen
)

LoginButton: Button = Button(
    name="LoginButton",
    description="Go to login screen",
    label="Sign in",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
) 


SearchItemsField: InputField = InputField(
    name="SearchItemsField",
    description="Search items by title or description keywords.",
    type=InputFieldType.Search
)

CommunityFilterField: InputField = InputField(
    name="CommunityFilterField",
    description="Filter items by selected community or faculty.",
    type=InputFieldType.Text
)

StatusFilterField: InputField = InputField(
    name="StatusFilterField",
    description="Filter items based on their status (Available, Sold...).",
    type=InputFieldType.Text
)

TagFilterField: InputField = InputField(
    name="TagFilterField",
    description="Filter items by associated tags or keywords.",
    type=InputFieldType.Text
)

TransactionTypeFilterField: InputField = InputField(
    name="TransactionTypeFilterField",
    description="Filter items by transaction type (Donation, Sale, Exchange).",
    type=InputFieldType.Text
)

ItemsList: DataList = DataList(
    name="ItemsList",
    description="List of available items",
    list_sources={ItemsDataSource}
)

"""
ItemsListImage: ImageElement = ImageElement( # type: ignore
    name="ItemsListImage",
    description="Banner or illustration on top of the items list screen",
    imagePath="assets/images/items_list.png",   # Putanja do slike u aplikaciji
    width=350,
    height=180
)
"""

ItemListScreen: Screen = Screen(
    name="ItemListScreen",
    description="Browse items available in the community",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    view_elements={
        ItemsList,
        ViewItemDetailsButton,
        ProfileButton,
        #LoginButton,
        RegisterButton,
        SearchItemsField, 
        CommunityFilterField, 
        StatusFilterField, 
        TagFilterField, 
        TransactionTypeFilterField,
        #ItemsListImage
    },
    is_main_page=True
)



# --- Login screen ---

PhoneLoginButton: Button = Button(
    name="PhoneLoginButton",
    description="Sign in with phone number",
    label="Sign in with phone number",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Navigate,
    targetScreen=BlankScreen
)

OAuthLoginButton: Button = Button(
    name="OAuthLoginButton",
    description="Sign in with Google account",
    label="Sign in with Google account",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Navigate,   
    targetScreen=BlankScreen
)

SubmitLoginButton: Button = Button(
    name="SubmitLoginButton",
    description="Sign in and open items list",
    label="Sign in",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.OpenForm

)


EmailFieldLogin: InputField = InputField(
    name="EmailFieldLogin",
    description="Email address used for user authentication.",
    type=InputFieldType.Email,

    # Validation rules improved for production-level login form:
    validationRules=(
        "required;"                     # field cannot be empty
        "format:email;"                 # must follow standard email format
        "minLength:6;"                  # minimal meaningful length (e.g. a@b.com)
        "regex:^\\S+@\\S+\\.\\S+$"       # enforces user@domain.tld pattern
    )
)

PasswordFieldLogin: InputField = InputField(
    name="PasswordFieldLogin",
    description="Password used for user authentication.",
    type=InputFieldType.Password,

    # Strong and security-oriented validation policy:
    validationRules=(
        "required;"                     # cannot be submitted blank
        "minLength:8;"                  # minimum standard security length
        "mustContainUpperCase;"         # must include at least one uppercase letter
        "mustContainLowerCase;"         # must include at least one lowercase letter
        "mustContainDigit;"             # must include at least one numeric character
        "mustContainSpecialChars"       # must contain a special symbol (!, @, %, _ ...)
    )
)


LoginScreen: Screen = Screen(
    name="LoginScreen",
    description="Sign in to the community platform",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    view_elements={
        PhoneLoginButton,
        OAuthLoginButton,
        SubmitLoginButton,
        EmailFieldLogin, 
        PasswordFieldLogin 
    },
    is_main_page=False
)



##################################
#            Targets             #
##################################




LoginButton.actionType=  ButtonActionType.Navigate
LoginButton.targetScreen = LoginScreen

BackToItemListButton.actionType=  ButtonActionType.Navigate
BackToItemListButton.targetScreen = ItemListScreen



##################################
#        MODULE & GUI MODEL      #
##################################

MainModule: Module = Module(
    name="MainModule",
    screens={
        LoginScreen,
        ItemListScreen,
        ItemDetailsScreen,
        BlankScreen
    }
)

community_gui_model: GUIModel = GUIModel(
    name="LocalSwapApp",
    package="com.example.community_platform",
    versionCode="1",
    versionName="1.0",
    description="GUI model for the community item exchange platform.",
    screenCompatibility=True,
    modules={MainModule}
)


























