from django.db import models


class TxMode(models.TextChoices):
    Donation = 'Donation', 'Donation'
    Sale = 'Sale', 'Sale'
    Exchange = 'Exchange', 'Exchange'

class MessageKind(models.TextChoices):
    Image = 'Image', 'Image'
    System = 'System', 'System'
    Text = 'Text', 'Text'

class ReservationStatus(models.TextChoices):
    Active = 'Active', 'Active'
    Released = 'Released', 'Released'
    Expired = 'Expired', 'Expired'

class ReportStatus(models.TextChoices):
    UnderReview = 'UnderReview', 'UnderReview'
    Resolved = 'Resolved', 'Resolved'
    Ignored = 'Ignored', 'Ignored'
    Open = 'Open', 'Open'

class ItemState(models.TextChoices):
    Active = 'Active', 'Active'
    Archived = 'Archived', 'Archived'
    Reserved = 'Reserved', 'Reserved'
    Completed = 'Completed', 'Completed'
    Draft = 'Draft', 'Draft'

class OfferStatus(models.TextChoices):
    Accepted = 'Accepted', 'Accepted'
    Rejected = 'Rejected', 'Rejected'
    Withdrawn = 'Withdrawn', 'Withdrawn'
    Expired = 'Expired', 'Expired'
    Pending = 'Pending', 'Pending'

class ReportReason(models.TextChoices):
    Offensive = 'Offensive', 'Offensive'
    Safety = 'Safety', 'Safety'
    Other = 'Other', 'Other'
    Spam = 'Spam', 'Spam'
    Fraud = 'Fraud', 'Fraud'

class ItemKind(models.TextChoices):
    Service = 'Service', 'Service'
    Product = 'Product', 'Product'

class UserStatus(models.TextChoices):
    Active = 'Active', 'Active'
    Suspended = 'Suspended', 'Suspended'

class ExchangeMode(models.TextChoices):
    Price = 'Price', 'Price'
    Exchange = 'Exchange', 'Exchange'
    Donation = 'Donation', 'Donation'

class TxStatus(models.TextChoices):
    Cancelled = 'Cancelled', 'Cancelled'
    Completed = 'Completed', 'Completed'

class Condition(models.TextChoices):
    Good = 'Good', 'Good'
    New = 'New', 'New'
    LikeNew = 'LikeNew', 'LikeNew'
    Poor = 'Poor', 'Poor'
    Fair = 'Fair', 'Fair'

class DeliveryMode(models.TextChoices):
    Locker = 'Locker', 'Locker'
    InPerson = 'InPerson', 'InPerson'
    Mail = 'Mail', 'Mail'

class OfferType(models.TextChoices):
    Request = 'Request', 'Request'
    PriceOffer = 'PriceOffer', 'PriceOffer'
    ExchangeOffer = 'ExchangeOffer', 'ExchangeOffer'

class PaymentMethod(models.TextChoices):
    NoPayment = 'NoPayment', 'NoPayment'
    Multibanco = 'Multibanco', 'Multibanco'
    MBWay = 'MBWay', 'MBWay'
    PayPal = 'PayPal', 'PayPal'

class PaymentProvider(models.Model):
    """
    Represents a paymentProvider in the system.
    """
    publicKey =  models.CharField(max_length=255)
    type =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    secretRef =  models.CharField(max_length=255)
    

    class Meta:
        verbose_name = "PaymentProvider"
        verbose_name_plural = "PaymentProviders"

    def __str__(self):
        """
        Returns a string representation of the paymentProvider
        """
        return str(self.publicKey)

class Report(models.Model):
    """
    Represents a report in the system.
    """
    reason =  models.CharField(max_length=255, choices=ReportReason.choices)
    details =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    status =  models.CharField(max_length=255, choices=ReportStatus.choices)
    uid =  models.CharField(max_length=255)
    
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
        return str(self.details)

class Rating(models.Model):
    """
    Represents a rating in the system.
    """
    comment =  models.CharField(max_length=255)
    stars =  models.IntegerField()
    uid =  models.CharField(max_length=255)
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
        return str(self.comment)

