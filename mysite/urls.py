from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(
        template_name='auth/login.html'
    ), name='logout'),

    # Homepage
    path('home/', home, name='home'),

    # Your Apps
    path('registrar/', include('apps.app1.urls')),
    path('library/', include('apps.app2.urls')),
    path('gates/', include('apps.app3.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
