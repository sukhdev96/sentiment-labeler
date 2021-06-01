from django.urls import include, path
from .views import (
    CourseView,
    CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
    # my_fbv
)

app_name = 'articles'

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', my_fbv, name='courses-list'),

    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete')
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
    # path('products/', include('products.urls')),
    # path('', home_view, name='home'),
    # path('about/<int:id>/', about_view, name='product-detail'),
    # path('contact/', contact_view),
    # path('admin/', admin.site.urls),
]
