from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views,login 
from django.shortcuts import render,redirect
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


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
    path('register/', register, name='register'),
    # Homepage
    path('home/', home, name='home'),

    # Your Apps
    path('registrar/', include('apps.app1.urls')),
    path('library/', include('apps.app2.urls')),
    path('gates/', include('apps.app3.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
