from django.contrib.auth.models import User
from django.utils import timezone
from myapp.models import UserUpdate

def update_user_from_google_or_microsoft(request, provider):
    # Get the user's basic profile information from the authentication provider
    if provider == 'google':
        profile = request.user.social_auth.get(provider=provider).extra_data['id_info']['basic_profile']
    elif provider == 'microsoft':
        profile = request.user.social_auth.get(provider=provider).extra_data['raw_user']
    
    # Check if the user already exists in the database
    try:
        user = User.objects.get(username=profile['email'])
    except User.DoesNotExist:
        # If the user doesn't exist, create a new user object
        user = User.objects.create_user(username=profile['email'], email=profile['email'])
    
    # Update the user's information based on the profile data from the authentication provider
    user.first_name = profile.get('given_name', '')
    user.last_name = profile.get('family_name', '')
    user.save()
    
    # Create a new UserUpdate object to record the update
    update = UserUpdate(user=user, timestamp=timezone.now())
    update.message = f'{user.username} updated their profile from {provider}'
    update.save()
    
    return update
