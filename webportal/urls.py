from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webportal.views.home', name='home'),
    url(r'^webapp/', include('webapp.urls')),
    
    url(r'^$','webapp.views.index'),
    url(r'^login/$','webapp.views.userlogin'),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^logout/$','webapp.views.user_logout'),
    url(r'^user/password/change/$','django.contrib.auth.views.password_change'),
    url(r'^user/password/change/done/$','django.contrib.auth.views.password_change_done'),
    url(r'^contributor/profile/$','webapp.views.contributor_profile'), #this takes us to the contributor profile
    url(r'^reviwer/profile/$','webapp.views.reviewer_profile'),
    url(r'^contributor/signup/$','webapp.views.contributor_signup'),
    url(r'^reviewer/signup/$','webapp.views.reviewer_signup'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$','django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}))