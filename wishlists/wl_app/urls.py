from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.show_main, name='main'),
    path('<int:wishlist_id>', views.show_wishlist, name='wishlist'),
    path('delete/<int:wishlist_id>', views.delete_wishlist, name='del_wishlist'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
