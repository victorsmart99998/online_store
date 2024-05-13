from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from paypal.standard.forms import PayPalPaymentsForm
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'store/index.html', context)

def shop(request):
    products = Product.objects.all()
    colors = Color.objects.all()
    sizes = Size.objects.all()
    context = {'products': products, 'colors': colors, 'sizes': sizes}
    return render(request, 'store/shop.html', context)

def filter(request):
    categories = request.GET.getlist("category[]")
    vendors = request.GET.getlist("vendor[]")

    products = Product.objects.filter(products_status="Published").order_by("id").distinct()

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()
    data = render_to_string("store/filter_list.html", {'products': products})
    return JsonResponse({'data': data})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def add_to_cart(request):
    cart_product = {}
    product = request.GET['id']

    print(product)
    print("what")


    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
    }
    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse(
        {"data": request.session['cart_data_obj'], "totalcartitems": len(request.session['cart_data_obj'])})


def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, 'store/cart.html', {"cart_data": request.session['cart_data_obj'],
                                                   "totalcartitems": len(request.session['cart_data_obj']),
                                                   'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, 'your cart is empty')
        return redirect("store:index")


def checkout_view(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '200',
        'item_name': 'Order-Item-No-3',
        'invoice': 'INVOICE_NO-4',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse("store:paypal-ipn")),
        'return_url': 'http://{}{}'.format(host, reverse("store:payment_completed")),
        'cancel_url': 'http://{}{}'.format(host, reverse("store:payment_failed")),
    }
    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, 'store/checkout.html', {"cart_data": request.session['cart_data_obj'],
                                                       "totalcartitems": len(request.session['cart_data_obj']),
                                                       'cart_total_amount': cart_total_amount, 'paypal_payment_button': paypal_payment_button})

def payment_completed(request):
    return render(request, 'store/payment_completed.html')

def payment_failed(request):
    return render(request, 'store/payment_failed.html')