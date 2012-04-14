from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^$', 'around.views.index', name='home'),
    url(r'^search/$', 'around.views.search', name='search'),
    url(r'^category/(?P<category>[\w|\W]+)/$', 'around.views.category', name='category_list'),
    url(r'^company/(?P<id>[\w|\W]+)/$', 'around.views.company', name='company_info'),
    url(r'^ajax/sms/$', 'around.views.send_addresses', name='sms'),
    url(r'^about/$', 'around.views.about', name='about'),
)
