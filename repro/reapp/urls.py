from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'reapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
