import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse


logger = logging.getLogger(__name__)


def show_main(request):
    if request.method == 'POST':
        if 'wishes' not in request.session:
            request.session['wishes'] = {}
        request.session['wishes'][f"{request.POST['wish']}"] = "wishes_params"
        request.session.save()
        return redirect('main')
    logger.info(logger.info(request.session.items()))
    return render(request, template_name="index.html", context={"wishes": request.session.get('wishes')})


def get_wish(request, wish):
    return JsonResponse({'wishes': request.session.get('wishes').get(wish)})

