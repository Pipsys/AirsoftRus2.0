from .models import Cart

def cart(request):
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).order_by('-created').first()
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.filter(id=cart_id).first()
    
    return {'cart': cart}