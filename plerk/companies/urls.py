from django.urls import path
from .api.routing import router

app_name = 'companies'
urlpatterns = []

router_urls = router.urls
urlpatterns += router.urls