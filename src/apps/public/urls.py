from django.urls import path
from . import views

app_name = 'apps.public'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.DetailProjectView.as_view(), name='project_detail'),

]
