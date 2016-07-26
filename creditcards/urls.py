from django.conf.urls import url
from card_views import CardCreateView
from creditcards import card_views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/update/$', card_views.CardUpdateView.as_view(), name='card-update-pk'),
    url(r'^add/$',card_views.CardCreateView.as_view(),name='create-card'),
    url(r'^list/$',card_views.CardListView.as_view(),name='cards-list'),
    #url(r'^(?P<friendly_name>[A-Za-z\s]+)/details/$',card_views.CardDetailsView.as_view(),name='card-details'),
    url(r'^(?P<pk>[0-9]+)/details/$',card_views.CardDetailsView.as_view(),name='card-details-pk'),
    url(r'^(?P<pk>[0-9]+)/delete/$', card_views.CardDeleteView.as_view(), name='card-delete-pk'),

]