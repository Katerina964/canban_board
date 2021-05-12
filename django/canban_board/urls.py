from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views


app_name = 'canban_board'
urlpatterns = [

    path('', views.list, name='list'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
