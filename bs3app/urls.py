from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'bs3app.views.home', name='home'),
)
