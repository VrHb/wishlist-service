import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse


logger = logging.getLogger(__name__)


def show_main(request):
    if request.method == 'POST':
        if 'wishlists' not in request.session:
            request.session['wishlists'] = []
        wishlist_title = request.POST['wishlist']
        if wishlist_title:
            wishlist_id = len(request.session['wishlists'])
            wishlist_params = {
                'id': wishlist_id,
                'title': wishlist_title,
                'wishes': []
                }
            request.session['wishlists'].append(wishlist_params)
            request.session.save()
            return redirect('main')
    logger.info(logger.info(request.session.items()))
    wishlists_params = {"wishlists": request.session.get('wishlists')}
    return render(request, template_name="index.html", context=wishlists_params)


def show_wishlist(request, wishlist_id):
    wishlist = request.session.get('wishlists')[wishlist_id]
    if request.method == 'POST':
        wish_title = request.POST['wish']
        wish_link = request.POST['link']
        wish_price = request.POST['price']
        if wish_title:
            wishlist.get('wishes').append({
                'title': wish_title,
                'link': wish_link,
                'price': wish_price,
                'id': len(wishlist.get('wishes')),

                # need give status from share list
                'will_give': False, 
            })
            request.session.save()
            return redirect(f'/{wishlist_id}')
    logger.info(request.session.items())
    wishes = wishlist.get('wishes')
    if request.GET.get('delete'):
        wishes.pop(int(request.GET['delete']))
        request.session.save()
        return redirect(f'/{wishlist_id}')
    logger.info(request.GET)
    wishlist_params = {'wishlist': wishlist, 'wishes': wishes}
    return render(request, template_name="wishlist.html", context=wishlist_params)


def delete_wishlist(request, wishlist_id):
    wishlists = request.session.get('wishlists')
    wishlists.pop(wishlist_id)
    request.session.save()
    return redirect('main')
