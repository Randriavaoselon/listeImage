from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from affichageImage.views import CustomLoginView

from affichageImage.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('affichageImage.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                         authentication_form=LoginForm), name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)