from rest_framework.routers import SimpleRouter
from Users import views


router = SimpleRouter()

router.register(r'sdesgin_users', views.Sdesgin_UsersViewSet, 'Sdesgin_Users')

urlpatterns = router.urls