class Transaction(models.Model):
    """
    Represents a transaction in the system.
    """
    delivery =  models.CharField(max_length=255, choices=DeliveryMode.choices)
    receiptUrl =  models.CharField(max_length=255)
    paymentMethod =  models.CharField(max_length=255, choices=PaymentMethod.choices)
    uid =  models.CharField(max_length=255)
    status =  models.CharField(max_length=255, choices=TxStatus.choices)
    closedAt =  models.DateTimeField()
    mode =  models.CharField(max_length=255, choices=TxMode.choices)
    
    Item = models.ForeignKey(
        'Item', related_name='Transaction', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Transaction', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Transaction', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        """
        Returns a string representation of the transaction
        """
        return str(self.receiptUrl)

class Reservation(models.Model):
    """
    Represents a reservation in the system.
    """
    reservedUntil =  models.DateTimeField()
    reservedFrom =  models.DateTimeField()
    status =  models.CharField(max_length=255, choices=ReservationStatus.choices)
    uid =  models.CharField(max_length=255)
    
    Item = models.ForeignKey(
        'Item', related_name='Reservation', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Reservation', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        """
        Returns a string representation of the reservation
        """
        return str(self.reservedUntil)

class Offer(models.Model):
    """
    Represents a offer in the system.
    """
    type =  models.CharField(max_length=255, choices=OfferType.choices)
    message =  models.CharField(max_length=255)
    createdAt =  models.DateTimeField()
    status =  models.CharField(max_length=255, choices=OfferStatus.choices)
    uid =  models.CharField(max_length=255)
    
    User = models.ForeignKey(
        'User', related_name='Offer', on_delete=models.PROTECT)
    
    Item = models.ForeignKey(
        'Item', related_name='Offer', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Offer', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        """
        Returns a string representation of the offer
        """
        return str(self.message)

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
    updatedAt =  models.DateTimeField()
    title =  models.CharField(max_length=255)
    unit =  models.CharField(max_length=255)
    state =  models.CharField(max_length=255, choices=ItemState.choices)
    description =  models.CharField(max_length=255)
    expiresAt =  models.DateTimeField()
    condition =  models.CharField(max_length=255, choices=Condition.choices)
    mediaUrls =  models.CharField(max_length=255)
    kind =  models.CharField(max_length=255, choices=ItemKind.choices)
    tags =  models.CharField(max_length=255)
    exchangeModes =  models.CharField(max_length=255, choices=ExchangeMode.choices)
    createdAt =  models.DateTimeField()
    uid =  models.CharField(max_length=255)
    quantity =  models.IntegerField()
    
    
    
    
    Category = models.ForeignKey(
        'Category', related_name='Item', on_delete=models.PROTECT)
    
    Location = models.ForeignKey(
        'Location', related_name='Item', on_delete=models.PROTECT)
    
    Money = models.OneToOneField(
        'Money', related_name='Item', on_delete=models.PROTECT)
    
    User = models.ForeignKey(
        'User', related_name='Item', on_delete=models.PROTECT)
    
    

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        """
        Returns a string representation of the item
        """
        return str(self.updatedAt)

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
    lat =  models.FloatField()
    lon =  models.FloatField()
    uid =  models.CharField(max_length=255)
    label =  models.CharField(max_length=255)
    address =  models.CharField(max_length=255)
    
    
    Community = models.ForeignKey(
        'Community', related_name='Location', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        """
        Returns a string representation of the location
        """
        return str(self.lat)

class Category(models.Model):
    """
    Represents a category in the system.
    """
    uid =  models.CharField(max_length=255)
    icon =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    
    
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
    createdAt =  models.DateTimeField()
    username =  models.CharField(max_length=255)
    isAdmin =  models.BooleanField()
    fullName =  models.CharField(max_length=255)
    isModerator =  models.BooleanField()
    email =  models.CharField(max_length=255)
    avgRating =  models.FloatField()
    phone =  models.CharField(max_length=255)
    status =  models.CharField(max_length=255, choices=UserStatus.choices)
    ratingCount =  models.IntegerField()
    avatarUrl =  models.CharField(max_length=255)
    uid =  models.CharField(max_length=255)
    
    
    
    Community = models.ForeignKey(
        'Community', related_name='User', on_delete=models.PROTECT)
    
    
    
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """
        Returns a string representation of the user
        """
        return str(self.createdAt)

class Community(models.Model):
    """
    Represents a community in the system.
    """
    allowSubcommunities =  models.BooleanField()
    uid =  models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    logoUrl =  models.CharField(max_length=255)
    rulesMarkdown =  models.CharField(max_length=255)
    
    
    
    
    PaymentProvider = models.OneToOneField(
        'PaymentProvider', related_name='Community', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communitys"

    def __str__(self):
        """
        Returns a string representation of the community
        """
        return str(self.allowSubcommunities)
