from django.urls import path
from .views import homepage, taskpage

urlpatterns = [
    path('', homepage, name = 'home'),
    path('task/', taskpage, name = 'task')
]