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
ItemState: Enumeration = Enumeration(
    name="ItemState",
    literals={
            EnumerationLiteral(name="Draft"),
			EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Reserved"),
			EnumerationLiteral(name="Completed"),
			EnumerationLiteral(name="Archived")
    }
)

Condition: Enumeration = Enumeration(
    name="Condition",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="LikeNew"),
			EnumerationLiteral(name="Good"),
			EnumerationLiteral(name="Fair"),
			EnumerationLiteral(name="Poor")
    }
)

ItemKind: Enumeration = Enumeration(
    name="ItemKind",
    literals={
            EnumerationLiteral(name="Product"),
			EnumerationLiteral(name="Service")
    }
)

ExchangeMode: Enumeration = Enumeration(
    name="ExchangeMode",
    literals={
            EnumerationLiteral(name="Price"),
			EnumerationLiteral(name="Exchange"),
			EnumerationLiteral(name="Donation")
    }
)

OfferType: Enumeration = Enumeration(
    name="OfferType",
    literals={
            EnumerationLiteral(name="PriceOffer"),
			EnumerationLiteral(name="ExchangeOffer"),
			EnumerationLiteral(name="Request")
    }
)

OfferStatus: Enumeration = Enumeration(
    name="OfferStatus",
    literals={
            EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="Accepted"),
			EnumerationLiteral(name="Rejected"),
			EnumerationLiteral(name="Withdrawn"),
			EnumerationLiteral(name="Expired")
    }
)

ReservationStatus: Enumeration = Enumeration(
    name="ReservationStatus",
    literals={
            EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Released"),
			EnumerationLiteral(name="Expired")
    }
)

TxMode: Enumeration = Enumeration(
    name="TxMode",
    literals={
            EnumerationLiteral(name="Sale"),
			EnumerationLiteral(name="Exchange"),
			EnumerationLiteral(name="Donation")
    }
)

DeliveryMode: Enumeration = Enumeration(
    name="DeliveryMode",
    literals={
            EnumerationLiteral(name="InPerson"),
			EnumerationLiteral(name="Mail"),
			EnumerationLiteral(name="Locker")
    }
)

TxStatus: Enumeration = Enumeration(
    name="TxStatus",
    literals={
            EnumerationLiteral(name="Completed"),
			EnumerationLiteral(name="Cancelled")
    }
)

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Image"),
			EnumerationLiteral(name="System")
    }
)

ReportReason: Enumeration = Enumeration(
    name="ReportReason",
    literals={
            EnumerationLiteral(name="Spam"),
			EnumerationLiteral(name="Fraud"),
			EnumerationLiteral(name="Offensive"),
			EnumerationLiteral(name="Safety"),
			EnumerationLiteral(name="Other")
    }
)

ReportStatus: Enumeration = Enumeration(
    name="ReportStatus",
    literals={
            EnumerationLiteral(name="Open"),
			EnumerationLiteral(name="UnderReview"),
			EnumerationLiteral(name="Resolved"),
			EnumerationLiteral(name="Ignored")
    }
)

PaymentMethod: Enumeration = Enumeration(
    name="PaymentMethod",
    literals={
            EnumerationLiteral(name="MBWay"),
			EnumerationLiteral(name="Multibanco"),
			EnumerationLiteral(name="PayPal"),
			EnumerationLiteral(name="NoPayment")
    }
)

UserStatus: Enumeration = Enumeration(
    name="UserStatus",
    literals={
            EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Suspended")
    }
)

# Classes
Community = Class(name="Community")
SubCommunity = Class(name="SubCommunity")
User = Class(name="User")
Category = Class(name="Category")
Location = Class(name="Location")
Money = Class(name="Money")
Item = Class(name="Item")
ItemVariant = Class(name="ItemVariant")
Offer = Class(name="Offer")
Reservation = Class(name="Reservation")
Transaction = Class(name="Transaction")
Rating = Class(name="Rating")
Conversation = Class(name="Conversation")
Message = Class(name="Message")
Report = Class(name="Report")
PaymentProvider = Class(name="PaymentProvider")

