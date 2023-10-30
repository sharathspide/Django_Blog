from django.urls import path
from .views import HomeView, PostDetail
#from . import views

urlpatterns = [
    #path('', views.home, name="Home"),
    path('', HomeView.as_view(), name="Home"),
    path('PostDetail/<int:pk>', PostDetail.as_view(), name = "Post Detail"),
]
