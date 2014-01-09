from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventoryman.views.home', name='home'),

    url(r'^$', 'whitelist_auth.views.login', name='home'),
    url(r'^bs3app/', include('bs3app.urls')),
    url(r'^login/', include('whitelist_auth.urls')),
    url(r'', include('social_auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
