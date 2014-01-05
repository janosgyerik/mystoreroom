from django.db import models


class Whitelisted(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def summary(self):
        return '%s active=%s staff=%s super=%s' % (
                self.email, self.is_active, self.is_staff, self.is_superuser)

    def __unicode__(self):
        return self.email
