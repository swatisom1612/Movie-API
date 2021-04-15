from django.contrib import admin
from django.urls import path, include

from user.views import RequestCountView, RequestCountResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', include('movie.urls')),
    path('request-count/', RequestCountView.as_view(), name='user_request_count'),
    path('request-count/reset/', RequestCountResetView.as_view(), name='user_request_count_reset'),
]
