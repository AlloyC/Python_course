from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user, name='users'),
    path('login/', views.signup, name='login'),
    path('api/user/cart/', views.cart, name='cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)