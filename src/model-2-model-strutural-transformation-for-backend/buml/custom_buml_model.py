from besser.BUML.metamodel.structural import *

PaymentMethod = Enumeration(name='PaymentMethod', literals={EnumerationLiteral("NoPayment"), EnumerationLiteral("PayPal"), EnumerationLiteral("Multibanco"), EnumerationLiteral("MBWay")})
Condition = Enumeration(name='Condition', literals={EnumerationLiteral("Poor"), EnumerationLiteral("Good"), EnumerationLiteral("Fair"), EnumerationLiteral("New"), EnumerationLiteral("LikeNew")})
ItemKind = Enumeration(name='ItemKind', literals={EnumerationLiteral("Product"), EnumerationLiteral("Service")})
TxStatus = Enumeration(name='TxStatus', literals={EnumerationLiteral("Cancelled"), EnumerationLiteral("Completed")})
OfferType = Enumeration(name='OfferType', literals={EnumerationLiteral("Request"), EnumerationLiteral("ExchangeOffer"), EnumerationLiteral("PriceOffer")})
UserStatus = Enumeration(name='UserStatus', literals={EnumerationLiteral("Active"), EnumerationLiteral("Suspended")})
MessageKind = Enumeration(name='MessageKind', literals={EnumerationLiteral("System"), EnumerationLiteral("Image"), EnumerationLiteral("Text")})
OfferStatus = Enumeration(name='OfferStatus', literals={EnumerationLiteral("Rejected"), EnumerationLiteral("Withdrawn"), EnumerationLiteral("Expired"), EnumerationLiteral("Pending"), EnumerationLiteral("Accepted")})
ReportReason = Enumeration(name='ReportReason', literals={EnumerationLiteral("Other"), EnumerationLiteral("Spam"), EnumerationLiteral("Fraud"), EnumerationLiteral("Offensive"), EnumerationLiteral("Safety")})
ReservationStatus = Enumeration(name='ReservationStatus', literals={EnumerationLiteral("Released"), EnumerationLiteral("Active"), EnumerationLiteral("Expired")})
ItemState = Enumeration(name='ItemState', literals={EnumerationLiteral("Archived"), EnumerationLiteral("Reserved"), EnumerationLiteral("Completed"), EnumerationLiteral("Draft"), EnumerationLiteral("Active")})
TxMode = Enumeration(name='TxMode', literals={EnumerationLiteral("Exchange"), EnumerationLiteral("Sale"), EnumerationLiteral("Donation")})
ReportStatus = Enumeration(name='ReportStatus', literals={EnumerationLiteral("Open"), EnumerationLiteral("Ignored"), EnumerationLiteral("Resolved"), EnumerationLiteral("UnderReview")})
DeliveryMode = Enumeration(name='DeliveryMode', literals={EnumerationLiteral("Mail"), EnumerationLiteral("InPerson"), EnumerationLiteral("Locker")})
ExchangeMode = Enumeration(name='ExchangeMode', literals={EnumerationLiteral("Donation"), EnumerationLiteral("Exchange"), EnumerationLiteral("Price")})

# Classes
Community = Class(name='Community')
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
Report = Class(name='Report')
PaymentProvider = Class(name='PaymentProvider')

