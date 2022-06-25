from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm
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


class UpdateCustomUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "update_customuser.html"
    context_object_name = "custom_user"

    def get_success_url(self):
        return reverse("accounts:user_detail", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
