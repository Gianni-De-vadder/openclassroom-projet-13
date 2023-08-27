from django.shortcuts import render
from .models import Profile

def index(request):
    """
    Display a list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/profiles_index.html', context)

def profile(request, username):
    """
    Display the details of a specific profile.
    Args:
        username (str): The username of the profile's associated user.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
