from django.urls import path
from . import views
#importing class views
from .views import homeview, articledetailview, postview, updatepost


urlpatterns = [
    path('', views.home, name='index'),
    path('programs/', views.program, name='programs'),
    path('videos/', views.videos, name='videos'),    
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('trainers/', views.trainers, name='trainers'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('blogs/', homeview.as_view(), name="blogs"),
    path('article/<int:pk>', articledetailview.as_view(), name="article-detail"),
    path('add_post/', postview.as_view(), name="add_post"),
    path('article/edit/<int:pk>', updatepost.as_view(), name="update_post" ),
  
   
]

#urlpatterns = [
 ##  path('article/<int:pk>', articledetailview.as_view(), name="article-detail"),
#]
