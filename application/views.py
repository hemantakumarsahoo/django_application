from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import App, User,Screenshot
from .serializers import AppSerializer, UserSerializer
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import AppForm  # Assuming you have a form class

 # default user page
def home(request):
    return render(request, 'home.html')  # 

# Admin or user login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:  # Checks if the user is an admin
                return redirect('admin_dashboard')
            else:
                return redirect('')  # Redirect normal users to their profile
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


@api_view(['GET'])
def list_apps(request):
    apps = App.objects.all()
    serializer = AppSerializer(apps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# Admin dashboard adding application  
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponse("Unauthorized", status=401)

    if request.method == "POST":
        # Handle form submission
        name = request.POST.get('name')
        app_link = request.POST.get('app_link')
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        points = request.POST.get('points')
        icon=request.POST.get('icon')

        App.objects.create(
            name=name,
            app_link=app_link,
            points=points,
            icon=icon
        )
        return redirect('admin_dashboard')

    apps = App.objects.all()
    return render(request, 'admin_dashboard.html', {'apps': apps})

# -----------------------------------------------------------------------user----------------------------

User = get_user_model()  # Use the custom user model
# Create the  new user 
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Create the user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        return render(request, "userlogin.html", {"user": user})
    return render(request, "signup.html")
# user  login 
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:  # If authentication is successful
            login(request, user)  # Log the user in
            
            # Redirect based on user type or other conditions
            if user.is_superuser:
                return redirect("admin_home")  # Redirect superuser to admin home
            else:
                return redirect("user_home")  # Redirect regular users to user home
        
        # If authentication fails
        return render(request, "userlogin.html", {"error": "Invalid username or password"})
    
    return render(request, "userlogin.html")

# profile
@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        # Handling profile update
        if 'firstName' in request.POST:
            user.first_name = request.POST['firstName']
            user.last_name = request.POST['lastName']
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        
        # Handling password change
        elif 'currentPassword' in request.POST:
            current_password = request.POST['currentPassword']
            new_password = request.POST['newPassword']
            confirm_password = request.POST['confirmPassword']

            if not user.check_password(current_password):
                messages.error(request, 'Current password is incorrect.')
            elif new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
            elif len(new_password) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Keep the user logged in
                messages.success(request, 'Password changed successfully!')
                return redirect('profile')

    return render(request, 'profile.html', {'user': user})

def admin_home(request):
    return render(request, 'admin_dashboard.html')

# show the details of application 
def app_details(request, app_id):
    app = get_object_or_404(App, id=app_id)
    
    # If the app doesn't have an icon set, assign a default icon URL
    if not app.icon:
        app.icon_url = '/media/app_icon/default_icon.png'
    else:
        app.icon_url = app.icon.url
    
    if request.method == 'POST' and request.FILES.get('screenshot'):
        screenshot = Screenshot(app=app, image=request.FILES['screenshot'])
        screenshot.save()
        return JsonResponse({'message': 'Screenshot uploaded successfully!'})

    return render(request, 'app_details.html', {'app': app})


def user_home(request):
    apps = App.objects.all()
    for app in apps:
        if not app.icon:
            app.icon_url = '/media/app_icon/default_icon.png'
        else:
            app.icon_url = app.icon.url
    return render(request, 'user_home.html', {'apps': apps})


def add_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('app_list')  # Replace 'app_list' with your desired redirect
    else:
        form = AppForm()

    return render(request, 'add_app.html', {'form': form})

