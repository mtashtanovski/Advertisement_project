from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        customuser = form.save()
        login(self.request, customuser)
        return redirect('accounts:user_detail', pk=customuser.pk)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'custom_user'