# Community class attributes and methods
Community_uid: Property = Property(name="uid", type=StringType)
Community_name: Property = Property(name="name", type=StringType)
Community_description: Property = Property(name="description", type=StringType)
Community_logoUrl: Property = Property(name="logoUrl", type=StringType)
Community_rulesMarkdown: Property = Property(name="rulesMarkdown", type=StringType)
Community_allowSubcommunities: Property = Property(name="allowSubcommunities", type=BooleanType)
Community.attributes={Community_description, Community_rulesMarkdown, Community_uid, Community_allowSubcommunities, Community_logoUrl, Community_name}

# SubCommunity class attributes and methods
SubCommunity_uid: Property = Property(name="uid", type=StringType)
SubCommunity_name: Property = Property(name="name", type=StringType)
SubCommunity_description: Property = Property(name="description", type=StringType)
SubCommunity.attributes={SubCommunity_description, SubCommunity_name, SubCommunity_uid}

# User class attributes and methods
User_status: Property = Property(name="status", type=UserStatus)
User_uid: Property = Property(name="uid", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_fullName: Property = Property(name="fullName", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_phone: Property = Property(name="phone", type=StringType)
User_avatarUrl: Property = Property(name="avatarUrl", type=StringType)
User_createdAt: Property = Property(name="createdAt", type=DateTimeType)
User_isAdmin: Property = Property(name="isAdmin", type=BooleanType)
User_isModerator: Property = Property(name="isModerator", type=BooleanType)
User_avgRating: Property = Property(name="avgRating", type=FloatType)
User_ratingCount: Property = Property(name="ratingCount", type=IntegerType)
User.attributes={User_avatarUrl, User_ratingCount, User_username, User_fullName, User_isAdmin, User_phone, User_isModerator, User_createdAt, User_avgRating, User_uid, User_status, User_email}

# Category class attributes and methods
Category_uid: Property = Property(name="uid", type=StringType)
Category_name: Property = Property(name="name", type=StringType)
Category_icon: Property = Property(name="icon", type=StringType)
Category.attributes={Category_uid, Category_name, Category_icon}

# Location class attributes and methods
Location_uid: Property = Property(name="uid", type=StringType)
Location_label: Property = Property(name="label", type=StringType)
Location_address: Property = Property(name="address", type=StringType)
Location_lat: Property = Property(name="lat", type=FloatType)
Location_lon: Property = Property(name="lon", type=FloatType)
Location.attributes={Location_lat, Location_uid, Location_lon, Location_label, Location_address}

# Money class attributes and methods
Money_amount: Property = Property(name="amount", type=FloatType)
Money_currency: Property = Property(name="currency", type=StringType)
Money.attributes={Money_currency, Money_amount}

# Item class attributes and methods
Item_uid: Property = Property(name="uid", type=StringType)
Item_title: Property = Property(name="title", type=StringType)
Item_description: Property = Property(name="description", type=StringType)
Item_mediaUrls: Property = Property(name="mediaUrls", type=StringType)
Item_tags: Property = Property(name="tags", type=StringType)
Item_createdAt: Property = Property(name="createdAt", type=DateTimeType)
Item_updatedAt: Property = Property(name="updatedAt", type=DateTimeType)
Item_state: Property = Property(name="state", type=ItemState)
Item_condition: Property = Property(name="condition", type=Condition)
Item_kind: Property = Property(name="kind", type=ItemKind)
Item_exchangeModes: Property = Property(name="exchangeModes", type=ExchangeMode)
Item_quantity: Property = Property(name="quantity", type=IntegerType)
Item_unit: Property = Property(name="unit", type=StringType)
Item_expiresAt: Property = Property(name="expiresAt", type=DateTimeType)
Item.attributes={Item_kind, Item_createdAt, Item_quantity, Item_title, Item_condition, Item_updatedAt, Item_expiresAt, Item_tags, Item_state, Item_description, Item_unit, Item_exchangeModes, Item_uid, Item_mediaUrls}

# ItemVariant class attributes and methods
ItemVariant_name: Property = Property(name="name", type=StringType)
ItemVariant_value: Property = Property(name="value", type=StringType)
ItemVariant.attributes={ItemVariant_value, ItemVariant_name}

# Offer class attributes and methods
Offer_uid: Property = Property(name="uid", type=StringType)
Offer_type: Property = Property(name="type", type=OfferType)
Offer_message: Property = Property(name="message", type=StringType)
Offer_createdAt: Property = Property(name="createdAt", type=DateTimeType)
Offer_status: Property = Property(name="status", type=OfferStatus)
Offer.attributes={Offer_uid, Offer_message, Offer_status, Offer_createdAt, Offer_type}

# Reservation class attributes and methods
Reservation_reservedFrom: Property = Property(name="reservedFrom", type=DateTimeType)
Reservation_reservedUntil: Property = Property(name="reservedUntil", type=DateTimeType)
Reservation_uid: Property = Property(name="uid", type=StringType)
Reservation_status: Property = Property(name="status", type=ReservationStatus)
Reservation.attributes={Reservation_status, Reservation_reservedUntil, Reservation_uid, Reservation_reservedFrom}

# Transaction class attributes and methods
Transaction_uid: Property = Property(name="uid", type=StringType)
Transaction_closedAt: Property = Property(name="closedAt", type=DateTimeType)
Transaction_mode: Property = Property(name="mode", type=TxMode)
Transaction_delivery: Property = Property(name="delivery", type=DeliveryMode)
Transaction_receiptUrl: Property = Property(name="receiptUrl", type=StringType)
Transaction_paymentMethod: Property = Property(name="paymentMethod", type=PaymentMethod)
Transaction_status: Property = Property(name="status", type=TxStatus)
Transaction.attributes={Transaction_status, Transaction_uid, Transaction_delivery, Transaction_mode, Transaction_receiptUrl, Transaction_closedAt, Transaction_paymentMethod}

# Rating class attributes and methods
Rating_uid: Property = Property(name="uid", type=StringType)
Rating_stars: Property = Property(name="stars", type=IntegerType)
Rating_comment: Property = Property(name="comment", type=StringType)
Rating_createdAt: Property = Property(name="createdAt", type=DateTimeType)
Rating.attributes={Rating_stars, Rating_comment, Rating_createdAt, Rating_uid}

# Conversation class attributes and methods
Conversation_uid: Property = Property(name="uid", type=StringType)
Conversation_createdAt: Property = Property(name="createdAt", type=DateTimeType)
Conversation.attributes={Conversation_createdAt, Conversation_uid}

# Message class attributes and methods
Message_uid: Property = Property(name="uid", type=StringType)
Message_content: Property = Property(name="content", type=StringType)
Message_sentAt: Property = Property(name="sentAt", type=DateTimeType)
Message_kind: Property = Property(name="kind", type=MessageKind)
Message_attachments: Property = Property(name="attachments", type=StringType)
Message.attributes={Message_sentAt, Message_kind, Message_attachments, Message_uid, Message_content}

# Report class attributes and methods
Report_uid: Property = Property(name="uid", type=StringType)
Report_reason: Property = Property(name="reason", type=ReportReason)
Report_details: Property = Property(name="details", type=StringType)
Report_createdAt: Property = Property(name="createdAt", type=DateTimeType)
Report_status: Property = Property(name="status", type=ReportStatus)
Report.attributes={Report_details, Report_status, Report_uid, Report_reason, Report_createdAt}

# PaymentProvider class attributes and methods
PaymentProvider_name: Property = Property(name="name", type=StringType)
PaymentProvider_type: Property = Property(name="type", type=StringType)
PaymentProvider_publicKey: Property = Property(name="publicKey", type=StringType)
PaymentProvider_secretRef: Property = Property(name="secretRef", type=StringType)
PaymentProvider.attributes={PaymentProvider_publicKey, PaymentProvider_name, PaymentProvider_type, PaymentProvider_secretRef}

# Relationships
minExchangeValue: BinaryAssociation = BinaryAssociation(
    name="minExchangeValue",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Money", type=Money, multiplicity=Multiplicity(1, 1))
    }
)
owned_items: BinaryAssociation = BinaryAssociation(
    name="owned_items",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
category_items: BinaryAssociation = BinaryAssociation(
    name="category_items",
    ends={
        Property(name="Category", type=Category, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
offer_amount: BinaryAssociation = BinaryAssociation(
    name="offer_amount",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Money", type=Money, multiplicity=Multiplicity(1, 1))
    }
)
agreed_price: BinaryAssociation = BinaryAssociation(
    name="agreed_price",
    ends={
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Money", type=Money, multiplicity=Multiplicity(1, 1))
    }
)
community_subs: BinaryAssociation = BinaryAssociation(
    name="community_subs",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(0, 9999))
    }
)
community_members: BinaryAssociation = BinaryAssociation(
    name="community_members",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
community_categories: BinaryAssociation = BinaryAssociation(
    name="community_categories",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Category", type=Category, multiplicity=Multiplicity(0, 9999))
    }
)
community_locations: BinaryAssociation = BinaryAssociation(
    name="community_locations",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Location", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
payment_config: BinaryAssociation = BinaryAssociation(
    name="payment_config",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(0, 1), is_navigable=False),
        Property(name="PaymentProvider", type=PaymentProvider, multiplicity=Multiplicity(1, 1))
    }
)
sub_members: BinaryAssociation = BinaryAssociation(
    name="sub_members",
    ends={
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
sub_items: BinaryAssociation = BinaryAssociation(
    name="sub_items",
    ends={
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
ratings_as_rated: BinaryAssociation = BinaryAssociation(
    name="ratings_as_rated",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Rating", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
reports_against_user: BinaryAssociation = BinaryAssociation(
    name="reports_against_user",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Report", type=Report, multiplicity=Multiplicity(0, 9999))
    }
)
location_items: BinaryAssociation = BinaryAssociation(
    name="location_items",
    ends={
        Property(name="Location", type=Location, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
variants: BinaryAssociation = BinaryAssociation(
    name="variants",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="ItemVariant", type=ItemVariant, multiplicity=Multiplicity(0, 9999))
    }
)
target_item: BinaryAssociation = BinaryAssociation(
    name="target_item",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
buyer_user: BinaryAssociation = BinaryAssociation(
    name="buyer_user",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
user_reservations: BinaryAssociation = BinaryAssociation(
    name="user_reservations",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Reservation", type=Reservation, multiplicity=Multiplicity(0, 9999))
    }
)
reserved_item: BinaryAssociation = BinaryAssociation(
    name="reserved_item",
    ends={
        Property(name="Reservation", type=Reservation, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
item_sold_in_tx: BinaryAssociation = BinaryAssociation(
    name="item_sold_in_tx",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
seller_transactions: BinaryAssociation = BinaryAssociation(
    name="seller_transactions",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
target_r_item: BinaryAssociation = BinaryAssociation(
    name="target_r_item",
    ends={
        Property(name="Report", type=Report, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
item_conversations: BinaryAssociation = BinaryAssociation(
    name="item_conversations",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(0, 9999))
    }
)
participated_chats: BinaryAssociation = BinaryAssociation(
    name="participated_chats",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(2, 9999), is_navigable=False),
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(0, 9999))
    }
)
messages: BinaryAssociation = BinaryAssociation(
    name="messages",
    ends={
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Message", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
author: BinaryAssociation = BinaryAssociation(
    name="author",
    ends={
        Property(name="Message", type=Message, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Community, SubCommunity, User, Category, Location, Money, Item, ItemVariant, Offer, Reservation, Transaction, Rating, Conversation, Message, Report, PaymentProvider, ItemState, Condition, ItemKind, ExchangeMode, OfferType, OfferStatus, ReservationStatus, TxMode, DeliveryMode, TxStatus, MessageKind, ReportReason, ReportStatus, PaymentMethod, UserStatus},
    associations={minExchangeValue, owned_items, category_items, offer_amount, agreed_price, community_subs, community_members, community_categories, community_locations, payment_config, sub_members, sub_items, ratings_as_rated, reports_against_user, location_items, variants, target_item, buyer_user, user_reservations, reserved_item, item_sold_in_tx, seller_transactions, target_r_item, item_conversations, participated_chats, messages, author},
    generalizations={},
    metadata=None
)
