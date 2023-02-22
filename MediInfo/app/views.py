from django.shortcuts import render


#VISTA DEL HOME
def home(request):
    return render(request, 'app/home.html')

#VISTA DEL CONTACTO
def contacto(request):
    return render(request, 'app/contacto.html')    

#VISTA DE MEDICAMENTOS
def medicamentos(request):
    return render(request, 'app/medicamentos.html')    