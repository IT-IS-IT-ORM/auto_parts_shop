from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('api/', include('user.urls')),
    # Product
    path('api/', include('product.urls')),
    # Order
    path('api/', include('order.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,
            {"document_root": settings.MEDIA_ROOT}),
]