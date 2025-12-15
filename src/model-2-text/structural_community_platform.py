"""
Structural Model Stub for GUI Generator
Provides minimal stubs for domain classes used in DataSource definitions
"""

# Stub classes - just need to exist for DataSource references
class _DomainClass:
    """Base stub for domain model classes"""
    def __init__(self, name):
        self.name = name

# Domain classes
Community = _DomainClass("Community")
Item = _DomainClass("Item")
Review = _DomainClass("Review")
Tag = _DomainClass("Tag")
User = _DomainClass("User")
Order = _DomainClass("Order")
Payment = _DomainClass("Payment")
Message = _DomainClass("Message")

# Property stubs - just need to exist
class _Property:
    """Base stub for properties"""
    def __init__(self, name):
        self.name = name

# Community properties
Community_name = _Property("name")
Community_description = _Property("description")

# Item properties
Item_title = _Property("title")
Item_description = _Property("description")
Item_price = _Property("price")
Item_publicationDate = _Property("publicationDate")
Item_status = _Property("status")
Item_transactionType = _Property("transactionType")

# Review properties
Review_rating = _Property("rating")
Review_comment = _Property("comment")
Review_reviewDate = _Property("reviewDate")

# Tag properties
Tag_name = _Property("name")

# User properties
User_name = _Property("name")
User_email = _Property("email")
User_username = _Property("username")

# Order properties
Order_orderDate = _Property("orderDate")
Order_status = _Property("status")

# Payment properties
Payment_amount = _Property("amount")
Payment_method = _Property("method")
Payment_status = _Property("status")

# Message properties
Message_content = _Property("content")
Message_timestamp = _Property("timestamp")
