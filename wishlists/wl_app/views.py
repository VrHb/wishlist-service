import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse


logger = logging.getLogger(__name__)


def show_main(request):
    if request.method == 'POST':
        if 'wishlists' not in request.session:
            request.session['wishlists'] = {}
        
        # need generate wish id for wish key
        wishlist_title = request.POST['wishlist']
        if wishlist_title:
            request.session['wishlists'][f"{wishlist_title}"] = {"link": "", "Image": ""}
            request.session.save()
            return redirect('main')
    logger.info(logger.info(request.session.items()))
    return render(request, template_name="index.html", context={"wishlists": request.session.get('wishlists')})


def show_wishlist(request, wishlist):
    if request.method == 'POST':
        wishlists = request.session.get('wishlists')
        if 'wishes' not in wishlists.get(wishlist):
            wishlists.get(wishlist)['wishes'] = {}

        # need generate wish id for wish key
        wish_title = request.POST['wish']
        if wish_title:
            wishlists.get(wishlist)['wishes'][f"{wish_title}"] = {}
            request.session.save()
            return redirect(f'/{wishlist}')
    logger.info(request.session.items())
    if request.GET.get('delete'):
        wishes = request.session.get('wishlists').get(wishlist).get('wishes')
        wishes.pop(request.GET['delete'])
        request.session.save()
        return redirect(f'/{wishlist}')
    logger.info(request.GET)
    return render(request, template_name="wishlist.html", context={'wishlist': wishlist, 'wishes': request.session.get('wishlists').get(wishlist).get('wishes')})


def delete_wishlist(request, wishlist):
    wishes = request.session.get('wishlists')
    wishes.pop(wishlist)
    request.session.save()
    return redirect('main')

