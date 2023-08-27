from django.test import TestCase, Client
from lettings.models import Address, Letting
from django.urls import reverse

class LettingsIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(number=123, street="Test Street", city="Test City", state="TS", zip_code=12345, country_iso_code="TST")
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_list_page(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_letting_detail_page(self):
        letting_url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(letting_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "Test Street")
