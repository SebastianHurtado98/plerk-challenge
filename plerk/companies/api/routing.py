from rest_framework.routers import DefaultRouter

from .viewsets import (
    CompanyViewSet,
)

router = DefaultRouter()
router.register("", CompanyViewSet)