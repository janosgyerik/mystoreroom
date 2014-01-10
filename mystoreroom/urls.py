from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mystoreroom.views.home', name='home'),

    url(r'^$', 'whitelist_auth.views.login', name='home'),
    url(r'^stock/', include('stock.urls')),
    url(r'^login/', include('whitelist_auth.urls')),
    url(r'', include('social_auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
