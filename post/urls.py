from django.urls import path
from .views import PostListCreateView, PostRetriveUpdateDestroyView

urlpatterns = [
    path('post/', PostListCreateView.as_view(), name='post_list_create'),
    path('post<int:pk>', PostRetriveUpdateDestroyView.as_view(), name='post_update')
]
