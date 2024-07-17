from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('brands/', views.brands, name="brands"),
    path('store/', views.stores, name="stores"),
    path('orders/', views.orders, name="orders"),
    path('category/', views.categories, name="category"),
    path('products/', views.products, name="products"),
    # Marcas
    path('addBrand/', views.add_new_brand, name="add_brand"),
    path('deleteBrand/<str:pk>', views.delete_brand, name="delete_brand"),
    path('updateBrand/<str:pk>', views.update_brand, name="update_brand"),
    # Tiendas
    path('addStore/', views.add_store, name="add_store"),
    path('deleteStore/<str:pk>', views.delete_store, name="delete_store"),
    path('updateStore/<str:pk>', views.update_store, name="update_store"),
    # Categorias
    path('addCategory/', views.add_category, name="add_category"),
    path('updateCategory/<str:pk>', views.update_category, name="update_category"),
    path('deleteCategory/<str:pk>', views.delete_category, name="delete_category"),
    # Productos
    path('addProduct/', views.add_product, name="new_product"),
    # Pedidos
    path('addOrder/', views.add_order, name="add_order"),
    path('deleteOrder/<str:pk>', views.delete_order, name="delete_order"),
    path('orderReport/<str:pk>', views.generate_order_report, name="generate_report"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)