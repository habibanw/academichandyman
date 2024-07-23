from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Handyman, regularUser, Handyman


# Create your views here.
def home(request):
    return render(request, 'handyman/home.html')



def services(request):
    providers = Handyman.objects.all()
    return render(request, 'handyman/providers/services.html', {'providers': providers})


def about(request):
    return render(request, 'handyman/providers/about.html')


# def provider_detail(request, provider_id):
#     providers = Handyman.objects.all()
#     for provider in providers:
#         if provider.id == provider_id:
#             return render(request, 'handyman/providers/provider_detail.html', {'provider': providers})
#     return render(request, 'handyman/providers/services.html', {'providers': providers})

def provider_detail(request, provider_id):
    # Get the provider by ID and handle the case where it doesn't exist
    provider = get_object_or_404(Handyman, id=provider_id)
    return render(request, 'handyman/providers/provider_detail.html', {'provider': provider})


def add_provider(request):
    if not request.session.get('username', False):
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('add-name')
        email = request.POST.get('add-email')
        services = request.POST.get('add-services')
        description = request.POST.get('add-description')
        provider = Handyman(name=name, email=email, services=services, description=description)
        provider.save()
        messages.add_message(request, messages.SUCCESS, 'Provider added successfully')
        return redirect('providers:provider_detail', provider.id)
    return render(request, 'handyman/providers/add_provider.html')

@login_required
def rate_provider(request, provider_id):
    if request.method == 'POST':
        try:
            rating = int(request.POST.get('rating'))
            provider = get_object_or_404(Handyman, id=provider_id)
            total_rating = provider.average_rating * provider.rating_count + rating
            provider.rating_count += 1
            provider.average_rating = total_rating / provider.rating_count
            provider.save()
            return JsonResponse({'success': True, 'rating': provider.average_rating})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@login_required
def edit_provider(request, provider_id):
    provider = get_object_or_404(Handyman, id=provider_id)
    if request.method == 'POST':
        provider.name = request.POST.get('edit-name')
        provider.email = request.POST.get('edit-email')
        provider.services = request.POST.get('edit-services')
        provider.description = request.POST.get('edit-description')
        provider.save()
        messages.add_message(request, messages.SUCCESS, 'Provider updated successfully')
        return redirect('providers:edit_provider', provider.id)
    return render(request, 'handyman/providers/edit_provider.html', {'provider': provider})
