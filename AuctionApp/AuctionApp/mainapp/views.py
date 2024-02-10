import json

from django.shortcuts import render

from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth import get_user_model
from .forms import LoginForm, SignupForm

from mainapp.models import Listing, Bid, Message



# Create your views here.

User = get_user_model()

def login_view(request):
    """ Creates a function for logging in """

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                
                return redirect('http://127.0.0.1:5173/')

            # failed authentication
            return render(request, 'error.html', {
                'error': 'User not registered. Sign up first.'
            })

        # invalid form
        return render(request, 'mainapp/auth/login.html', {
            'form': form
        })

    return render(request, 'mainapp/auth/login.html', {'form': form})


def signup_view(request):
    """ Creates a function for signing up """

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username,email,password)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('http://127.0.0.1:5173/')
    
    return render(request, 'mainapp/auth/signup.html', {'form': SignupForm})


@login_required
def logout(request):
    """ Creates a function for logging out """

    auth.logout(request)
    return redirect('mainapp:login')


@login_required
def listings(request):
    """ Creates a function for showing and posting listings """

    if request.method == "GET":
        return JsonResponse({
            "listings" : [
                listing.to_dict()
                for listing in Listing.objects.all()
            ]
        })
    if request.method == "POST":
        data = json.loads(request.body)
        owner = User.objects.get(id=request.user.id)
        listing = Listing.objects.create(
              title=data['title'],
              description=data['description'],
              price=data['price'],
              closing_time=data['closing_time'],
              owner=owner
            )
        return JsonResponse(listing.to_dict())
    

@login_required
def users_view(request):
    """ Creates a function for displaying user information and updating user information """

    user = request.user
    if request.method == "GET":
        return JsonResponse({
            "users" : 
                user.to_dict()  
        })
    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        if data['updated_username'] != "":
            user.username = data['updated_username']
        if data['updated_email'] != "":
            user.email = data['updated_email']
        if data['updated_city'] != "":
            user.city = data['updated_city']
        if data['updated_date_of_birth'] != "":
            user.date_of_birth = data['updated_date_of_birth']
        user.save()
        return JsonResponse(data)
  

@login_required
def bids(request):
    """ Creates a function for displaying and making bids"""

    if request.method == "GET":
        return JsonResponse({
            "bids" : [
                bid.to_dict()
                for bid in Bid.objects.all()
            ]
        })
    if request.method == "POST":
        data = json.loads(request.body)
        listing_name = data['listing_id']
        listing = Listing.objects.get(title=listing_name)
        price = listing.price
        new_price = data['new_price']
        if Bid.objects.filter(listing_id=listing.id).count() >= 1:
            bid = Bid.objects.get(listing_id=listing.id)
            price = bid.new_price
            if new_price > price:
                user = User.objects.get(id=request.user.id)
                bid = Bid(listing_id=listing, user_id=user, new_price=new_price)
                bid.save()
                return JsonResponse(data)
            else:
                return render(request, 'error.html', {
                    'error': 'Bid should be greater than current bid!'
                })
        else:
            if new_price > price:
                user = User.objects.get(id=request.user.id)
                bid = Bid(listing_id=listing, user_id=user, new_price=new_price)
                bid.save()
                return JsonResponse(data)
            else:
                return render(request, 'error.html', {
                    'error': 'Bid should be greater than current bid!'
                })


@login_required
def message(request):
    """ Creates a function for creating and displaying messages """
    
    if request.method == "GET":
        user = request.user
        return JsonResponse({
            "messages" : [
                message.to_dict()
                for message in Message.objects.all()
            ]
        })
    if request.method == "POST":
        user = request.user
        data = json.loads(request.body)
        listing = data['listing_id']
        listing = Listing.objects.get(title=listing)
        receiver = data['receiver']
        receiver = User.objects.get(username=receiver)
        text = data['text']
        message = Message(listing_id=listing, sender=user, receiver=receiver,text=text)
        message.save()
        return JsonResponse(data)


@login_required
def search(request):
    """ Creates a function for making a search query"""
    
    if request.method == "POST":
        data = json.loads(request.body)
        title = data['searchListing']
        return JsonResponse({
            "listings" : [
                listing.to_dict()
                for listing in Listing.objects.all().filter(title=title)
            ]
        })