from django.urls import path
from . import views

app_name = 'apps.public'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('skills/<int:category_id>/', views.HomeView.as_view(), name='skill_category'),  # TODO
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.DetailProjectView.as_view(), name='project_detail'),

]