# Attributes
Community.attributes = {Property(name='allowSubcommunities', type=BooleanType, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='name', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='description', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='logoUrl', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='rulesMarkdown', type=StringType, multiplicity=Multiplicity(1, 1))}
User.attributes = {Property(name='createdAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='username', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='isAdmin', type=BooleanType, multiplicity=Multiplicity(1, 1)), Property(name='fullName', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='isModerator', type=BooleanType, multiplicity=Multiplicity(1, 1)), Property(name='email', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='avgRating', type=FloatType, multiplicity=Multiplicity(1, 1)), Property(name='phone', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='status', type=UserStatus, multiplicity=Multiplicity(1, 1)), Property(name='ratingCount', type=IntegerType, multiplicity=Multiplicity(1, 1)), Property(name='avatarUrl', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1))}
Category.attributes = {Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='icon', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='name', type=StringType, multiplicity=Multiplicity(1, 1))}
Location.attributes = {Property(name='lat', type=FloatType, multiplicity=Multiplicity(1, 1)), Property(name='lon', type=FloatType, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='label', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='address', type=StringType, multiplicity=Multiplicity(1, 1))}
Money.attributes = {Property(name='amount', type=FloatType, multiplicity=Multiplicity(1, 1)), Property(name='currency', type=StringType, multiplicity=Multiplicity(1, 1))}
Item.attributes = {Property(name='updatedAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='title', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='unit', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='state', type=ItemState, multiplicity=Multiplicity(1, 1)), Property(name='description', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='expiresAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='condition', type=Condition, multiplicity=Multiplicity(1, 1)), Property(name='mediaUrls', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='kind', type=ItemKind, multiplicity=Multiplicity(1, 1)), Property(name='tags', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='exchangeModes', type=ExchangeMode, multiplicity=Multiplicity(1, 1)), Property(name='createdAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='quantity', type=IntegerType, multiplicity=Multiplicity(1, 1))}
ItemVariant.attributes = {Property(name='name', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='value', type=StringType, multiplicity=Multiplicity(1, 1))}
Offer.attributes = {Property(name='type', type=OfferType, multiplicity=Multiplicity(1, 1)), Property(name='message', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='createdAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='status', type=OfferStatus, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1))}
Reservation.attributes = {Property(name='reservedUntil', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='reservedFrom', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='status', type=ReservationStatus, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1))}
Transaction.attributes = {Property(name='delivery', type=DeliveryMode, multiplicity=Multiplicity(1, 1)), Property(name='receiptUrl', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='paymentMethod', type=PaymentMethod, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='status', type=TxStatus, multiplicity=Multiplicity(1, 1)), Property(name='closedAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='mode', type=TxMode, multiplicity=Multiplicity(1, 1))}
Rating.attributes = {Property(name='comment', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='stars', type=IntegerType, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='createdAt', type=DateTimeType, multiplicity=Multiplicity(1, 1))}
Report.attributes = {Property(name='reason', type=ReportReason, multiplicity=Multiplicity(1, 1)), Property(name='details', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='createdAt', type=DateTimeType, multiplicity=Multiplicity(1, 1)), Property(name='status', type=ReportStatus, multiplicity=Multiplicity(1, 1)), Property(name='uid', type=StringType, multiplicity=Multiplicity(1, 1))}
PaymentProvider.attributes = {Property(name='publicKey', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='type', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='name', type=StringType, multiplicity=Multiplicity(1, 1)), Property(name='secretRef', type=StringType, multiplicity=Multiplicity(1, 1))}

# Associations
minExchangeValue = BinaryAssociation(name='minExchangeValue', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
buyer_user = BinaryAssociation(name='buyer_user', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(0, 9999), is_navigable=False)
})
reports_against_user = BinaryAssociation(name='reports_against_user', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
    Property(name='Report', type=Report, multiplicity=Multiplicity(0, 9999), is_navigable=True)
})
payment_config = BinaryAssociation(name='payment_config', ends={
    Property(name='Community', type=Community, multiplicity=Multiplicity(0, 1), is_navigable=False),
    Property(name='PaymentProvider', type=PaymentProvider, multiplicity=Multiplicity(1, 1), is_navigable=True)
})
target_r_item = BinaryAssociation(name='target_r_item', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 1), is_navigable=True),
    Property(name='Report', type=Report, multiplicity=Multiplicity(0, 9999), is_navigable=False)
})
owned_items = BinaryAssociation(name='owned_items', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
user_reservations = BinaryAssociation(name='user_reservations', ends={
    Property(name='Reservation', type=Reservation, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
location_items = BinaryAssociation(name='location_items', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Location', type=Location, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
community_members = BinaryAssociation(name='community_members', ends={
    Property(name='User', type=User, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
category_items = BinaryAssociation(name='category_items', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Category', type=Category, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
reserved_item = BinaryAssociation(name='reserved_item', ends={
    Property(name='Reservation', type=Reservation, multiplicity=Multiplicity(0, 9999), is_navigable=False),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1), is_navigable=True)
})
variants = BinaryAssociation(name='variants', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False),
    Property(name='ItemVariant', type=ItemVariant, multiplicity=Multiplicity(0, 9999), is_navigable=True)
})
community_categories = BinaryAssociation(name='community_categories', ends={
    Property(name='Category', type=Category, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
offer_amount = BinaryAssociation(name='offer_amount', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
item_sold_in_tx = BinaryAssociation(name='item_sold_in_tx', ends={
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
target_item = BinaryAssociation(name='target_item', ends={
    Property(name='Item', type=Item, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name='Offer', type=Offer, multiplicity=Multiplicity(0, 9999), is_navigable=False)
})
ratings_as_rated = BinaryAssociation(name='ratings_as_rated', ends={
    Property(name='Rating', type=Rating, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
community_locations = BinaryAssociation(name='community_locations', ends={
    Property(name='Location', type=Location, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='Community', type=Community, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
agreed_price = BinaryAssociation(name='agreed_price', ends={
    Property(name='Money', type=Money, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(1, 1), is_navigable=False)
})
seller_transactions = BinaryAssociation(name='seller_transactions', ends={
    Property(name='Transaction', type=Transaction, multiplicity=Multiplicity(0, 9999), is_navigable=True),
    Property(name='User', type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
})

domain_model = DomainModel(name='CustomModel', types={Community, User, Category, Location, Money, Item, ItemVariant, Offer, Reservation, Transaction, Rating, Report, PaymentProvider, PaymentMethod, Condition, ItemKind, TxStatus, OfferType, UserStatus, MessageKind, OfferStatus, ReportReason, ReservationStatus, ItemState, TxMode, ReportStatus, DeliveryMode, ExchangeMode}, associations={minExchangeValue, buyer_user, reports_against_user, payment_config, target_r_item, owned_items, user_reservations, location_items, community_members, category_items, reserved_item, variants, community_categories, offer_amount, item_sold_in_tx, target_item, ratings_as_rated, community_locations, agreed_price, seller_transactions})
