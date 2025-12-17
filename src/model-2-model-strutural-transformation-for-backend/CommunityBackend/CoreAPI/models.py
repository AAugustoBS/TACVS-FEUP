from django.db import models


class ReservationStatus(models.TextChoices):
    Released = 'Released', 'Released'
    Active = 'Active', 'Active'
    Expired = 'Expired', 'Expired'

class ReportReason(models.TextChoices):
    Fraud = 'Fraud', 'Fraud'
    Safety = 'Safety', 'Safety'
    Offensive = 'Offensive', 'Offensive'
    Spam = 'Spam', 'Spam'
    Other = 'Other', 'Other'

class TxMode(models.TextChoices):
    Donation = 'Donation', 'Donation'
    Sale = 'Sale', 'Sale'
    Exchange = 'Exchange', 'Exchange'

class ReportStatus(models.TextChoices):
    Open = 'Open', 'Open'
    Ignored = 'Ignored', 'Ignored'
    Resolved = 'Resolved', 'Resolved'
    UnderReview = 'UnderReview', 'UnderReview'

class ItemState(models.TextChoices):
    Draft = 'Draft', 'Draft'
    Active = 'Active', 'Active'
    Reserved = 'Reserved', 'Reserved'
    Completed = 'Completed', 'Completed'
    Archived = 'Archived', 'Archived'

class PaymentMethod(models.TextChoices):
    MBWay = 'MBWay', 'MBWay'
    PayPal = 'PayPal', 'PayPal'
    NoPayment = 'NoPayment', 'NoPayment'
    Multibanco = 'Multibanco', 'Multibanco'

class ExchangeMode(models.TextChoices):
    Donation = 'Donation', 'Donation'
    Exchange = 'Exchange', 'Exchange'
    Price = 'Price', 'Price'

class DeliveryMode(models.TextChoices):
    Locker = 'Locker', 'Locker'
    Mail = 'Mail', 'Mail'
    InPerson = 'InPerson', 'InPerson'

class UserStatus(models.TextChoices):
    Active = 'Active', 'Active'
    Suspended = 'Suspended', 'Suspended'

class OfferType(models.TextChoices):
    Request = 'Request', 'Request'
    ExchangeOffer = 'ExchangeOffer', 'ExchangeOffer'
    PriceOffer = 'PriceOffer', 'PriceOffer'

class TxStatus(models.TextChoices):
    Cancelled = 'Cancelled', 'Cancelled'
    Completed = 'Completed', 'Completed'

class ItemKind(models.TextChoices):
    Product = 'Product', 'Product'
    Service = 'Service', 'Service'

class OfferStatus(models.TextChoices):
    Withdrawn = 'Withdrawn', 'Withdrawn'
    Pending = 'Pending', 'Pending'
    Expired = 'Expired', 'Expired'
    Accepted = 'Accepted', 'Accepted'
    Rejected = 'Rejected', 'Rejected'

class MessageKind(models.TextChoices):
    System = 'System', 'System'
    Text = 'Text', 'Text'
    Image = 'Image', 'Image'

class Condition(models.TextChoices):
    Poor = 'Poor', 'Poor'
    New = 'New', 'New'
    LikeNew = 'LikeNew', 'LikeNew'
    Good = 'Good', 'Good'
    Fair = 'Fair', 'Fair'

class PaymentProvider(models.Model):
    """
    Represents a paymentProvider in the system.
    """
    name =  models.CharField(max_length=255)
    type =  models.CharField(max_length=255)
    publicKey =  models.CharField(max_length=255)
    secretRef =  models.CharField(max_length=255)
    

    class Meta:
        verbose_name = "PaymentProvider"
        verbose_name_plural = "PaymentProviders"

    def __str__(self):
        """
        Returns a string representation of the paymentProvider
        """
        return str(self.name)

