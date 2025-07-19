from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SkillLevel(TextChoices):
    BEGINNER = 'beginner', _('Beginner')
    INTERMEDIATE = 'intermediate', _('Intermediate')
    EXPERT = 'expert', _('Expert')

