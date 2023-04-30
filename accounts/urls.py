from .views import *
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    ]