from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    """Makes use of abstract user model and adds extra fields """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True,)
    image = models.ImageField(upload_to='images', null=True)
    messages = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='Message',
        related_name='related_to'
    )

    def __str__(self):
        return self.username

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'city': self.city,
            'date_of_birth': self.date_of_birth.strftime("%d-%m-%Y") if self.date_of_birth else None,
            'image': self.image.url if self.image else None,
        }


class Listing(models.Model):
    """ Creates a Listing class """
    title = models.CharField(max_length=64)
    image = models. ImageField(blank=True)
    description = models.TextField()
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_owner")
    open = models.BooleanField(default=True)
    closing_time = models.TimeField()

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'owner': self.owner.username,
            'closing_time': self.closing_time,
            'open': self.open,
        }
    
    @property
    def closed(self):
        if timezone.now() < self.closing_time:
            return self.closed == True


class Bid(models.Model):
    """ Creates a Bid class """
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participated_bid")
    new_price = models.FloatField()
    winner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} bids £{self.new_price} on {self.listing_id}"

    def to_dict(self):
        return {
            'id': self.id,
            'listing_id': self.listing_id.id,
            'user_id': self.user_id.username,
            'new_price': self.new_price,
        }


class Message(models.Model):
    """ Creates a Message class """
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_message")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receiver",)
    text = models.TextField(null=True,max_length=4096)

    def __str__(self):
        return f"{self.sender} sent a message to {self.receiver} on {self.listing_id}: {self.text}"

    def to_dict(self):
        return {
            'id': self.id,
            'listing_id': self.listing_id.title,
            'sender': self.sender.username,
            'receiver': self.receiver.username,          
            'text': self.text,
        }


class Profile(models.Model):
    """ Creates a Profile class """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images')

    def to_dict(self):
        return {
            'image': self.image.url if self.image else None,
        }