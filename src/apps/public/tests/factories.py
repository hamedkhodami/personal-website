import factory
from factory.django import DjangoModelFactory
from django.core.files.base import ContentFile
from faker import Faker

from apps.public.models import AboutMe

faker = Faker(locale='fa_IR')


class AboutMeFactory(DjangoModelFactory):
    class Meta:
        model = AboutMe

    bio = factory.LazyFunction(lambda: faker.paragraph(nb_sentences=3))
    resume_file = factory.LazyAttribute(lambda o: ContentFile(b'Fake PDF content', name='resume.pdf'))
    github = factory.LazyFunction(lambda: faker.url())
    linkedin = factory.LazyFunction(lambda: faker.url())
    telegram = factory.LazyFunction(lambda: faker.url())
    instagram = factory.LazyFunction(lambda: faker.url())
    email = factory.LazyFunction(lambda: faker.email())