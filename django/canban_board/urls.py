from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

app_name = 'canban_board'
urlpatterns = [
    path('', views.list, name='list'),
    path('logout_view', views.logout_view, name='logout_view')
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
