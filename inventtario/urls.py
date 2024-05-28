from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import add_user, login, user_signin, unauthorized

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista de inicio
    path('add_user/', add_user, name='add_user'),
    path('login/', login, name='login'),  # Añadir la URL de login
    path('signin/', user_signin, name='signin'),
    path('unauthorized/', unauthorized, name='unauthorized'),
]

# Agregar las URLs para servir archivos media solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



