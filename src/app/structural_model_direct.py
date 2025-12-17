from __future__ import annotations

# Auto-generated: Structural B-UML model (BESSER-compatible) built WITHOUT the PlantUML grammar.
# Reason: the BESSER PlantUML parser supports only a restricted subset of PlantUML; this script
# parses your original PlantUML and builds the DomainModel directly using B-UML meta-classes.

from besser.BUML.metamodel.structural import (
    Class, Property, BinaryAssociation, DomainModel, Enumeration, EnumerationLiteral,
    Multiplicity,
    StringType, IntegerType, FloatType, BooleanType, TimeType, DateType, DateTimeType,
    Constraint
)

# Raw OCL (kept for the validation step in the M2M pipeline)
OCL_TEXT = r"""context User inv UsernameUniqueInCommunity:
  User.allInstances()->forAll(u1, u2 | u1 <> u2 and u1.community = u2.community implies u1.username <> u2.username)

context Money inv NonNegative:
  self.amount >= 0

context Item inv PriceRequiredWhenForSale:
  self.exchangeModes->includes(ExchangeMode::Price) implies self.price.oclIsDefined()

context Item inv ExclusiveGiveawayPricing:
  self.exchangeModes = Set{ExchangeMode::Giveaway} implies self.price.oclIsUndefined()

context Item inv QuantityPositive:
  self.quantity >= 1

context Offer inv AmountRequiredForPriceOffer:
  self.type = OfferType::PriceOffer implies self.amount.oclIsDefined() and self.amount.amount > 0

context Reservation inv ValidPeriod:
  self.reservedUntil > self.reservedFrom

context ChatThread inv TwoOrMoreParticipants:
  self.participants->size() >= 2

context Rating inv StarsBetween1And5:
  self.stars >= 1 and self.stars <= 5

context Transaction inv ConsistentModeAndPrice:
  (self.mode = TxMode::Sale implies self.agreedPrice.oclIsDefined()) and
  (self.mode <> TxMode::Sale implies self.agreedPrice.oclIsUndefined() or self.agreedPrice.amount = 0)

context Report inv AtLeastOneTarget:
  not (self.reported.oclIsUndefined() and self.item.oclIsUndefined())

-- Derived user reputation (generated)
context User
def: ratingCount : Integer = self.Rating->size()
def: avgRating : Real =
  if self.ratingCount = 0 then 0
  else self.Rating->collect(stars)->sum().toReal() / self.ratingCount
  endif"""

# =====================
# Enumerations
# =====================
ItemState = Enumeration(name="ItemState")
ItemState_Draft = EnumerationLiteral(name="Draft")
ItemState_Active = EnumerationLiteral(name="Active")
ItemState_Reserved = EnumerationLiteral(name="Reserved")
ItemState_Completed = EnumerationLiteral(name="Completed")
ItemState_Archived = EnumerationLiteral(name="Archived")
ItemState.literals = {ItemState_Draft, ItemState_Active, ItemState_Reserved, ItemState_Completed, ItemState_Archived}

Condition = Enumeration(name="Condition")
Condition_New = EnumerationLiteral(name="New")
Condition_LikeNew = EnumerationLiteral(name="LikeNew")
Condition_Good = EnumerationLiteral(name="Good")
Condition_Fair = EnumerationLiteral(name="Fair")
Condition_Poor = EnumerationLiteral(name="Poor")
Condition.literals = {Condition_New, Condition_LikeNew, Condition_Good, Condition_Fair, Condition_Poor}

ItemKind = Enumeration(name="ItemKind")
ItemKind_Product = EnumerationLiteral(name="Product")
ItemKind_Service = EnumerationLiteral(name="Service")
ItemKind.literals = {ItemKind_Product, ItemKind_Service}

ExchangeMode = Enumeration(name="ExchangeMode")
ExchangeMode_Price = EnumerationLiteral(name="Price")
ExchangeMode_Exchange = EnumerationLiteral(name="Exchange")
ExchangeMode_Donation = EnumerationLiteral(name="Donation")
ExchangeMode.literals = {ExchangeMode_Price, ExchangeMode_Exchange, ExchangeMode_Donation}

