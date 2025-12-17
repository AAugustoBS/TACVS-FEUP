from besser.BUML.metamodel.structural import (
    Class, Property, BinaryAssociation, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    DateTimeType
)

# 1. ENUMERATIONS
ItemState = Enumeration(name='ItemState', literals={
    EnumerationLiteral("Draft"), EnumerationLiteral("Active"), 
    EnumerationLiteral("Reserved"), EnumerationLiteral("Completed"), 
    EnumerationLiteral("Archived")
})

Condition = Enumeration(name='Condition', literals={
    EnumerationLiteral("New"), EnumerationLiteral("LikeNew"), 
    EnumerationLiteral("Good"), EnumerationLiteral("Fair"), 
    EnumerationLiteral("Poor")
})

ItemKind = Enumeration(name='ItemKind', literals={
    EnumerationLiteral("Product"), EnumerationLiteral("Service")
})

ExchangeMode = Enumeration(name='ExchangeMode', literals={
    EnumerationLiteral("Price"), EnumerationLiteral("Exchange"), 
    EnumerationLiteral("Donation")
})

OfferType = Enumeration(name='OfferType', literals={
    EnumerationLiteral("PriceOffer"), EnumerationLiteral("ExchangeOffer"), 
    EnumerationLiteral("Request")
})

OfferStatus = Enumeration(name='OfferStatus', literals={
    EnumerationLiteral("Pending"), EnumerationLiteral("Accepted"), 
    EnumerationLiteral("Rejected"), EnumerationLiteral("Withdrawn"), 
    EnumerationLiteral("Expired")
})

ReservationStatus = Enumeration(name='ReservationStatus', literals={
    EnumerationLiteral("Active"), EnumerationLiteral("Released"), 
    EnumerationLiteral("Expired")
})

TxMode = Enumeration(name='TxMode', literals={
    EnumerationLiteral("Sale"), EnumerationLiteral("Exchange"), 
    EnumerationLiteral("Donation")
})

DeliveryMode = Enumeration(name='DeliveryMode', literals={
    EnumerationLiteral("InPerson"), EnumerationLiteral("Mail"), 
    EnumerationLiteral("Locker")
})

TxStatus = Enumeration(name='TxStatus', literals={
    EnumerationLiteral("Completed"), EnumerationLiteral("Cancelled")
})

MessageKind = Enumeration(name='MessageKind', literals={
    EnumerationLiteral("Text"), EnumerationLiteral("Image"), 
    EnumerationLiteral("System")
})

ReportReason = Enumeration(name='ReportReason', literals={
    EnumerationLiteral("Spam"), EnumerationLiteral("Fraud"), 
    EnumerationLiteral("Offensive"), EnumerationLiteral("Safety"), 
    EnumerationLiteral("Other")
})

ReportStatus = Enumeration(name='ReportStatus', literals={
    EnumerationLiteral("Open"), EnumerationLiteral("UnderReview"), 
    EnumerationLiteral("Resolved"), EnumerationLiteral("Ignored")
})

PaymentMethod = Enumeration(name='PaymentMethod', literals={
    EnumerationLiteral("MBWay"), EnumerationLiteral("Multibanco"), 
    EnumerationLiteral("PayPal"), EnumerationLiteral("NoPayment")
})

UserStatus = Enumeration(name='UserStatus', literals={
    EnumerationLiteral("Active"), EnumerationLiteral("Suspended")
})

# 2. CLASSES
Community = Class(name='Community')
SubCommunity = Class(name='SubCommunity')
User = Class(name='User')
Category = Class(name='Category')
Location = Class(name='Location')
Money = Class(name='Money')
Item = Class(name='Item')
ItemVariant = Class(name='ItemVariant')
Offer = Class(name='Offer')
Reservation = Class(name='Reservation')
Transaction = Class(name='Transaction')
Rating = Class(name='Rating')
Conversation = Class(name='Conversation')
Message = Class(name='Message')
Report = Class(name='Report')
PaymentProvider = Class(name='PaymentProvider')

