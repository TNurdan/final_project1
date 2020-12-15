from django.test import TestCase

# Create your tests here.

from catalog.models import Club
from django.urls import reverse

class ClubListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_clubs = 13
        for club_num in range(number_of_clubs):
            Club.objects.create(name='Chelsea %s' % club_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/clubs/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('clubs'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('clubs'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/club_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('clubs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['club_list']) == 10)

    def test_lists_all_clubs(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('clubs')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['club_list']) == 3)