from django.contrib import admin 	
from django.conf.urls import url,include
from django.urls import include, path


urlpatterns = [
    url(r'^', include('myapp.urls')),
    url(r'^admin/', admin.site.urls),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]	