OfferType = Enumeration(name="OfferType")
OfferType_PriceOffer = EnumerationLiteral(name="PriceOffer")
OfferType_ExchangeOffer = EnumerationLiteral(name="ExchangeOffer")
OfferType_Request = EnumerationLiteral(name="Request")
OfferType.literals = {OfferType_PriceOffer, OfferType_ExchangeOffer, OfferType_Request}

OfferStatus = Enumeration(name="OfferStatus")
OfferStatus_Pending = EnumerationLiteral(name="Pending")
OfferStatus_Accepted = EnumerationLiteral(name="Accepted")
OfferStatus_Rejected = EnumerationLiteral(name="Rejected")
OfferStatus_Withdrawn = EnumerationLiteral(name="Withdrawn")
OfferStatus_Expired = EnumerationLiteral(name="Expired")
OfferStatus.literals = {OfferStatus_Pending, OfferStatus_Accepted, OfferStatus_Rejected, OfferStatus_Withdrawn, OfferStatus_Expired}

ReservationStatus = Enumeration(name="ReservationStatus")
ReservationStatus_Active = EnumerationLiteral(name="Active")
ReservationStatus_Released = EnumerationLiteral(name="Released")
ReservationStatus_Expired = EnumerationLiteral(name="Expired")
ReservationStatus.literals = {ReservationStatus_Active, ReservationStatus_Released, ReservationStatus_Expired}

TxMode = Enumeration(name="TxMode")
TxMode_Sale = EnumerationLiteral(name="Sale")
TxMode_Exchange = EnumerationLiteral(name="Exchange")
TxMode_Donation = EnumerationLiteral(name="Donation")
TxMode.literals = {TxMode_Sale, TxMode_Exchange, TxMode_Donation}

DeliveryMode = Enumeration(name="DeliveryMode")
DeliveryMode_InPerson = EnumerationLiteral(name="InPerson")
DeliveryMode_Mail = EnumerationLiteral(name="Mail")
DeliveryMode_Locker = EnumerationLiteral(name="Locker")
DeliveryMode.literals = {DeliveryMode_InPerson, DeliveryMode_Mail, DeliveryMode_Locker}

TxStatus = Enumeration(name="TxStatus")
TxStatus_Completed = EnumerationLiteral(name="Completed")
TxStatus_Cancelled = EnumerationLiteral(name="Cancelled")
TxStatus.literals = {TxStatus_Completed, TxStatus_Cancelled}

MessageKind = Enumeration(name="MessageKind")
MessageKind_Text = EnumerationLiteral(name="Text")
MessageKind_Image = EnumerationLiteral(name="Image")
MessageKind_System = EnumerationLiteral(name="System")
MessageKind.literals = {MessageKind_Text, MessageKind_Image, MessageKind_System}

ReportReason = Enumeration(name="ReportReason")
ReportReason_Spam = EnumerationLiteral(name="Spam")
ReportReason_Fraud = EnumerationLiteral(name="Fraud")
ReportReason_Offensive = EnumerationLiteral(name="Offensive")
ReportReason_Safety = EnumerationLiteral(name="Safety")
ReportReason_Other = EnumerationLiteral(name="Other")
ReportReason.literals = {ReportReason_Spam, ReportReason_Fraud, ReportReason_Offensive, ReportReason_Safety, ReportReason_Other}

ReportStatus = Enumeration(name="ReportStatus")
ReportStatus_Open = EnumerationLiteral(name="Open")
ReportStatus_UnderReview = EnumerationLiteral(name="UnderReview")
ReportStatus_Resolved = EnumerationLiteral(name="Resolved")
ReportStatus_Ignored = EnumerationLiteral(name="Ignored")
ReportStatus.literals = {ReportStatus_Open, ReportStatus_UnderReview, ReportStatus_Resolved, ReportStatus_Ignored}

PaymentMethod = Enumeration(name="PaymentMethod")
PaymentMethod_MBWay = EnumerationLiteral(name="MBWay")
PaymentMethod_Multibanco = EnumerationLiteral(name="Multibanco")
PaymentMethod_PayPal = EnumerationLiteral(name="PayPal")
PaymentMethod_None = EnumerationLiteral(name="None")
PaymentMethod.literals = {PaymentMethod_MBWay, PaymentMethod_Multibanco, PaymentMethod_PayPal, PaymentMethod_None}

