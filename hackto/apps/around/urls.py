from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^$', 'around.views.index', name='home'),
)
