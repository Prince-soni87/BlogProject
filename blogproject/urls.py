
from django.contrib import admin
from django.urls import include, path,include
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('create/',views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
