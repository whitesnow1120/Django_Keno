from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def apuestas(request):
        
    return render(request, 'apuestas.html')

def apuestas_ajax(request):
    
    if request.is_ajax():
        
        now = datetime.now()
        today_date = now.strftime("%Y-%m-%d")
        toady_time = now.strftime("%H:%M:%S")
        
        # request for cartonkeno
        apuesta_keno = request.POST.get('keno')
        valor_apuesta_k = int(request.POST.get('keno_valor'))
        
        cartonkeno = CartonKeno()
        cartonkeno.apuesta_keno = apuesta_keno
        cartonkeno.valor_apuesta_k = valor_apuesta_k
        cartonkeno.fecha_keno = today_date
        cartonkeno.hora_keno = toady_time
        
        cartonkeno.save()
        
        # request for cartoncartas
        valor_apuesta_c = request.POST.get('cartas_valor')
        alta_baja = request.POST.get('cartas_alta_baja')
        color = request.POST.get('cartas_color')
        
        if alta_baja != '' and color != '':
        
            cartoncartas = CartonCartas()
            cartoncartas.alta_baja = alta_baja
            cartoncartas.color = color
            cartoncartas.valor_apuesta_c = valor_apuesta_c
            cartoncartas.fecha_cartas = today_date
            cartoncartas.hora_cartas = toady_time
            
            cartoncartas.save()
        
        message = 'saved'
    else:
        message = 'failed'
        
    return HttpResponse(message)