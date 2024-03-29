from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FruitForm
from .models import Fruit
from django.http import HttpResponse


@login_required(login_url="login_url")
def create_order(request):
    template_name = "fruitapp/create.html"
    form = FruitForm()
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = "fruitapp/show.html"
    orders = Fruit.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def update_order(request, pk):
    obj = Fruit.objects.get(id=pk)
    form = FruitForm(instance=obj)
    if request.method == "POST":
        form = FruitForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = "fruitapp/create.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def cancel_order(request, pk):
    obj = Fruit.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'fruitapp/confirm.html')
