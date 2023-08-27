from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse

class ProfilesIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_page(self):
        login_success = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(login_success)

        profile_url = reverse("profiles:profile", args=[self.user.username])
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test City")
