from django.urls import path
from . import views
import main.views as mv
urlpatterns = [
    # The views to handle the logic at home page route is 'views.home'
    path('', views.home,name='main-home'),
    # path('about/', views.about, name='main-about'),
    path('register/', mv.Register.as_view()),
]