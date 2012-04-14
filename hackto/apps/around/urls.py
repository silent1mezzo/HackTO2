from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^$', 'around.views.index', name='home'),
    url(r'^search/$', 'around.views.search', name='search'),
    url(r'^about/$', 'around.views.index', name='about'),
)
