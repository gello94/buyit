from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from home.views import index
from dashboard.views import dashboard_product

# Create your views here.


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    """
    Product view
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})


def edit_product(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(product_detail)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})


def remove_product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    item.delete()
    return redirect(dashboard_product)


def toggle_status(request, id):
    item = get_object_or_404(Product, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
