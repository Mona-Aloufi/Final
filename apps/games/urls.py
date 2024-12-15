from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="homePage"),
    path('list',views.list,name="gameslis"),
]