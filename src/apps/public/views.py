from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404

from .models import AboutMe, SkillCategory, Skill, Project


class HomeView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = kwargs.get('category_id')
        category = get_object_or_404(SkillCategory, id=category_id) if category_id else None

        context['category'] = category
        context['skills'] = Skill.objects.filter(category=category).order_by('-created_at') if category else []
        context['projects'] = Project.objects.all().order_by('-created_at')[:2]

        return context


class AboutView(TemplateView):
    template_name = 'public/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.first()

        return context


class ProjectsView(TemplateView):
    template_name = 'public/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('-created_at')

        return context


class DetailProjectView(DetailView):
    model = Project
    template_name = 'public/project_detail.html'
    context_object_name = 'project_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




