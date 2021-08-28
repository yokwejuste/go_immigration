from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from records.forms import UserRegistrationForm, UserLoginForm, GoCustomerRegistrationForm
from .models import GoCustomerRegistration, GoUser


# Registration View of the user
def register(request):
    context = {}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:
        form = UserRegistrationForm
        context['register_form'] = form

    return render(request, 'register.html', context)


# Login view for user
def login_go_user(request):
    context = {}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('choices')
    else:
        form = UserLoginForm
        context['login_form'] = form
    return render(request, 'login.html', context)


# Logout for user
def logout_go_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login/")
def choices(request):
    context = {}
    if request.method == "POST":
        return render(request, "choices.html", context)
    else:
        redirect("login")
    return render(request, 'choices.html', context)


class SearchResult(ListView):
    model = GoCustomerRegistration
    template_name = 'records_search.html'

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = GoCustomerRegistration.objects.filter(
            Q(
                name__icontains=query
            ) | Q(
                registered_by__icontains=query
            ) | Q(
                destination__icontains=query
            ) | Q(
                type__icontains=query
            )
        )

        return object_list


@login_required(login_url="/login/")
def records(request):
    context = {}
    return render(request, 'records.html', context)


@login_required(login_url="/login/")
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)


@login_required(login_url="/login/")
def profile(request):
    context = {}
    return render(request, 'profile.html', context)


@login_required(login_url="/login/")
def h404(request):
    return render(request, "404.html", {})


def handler404(request, *args, **agv):
    return redirect('h404')


@login_required(login_url="/login/")
def preview(request):
    documents = GoCustomerRegistration.objects.all()
    context = {
        'documents': documents
    }
    return render(request, 'doc_preview.html', context)


@login_required(login_url="/login/")
def send_files_1(request):
    username = GoUser.username
    context = {
        'username': username,
    }
    if request.POST:
        form = GoCustomerRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('preview')
        else:
            HttpResponse(f'Invalid data {request.user.username}')
        context['document_form'] = form

    else:
        form = GoCustomerRegistrationForm
        context['document_form'] = form

    return render(request, 'files_1.html', context)


@login_required(login_url="/login/")
def send_files_2(request):
    username = GoUser.username
    context = {
        'username': username,
    }
    if request.POST:
        form = GoCustomerRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('preview')
        else:
            HttpResponse(f'Invalid data {request.user.username}')
        context['document_form'] = form

    else:
        form = GoCustomerRegistrationForm
        context['document_form'] = form

    return render(request, 'files_2.html', context)


@login_required(login_url="/login/")
def send_files_3(request):
    username = GoUser.username
    context = {
        'username': username,
    }
    if request.POST:
        form = GoCustomerRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('preview')
        else:
            HttpResponse(f'Invalid data {request.user.username}')
        context['document_form'] = form

    else:
        form = GoCustomerRegistrationForm
        context['document_form'] = form

    return render(request, 'files_3.html', context)
