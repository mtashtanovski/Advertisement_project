from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import (
    ListView,
    CreateView,
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
        form.instance.author = self.request.user
        return super().form_valid(form)
