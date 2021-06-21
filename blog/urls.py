from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.PostsView.as_view(), name='post-page'),
    path('posts/<slug:slug>', views.DetailPostView.as_view(), name='post-detail-page')
]
