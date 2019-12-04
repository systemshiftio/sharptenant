from django.urls import path
from django.conf.urls import handler404
from . import views
import main.views as mv

urlpatterns = [

    path('', views.home, name='main-home'),
    path('', views.about, name='main-about'),
    path('register/', mv.Register.as_view()),
    path('signin/', mv.Authentication.as_view()),
    path('review/', views.all_review),
    path('logout/', views.logout_view),
    path('search-review/', views.searchReview),
    path('write-review/', views.writeReview),
    path('review-detail/<int:review_id>/', views.detailReview),
    path('subscribe/', views.subscribe),
    path('about/', views.about),
]

handler404 = 'main.views.error_404_view'
