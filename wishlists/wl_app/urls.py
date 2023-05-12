from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.main_view, name='main'),
    path('wishlists/', views.wishlists_view, name='wishlists'),
    path('<int:wishlist_id>', views.wishlist_view, name='wishlist'),
    path('share/<int:user_id>/<int:wishlist_id>', views.shared_wishlist_view, name='share_wishlist'),
    path('delete/<int:wishlist_id>', views.delete_wishlist, name='del_wishlist'),
    path('gifts/', views.selected_gifts_view, name='gifts'),
    path('about/', views.about_view, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
