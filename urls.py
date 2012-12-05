from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),


    (r'^accounts/login/$', 'django.contrib.auth.views.login',
         { 'template_name' :'canal/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
         { 'template_name' :'canal/logout.html'}),

    # Les rebons commerciaux
    (r'^accounts/register/$', 'rbons.views.register',
         { 'template_name' :'register.html'}),

    (r'^/?$' ,'rbons.views.dashboad'), 
    (r'^dashboard$', 'rbons.views.dashboad'),               
    
    (r'^rbons_check/$', 'rbons.views.rbon_check',
         { 'template_name' :'rbon_check.html'}),

   
)
