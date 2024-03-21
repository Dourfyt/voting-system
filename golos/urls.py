
from django.urls import path
from golos.views import index,login, logout_user

app_name="golos"
urlpatterns = [
    path('login/', login, name="login"),
    path('', index, name="index"),
    path('logout/', logout_user, name="logout"),
]