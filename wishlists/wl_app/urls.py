from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.main_view, name='main'),
    path('wishlists/', views.wishlists_view, name='wishlists'),
    path('<int:wishlist_id>', views.show_wishlist, name='wishlist'),
    path('share/<session_key>/<int:wishlist_id>', views.show_shared_wishlist, name='share_wishlist'),
    path('delete/<int:wishlist_id>', views.delete_wishlist, name='del_wishlist'),
    path('gifts/', views.show_selected_gifts, name='gifts'),
    path('about/', views.show_about, name='about'),
    path('logout/', views.show_logout, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
