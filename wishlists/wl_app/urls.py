from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.show_main, name='main'),
    path('<wishlist>', views.get_wishlist, name='get_wishlist'),
    path('delete/<wishlist>', views.delete_wishlist, name='del_wishlist'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
