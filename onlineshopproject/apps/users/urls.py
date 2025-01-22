from django.urls import path
from apps.users.views import UsersnameCountView

urlpatterns = [
    path('usernames/<username:username>/count/', UsersnameCountView.as_view()),


]