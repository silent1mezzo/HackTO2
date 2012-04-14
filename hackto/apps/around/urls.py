from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^$', 'around.views.index', name='home'),
    url(r'^about/$', 'around.views.index', name='about')
)
