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
            wishlists.get(wishlist)['wishes'] = []

        # need generate wish id for wish key
        wish_title = request.POST['wish']
        wish_link = request.POST['link']
        wish_price = request.POST['price']
        if wish_title:
            wishlists.get(wishlist)['wishes'] += [{
                'title': wish_title,
                'link': wish_link,
                'price': wish_price,
                'id': len(wishlists.get(wishlist)['wishes'])
            }]
            request.session.save()
            return redirect(f'/{wishlist}')
    logger.info(request.session.items())
    wishes = request.session.get('wishlists').get(wishlist).get('wishes')
    if request.GET.get('delete'):
        wishes.pop(int(request.GET['delete']))
        request.session.save()
        return redirect(f'/{wishlist}')
    logger.info(request.GET)
    return render(request, template_name="wishlist.html", context={'wishlist': wishlist, 'wishes': wishes})


def delete_wishlist(request, wishlist):
    wishes = request.session.get('wishlists')
    wishes.pop(wishlist)
    request.session.save()
    return redirect('main')

