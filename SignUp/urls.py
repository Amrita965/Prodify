
from django.urls import path
from SignUp.views import signup

urlpatterns = [
    path('signup/', signup),
]
