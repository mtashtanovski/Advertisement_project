from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from adverts.forms import SearchForm, AdvertsForm
from adverts.models import Adverts


class AdvertsListView(ListView):
    model = Adverts
    context_object_name = "adverts"
    template_name = "index.html"
    paginate_by = 4
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-public_at")

        if self.search_value:
            query = Q(title__icontains=self.search_value) | \
                    Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class AdvertsCreateView(LoginRequiredMixin, CreateView):
    model = Adverts
    form_class = AdvertsForm
    template_name = "create.html"

    def form_valid(self, form):
        adverts = form.save(commit=False)
        adverts.author = self.request.user
        adverts.save()
        return redirect('adverts:adverts_detail', pk=adverts.pk)


class AdvertsDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'adverts_detail.html'
    model = Adverts
    permission_required = 'adverts.view_adverts'

    def has_permission(self):
        return (
                super().has_permission() and
                self.get_object().author == self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdvertsEditView(PermissionRequiredMixin, UpdateView):
    form_class = AdvertsForm
    template_name = 'adverts_edit.html'
    model = Adverts
    permission_required = 'adverts.change_adverts'

    def has_permission(self):
        return (
                super().has_permission() and
                self.get_object().author == self.request.user
        )

    def get_success_url(self):
        return reverse('adverts:new_adverts_detail', kwargs={'pk': self.object.pk})


class AdvertsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'adverts_delete.html'
    model = Adverts
    context_object_name = 'adverts'
    success_url = reverse_lazy('adverts:index')
    permission_required = 'adverts.delete_adverts'

    def has_permission(self):
        return (
                super().has_permission() and
                self.get_object().author == self.request.user
        )
