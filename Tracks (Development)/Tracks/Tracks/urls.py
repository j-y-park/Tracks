from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tracks.views.home', name='home'),
    # url(r'^Tracks/', include('Tracks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
##    url(r'^$', include('TracksApp.urls', namespace='TracksApp')),
##    url(r'^Tracks/', include('TracksApp.urls', namespace='TracksApp')),
    url(r'^tracks/', include('TracksApp.urls', namespace='TracksApp')),
)
