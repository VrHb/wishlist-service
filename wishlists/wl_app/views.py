import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse


logger = logging.getLogger(__name__)

wishes = []

def show_main(request):
    if request.method == 'POST':
        wishes.append(request.POST['wish'])
        request.session['wishes'] = wishes
        request.session.save()
        return redirect('/')
    logger.info(logger.info(request.session.items()))
    return render(request, template_name="index.html", context={"wishes": request.session.get('wishes')})


def show_user_wishes(request):
    user = request.user
    wishes = [wish.title for wish in user.wishes.all()]
    return JsonResponse({'wishes': wishes})




