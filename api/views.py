from .serializers import GreetingSerializer
from .models import Greeting
from rest_framework.viewsets import ModelViewSet
from .clients import client, session
import requests
from rest_framework.response import Response


class GreetingsAPIModelView(ModelViewSet):
    """
     A viewset for viewing and editing user greetings.
     """
    serializer_class = GreetingSerializer
    queryset = Greeting.objects.all()

    def create(self, request, *args, **kwargs):
        # This will create a http request client that points to the LMS.
        lms = client.create_client('lms')
        greeting = request.data.get("text", None)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        print(greeting)
        token = session.fetch_token(lms.access_token_url, username=username, password=password)
        # Here, we authenticate the client with the token we got from the LMS. In a real-world
        # application, we'd save this token somehow for subsequent requests.
        # And then, we use this token to fetch the user's info.
        resp = lms.get('/api/user/v1/me?greeting={}'.format(greeting), token=token)
        resp.raise_for_status()
        response = super().create(request, *args, **kwargs)
        if greeting == "hello":
            # call again using 'goodbye' as a greeting
            greeting = "goodbye"
            uri = request.build_absolute_uri()
            data = dict(text=greeting, username=username, password=password)
            response = requests.post(uri, data).json()
            response = Response(response)
        return response
