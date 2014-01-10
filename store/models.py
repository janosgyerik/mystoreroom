from datetime import timedelta
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers

from django.utils import timezone
from django.db import models


def tomorrow():
    return timezone.now() + timedelta(days=1)


class Item(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=1)
    buy_dt = models.DateTimeField(default=timezone.now)
    expires_dt = models.DateTimeField(default=tomorrow, null=True, blank=True)
    created_dt = models.DateTimeField(default=timezone.now, blank=True)
    updated_dt = models.DateTimeField(default=timezone.now, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('expires_dt',)


class Tag(models.Model):
    name = models.SlugField()
    label = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.label, self.name)

    def save(self, *args, **kwargs):
        if not self.label:
            self.label = self.name.title()
        super(Tag, self).save(*args, **kwargs)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))


class ItemTag(models.Model):
    item = models.ForeignKey(Item)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return '%s - %s' % (self.item, self.tag)
