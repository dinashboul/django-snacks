from django.urls import reverse
from django.test import SimpleTestCase

# Create your tests here.
class ThingsTests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        # print(response)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
    
    def test_base_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'base.html')