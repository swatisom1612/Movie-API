import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response


def fetch_movie_list(page):
    try:
        fetched = False
        attempt = 0
        # Credy movie API
        api_url = 'https://demo.credy.in/api/v1/maya/movies/'
        # Checks for pagination
        if page is not None:
            api_url += f'?page={page}'
        # check for multiple attempt
        while not fetched:
            attempt += 1
            print(attempt)
            # Credy movie API response
            response = requests.get(api_url, auth=HTTPBasicAuth(settings.MOVIE_LIST_API_CLIENT_ID,
                                                                settings.MOVIE_LIST_API_CLIENT_SECRET))

            if response.status_code == 200:
                # if we get the successful response than setting it to true
                fetched = True
                return Response(response.json())
    except requests.exceptions.ConnectionError:
        return Response({
            'error': 'Please check your internet connection'
        })
