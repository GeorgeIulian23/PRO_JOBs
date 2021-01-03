from django.urls import path

from aplicatie3 import views

app_name = 'aplicatie3'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('add_jobs/', views.CreateJobsView.as_view(), name="adaugare"),
    path('edit_jobs/<int:pk>/', views.UpdateJobsView.as_view(), name="modificare"),
]
