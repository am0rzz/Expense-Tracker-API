from django.urls import path, include
from .views import Register, LogOutView

urlpatterns =[
    path('register/',Register.as_view()),
    path('logout/', LogOutView.as_view())
]