####################
# STRUCTURAL MODEL #
####################

# mypy: ignore-errors

from besser.BUML.metamodel.structural import (  
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
TransactionType: Enumeration = Enumeration(
    name="TransactionType",
    literals={
            EnumerationLiteral(name="Donation"),
			EnumerationLiteral(name="Sale"),
			EnumerationLiteral(name="Exchange")
    }
)

OrderStatus: Enumeration = Enumeration(
    name="OrderStatus",
    literals={
            EnumerationLiteral(name="Donated"),
			EnumerationLiteral(name="Exchanged"),
			EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="Delivered"),
			EnumerationLiteral(name="Canceled")
    }
)

ItemStatus: Enumeration = Enumeration(
    name="ItemStatus",
    literals={
            EnumerationLiteral(name="Exchanged"),
			EnumerationLiteral(name="Paused"),
			EnumerationLiteral(name="Donated"),
			EnumerationLiteral(name="Sold"),
			EnumerationLiteral(name="Available")
    }
)

# Classes
Community = Class(name="Community")
Tag = Class(name="Tag")
OrderItem = Class(name="OrderItem")
User = Class(name="User")
Conversation = Class(name="Conversation")
ExchangeSuggestion = Class(name="ExchangeSuggestion")
Item = Class(name="Item")
Message = Class(name="Message")
CommunityConfiguration = Class(name="CommunityConfiguration")
Review = Class(name="Review")
Order = Class(name="Order")

# Community class attributes and methods
Community_name: Property = Property(name="name", type=StringType)
Community_color: Property = Property(name="color", type=StringType)
Community_description: Property = Property(name="description", type=StringType)
Community_faculty: Property = Property(name="faculty", type=StringType)
Community_id: Property = Property(name="id", type=StringType)
Community_creationDate: Property = Property(name="creationDate", type=DateType)
Community.attributes={Community_faculty, Community_id, Community_color, Community_name, Community_creationDate, Community_description}

# Tag class attributes and methods
Tag_id: Property = Property(name="id", type=StringType)
Tag_name: Property = Property(name="name", type=StringType)
Tag.attributes={Tag_name, Tag_id}

# OrderItem class attributes and methods
OrderItem_id: Property = Property(name="id", type=StringType)
OrderItem.attributes={OrderItem_id}

