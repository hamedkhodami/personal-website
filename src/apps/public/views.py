from django.views.generic import DetailView, TemplateView

from .models import AboutMe, Skill, Project


class HomeView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_skills = Skill.objects.all()
        ordered_levels = ['expert', 'intermediate', 'beginner']

        sorted_skills = sorted(
            all_skills,
            key=lambda skill: ordered_levels.index(skill.level) if skill.level in ordered_levels else 3
        )

        context.update({
            'about': AboutMe.objects.first(),
            'skills': sorted_skills,
            'projects': Project.objects.order_by('-created_at')[:2],
        })

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




