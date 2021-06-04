from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views
# from django.views.generic import RedirectView

app_name = 'canban_board'
urlpatterns = [
    path('list', views.list, name='list'),
    path('', views.lending, name='lending'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('delete_card/<int:pk>/', views.delete_card, name='delete_card'),
    path('change_card/<int:pk>/', views.change_card, name='change_card'),
    path('register', views.register, name='register'),
    path('create_card', views.create_card, name='create_card'),
    path('contact', views.contact, name='contact'),
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
