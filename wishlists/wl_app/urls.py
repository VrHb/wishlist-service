from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import UserLoginView, RegistrationView, WishlistsView, WishlistView, \
    SharedWishlistView, SelectedGiftsView, View404, LogoutView


handler404 = View404.as_view()

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('wishlists/', WishlistsView.as_view(), name='wishlists'),
    path('lists/<int:wishlist_id>', WishlistView.as_view(), name='wishlist'),
    path('share/<int:user_id>/<int:wishlist_id>', SharedWishlistView.as_view(), name='share_wishlist'),
    path('gifts/', SelectedGiftsView.as_view(), name='gifts'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
