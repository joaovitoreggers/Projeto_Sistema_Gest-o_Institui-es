from django.urls import path
from .views import UserListCreateView, UserRetriveUpdateDestroyView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('accounts/', UserListCreateView.as_view(), name='user_list_create'),
    path('accounts/<int:pk>/', UserRetriveUpdateDestroyView.as_view(), name='user_list_create'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
