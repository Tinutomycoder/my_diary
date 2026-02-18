from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import RegistrationForm, LoginForm, DiaryEntryForm
from .models import DiaryEntry


def register_view(request):
    if request.user.is_authenticated:
        return redirect('diary_home')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created successfully.')
            return redirect('diary_home')
    else:
        form = RegistrationForm()
    
    return render(request, 'diary/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('diary_home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('diary_home')
    else:
        form = LoginForm()
    
    return render(request, 'diary/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required
def diary_home(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    search_query = request.GET.get('search', '')
    
    if search_query:
        entries = entries.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(mood__icontains=search_query)
        )
    
    return render(request, 'diary/home.html', {
        'entries': entries,
        'search_query': search_query
    })


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Diary entry created successfully!')
            return redirect('diary_home')
    else:
        form = DiaryEntryForm()
    
    return render(request, 'diary/entry_form.html', {
        'form': form,
        'action': 'Create'
    })


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diary entry updated successfully!')
            return redirect('diary_home')
    else:
        form = DiaryEntryForm(instance=entry)
    
    return render(request, 'diary/entry_form.html', {
        'form': form,
        'action': 'Edit',
        'entry': entry
    })


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Diary entry deleted successfully!')
        return redirect('diary_home')
    
    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})


@login_required
def view_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})
