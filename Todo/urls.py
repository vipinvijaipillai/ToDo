from django.urls import path
from Todo import views
urlpatterns = [
    path('',views.home, name='home'),
]