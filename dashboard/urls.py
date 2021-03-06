from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, dashboard_orders, dashboard_order_details, add_a_category, users_info
from products.views import toggle_status, add_a_product, confirm_delete_product, edit_a_product
from orders.views import change_order_status
from api import urls as urls_api
from voucher.views import add_new_voucher, edit_a_voucher, voucher_view

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
     path('dashboardorders', views.dashboard_orders, name='dashboard_orders'),
     path('dashboardorder/<int:id>', views.dashboard_order_details,
         name='dashboard_order_details'),
     path('dashboardproducts', views.dashboard_product, name='dashboard_product'),
     path('dashboardproducts/confirmdeleteproduct/<int:pk>',
         confirm_delete_product, name='confirm_delete_product'),
     path('dashboardaddproduct', add_a_product, name='add_a_product'),
     path('dashboardeditproduct/<int:id>',
         edit_a_product, name='edit_a_product'),
     path('dashboardaddcategory', add_a_category, name='add_a_category'),
     path('dashboardusers', users_info, name='users'),
     path('toggle_status/<int:id>', toggle_status),
     path('changeorderstatus/<int:id>',
         change_order_status, name='change_order_status'),
     path('dashboardvouchers', voucher_view, name='voucher_view'),
     path('dashboardaddvoucher', add_new_voucher, name='add_new_voucher'),
     path('dashboardeditvoucher/<int:id>', edit_a_voucher, name='edit_a_voucher'),    
     path('api/', include(urls_api)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
