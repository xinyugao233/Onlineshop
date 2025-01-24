from django.urls import path
from apps.users.views import UsersnameCountView,RegisterView

urlpatterns = [
    path('usernames/<username:username>/count/', UsersnameCountView.as_view()),
    path('register/', RegisterView.as_view()),

]