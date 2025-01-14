
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.login_view, name='login'),
    path('admin_login/', views.login_view, name='admin_login'),
    path('userlogin_page/', views.userlogin, name='userlogin_page'),
    path('signup/', views.sign_up, name='signup'),
    path("login/", views.userlogin, name="login"),
    path("adminhome/", views.admin_home, name="admin_home"),
    path("userhome/", views.user_home, name="user_home"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('app/<int:app_id>/', views.app_details, name='app_details'),
    path('profile/', views.profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)