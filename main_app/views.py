from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ResaleForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sneaker, Condition, Photo
import uuid
import boto3
import os

#VIEW FUNCTIONS
# Create your views here.
def home(request):
    return render(request, 'home.html')
   
def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    sneakers = Sneaker.objects.all() 
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    conditions_sneaker_doesnt_have = Condition.objects.exclude(id__in = sneaker.conditions.all().values_list('id'))
    resale_form = ResaleForm()
    return render(request, 'sneakers/detail.html', { 
        'sneaker': sneaker, 'resale_form': resale_form,
        'conditions': conditions_sneaker_doesnt_have
        })

def add_resale(request, sneaker_id):
    form = ResaleForm(request.POST)
    if form.is_valid():
        new_resale = form.save(commit=False)
        new_resale.sneaker_id = sneaker_id
        new_resale.save()
    return redirect('detail', sneaker_id=sneaker_id)

def assoc_condition(request, sneaker_id, condition_id):
  Sneaker.objects.get(id=sneaker_id).conditions.add(condition_id)
  return redirect('detail', sneaker_id=sneaker_id)

def unassoc_condition(request, sneaker_id, condition_id):
  Sneaker.objects.get(id=sneaker_id).conditions.remove(condition_id)
  return redirect('detail', sneaker_id=sneaker_id)

def add_photo(request, sneaker_id):
  photo_file = request.FILES.get('photo-file', None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try: 
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, sneaker_id=sneaker_id)
    except:
      print('An error occurred uploading file to S3')
    return redirect('detail', sneaker_id=sneaker_id)


# Class-Based Views
class SneakerCreate(CreateView):
    model = Sneaker
    fields = ['name', 'year', 'size', 'price']
    success_url = '/sneakers'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['name', 'year', 'size', 'price']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

class ConditionList(ListView):
  model = Condition

class ConditionDetail(DetailView):
  model = Condition

class ConditionCreate(CreateView):
  model = Condition
  fields = '__all__'

class ConditionUpdate(UpdateView):
  model = Condition
  fields = '__all__'

class ConditionDelete(DeleteView):
  model = Condition
  success_url = '/conditions/'





