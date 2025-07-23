from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .enums import SkillLevel as Level


class AboutMe(BaseModel):
    bio = models.TextField(_('Biography'))
    resume_file = models.FileField(_('Resume (PDF)'), upload_to='resumes/')
    github = models.URLField(_('GitHub'), blank=True, null=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True, null=True)
    telegram = models.URLField(_('Telegram'), blank=True, null=True)
    instagram = models.URLField(_('Instagram'), blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)

    class Meta:
        verbose_name = _("About Me")

    def __str__(self):
        return str(_('About Me'))


class Skill(BaseModel):
    title = models.CharField(_('Skill'), max_length=64)
    icon = models.ImageField(_('Icon'), upload_to='skill/icon', null=True, blank=True)
    level = models.CharField(_('Level'), choices=Level.choices, default=Level.BEGINNER
                             , null=True, blank=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.title


class Project(BaseModel):
    title = models.CharField(_('Title'), max_length=128)
    slug = models.SlugField(_('Slug'), unique=True)
    description = models.TextField(_('Description'))
    short_description = models.CharField(_('Shot Description'), max_length=250)
    tech_stack = models.ManyToManyField('public.Skill', verbose_name=_('Technologies Used'), blank=True)
    image = models.ImageField(_('Image'), upload_to='projects/image', null=True, blank=True)
    project_url = models.URLField(_('Live URL'), null=True, blank=True)
    github_url = models.URLField(_('GitHub URL'), null=True, blank=True)
    creation_at = models.CharField(_("Creation At"), null=True, blank=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class ProjectImage(BaseModel):
    project = models.ForeignKey('public.Project', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_('Image'), upload_to='projects/gallery/')
    alt_text = models.CharField(_('Alt Text'), max_length=128, blank=True)

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')

    def __str__(self):
        return f"{self.project.title} - Image"


class JobExperience(BaseModel):
    company_name = models.CharField(_('Company Name'), max_length=128)
    position = models.CharField(_('Job Title'), max_length=128)
    start_date = models.CharField(_('Start Date'), max_length=128)
    end_date = models.CharField(_('End Date'), max_length=128, default=_("now"))
    location = models.CharField(_('Location'), max_length=128, blank=True)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _('Job Experience')
        verbose_name_plural = _('Job Experiences')

    def __str__(self):
        return f"{self.position} at {self.company_name}"


