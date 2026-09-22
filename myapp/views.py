from django.shortcuts import render
from .models import temperature_db
from django.forms.models import model_to_dict
from django.http import HttpResponse

# Create your views here.
def view_history_temperature(request):
    history = temperature_db.objects.all().order_by('-myid')
    #return HttpResponse("test")
    return render(request, "views.view_history_temperature.html", {"history": history})

from django.http import JsonResponse
import django.views.decorators.csrf as csrf
@csrf.csrf_exempt
def add_temperature_API(request):
    try:
        if request.method == 'GET':
            sensor_id = request.GET["sensor_id"]
            temperature = request.GET["temperature"]
            humidity = request.GET["humidity"]
            timestamp = request.GET["timestamp"]
            print("GET")
            print(f"sensor_id: {sensor_id}, temperature: {temperature}, humidity: {humidity}, timestamp: {timestamp}")
        elif request.method == 'POST':
            sensor_id = request.POST["sensor_id"]
            temperature = request.POST["temperature"]
            humidity = request.POST["humidity"]
            timestamp = request.POST["timestamp"]
            print("POST")
            print(f"sensor_id: {sensor_id}, temperature: {temperature}, humidity: {humidity}, timestamp: {timestamp}")
    except Exception as e:
        return HttpResponse(f"Failed to add temperature: {e}")
    save_data = temperature_db(sensor_id=sensor_id, temperature=temperature, humidity=humidity, timestamp=timestamp)
    save_data.save()
    return JsonResponse({
            "status": "success",
            "sensor_id": sensor_id,
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": timestamp
        })
def add_temperature(request):
    if request.method == 'POST':
        sensor_id = request.POST["sensor_id"]
        temperature = request.POST["temperature"]
        humidity = request.POST["humidity"]
        save_data = temperature_db(sensor_id=sensor_id, temperature=temperature, humidity=humidity)
        save_data.save()
        return HttpResponse("Temperature added successfully")
    return render(request, "add_temperature.html")
def show_temperature(request):
    temperatures = temperature_db.objects.all().order_by('-timestamp')
    return render(request, "show_temperature.html", {"data": model_to_dict(temperatures[0])}) if temperatures else HttpResponse("No temperatures found")
def show_temperature_API(request):
    temperatures = temperature_db.objects.all().order_by('-timestamp')[:1]
    if temperatures:
        #顯示包含時間的即時資料
        return JsonResponse({
            "status": "success",
            "data": list(temperatures.values())
        })
    else:
        return JsonResponse({
            "status": "error",
            "message": "No temperatures found"
        })
def show_temperature2(request):
    temperatures = temperature_db.objects.all().order_by('-timestamp')[:2]
    return render(request, "show_temperature2.html", {"data": list(temperatures.values())}) if temperatures else HttpResponse("No temperatures found")  