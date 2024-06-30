from django.contrib import admin
from django.urls import path, include
#from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# este + se encarga de indicar de vamos a importar archivos estaticos