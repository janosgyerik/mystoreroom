from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'store.views.home', name='home'),
)
