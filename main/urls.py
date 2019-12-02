from django.urls import path
from django.conf.urls import handler404
from . import views
import main.views as mv

urlpatterns = [
<<<<<<< HEAD

    path('', views.home,name='main-home'),
    path('register/', mv.Register.as_view()),
    path('signin/', mv.Authentication.as_view()),
    path('review/', views.all_review),
    path('logout/', views.logout_view),
    path('search-review/', views.searchReview),
    path('write-review/', views.writeReview),
    path('review-detail/<int:review_id>/', views.detailReview),
]

handler404 = 'main.views.error_404_view'
=======
    # The views to handle the logic at home page route is 'views.home'
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('register/', mv.Register.as_view(), name="main-register"),
    path('login/', mv.Login.as_view(), name="main-login"),
]
>>>>>>> ec537d404eab69e22f922a581b3565d90fb208c0
