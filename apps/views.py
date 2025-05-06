from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Product, CartItem


# ---------------------- USER VIEWS ----------------------

def product_list(request):
    products = Product.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    sort_option = request.GET.get('sort')
    if sort_option in ['price', '-price', 'sales', '-created_at', 'category']:
        products = products.order_by(sort_option)

    return render(request, 'store/product_list.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart_item = CartItem.objects.filter(product=product).first()

    if cart_item:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        CartItem.objects.create(product=product, quantity=quantity)

    return redirect('view_cart')


def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('supper_product_list')
    else:
        form = LoginForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Product saved!")  # ✅ mahsulot saqlandi
            return redirect('supper_product_list')
        else:
            print("Form xatolari:", form.errors)  # ❗ xatolarni ko‘rish
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # If the form is submitted via POST
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # instance is used to update the product
        if form.is_valid():
            form.save()  # Save the updated product to the database
            return redirect('supper_product_list')  # Redirect to the product list after updating
    else:
        form = ProductForm(instance=product)  # If GET, display the existing product data in the form

    return render(request, 'store/edit_product.html', {'form': form, 'product': product})


# View for deleting a product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()  # Delete the product from the database
    return redirect('supper_product_list')  # Redirect to the product list after deletion


def supper_product_list(request):
    # return render(request, 'apps/supper_product_list.html')
    products = Product.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    sort_option = request.GET.get('sort')
    if sort_option in ['price', '-price', 'sales', '-created_at', 'category']:
        products = products.order_by(sort_option)

    return render(request, 'store/supper_product_list.html', {'products': products})
