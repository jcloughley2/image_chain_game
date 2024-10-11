from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Image, Description
from .forms import DescriptionForm
from .utils import generate_image
from .tasks import generate_daily_image

def home(request):
    today = timezone.now().date()
    all_images = Image.objects.all().order_by('-created_at', 'id')
    images_by_date = {}

    for image in all_images:
        date = image.created_at
        if date not in images_by_date:
            images_by_date[date] = []
        images_by_date[date].append(image)

    latest_image = Image.objects.filter(created_at=today, has_been_described=False).first()

    if not latest_image:
        generate_daily_image()
        latest_image = Image.objects.filter(created_at=today, has_been_described=False).first()

    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            Description.objects.create(image=latest_image, text=description)
            latest_image.has_been_described = True
            latest_image.save()
            generate_daily_image()
            return redirect('thank_you')
    else:
        form = DescriptionForm()

    context = {
        'images_by_date': images_by_date,
        'latest_image': latest_image,
        'form': form,
    }
    return render(request, 'game/home.html', context)

def thank_you(request):
    return render(request, 'game/thank_you.html')
