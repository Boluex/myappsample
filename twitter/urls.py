from django.urls import path
from .import views
urlpatterns =[
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('userposts/<str:username>',views.userpost,name='userposts'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.remove,name='delete'),
    path('interest/',views.interest,name='like'),
    path('add/',views.add,name='create'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('comment/<int:id>',views.Comment,name='comment'),
    path('comments/<int:id>',views.commentpost,name='comments'),
]