import logging

from django.shortcuts import render, redirect, get_object_or_404

from .models import Wishlist, Gift
from .forms import WishForm, WishlistForm


logger = logging.getLogger(__name__)


def show_main(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session_id = request.session.session_key  # check expire session for lost db data
    logger.info(request.session.session_key)
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_title = form.cleaned_data.get('wishlist', False)
            Wishlist.objects.create(
                session_id=session_id,
                title=wishlist_title
            )
            return redirect('main')
        else:
            logger.info(form.errors.as_data())
    else:
        form = WishForm() 
    wishlists_params = {
        "wishlists": Wishlist.objects.filter(session_id=session_id),
        'form': form
    }
    return render(request, template_name="index.html", context=wishlists_params)


def show_wishlist(request, wishlist_id):
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


def show_shared_wishlist(request, session_key, wishlist_id):
    wishlist = Wishlist.objects.filter(session_id=session_key).get(id=wishlist_id)
    wishes = wishlist.wishes.all()
    logger.info(wishes)
    if request.GET.get('will_give'):
        wish_id = int(request.GET.get('will_give'))
        selected_wish = wishes.get(id=wish_id)
        selected_wish.is_given = True
        selected_wish.save()
        Gift.objects.create(
            session_id=request.session.session_key,
            title=selected_wish.title,
            price=selected_wish.price,
            link=selected_wish.link
        )
        return redirect(f'/share/{session_key}/{wishlist_id}')
    wishlist_params = {'wishlist': wishlist, 'wishes': wishes}
    return render(request, template_name="share.html", context=wishlist_params)


def delete_wishlist(request, wishlist_id):
    Wishlist.objects.filter(id=wishlist_id).delete()
    return redirect('main')


def show_selected_gifts(request):
    session_id = request.session.session_key
    gifts = Gift.objects.filter(session_id=session_id)
    gifts_params = {'gifts': gifts}
    return render(request, template_name='gifts.html', context=gifts_params)


def show_about(request):
    return render(request, template_name='about.html', context={})

