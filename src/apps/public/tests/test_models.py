import pytest
from apps.public.tests.factories import AboutMeFactory


@pytest.mark.django_db
class TestAboutMe:

    def test_aboutme_model_creation(self):
        instance = AboutMeFactory()

        assert instance.pk is not None
        assert str(instance) == 'About Me'
        assert instance.resume_file.name.endswith('.pdf')
        assert '@' in instance.email
        assert instance.github.startswith('http')
        assert len(instance.bio.strip()) > 0
