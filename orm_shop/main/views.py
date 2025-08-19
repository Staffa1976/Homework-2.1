from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Car, Sale

def index(request):
    return HttpResponse('Привет! Это сайт про автомагазин.')

def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'cars':cars, })  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    car = get_object_or_404(Car, pk = car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'car':car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = get_object_or_404(Car, pk=car_id)
        sale = Sale.objects.filter(car=car)

        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales':sale})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