# User class attributes and methods
User_birthDay: Property = Property(name="birthDay", type=DateType)
User_email: Property = Property(name="email", type=StringType)
User_name: Property = Property(name="name", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_biography: Property = Property(name="biography", type=StringType)
User_contactNumber: Property = Property(name="contactNumber", type=StringType)
User_onlineStatus: Property = Property(name="onlineStatus", type=BooleanType)
User_averageRating: Property = Property(name="averageRating", type=FloatType)
User_id: Property = Property(name="id", type=StringType)
User_faculty: Property = Property(name="faculty", type=StringType)
User.attributes={User_email, User_name, User_onlineStatus, User_faculty, User_birthDay, User_contactNumber, User_password, User_averageRating, User_biography, User_id}

# Conversation class attributes and methods
Conversation_subject: Property = Property(name="subject", type=StringType)
Conversation_id: Property = Property(name="id", type=StringType)
Conversation_lastMessageDate: Property = Property(name="lastMessageDate", type=DateType)
Conversation.attributes={Conversation_lastMessageDate, Conversation_subject, Conversation_id}

# ExchangeSuggestion class attributes and methods
ExchangeSuggestion_description: Property = Property(name="description", type=StringType)
ExchangeSuggestion.attributes={ExchangeSuggestion_description}

# Item class attributes and methods
Item_description: Property = Property(name="description", type=StringType)
Item_status: Property = Property(name="status", type=ItemStatus)
Item_price: Property = Property(name="price", type=FloatType)
Item_title: Property = Property(name="title", type=StringType)
Item_id: Property = Property(name="id", type=StringType)
Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
Item_transactionType: Property = Property(name="transactionType", type=TransactionType)
Item.attributes={Item_id, Item_title, Item_price, Item_status, Item_publicationDate, Item_description, Item_transactionType}

# Message class attributes and methods
Message_content: Property = Property(name="content", type=StringType)
Message_isRead: Property = Property(name="isRead", type=BooleanType)
Message_id: Property = Property(name="id", type=StringType)
Message_sendDate: Property = Property(name="sendDate", type=DateType)
Message.attributes={Message_content, Message_isRead, Message_id, Message_sendDate}

# CommunityConfiguration class attributes and methods
CommunityConfiguration_requiresItemApproval: Property = Property(name="requiresItemApproval", type=BooleanType)
CommunityConfiguration_allowStudentOutsideFaculty: Property = Property(name="allowStudentOutsideFaculty", type=BooleanType)
CommunityConfiguration_id: Property = Property(name="id", type=StringType)
CommunityConfiguration_allowOnlinePayment: Property = Property(name="allowOnlinePayment", type=BooleanType)
CommunityConfiguration_allowsDonating: Property = Property(name="allowsDonating", type=BooleanType)
CommunityConfiguration_allowsServicesOffer: Property = Property(name="allowsServicesOffer", type=BooleanType)
CommunityConfiguration_allowsSelling: Property = Property(name="allowsSelling", type=BooleanType)
CommunityConfiguration_allowsExchanging: Property = Property(name="allowsExchanging", type=BooleanType)
CommunityConfiguration.attributes={CommunityConfiguration_allowsSelling, CommunityConfiguration_allowsExchanging, CommunityConfiguration_id, CommunityConfiguration_requiresItemApproval, CommunityConfiguration_allowsDonating, CommunityConfiguration_allowOnlinePayment, CommunityConfiguration_allowsServicesOffer, CommunityConfiguration_allowStudentOutsideFaculty}

# Review class attributes and methods
Review_id: Property = Property(name="id", type=StringType)
Review_reviewDate: Property = Property(name="reviewDate", type=DateType)
Review_comment: Property = Property(name="comment", type=StringType)
Review_rating: Property = Property(name="rating", type=IntegerType)
Review.attributes={Review_rating, Review_id, Review_comment, Review_reviewDate}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=StringType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order_orderDate: Property = Property(name="orderDate", type=DateType)
Order_deliveryAddress: Property = Property(name="deliveryAddress", type=StringType)
Order_transactionType: Property = Property(name="transactionType", type=TransactionType)
Order.attributes={Order_id, Order_deliveryAddress, Order_status, Order_transactionType, Order_orderDate}

# Relationships
user_publishes_item: BinaryAssociation = BinaryAssociation(
    name="user_publishes_item",
    ends={
        Property(name="publishedItems", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="publisher", type=User, multiplicity=Multiplicity(1, 1))
    }
)
item_has_order_items: BinaryAssociation = BinaryAssociation(
    name="item_has_order_items",
    ends={
        Property(name="item", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItems", type=OrderItem, multiplicity=Multiplicity(0, 9999))
    }
)
community_members: BinaryAssociation = BinaryAssociation(
    name="community_members",
    ends={
        Property(name="communities", type=Community, multiplicity=Multiplicity(1, 9999)),
        Property(name="members", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
community_contains_item: BinaryAssociation = BinaryAssociation(
    name="community_contains_item",
    ends={
        Property(name="publishedIn", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
user_sends_message: BinaryAssociation = BinaryAssociation(
    name="user_sends_message",
    ends={
        Property(name="sender", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="sentMessages", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
order_associated_with_community: BinaryAssociation = BinaryAssociation(
    name="order_associated_with_community",
    ends={
        Property(name="communityOrders", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="communityForOrder", type=Community, multiplicity=Multiplicity(1, 1))
    }
)
user_participates_conversation: BinaryAssociation = BinaryAssociation(
    name="user_participates_conversation",
    ends={
        Property(name="conversations", type=Conversation, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants", type=User, multiplicity=Multiplicity(2, 2))
    }
)
order_contains_order_items: BinaryAssociation = BinaryAssociation(
    name="order_contains_order_items",
    ends={
        Property(name="order", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="containsItems", type=OrderItem, multiplicity=Multiplicity(0, 9999))
    }
)
user_gives_review: BinaryAssociation = BinaryAssociation(
    name="user_gives_review",
    ends={
        Property(name="reviewer", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="givenReviews", type=Review, multiplicity=Multiplicity(0, 9999))
    }
)
community_has_configuration: BinaryAssociation = BinaryAssociation(
    name="community_has_configuration",
    ends={
        Property(name="community", type=Community, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=CommunityConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
message_belongs_to_conversation: BinaryAssociation = BinaryAssociation(
    name="message_belongs_to_conversation",
    ends={
        Property(name="messages", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="conversation", type=Conversation, multiplicity=Multiplicity(1, 1))
    }
)
item_has_exchange_suggestion: BinaryAssociation = BinaryAssociation(
    name="item_has_exchange_suggestion",
    ends={
        Property(name="exchangeSuggestion", type=ExchangeSuggestion, multiplicity=Multiplicity(0, 1)),
        Property(name="itemWithSuggestion", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
item_receives_review: BinaryAssociation = BinaryAssociation(
    name="item_receives_review",
    ends={
        Property(name="itemReviews", type=Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="reviewedItem", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
user_places_order: BinaryAssociation = BinaryAssociation(
    name="user_places_order",
    ends={
        Property(name="placedOrders", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="buyer", type=User, multiplicity=Multiplicity(1, 1))
    }
)
item_associated_with_tag: BinaryAssociation = BinaryAssociation(
    name="item_associated_with_tag",
    ends={
        Property(name="taggedItems", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="tags", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
community_subcommunities: BinaryAssociation = BinaryAssociation(
    name="community_subcommunities",
    ends={
        Property(name="subcommunities", type=Community, multiplicity=Multiplicity(0, 9999)),
        Property(name="parentCommunity", type=Community, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Community, Tag, OrderItem, User, Conversation, ExchangeSuggestion, Item, Message, CommunityConfiguration, Review, Order, TransactionType, OrderStatus, ItemStatus},
    associations={user_publishes_item, item_has_order_items, community_members, community_contains_item, user_sends_message, order_associated_with_community, user_participates_conversation, order_contains_order_items, user_gives_review, community_has_configuration, message_belongs_to_conversation, item_has_exchange_suggestion, item_receives_review, user_places_order, item_associated_with_tag, community_subcommunities},
    generalizations=set()
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata 

metadata = Metadata(description="Community Platform B-UML Model")
project = Project(
    name="community_platform",
    models=[domain_model],
    owner="User",
    metadata=metadata
)
