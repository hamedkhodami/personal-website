from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import AboutMe, Project, ProjectImage, Skill, JobExperience


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'github_link', 'linkedin_link', 'resume_download')
    readonly_fields = ('resume_preview',)
    fieldsets = (
        (_('Personal Info'), {
            'fields': ('bio', 'email', 'resume_file', 'resume_preview')
        }),
        (_('Social Links'), {
            'fields': ('github', 'linkedin', 'telegram', 'instagram')
        }),
    )

    def github_link(self, obj):
        if obj.github:
            return format_html("<a href='{}' target='_blank'>GitHub</a>", obj.github)
        return "-"
    github_link.short_description = _('GitHub')

    def linkedin_link(self, obj):
        if obj.linkedin:
            return format_html("<a href='{}' target='_blank'>LinkedIn</a>", obj.linkedin)
        return "-"
    linkedin_link.short_description = _('LinkedIn')

    def resume_download(self, obj):
        if obj.resume_file:
            return format_html("<a href='{}' download>Download Resume</a>", obj.resume_file.url)
        return "-"
    resume_download.short_description = _('Resume')

    def resume_preview(self, obj):
        if obj.resume_file:
            return format_html("<iframe src='{}' style='width:100%;height:500px;'></iframe>", obj.resume_file.url)
        return _("No resume uploaded")
    resume_preview.short_description = _('Resume Preview')


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('title',)
    show_change_link = True


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'icon')
    list_filter = ('level',)
    search_fields = ('title',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'alt_text', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html("<img src='{}' style='max-width:100px; max-height:100px;' />", obj.image.url)
        return "-"

    image_preview.short_description = _("Preview")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'creation_at', 'project_url_link', 'github_url_link')
    list_filter = ('tech_stack',)
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    fieldsets = (
        (_('Project Info'), {
            'fields': ('title', 'slug', 'short_description', 'description', 'image')
        }),
        (_('Links'), {
            'fields': ('project_url', 'github_url')
        }),
        (_('Technology Stack'), {
            'fields': ('tech_stack',)
        }),
        (_('date'), {
            'fields': ('creation_at',)
        }),
    )

    def project_url_link(self, obj):
        if obj.project_url:
            return format_html("<a href='{}' target='_blank'>Site</a>", obj.project_url)
        return "-"

    project_url_link.short_description = _("Live URL")

    def github_url_link(self, obj):
        if obj.github_url:
            return format_html("<a href='{}' target='_blank'>GitHub</a>", obj.github_url)
        return "-"

    github_url_link.short_description = _("GitHub URL")


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date', 'location', 'description', 'created_at')
    list_filter = ('company_name', 'position')
    search_fields = ('company_name', 'position',)
    fieldsets = (
        (_('job Info'), {
            'fields': ('company_name', 'position', 'location', 'description')
        }),
        (_('date'), {
            'fields': ('start_date', 'end_date')
        }),
    )
