from django.contrib import admin
from mainapp.models import User, Listing, Bid, Message
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Message)