# Added: UserStatus (from inline enum in PlantUML)
UserStatus = Enumeration(name="UserStatus")
UserStatus_Active = EnumerationLiteral(name="Active")
UserStatus_Suspended = EnumerationLiteral(name="Suspended")
UserStatus.literals = {UserStatus_Active, UserStatus_Suspended}


# =====================
# Classes
# =====================
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

# =====================
# Attributes
# =====================
Community_id = Property(name="id", type=StringType)
Community_name = Property(name="name", type=StringType)
Community_description = Property(name="description", type=StringType)
Community_logoUrl = Property(name="logoUrl", type=StringType)
Community_rulesMarkdown = Property(name="rulesMarkdown", type=StringType)
Community_allowSubcommunities = Property(name="allowSubcommunities", type=BooleanType)
Community.attributes = {Community_id, Community_name, Community_description, Community_logoUrl, Community_rulesMarkdown, Community_allowSubcommunities}

SubCommunity_id = Property(name="id", type=StringType)
SubCommunity_name = Property(name="name", type=StringType)
SubCommunity_description = Property(name="description", type=StringType)
SubCommunity.attributes = {SubCommunity_id, SubCommunity_name, SubCommunity_description}

User_id = Property(name="id", type=StringType)
User_username = Property(name="username", type=StringType)
User_fullName = Property(name="fullName", type=StringType)
User_email = Property(name="email", type=StringType)
User_phone = Property(name="phone", type=StringType)
User_avatarUrl = Property(name="avatarUrl", type=StringType)
User_createdAt = Property(name="createdAt", type=DateTimeType)
User_isAdmin = Property(name="isAdmin", type=BooleanType)
User_isModerator = Property(name="isModerator", type=BooleanType)
User_avgRating = Property(name="avgRating", type=FloatType)
User_avgRating.isDerived = True
User_ratingCount = Property(name="ratingCount", type=IntegerType)
User_ratingCount.isDerived = True
User_status = Property(name="status", type=UserStatus)
User_avgRating = Property(name="avgRating", type=FloatType)
User_avgRating.isDerived = True

Category_id = Property(name="id", type=StringType)
Category_name = Property(name="name", type=StringType)
Category_icon = Property(name="icon", type=StringType)
Category.attributes = {Category_id, Category_name, Category_icon}

Location_id = Property(name="id", type=StringType)
Location_label = Property(name="label", type=StringType)
Location_address = Property(name="address", type=StringType)
Location_lat = Property(name="lat", type=FloatType)
Location_lon = Property(name="lon", type=FloatType)
Location.attributes = {Location_id, Location_label, Location_address, Location_lat, Location_lon}

Money_amount = Property(name="amount", type=FloatType)
Money_currency = Property(name="currency", type=StringType)
Money.attributes = {Money_amount, Money_currency}

Item_id = Property(name="id", type=StringType)
Item_title = Property(name="title", type=StringType)
Item_description = Property(name="description", type=StringType)
Item_mediaUrls = Property(name="mediaUrls", type=StringType, multiplicity=Multiplicity(0, 9999))
Item_tags = Property(name="tags", type=StringType, multiplicity=Multiplicity(0, 9999))
Item_createdAt = Property(name="createdAt", type=DateTimeType)
Item_updatedAt = Property(name="updatedAt", type=DateTimeType)
Item_state = Property(name="state", type=ItemState)
Item_condition = Property(name="condition", type=Condition)
Item_kind = Property(name="kind", type=ItemKind)
Item_exchangeModes = Property(name="exchangeModes", type=ExchangeMode, multiplicity=Multiplicity(0, 9999))
Item_quantity = Property(name="quantity", type=IntegerType)
Item_unit = Property(name="unit", type=StringType)
Item_price = Property(name="price", type=Money)
Item_minExchangeValue = Property(name="minExchangeValue", type=Money)
Item_expiresAt = Property(name="expiresAt", type=DateType)
Item.attributes = {Item_id, Item_title, Item_description, Item_mediaUrls, Item_tags, Item_createdAt, Item_updatedAt, Item_state, Item_condition, Item_kind, Item_exchangeModes, Item_quantity, Item_unit, Item_price, Item_minExchangeValue, Item_expiresAt}

ItemVariant_name = Property(name="name", type=StringType)
ItemVariant_value = Property(name="value", type=StringType)
ItemVariant.attributes = {ItemVariant_name, ItemVariant_value}

