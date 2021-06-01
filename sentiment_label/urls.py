from django.urls import include, path
from .views import (
    SplashView,
    LabelView
)

app_name = 'sentiment_label'

urlpatterns = [
    path('', SplashView, name='splash'),
    path('label/', LabelView, name='label'),
    # path('products/', include('products.urls')),
    # path('', home_view, name='home'),
    # path('about/<int:id>/', about_view, name='product-detail'),
    # path('contact/', contact_view),
    # path('admin/', admin.site.urls),
]
