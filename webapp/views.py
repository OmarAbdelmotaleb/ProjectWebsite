from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
# Create your views here.

# from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth.decorators import login_required

# from .models import ClickCount
# from .serializers import ClickCountSerializer
from .models import Users
from .serializers import UsersSerializer

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

def index(request):
    return render(request, 'index.html')

class UsersAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                user = Users.objects.get(pk=pk)
                serializer = UsersSerializer(user)
                return Response(serializer.data)
            except Users.DoesNotExist:
                raise Http404
        else:
            users = Users.objects.all()
            serializer = UsersSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