Offer_id = Property(name="id", type=StringType)
Offer_type = Property(name="type", type=OfferType)
Offer_amount = Property(name="amount", type=Money)
Offer_message = Property(name="message", type=StringType)
Offer_createdAt = Property(name="createdAt", type=DateTimeType)
Offer_status = Property(name="status", type=OfferStatus)
Offer.attributes = {Offer_id, Offer_type, Offer_amount, Offer_message, Offer_createdAt, Offer_status}

Reservation_id = Property(name="id", type=StringType)
Reservation_reservedFrom = Property(name="reservedFrom", type=DateTimeType)
Reservation_reservedUntil = Property(name="reservedUntil", type=DateTimeType)
Reservation_status = Property(name="status", type=ReservationStatus)
Reservation.attributes = {Reservation_id, Reservation_reservedFrom, Reservation_reservedUntil, Reservation_status}

Transaction_id = Property(name="id", type=StringType)
Transaction_closedAt = Property(name="closedAt", type=DateTimeType)
Transaction_mode = Property(name="mode", type=TxMode)
Transaction_agreedPrice = Property(name="agreedPrice", type=Money)
Transaction_delivery = Property(name="delivery", type=DeliveryMode)
Transaction_receiptUrl = Property(name="receiptUrl", type=StringType)
Transaction_paymentMethod = Property(name="paymentMethod", type=PaymentMethod)
Transaction_status = Property(name="status", type=TxStatus)
Transaction.attributes = {Transaction_id, Transaction_closedAt, Transaction_mode, Transaction_agreedPrice, Transaction_delivery, Transaction_receiptUrl, Transaction_paymentMethod, Transaction_status}

Rating_id = Property(name="id", type=StringType)
Rating_stars = Property(name="stars", type=IntegerType)
Rating_comment = Property(name="comment", type=StringType)
Rating_createdAt = Property(name="createdAt", type=DateTimeType)
Rating.attributes = {Rating_id, Rating_stars, Rating_comment, Rating_createdAt}

Conversation_id = Property(name="id", type=StringType)
Conversation_createdAt = Property(name="createdAt", type=DateTimeType)
Conversation.attributes = {Conversation_id, Conversation_createdAt}

Message_id = Property(name="id", type=StringType)
Message_content = Property(name="content", type=StringType)
Message_sentAt = Property(name="sentAt", type=DateTimeType)
Message_kind = Property(name="kind", type=MessageKind)
Message_attachments = Property(name="attachments", type=StringType, multiplicity=Multiplicity(0, 9999))
Message.attributes = {Message_id, Message_content, Message_sentAt, Message_kind, Message_attachments}

Report_id = Property(name="id", type=StringType)
Report_reason = Property(name="reason", type=ReportReason)
Report_details = Property(name="details", type=StringType)
Report_createdAt = Property(name="createdAt", type=DateTimeType)
Report_status = Property(name="status", type=ReportStatus)
Report.attributes = {Report_id, Report_reason, Report_details, Report_createdAt, Report_status}

PaymentProvider_name = Property(name="name", type=StringType)
PaymentProvider_type = Property(name="type", type=StringType)
PaymentProvider_publicKey = Property(name="publicKey", type=StringType)
PaymentProvider_secretRef = Property(name="secretRef", type=StringType)
PaymentProvider.attributes = {PaymentProvider_name, PaymentProvider_type, PaymentProvider_publicKey, PaymentProvider_secretRef}

