from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BankForm
from .models import BankModel
# Create your views here.


def MainPage(request):
    posts = BankModel.objects.filter(entered_date__lte=timezone.now()).order_by('entered_date')
    return render(request, 'app/index.html', {'posts': posts})


def createUser(request):
    posts = BankModel.objects.filter(entered_date__lte=timezone.now()).order_by('entered_date')
    return render(request, 'app/createAnAccount.html', {'posts': posts})


def withdrawlPage(request):
    posts = BankModel.objects.filter(entered_date__lte=timezone.now()).order_by('entered_date')
    return render(request, 'app/withdrawl.html', {'posts': posts})


def afterSignIn(request):
    posts = BankModel.objects.filter(entered_date__lte=timezone.now()).order_by('entered_date')
    return render(request, 'app/afterSignIn.html', {'posts': posts})
