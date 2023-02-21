from django.shortcuts import render, redirect

from item.models import Category, Item

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def underconstruction(request):
    return render(request, 'core/under-construction.html')


def contact(request):
    # return render(request, 'core/contact.html')
    return render(request, 'core/under-construction.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


@login_required
def signout(request):
    logout(request)
    return redirect('core/index.html')
