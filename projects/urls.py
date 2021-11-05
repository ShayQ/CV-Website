from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.ProjectView.as_view(), name='project_view'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('', views.ProfileView.as_view(), name='profile')
]