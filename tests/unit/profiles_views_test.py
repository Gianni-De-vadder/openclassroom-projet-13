from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.views import index, profile

class ProfilesViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        request = self.factory.get(reverse("profiles:index"))
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_profile_view(self):
        request = self.factory.get(reverse("profiles:profile", args=[self.user.username]))
        response = profile(request, self.user.username)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
