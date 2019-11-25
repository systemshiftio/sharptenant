from django.urls import path
from . import views
urlpatterns = [
    # The views to handle the logic at home page route is 'views.home'
    path('', views.home,name='main-home'),
    path('about/', views.about, name='main-about'),
    path('signup/', views.create_user, name='main-signup'),
    path('login/', views.login_user, name='main-login')
]