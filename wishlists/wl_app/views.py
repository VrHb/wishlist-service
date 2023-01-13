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


def get_wishlist(request, wishlist):
    return JsonResponse({'wish_params': request.session.get('wishlists').get(wishlist)})


def delete_wishlist(request, wishlist):
    wishes = request.session.get('wishlists')
    wishes.pop(wishlist)
    request.session.save()
    return redirect('main')
