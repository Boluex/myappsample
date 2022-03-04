from django.urls import path
from.import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.logins,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profiles,name='profile'),

]