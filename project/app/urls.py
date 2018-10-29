from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage, name='Home'),
    path('withdrawl/', views.withdrawlPage, name='withdrawl'),
    path('createUser/', views.createUser, name='createAnAccount'),
    path('afterSignIn/', views.afterSignIn, name='afterSignIn')
]