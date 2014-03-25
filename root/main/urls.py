from django.conf.urls import patterns, include, url

from django.contrib import admin

# This two line below is a part of line 21 -23
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^language/(?P<language>[a-z\-])/$', 'blog.views.language', name='language'),
    url(r'^post/(?P<id>\d+)/$', 'blog.views.post', name='post'),
    url(r'^like/(?P<id>\d+)/$', 'blog.views.like_post', name='like_post'),

    url(r'^category/$', 'blog.views.category', name='category'),
    url(r'^tag/(?P<tag>\w+)/$', 'blog.views.tagpage', name='tagpage'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^gallery/$', 'blog.views.gallery', name='gallery'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'blog.views.login', name='login'),
    url(r'^accounts/auth/$', 'blog.views.auth_view', name='auth_view'),
    url(r'^accounts/logout/$', 'blog.views.logout', name='logout'),
    url(r'^accounts/auth/loggedin/$', 'blog.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'blog.views.invalid_login', name='invalid_login'),
    url(r'^accounts/register/$', 'blog.views.register_user', name='register_user'),
    url(r'^accounts/register_success/$', 'blog.views.register_success', name='register_success'),

    url(r'^search/$', 'blog.views.search_titles', name='search_titles'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
