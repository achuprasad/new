from django.urls import path
from . import views

urlpatterns = [
    path('',views.TicketCreateView.as_view(),name='ticket_create'),
    path('list_view/',views.TicketListView.as_view(),name='ticket_list'),
]
