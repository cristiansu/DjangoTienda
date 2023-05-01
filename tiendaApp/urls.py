
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import home,agregar_producto,agregar_categoria,CategoriesListView,ProductsListView



urlpatterns = [
    path('', home, name='home'),
    path('category_create/', agregar_categoria, name='category_create'),
    #path('category_list/', listar_categorias, name='category_list'),
    path('category_list/', CategoriesListView.as_view(), name='category_list'),
    path('product_list/', ProductsListView.as_view(), name='product_list'),
    path('product_create/', agregar_producto, name='product_create'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)