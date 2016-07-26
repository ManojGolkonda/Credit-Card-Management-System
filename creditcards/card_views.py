from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView

from models import Card


@method_decorator(login_required,name='dispatch')
class CardDetailsView(DetailView):
    model = Card
    context_object_name = 'cards'

    def get_queryset(self):
        obj = Card.objects.all().filter(owner=self.request.user)
        return obj
        # return super(CardCreateView, self).get_queryset()


@method_decorator(login_required,name='dispatch')
class CardCreateView(CreateView):
    model = Card
    fields = ['friendly_name','name_on_card','card_number','type','expiry_date']

    def get_queryset(self):
        obj = Card.objects.all().filter(owner=self.request.user)
        return obj
        #return super(CardCreateView, self).get_queryset()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('cards-list')
        #return super(CardCreateView, self).get_success_url()


@method_decorator(login_required,name='dispatch')
class CardListView(ListView):
    model = Card

    def get_queryset(self):
        obj = Card.objects.all().filter(owner=self.request.user)
        return obj
        # return super(CardCreateView, self).get_queryset()


@method_decorator(login_required,name='dispatch')
class CardUpdateView(UpdateView):
    model = Card
    fields = ['friendly_name','name_on_card','card_number','type','expiry_date']

    def get_success_url(self):
        return reverse('card-details-pk')

    def get_queryset(self):
        obj = Card.objects.all().filter(owner=self.request.user)
        return obj
        # return super(CardCreateView, self).get_queryset()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardCreateView, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class CardDeleteView(DetailView):
    model = Card
    success_url = reverse_lazy('cards-list')

    def get_queryset(self):
        obj = Card.objects.all().filter(owner=self.request.user)
        return obj
        # return super(CardCreateView, self).get_queryset()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardCreateView, self).form_valid(form)