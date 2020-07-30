from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('', include(router.urls))
    
]
