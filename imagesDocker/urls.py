from django.conf.urls import patterns, url


urlpatterns = patterns('',
	
    url(r'^$', 'imagesDocker.views.home', name="images"),

    
)