# 3. ATTRIBUTES
Community.attributes = {
    Property(name='uid', type=StringType), Property(name='name', type=StringType),
    Property(name='description', type=StringType), Property(name='logoUrl', type=StringType),
    Property(name='rulesMarkdown', type=StringType), Property(name='allowSubcommunities', type=BooleanType)
}
SubCommunity.attributes = {
    Property(name='uid', type=StringType), Property(name='name', type=StringType), Property(name='description', type=StringType)
}
User.attributes = {
    Property(name='uid', type=StringType), Property(name='username', type=StringType),
    Property(name='fullName', type=StringType), Property(name='email', type=StringType),
    Property(name='phone', type=StringType), Property(name='avatarUrl', type=StringType),
    Property(name='createdAt', type=DateTimeType), Property(name='isAdmin', type=BooleanType),
    Property(name='isModerator', type=BooleanType), Property(name='avgRating', type=FloatType),
    Property(name='ratingCount', type=IntegerType), Property(name='status', type=UserStatus)
}
Category.attributes = {
    Property(name='uid', type=StringType), Property(name='name', type=StringType), Property(name='icon', type=StringType)
}
Location.attributes = {
    Property(name='uid', type=StringType), Property(name='label', type=StringType),
    Property(name='address', type=StringType), Property(name='lat', type=FloatType), Property(name='lon', type=FloatType)
}
Money.attributes = { Property(name='amount', type=FloatType), Property(name='currency', type=StringType) }
Item.attributes = {
    Property(name='uid', type=StringType), Property(name='title', type=StringType),
    Property(name='description', type=StringType), Property(name='mediaUrls', type=StringType),
    Property(name='tags', type=StringType), Property(name='createdAt', type=DateTimeType),
    Property(name='updatedAt', type=DateTimeType), Property(name='state', type=ItemState),
    Property(name='condition', type=Condition), Property(name='kind', type=ItemKind),
    Property(name='exchangeModes', type=ExchangeMode), Property(name='quantity', type=IntegerType),
    Property(name='unit', type=StringType), Property(name='expiresAt', type=DateTimeType)
}
ItemVariant.attributes = { Property(name='name', type=StringType), Property(name='value', type=StringType) }
Offer.attributes = {
    Property(name='uid', type=StringType), Property(name='type', type=OfferType),
    Property(name='message', type=StringType), Property(name='createdAt', type=DateTimeType), Property(name='status', type=OfferStatus)
}
Reservation.attributes = {
    Property(name='uid', type=StringType), Property(name='reservedFrom', type=DateTimeType),
    Property(name='reservedUntil', type=DateTimeType), Property(name='status', type=ReservationStatus)
}
Transaction.attributes = {
    Property(name='uid', type=StringType), Property(name='closedAt', type=DateTimeType),
    Property(name='mode', type=TxMode), Property(name='delivery', type=DeliveryMode),
    Property(name='receiptUrl', type=StringType), Property(name='paymentMethod', type=PaymentMethod), Property(name='status', type=TxStatus)
}
Rating.attributes = {
    Property(name='uid', type=StringType), Property(name='stars', type=IntegerType),
    Property(name='comment', type=StringType), Property(name='createdAt', type=DateTimeType)
}
Conversation.attributes = { Property(name='uid', type=StringType), Property(name='createdAt', type=DateTimeType) }
Message.attributes = {
    Property(name='uid', type=StringType), Property(name='content', type=StringType),
    Property(name='sentAt', type=DateTimeType), Property(name='kind', type=MessageKind), Property(name='attachments', type=StringType)
}
Report.attributes = {
    Property(name='uid', type=StringType), Property(name='reason', type=ReportReason),
    Property(name='details', type=StringType), Property(name='createdAt', type=DateTimeType), Property(name='status', type=ReportStatus)
}
PaymentProvider.attributes = {
    Property(name='name', type=StringType), Property(name='type', type=StringType),
    Property(name='publicKey', type=StringType), Property(name='secretRef', type=StringType)
}