# =====================
# Associations
# =====================
contains = BinaryAssociation(
    name="contains",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(0, 9999))
    }
)
members = BinaryAssociation(
    name="members",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
Community_Category = BinaryAssociation(
    name="Community_Category",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="Category", type=Category, multiplicity=Multiplicity(0, 9999))
    }
)
Community_Location = BinaryAssociation(
    name="Community_Location",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="Location", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
Community_PaymentProvider = BinaryAssociation(
    name="Community_PaymentProvider",
    ends={
        Property(name="Community", type=Community, multiplicity=Multiplicity(0, 1)),
        Property(name="PaymentProvider", type=PaymentProvider, multiplicity=Multiplicity(1, 1))
    }
)
members = BinaryAssociation(
    name="members",
    ends={
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
SubCommunity_Item = BinaryAssociation(
    name="SubCommunity_Item",
    ends={
        Property(name="SubCommunity", type=SubCommunity, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
owner = BinaryAssociation(
    name="owner",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
asRater = BinaryAssociation(
    name="asRater",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Rating", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
asRated = BinaryAssociation(
    name="asRated",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Rating", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
asBuyer = BinaryAssociation(
    name="asBuyer",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
asSeller = BinaryAssociation(
    name="asSeller",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
asReporter = BinaryAssociation(
    name="asReporter",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Report", type=Report, multiplicity=Multiplicity(0, 9999))
    }
)
Category_Item = BinaryAssociation(
    name="Category_Item",
    ends={
        Property(name="Category", type=Category, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Location_Item = BinaryAssociation(
    name="Location_Item",
    ends={
        Property(name="Location", type=Location, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Item_ItemVariant = BinaryAssociation(
    name="Item_ItemVariant",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ItemVariant", type=ItemVariant, multiplicity=Multiplicity(0, 9999))
    }
)
Item_Offer = BinaryAssociation(
    name="Item_Offer",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(0, 9999))
    }
)
Item_Reservation = BinaryAssociation(
    name="Item_Reservation",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Reservation", type=Reservation, multiplicity=Multiplicity(0, 9999))
    }
)
Item_Report = BinaryAssociation(
    name="Item_Report",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Report", type=Report, multiplicity=Multiplicity(0, 9999))
    }
)
Item_Conversation = BinaryAssociation(
    name="Item_Conversation",
    ends={
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(0, 9999))
    }
)
Conversation_Message = BinaryAssociation(
    name="Conversation_Message",
    ends={
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="Message", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
participants = BinaryAssociation(
    name="participants",
    ends={
        Property(name="Conversation", type=Conversation, multiplicity=Multiplicity(2, 9999)),
        Property(name="User", type=User, multiplicity=Multiplicity(2, 9999))
    }
)
author = BinaryAssociation(
    name="author",
    ends={
        Property(name="Message", type=Message, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Offer_Item = BinaryAssociation(
    name="Offer_Item",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
buyer = BinaryAssociation(
    name="buyer",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
seller = BinaryAssociation(
    name="seller",
    ends={
        Property(name="Offer", type=Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Reservation_Item = BinaryAssociation(
    name="Reservation_Item",
    ends={
        Property(name="Reservation", type=Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
buyer = BinaryAssociation(
    name="buyer",
    ends={
        Property(name="Reservation", type=Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Transaction_Item = BinaryAssociation(
    name="Transaction_Item",
    ends={
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
seller = BinaryAssociation(
    name="seller",
    ends={
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
buyer = BinaryAssociation(
    name="buyer",
    ends={
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Transaction_Rating = BinaryAssociation(
    name="Transaction_Rating",
    ends={
        Property(name="Transaction", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="Rating", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
reportedUser = BinaryAssociation(
    name="reportedUser",
    ends={
        Property(name="Report", type=Report, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Report_Item = BinaryAssociation(
    name="Report_Item",
    ends={
        Property(name="Report", type=Report, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 1))
    }
)

# =====================
# Domain Model
# =====================
domain_model = DomainModel(
    name="Community Exchange Domain",
    types={Community, SubCommunity, User, Category, Location, Money, Item, ItemVariant, Offer, Reservation, Transaction, Rating, Conversation, Message, Report, PaymentProvider, ItemState, Condition, ItemKind, ExchangeMode, OfferType, OfferStatus, ReservationStatus, TxMode, DeliveryMode, TxStatus, MessageKind, ReportReason, ReportStatus, PaymentMethod, UserStatus},
    associations={contains, members, Community_Category, Community_Location, Community_PaymentProvider, members, SubCommunity_Item, owner, asRater, asRated, asBuyer, asSeller, asReporter, Category_Item, Location_Item, Item_ItemVariant, Item_Offer, Item_Reservation, Item_Report, Item_Conversation, Conversation_Message, participants, author, Offer_Item, buyer, seller, Reservation_Item, buyer, Transaction_Item, seller, buyer, Transaction_Rating, reportedUser, Report_Item},
    generalizations={},
)

if __name__ == "__main__":
    print("DomainModel:", domain_model.name)
    print("Types:", len(domain_model.types))
    print("Associations:", len(domain_model.associations))