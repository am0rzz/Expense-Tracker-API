from rest_framework import routers
from .views import ExpenseViewSet

router = routers.SimpleRouter()
router.register(r'expenses', ExpenseViewSet, basename='expenses')
urlpatterns = router.urls