# 4. ASSOCIATIONS (Following PlantUML names)
minExchangeValue = BinaryAssociation(name='minExchangeValue', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1))
})
offer_amount = BinaryAssociation(name='offer_amount', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1)),
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(1, 1))
})
agreed_price = BinaryAssociation(name='agreed_price', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1)),
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(1, 1))
})
community_subs = BinaryAssociation(name='community_subs', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1)),
    Property(name='SubCommunity', type=SubCommunity, multiplicity=Multiplicity(0, 9999))
})
community_members = BinaryAssociation(name='community_members', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1)),
    Property(name='User', type=User, multiplicity=Multiplicity(0, 9999))
})
community_categories = BinaryAssociation(name='community_categories', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1)),
    Property(name='Category', type=Category, multiplicity=Multiplicity(0, 9999))
})
community_locations = BinaryAssociation(name='community_locations', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1)),
    Property(name='Location', type=Location, multiplicity=Multiplicity(0, 9999))
})
payment_config = BinaryAssociation(name='payment_config', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(0, 1)),
    Property(name='PaymentProvider', type=PaymentProvider, multiplicity=Multiplicity(1, 1))
})
sub_members = BinaryAssociation(name='sub_members', ends={
    Property(name='SubCommunity', type=SubCommunity, multiplicity=Multiplicity(1, 1)),
    Property(name='User', type=User, multiplicity=Multiplicity(0, 9999))
})
sub_items = BinaryAssociation(name='sub_items', ends={
    Property(name='SubCommunity', type=SubCommunity, multiplicity=Multiplicity(1, 1)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999))
})
owned_items = BinaryAssociation(name='owned_items', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999))
})
category_items = BinaryAssociation(name='category_items', ends={
    Property(name='Category', type=Category, multiplicity=Multiplicity(1, 1)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999))
})
location_items = BinaryAssociation(name='location_items', ends={
    Property(name='Location', type=Location, multiplicity=Multiplicity(1, 1)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999))
})
variants = BinaryAssociation(name='variants', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1)),
    Property(name='ItemVariant', type=ItemVariant, multiplicity=Multiplicity(0, 9999))
})
target_item = BinaryAssociation(name='target_item', ends={
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(0, 9999)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1))
})
buyer_user = BinaryAssociation(name='buyer_user', ends={
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(0, 9999)),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1))
})
user_reservations = BinaryAssociation(name='user_reservations', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1)),
    Property(name='Reservation', type=Reservation, multiplicity=Multiplicity(0, 9999))
})
reserved_item = BinaryAssociation(name='reserved_item', ends={
    Property(name='Reservation', type=Reservation, multiplicity=Multiplicity(0, 9999)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1))
})
item_sold_in_tx = BinaryAssociation(name='item_sold_in_tx', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1)),
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(0, 9999))
})
seller_transactions = BinaryAssociation(name='seller_transactions', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1)),
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(0, 9999))
})
ratings_as_rated = BinaryAssociation(name='ratings_as_rated', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1)),
    Property(name='Rating', type=Rating, multiplicity=Multiplicity(0, 9999))
})
reports_against_user = BinaryAssociation(name='reports_against_user', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1)),
    Property(name='Report', type=Report, multiplicity=Multiplicity(0, 9999))
})
target_r_item = BinaryAssociation(name='target_r_item', ends={
    Property(name='Report', type=Report, multiplicity=Multiplicity(0, 9999)),
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 1))
})
item_conversations = BinaryAssociation(name='item_conversations', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1)),
    Property(name='Conversation', type=Conversation, multiplicity=Multiplicity(0, 9999))
})
participated_chats = BinaryAssociation(name='participated_chats', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(2, 9999)),
    Property(name='Conversation', type=Conversation, multiplicity=Multiplicity(0, 9999))
})
messages = BinaryAssociation(name='messages', ends={
    Property(name='Conversation', type=Conversation, multiplicity=Multiplicity(1, 1)),
    Property(name='Message', type=Message, multiplicity=Multiplicity(0, 9999))
})
author = BinaryAssociation(name='author', ends={
    Property(name='Message', type=Message, multiplicity=Multiplicity(0, 9999)),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1))
})

# 5. DOMAIN MODEL
domain_model = DomainModel(name='CustomModel', types={
    Community, SubCommunity, User, Category, Location, Money, Item, ItemVariant, Offer, Reservation, Transaction, Rating, Conversation, Message, Report, PaymentProvider,
    ItemState, Condition, ItemKind, ExchangeMode, OfferType, OfferStatus, ReservationStatus, TxMode, DeliveryMode, TxStatus, MessageKind, ReportReason, ReportStatus, PaymentMethod, UserStatus
}, associations={
    minExchangeValue, offer_amount, agreed_price, community_subs, community_members, community_categories, community_locations, payment_config, sub_members, sub_items, owned_items, category_items, location_items, variants, target_item, buyer_user, user_reservations, reserved_item, item_sold_in_tx, seller_transactions, ratings_as_rated, reports_against_user, target_r_item, item_conversations, participated_chats, messages, author
})