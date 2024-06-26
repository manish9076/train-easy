from django.shortcuts import render, redirect
from .forms import DatasetUploadForm, PreprocessingForm, AlgorithmSelectionForm
from .models import Dataset, Preprocessing
from django.http import JsonResponse
from .preprocessing import preprocess_data
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            messages.success(request, 'Dataset uploaded successfully')
            return redirect('upload_success')
    else:
        form = DatasetUploadForm()
    return render(request, 'upload_dataset.html', {'form': form})

@login_required
def view_dataset(request):
    datasets = Dataset.objects.all()
    return render(request, 'view_dataset.html', {'datasets': datasets})

# TO BE TAKEN CARE later
def upload_dataset_api(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            messages.success(request, 'Dataset uploaded successfully')
            return redirect('upload_success')
    else:
        form = DatasetUploadForm()
    return render(request, 'components/upload_dataset.html', {'form': form})

def view_dataset_api(request):
    datasets = Dataset.objects.all()
    return render(request, 'components/view_dataset.html', {'datasets': datasets})


# Preprocessing view
def preprocess_selection(request):
    form = PreprocessingForm()
    if request.method == 'POST':
        form = PreprocessingForm(request.POST)
        if form.is_valid():
            preprocessing = form.save(commit=False)
            preprocessing.user = request.user
            preprocessing.save()
            messages.success(request, 'Preprocessing steps selected successfully')
            return redirect('algorithm_selection')
    ctx = {'form': form}
    return render(request, 'preprocess_selection.html', ctx)
            
            
def algorithm_selection(request):
    form = AlgorithmSelectionForm()
    if request.method == 'POST':
        form = AlgorithmSelectionForm(request.POST)
        if form.is_valid():
            algorithm = form.save(commit=False)
            algorithm.user = request.user
            algorithm.save()
            messages.success(request, 'Algorithm selected successfully')
            return redirect('algorithm_selection')
    ctx = {'form': form}
    return render(request, 'algorithm_selection.html', ctx)
    
    
        