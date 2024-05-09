from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
# Create your views here.

from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

# from .models import ClickCount
# from .serializers import ClickCountSerializer
from .models import Users
from .serializers import UsersSerializer
from .forms import RegistrationForm

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  


# @csrf_protect
# @cache_page(300)
# def index(request):
#     if request.method == 'POST':  # If the button was clicked
#         obj, created = ClickCount.objects.get_or_create(id=1)
#         obj.count += 1
#         obj.save()
#         return redirect('index')  # Reload the page

#     obj, created = ClickCount.objects.get_or_create(id=1)
#     context = {'count': obj.count}
#     return render(request, 'index.html', context)

def index(request):
    return render(request, 'index.html')

@login_required
def update_clicks(request):
    if request.method == 'POST':
        user_profile = Users.objects.get(user_id=request.user) # Fetch related Users object 
        user_profile.clicks += 1  
        user_profile.save()
        return Response({'message': 'Clicks updated succesfully'})
    else:
        return Response({'message': 'Use a POST request to update clicks'}, status=status.HTTP_400_BAD_REQUEST)

class CurrentUserAPIView(APIView):
    def get(self, request):
      serializer = UsersSerializer(request.user)
      return Response(serializer.data)
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            UserModel = get_user_model()  # Get the User model
            try:
                user = UserModel.objects.create_user(username, password=password)
                Users.objects.create(user_id=user)
                user.save()
                login(request, user)
                return Response({'message': 'Login successful (new user created)'})
            except Exception as e:
                # Handle potential user creation errors (e.g., duplicate username)
                print(f"Error creating user: {e}")  # Log the error for now
                return Response({'message': 'Login failed (user creation error)'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class UsersAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             try:
#                 user = Users.objects.get(pk=pk)
#                 serializer = UsersSerializer(user)
#                 return Response(serializer.data)
#             except Users.DoesNotExist:
#                 raise Http404
#         else:
#             users = Users.objects.all()
#             serializer = UsersSerializer(users, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         try:
#             user = Users.objects.get(pk=pk)
#         except Users.DoesNotExist:
#             raise Http404

#         serializer = UsersSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             user = Users.objects.get(pk=pk)
#         except Users.DoesNotExist:
#             raise Http404

#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UpdateClickCountView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def post(self, request):
#         obj, created = ClickCount.objects.get_or_create(user=request.user)
#         obj.count += 1
#         obj.save()
#         return Response({"status": "success"})

# class RegisterView(APIView):
#     def post(self, request):    
#         form = RegistrationForm(request.data)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  
#             return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

