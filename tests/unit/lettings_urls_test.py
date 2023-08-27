from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index, letting

class LettingsURLTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        url = reverse("lettings:letting", args=[1])  # Assuming you have a letting with ID 1
        self.assertEqual(resolve(url).func, letting)
