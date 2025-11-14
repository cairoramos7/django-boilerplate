from django.urls import path
from users.interfaces.api.views.user_list import UserListView
from users.interfaces.api.views.user_detail import UserDetailView

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("<int:user_id>/", UserDetailView.as_view(), name="user-detail"),
]
