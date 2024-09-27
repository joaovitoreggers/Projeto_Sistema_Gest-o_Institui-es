from django.urls import path
from .views import ( AuthorListCreateView, 
                    AuthorRetriveUpdateDestroyView )

urlpatterns = [
    path('author/', AuthorListCreateView.as_view(), 
         name='author-list-create'),
    path('author/<int:pk>/', AuthorRetriveUpdateDestroyView.as_view(), 
         name='author-update')
]
