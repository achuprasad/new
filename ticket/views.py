import random

from django.shortcuts import render, redirect
from django.views import View
from .forms import TicketForm
from .models import Ticket
import requests


class TicketCreateView(View):
    """
    View for creating a new ticket.
    GET request: Renders the ticket creation form.
    POST request: Saves the ticket data to the database.
    """

    def get(self, request):
        """
        Handle GET request to render the ticket creation form.
        """
        form = TicketForm()
        return render(request, 'create_ticket.html', {'form': form})

    def post(self, request):
        """
        Handle POST request to save the ticket data to the database.
        """
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)

            # Check the selected social media platform
            selected_platform = form.cleaned_data['social_media_platform']
            if selected_platform == 'facebook':
                # Get interests from Facebook
                email = form.cleaned_data['email']
                facebook_interests = get_facebook_interests(email)
                ticket.interests = facebook_interests
            if selected_platform == "pinterest":
                name = form.cleaned_data['name']
                pinterest_interests = get_pinterest_interests(name)
                ticket.interests = pinterest_interests

            ticket.save()

            return redirect('ticket_list')

        return render(request, 'ticket/create_ticket.html', {'form': form})


def get_facebook_interests(email):
    """
    Retrieve interests from Facebook based on the lead's email.
    """
    api_endpoint = 'https://graph.facebook.com'
    access_token = ''

    url = f'{api_endpoint}/v17.0/search'
    random_interests = ['Golf', 'Tennis', 'Soccer', 'Basketball']
    random_interest = random.choice(random_interests)
    params = {
        'type': 'adinterest',
        'q': random_interest,
        'access_token': access_token,
        'email': email
    }
    response = requests.get(url, params=params)
    interests = response.json().get('data', [])
    print(interests, '.....interest')

    return interests

def get_pinterest_interests(username):
    """
    Retrieve interests from Pinterest based on the user's email.
    """
    access_token = ''
    api_endpoint = 'https://api.pinterest.com'

    url = f'{api_endpoint}/v5/users/{username}/interests/follow'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    interests = response.json().get('data', [])
    print(interests,'....... interest')

    return interests


class TicketListView(View):
    """
    View for displaying a list of tickets.
    GET request: Renders the ticket list page.
    """
    def get(self, request):
        """
        Handle GET request to render the ticket list page.
        """
        tickets = Ticket.objects.all()
        return render(request, 'ticket_list.html', {'tickets': tickets})

