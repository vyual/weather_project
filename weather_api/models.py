from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        swappable = 'AUTH_USER_MODEL'


User._meta.get_field('groups').remote_field.related_name = 'weather_users'
User._meta.get_field('user_permissions').remote_field.related_name = 'weather_users_permissions'
