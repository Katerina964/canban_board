from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

app_name = 'canban_board'
urlpatterns = [
    path('', views.list, name='list'),
    path('logout_view', views.logout_view, name='logout_view'),
    # path('save_card', views.save_card, name='save_card'),
    path('delete_card/<int:pk>/', views.delete_card, name='delete_card'),
    path('change_card/<int:pk>/', views.change_card, name='change_card'),
    path('create_card', views.create_card, name='create_card'),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
