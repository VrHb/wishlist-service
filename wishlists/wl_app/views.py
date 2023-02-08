import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session

from .models import Wishlist, Gift



logger = logging.getLogger(__name__)


def show_main(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session_id = request.session.session_key  # check expire session for lost db data
    logger.info(request.session.session_key)
    if request.method == 'POST':
        wishlist_title = request.POST.get('wishlist', False)
        if wishlist_title:
            Wishlist.objects.create(
                session_id=session_id,
                title=wishlist_title
            )
            return redirect('main')
    wishlists_params = {"wishlists": Wishlist.objects.filter(session_id=session_id)}
    return render(request, template_name="index.html", context=wishlists_params)


def show_wishlist(request, wishlist_id):
    logger.info(request.session.session_key)
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id) 
    if request.method == 'POST':
        wish_title = request.POST.get('wish', None)
        wish_link = request.POST.get('link', None)
        wish_price = request.POST.get('price', 0.0)
        logger.info(request.POST)
        if wish_title:
            wishlist.wishes.create(
                title=wish_title,
                link=wish_link,
                price=wish_price
            )
            return redirect(f'/{wishlist_id}')
    if request.GET.get('delete'):
        delete_wish_id = int(request.GET.get('delete'))
        wishlist.wishes.filter(id=delete_wish_id).delete() 
        return redirect(f'/{wishlist_id}')
    wishlist_params = {'wishlist': wishlist, 'wishes': wishlist.wishes.all()}
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


def get_session_key(request):
    session_key = request.session.session_key
    return session_key

