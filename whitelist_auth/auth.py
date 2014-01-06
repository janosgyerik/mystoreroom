from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import logout
from django.dispatch import receiver

from whitelist_auth.models import Whitelisted


def get_whitelisted(user):
    try:
        return Whitelisted.objects.get(email=user.email, is_active=True)
    except Whitelisted.DoesNotExist:
        pass


def update_user_from_whitelisted(user, whitelisted):
    if whitelisted.is_staff != user.is_staff:
        user.is_staff = whitelisted.is_staff
        user.save()
    if whitelisted.is_superuser != user.is_superuser:
        user.is_superuser = not user.is_superuser
        user.save()


@receiver(user_logged_in)
def update_user_from_whitelisted_wrapper(sender, user, request, **kwargs):
    whitelisted = get_whitelisted(user)
    if whitelisted:
        update_user_from_whitelisted(user, whitelisted)
    else:
        # TODO: redirect to authorization failed page
        logout(request)