class Report(models.Model):
    """
    Represents a report in the system.
    """
    uid =  models.CharField(max_length=255)
    reason =  models.CharField(max_length=255, choices=ReportReason.choices)
    details =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    status =  models.CharField(max_length=255, choices=ReportStatus.choices)
    
    Item = models.ForeignKey(
        'Item', related_name='Report', on_delete=models.SET_NULL, blank=True, null=True)
    
    User = models.ForeignKey(
        'User', related_name='Report', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        """
        Returns a string representation of the report
        """
        return str(self.uid)

class Message(models.Model):
    """
    Represents a message in the system.
    """
    uid =  models.CharField(max_length=255)
    content =  models.CharField(max_length=255)
    sentAt =  models.DateTimeField()
    kind =  models.CharField(max_length=255, choices=MessageKind.choices)
    attachments =  models.CharField(max_length=255)
    
    Conversation = models.ForeignKey(
        'Conversation', related_name='Message', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Message', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        """
        Returns a string representation of the message
        """
        return str(self.uid)

class Conversation(models.Model):
    """
    Represents a conversation in the system.
    """
    uid =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    
    Item = models.ForeignKey(
        'Item', related_name='Conversation', on_delete=models.PROTECT)
    
    

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"

    def __str__(self):
        """
        Returns a string representation of the conversation
        """
        return str(self.uid)

class Rating(models.Model):
    """
    Represents a rating in the system.
    """
    uid =  models.CharField(max_length=255)
    stars =  models.IntegerField()
    comment =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    
    User = models.ForeignKey(
        'User', related_name='Rating', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        """
        Returns a string representation of the rating
        """
        return str(self.uid)

class Transaction(models.Model):
    """
    Represents a transaction in the system.
    """
    uid =  models.CharField(max_length=255)
    closedAt =  models.DateTimeField()
    mode =  models.CharField(max_length=255, choices=TxMode.choices)
    delivery =  models.CharField(max_length=255, choices=DeliveryMode.choices)
    receiptUrl =  models.CharField(max_length=255)
    paymentMethod =  models.CharField(max_length=255, choices=PaymentMethod.choices)
    status =  models.CharField(max_length=255, choices=TxStatus.choices)
    
    Item = models.ForeignKey(
        'Item', related_name='Transaction', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Transaction', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Transaction', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        """
        Returns a string representation of the transaction
        """
        return str(self.uid)

class Reservation(models.Model):
    """
    Represents a reservation in the system.
    """
    reservedFrom =  models.DateTimeField()
    reservedUntil =  models.DateTimeField()
    uid =  models.CharField(max_length=255)
    status =  models.CharField(max_length=255, choices=ReservationStatus.choices)
    
    User = models.ForeignKey(
        'User', related_name='Reservation', on_delete=models.PROTECT)
    
    Item = models.ForeignKey(
        'Item', related_name='Reservation', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        """
        Returns a string representation of the reservation
        """
        return str(self.reservedFrom)

class Offer(models.Model):
    """
    Represents a offer in the system.
    """
    uid =  models.CharField(max_length=255)
    type =  models.CharField(max_length=255, choices=OfferType.choices)
    message =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    status =  models.CharField(max_length=255, choices=OfferStatus.choices)
    
    Item = models.ForeignKey(
        'Item', related_name='Offer', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Offer', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Offer', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        """
        Returns a string representation of the offer
        """
        return str(self.uid)

class ItemVariant(models.Model):
    """
    Represents a itemVariant in the system.
    """
    name =  models.CharField(max_length=255)
    value =  models.CharField(max_length=255)
    
    Item = models.ForeignKey(
        'Item', related_name='ItemVariant', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "ItemVariant"
        verbose_name_plural = "ItemVariants"

    def __str__(self):
        """
        Returns a string representation of the itemVariant
        """
        return str(self.name)

class Item(models.Model):
    """
    Represents a item in the system.
    """
    uid =  models.CharField(max_length=255)
    title =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    mediaUrls =  models.CharField(max_length=255)
    tags =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    updatedAt =  models.DateTimeField()
    state =  models.CharField(max_length=255, choices=ItemState.choices)
    condition =  models.CharField(max_length=255, choices=Condition.choices)
    kind =  models.CharField(max_length=255, choices=ItemKind.choices)
    exchangeModes =  models.CharField(max_length=255, choices=ExchangeMode.choices)
    quantity =  models.IntegerField()
    unit =  models.CharField(max_length=255)
    expiresAt =  models.DateTimeField()
    
    
    
    
    
    SubCommunity = models.ForeignKey(
        'SubCommunity', related_name='Item', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Item', on_delete=models.PROTECT)
    
    
    
    Location = models.ForeignKey(
        'Location', related_name='Item', on_delete=models.PROTECT)
    
    Category = models.ForeignKey(
        'Category', related_name='Item', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Item', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        """
        Returns a string representation of the item
        """
        return str(self.uid)

class Money(models.Model):
    """
    Represents a money in the system.
    """
    amount =  models.FloatField()
    currency =  models.CharField(max_length=255)
    
    
    

    class Meta:
        verbose_name = "Money"
        verbose_name_plural = "Moneys"

    def __str__(self):
        """
        Returns a string representation of the money
        """
        return str(self.amount)

class Location(models.Model):
    """
    Represents a location in the system.
    """
    uid =  models.CharField(max_length=255)
    label =  models.CharField(max_length=255)
    address =  models.CharField(max_length=255)
    lat =  models.FloatField()
    lon =  models.FloatField()
    
    
    Community = models.ForeignKey(
        'Community', related_name='Location', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        """
        Returns a string representation of the location
        """
        return str(self.uid)

class Category(models.Model):
    """
    Represents a category in the system.
    """
    uid =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    icon =  models.CharField(max_length=255)
    
    Community = models.ForeignKey(
        'Community', related_name='Category', on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        """
        Returns a string representation of the category
        """
        return str(self.uid)

class User(models.Model):
    """
    Represents a user in the system.
    """
    status =  models.CharField(max_length=255, choices=UserStatus.choices)
    uid =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255)
    fullName =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    phone =  models.CharField(max_length=255)
    avatarUrl =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    isAdmin =  models.BooleanField()
    isModerator =  models.BooleanField()
    avgRating =  models.FloatField()
    ratingCount =  models.IntegerField()
    
    
    
    
    SubCommunity = models.ForeignKey(
        'SubCommunity', related_name='User', on_delete=models.PROTECT)
    
    
    
    Conversation = models.ManyToManyField(
        'Conversation', related_name='User', blank=True)
    
    Community = models.ForeignKey(
        'Community', related_name='User', on_delete=models.PROTECT)
    
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """
        Returns a string representation of the user
        """
        return str(self.uid)

class SubCommunity(models.Model):
    """
    Represents a subCommunity in the system.
    """
    uid =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    
    Community = models.ForeignKey(
        'Community', related_name='SubCommunity', on_delete=models.PROTECT)
    
    

    class Meta:
        verbose_name = "SubCommunity"
        verbose_name_plural = "SubCommunitys"

    def __str__(self):
        """
        Returns a string representation of the subCommunity
        """
        return str(self.uid)

class Community(models.Model):
    """
    Represents a community in the system.
    """
    uid =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    logoUrl =  models.CharField(max_length=255)
    rulesMarkdown =  models.CharField(max_length=255)
    allowSubcommunities =  models.BooleanField()
    
    
    
    
    
    PaymentProvider = models.OneToOneField(
        'PaymentProvider', related_name='Community', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communitys"

    def __str__(self):
        """
        Returns a string representation of the community
        """
        return str(self.uid)
