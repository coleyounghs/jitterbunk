from django.urls import path

from . import views

app_name = 'theapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bunk', views.bunk, name='bunk'),
    path('user/<int:idNo>', views.userView, name='user'),
    path('submit_bunk/', views.submit_bunk, name='submit_bunk')
]