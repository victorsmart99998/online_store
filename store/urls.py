from django.urls import path, include

from . import views

app_name = 'store'

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('filter-products/', views.filter, name="filter"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('cart_view/', views.cart_view, name="cart_view"),
    path('checkout_view/', views.checkout_view, name="checkout_view"),
    path('paypal', include('paypal.standard.ipn.urls')),
    path('payment_completed/', views.payment_completed, name="payment_completed"),
    path('payment_failed/', views.payment_failed, name="payment_failed"),

]
