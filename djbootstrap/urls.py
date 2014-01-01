from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djbootstrap.views.home', name='home'),

    url(r'^bs3app/', include('bs3app.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('social_auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
