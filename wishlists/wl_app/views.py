import logging

from django.shortcuts import render, redirect
from django.forms import Form
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, FormView, ListView
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Wishlist, Gift, Wish
from .forms import WishForm, WishlistForm, LoginForm, RegisterUser


logger = logging.getLogger(__name__)


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('wishlists')


    def form_invalid(self, form: Form) -> HttpResponse:
        messages.error(
            self.request,
            'Неправильный пароль или имя пользователя!'
        )
        response = super().form_invalid(form)
        response.status_code = 401
        return response

class RegistrationView(CreateView):
    form_class = RegisterUser 
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    # TODO send message after success reg to login page

class WishlistsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    form_class = WishlistForm 
    template_name = 'wishlists.html'
    context_object_name = 'wishlists'


    def get_queryset(self) -> QuerySet:
        if self.request.GET.get('delete'):
            wishlist_id = self.request.GET.get('delete')
            Wishlist.objects.filter(id=wishlist_id).delete()
        user = self.request.user
        return Wishlist.objects.filter(user=user)


    def get_context_data(self, **kwargs) -> dict:
        context = super(WishlistsView, self).get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        logger.info(context)
        return context


    def post(self, request: HttpRequest) -> HttpResponse:
        self.object_list = self.get_queryset()
        user = self.request.user
        form = self.form_class(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            wishlist_title = form.cleaned_data.get('wishlist', False)
            Wishlist.objects.create(
                user=user,
                title=wishlist_title
            )
            return self.render_to_response(context)
        messages.error(
            self.request,
            'Введите корректное название списка!'
        )
        return self.render_to_response(context)

# TODO may be use DetailView
class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    form_class = WishForm 
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'
    success_url = reverse_lazy('login')


    def get_queryset(self) -> QuerySet:
        if self.request.GET.get('delete'):
            wishlist_id = int(self.request.GET.get('delete'))
            Wishlist.objects.filter(id=wishlist_id).delete()
        return Wishlist.objects.get(id=self.kwargs['wishlist_id'])


    def get_context_data(self, **kwargs) -> dict:
        context = super(WishlistView, self).get_context_data(**kwargs)
        logger.info(context)
        return context
    

    def post(self, request: HttpRequest, wishlist_id: int) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            wishlist = Wishlist.objects.get(id=wishlist_id)
            wish_title = form.cleaned_data.get('wish')
            wish_link = form.cleaned_data.get('link')
            wish_price = form.cleaned_data.get('price')
            wishlist.wishes.create(
                title=wish_title,
                link=wish_link,
                price=wish_price
            )
            return redirect('wishlist', wishlist_id=wishlist_id)
        return render(request, self.template_name, {'form': form})

class SharedWishlistView(DetailView):
    model = Wishlist
    template_name = 'share.html'
    pk_url_kwarg = 'wishlist_id'
    context_object_name = 'wishlist'


    # TODO move will give logic to another func
    def get_context_data(self, **kwargs) -> dict:
        context = super(SharedWishlistView, self).get_context_data(**kwargs)
        wishlist = Wishlist.objects.get(id=self.kwargs['wishlist_id'])
        context['wishes'] = wishlist.wishes.all()
        if self.request.GET.get('will_give'):
            wish_id = int(self.request.GET.get('will_give'))
            selected_wish = context['wishes'].get(id=wish_id)
            selected_wish.is_given = True
            selected_wish.save()
            logger.info(selected_wish.id)
            Gift.objects.create(
                user=self.request.user,
                title=selected_wish.title,
                price=selected_wish.price,
                link=selected_wish.link,
                wish_id=selected_wish.id
            )
        logger.info(context)
        return context

class SelectedGiftsView(ListView):
    model = Gift
    template_name = 'gifts.html'
    context_object_name = 'gifts'
    

    def post(self, request: HttpRequest) -> HttpResponse:
        self.object_list = self.get_queryset()
        gifts = self.object_list
        gift_id = int(request.POST.get('gift_id'))
        gifts.get(id=gift_id).delete()
        wishes = Wish.objects.all()
        wish_id = int(request.POST.get('wish_id'))
        selected_wish = wishes.get(id=wish_id)
        selected_wish.is_given = False 
        selected_wish.save()
        return redirect('gifts')

class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('main')
