from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import CardForm, UserForm
from django.contrib.auth.models import User


def contact(request):
    return render(request, 'canban_board/contact.html')


def lending(request):
    if request.user.is_authenticated:
        return redirect('canban_board:list')
    else:
        todo = Card.objects.filter(state="TD", user=1)
        doing = Card.objects.filter(state="D", user=1)
        done = Card.objects.filter(state="DN", user=1)
    context = {'todo': todo, 'doing': doing, 'done': done}
    return render(request, 'canban_board/lending.html', context)


@login_required(login_url='/accounts/login/')
def list(request):
    user_id = request.user.id
    todo = Card.objects.filter(state="TD", user=user_id)
    doing = Card.objects.filter(state="D", user=user_id)
    done = Card.objects.filter(state="DN", user=user_id)
    context = {'todo': todo, 'doing': doing, 'done': done}
    return render(request, 'canban_board/list.html', context)


def logout_view(request):
    logout(request)
    return redirect('canban_board:list')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"],
                                                password=request.POST["password"])
                login(request, user)
                return redirect('canban_board:list')
            except Exception:
                print(form.errors)
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'canban_board/register.html', context)


def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('canban_board:list')
        else:
            print(form.errors)
    else:
        form = CardForm()
    context = {'form': form}
    return render(request, 'canban_board/create_card.html', context)


def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('canban_board:list')


def change_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('canban_board:list')
        else:
            print(form.errors)
    else:
        form = CardForm(instance=card)
    context = {"form": form}
    return render(request, 'canban_board/create_card.html', context)
