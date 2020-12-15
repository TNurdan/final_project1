from django.test import TestCase

# Create your tests here.

from catalog.models import Club

class ClubModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Club.objects.create(name='Chelsea')

    def test_name_label(self):
        club=Club.objects.get(id=1)
        field_label = club._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_country_label(self):
        club=Club.objects.get(id=1)
        field_label = club._meta.get_field('country').verbose_name
        self.assertEquals(field_label,'country')

    def test_trophies_label(self):
        club=Club.objects.get(id=1)
        field_label = club._meta.get_field('trophies').verbose_name
        self.assertEquals(field_label,'trophies')


    def test_get_absolute_url(self):
        club=Club.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(club.get_absolute_url(),'/catalog/club/1')