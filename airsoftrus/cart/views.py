from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import CartAddProductForm, OrderCreateForm
from django.contrib.auth.decorators import login_required

def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = get_object_or_404(Cart, id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    return cart

@require_POST
def cart_add(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': cd['quantity']}
        )
        if not created:
            if cd['override']:
                cart_item.quantity = cd['quantity']
            else:
                cart_item.quantity += cd['quantity']
            cart_item.save()
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = get_cart(request)
    for item in cart.items.all():
        item.update_quantity_form = CartAddProductForm(initial={
            'quantity': item.quantity,
            'override': True
        })
    return render(request, 'cart/detail.html', {'cart': cart})

@login_required
def order_create(request):
    cart = get_cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            cart.delete()
            request.session.pop('cart_id', None)
            return render(request, 'cart/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'cart/create.html', {'cart': cart, 'form': form})