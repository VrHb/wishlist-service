from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.show_main, name='main'),
    path('wishes/<wish>', views.get_wish, name='get_wish'),
    path('delete/<wish>', views.delete_wish, name='del_wish'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
