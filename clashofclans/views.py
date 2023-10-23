from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def rey(request):
    data={
        "titulo":"Rey Barbaro",
        'habilidad':"Habilidad Furia",
        'informacion':"Tiene la capacidad de Enfurecerse aumentando el daño y la velocidad",
        'imagen':'/static/imagenes/rey-barbaro.png',
    }
    return render(request,'informacionHeroes.html',data)

def reina(request):
    data={
        "titulo":"Reina Arquera",
        'habilidad':"Habilidad Invisibilidad",
        'informacion':"Tiene la capacidad de volverse invisible durante uno periodo de 10 segundos y su velocidad de disparo aumenta ",
        'imagen':'/static/imagenes/reina-arquera.png',
    }
    return render(request,'informacionHeroes.html',data)

def centinela(request):
    data={
        "titulo":"Centinela",
        'habilidad':"Habilidad Inmune",
        'informacion':"Tiene la capacidad de volver inmune ante el daño delas defensas a todo aquel que se encuentre en su radio ",
        'imagen':'/static/imagenes/centinela.png',
    }
    return render(request,'informacionHeroes.html',data)
