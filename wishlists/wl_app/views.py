import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .models import Wishlist, Gift
from .forms import WishForm, WishlistForm, LoginForm, RegisterUser


logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('wishlists')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password1']
            )
            login(request, user)
            return redirect('wishlists')
    else:
        form = RegisterUser()
    return render(request, 'registration.html', {'form': form})


def main_view(request):
    return render(request, template_name="index.html", context={})


@login_required(login_url='login')
def wishlists_view(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_title = form.cleaned_data.get('wishlist', False)
            Wishlist.objects.create(
                user=user,
                title=wishlist_title
            )
            return redirect('wishlists')
        else:
            logger.info(form.errors.as_data())
    else:
        form = WishForm() 
    wishlists_params = {
        "wishlists": wishlists,
        'form': form
    }
    return render(request, template_name="wishlists.html", context=wishlists_params)


@login_required(login_url='login')
def wishlist_view(request, wishlist_id):
    logger.info(request.session.session_key)
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id) 
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            wish_title = form.cleaned_data.get('wish')
            wish_link = form.cleaned_data.get('link')
            wish_price = form.cleaned_data.get('price')
            wishlist.wishes.create(
                title=wish_title,
                link=wish_link,
                price=wish_price
            )
            return redirect(f'/{wishlist_id}')
        else:
            logger.info(form.errors.as_data())
    else:
        form = WishForm() 
    if request.GET.get('delete'):
        delete_wish_id = int(request.GET.get('delete'))
        wishlist.wishes.filter(id=delete_wish_id).delete() 
    wishlist_params = {
        'wishlist': wishlist,
        'wishes': wishlist.wishes.all(),
        'form': form
    }
    return render(request, template_name="wishlist.html", context=wishlist_params)


@login_required(login_url='login')
def shared_wishlist_view(request, user_id, wishlist_id):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user_id).get(id=wishlist_id)
    wishes = wishlist.wishes.all()
    logger.info(wishes)
    if request.GET.get('will_give'):
        wish_id = int(request.GET.get('will_give'))
        selected_wish = wishes.get(id=wish_id)
        selected_wish.is_given = True
        selected_wish.save()
        Gift.objects.create(
            user=user,
            title=selected_wish.title,
            price=selected_wish.price,
            link=selected_wish.link
        )
        return redirect(f'/share/{user_id}/{wishlist_id}')
    wishlist_params = {'wishlist': wishlist, 'wishes': wishes}
    return render(request, template_name="share.html", context=wishlist_params)


@login_required(login_url='login')
def delete_wishlist(request, wishlist_id):
    Wishlist.objects.filter(id=wishlist_id).delete()
    return redirect('wishlists')


@login_required(login_url='login')
def selected_gifts_view(request):
    user = request.user
    gifts = Gift.objects.filter(user=user)
    gifts_params = {'gifts': gifts}
    return render(request, template_name='gifts.html', context=gifts_params)


def about_view(request):
    return render(request, template_name='about.html', context={})


def logout_view(request):
    logout(request)
    return redirect('main')

