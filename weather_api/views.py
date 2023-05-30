import requests
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .utils import check_available_memory


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WeatherView(generics.GenericAPIView):
    def get(self, request):
        city = request.query_params.get('city')
        date = request.query_params.get('date')
        url = f'https://wttr.in/{city}?date={date}&format=%C+%t'
        response = requests.get(url)
        data = {
            'city': city,
            'date': date,
            'weather': response.text.strip()
        }
        return Response(data)


class MemoryView(generics.GenericAPIView):
    def get(self, request):
        data = check_available_memory()
        return Response(data)
