from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import estudiante, qrScan
from .forms import estudianteform, qrform
# Create your views here.


def principal(request):
    return render(request, 'paginas/principal.html')

def lineas(request):
    return render(request, 'paginas/lineas.html')

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    print (estudiantes)
    escaneados = qrScan.objects.all()
    print (escaneados)
    return render(request, 'aprendices/index.html', {'estudiantes': estudiantes})#para leer desde el modelo al index. Desglosado en index.html

def nuevo(request):
    formulario = estudianteform(request.POST or None, request.FILES or None)# La clave para enviar o recibir informacion esta aqui
    
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    
    return render(request, 'aprendices/crear.html', {'formulario': formulario})# lee desde forms.py 

def guardarQr(request):
    form = qrform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contar')
    return render(request, 'paginas/crearQr.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contarQr(request):
    # Agrupar por 'qr_value' y contar repeticiones
    qr_data = qrScan.objects.values('qr_value').annotate(count=Count('qr_value')).order_by('-count')
    estudiantes = estudiante.objects.all()

    contar = []
    for item in qr_data:
        est = estudiantes.filter(documento=item['qr_value']).first()
        if est:
            contar.append({
                'documento': item['qr_value'],
                'nombre': est.nombres,
                'apellidos': est.apellidos,
                'linea': est.linea,
                'count': item['count']
            })

    return render(request, 'paginas/contarQr.html', {'contar': contar})