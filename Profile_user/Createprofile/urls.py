from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import login_view,logout_view,register_view,home_view,extend_profile_view,show_profile,update_profile,delete_profile

urlpatterns=[
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('extend/', extend_profile_view, name='extend'),
    path('show/', show_profile, name='show'),
    path('update/', update_profile, name='update'),
    path('delete/', delete_profile, name='delete'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)