from django.urls import path
from . import views
from .views import FavoriteView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # Add the following two lines for favorite functionality
    path('add_favorite/<int:news_story_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:news_story_id>/', views.remove_favorite, name='remove_favorite'),
    path('favorites/', views.FavoriteView, name='favorites'),
    path('add-story/', views.AddStoryView.as_view(), name='add_story'),
]
