from django.conf.urls import patterns, url


urlpatterns = patterns('',
	
    url(r'^addrepo/', 'imagesDocker.views.add_repo', name='add_repo'),
    
)