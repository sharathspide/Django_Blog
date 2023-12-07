from django.urls import path
from .views import HomeView, PostDetailView, CreatePostview
#from . import views

urlpatterns = [
    #path('', views.home, name="Home"),
    path('', HomeView.as_view(), name="Home"),
    path('PostDetail/<int:pk>', PostDetailView.as_view(), name = "Post Detail"),
    path('AddPost/', CreatePostview.as_view(), name="Create Post"),
]
