from django.shortcuts import render, redirect
from app.models import Alumno
from app.forms import AlumnoForm

def listar(request):
    ordering = request.GET.get('ordering', 'codigo')
    allowed_ordering = ['codigo', 'nombres', 'apellidos', 'fecha_nacimiento', 'edad', 'email', 'telefono', 'estado_estudio']
    if ordering not in allowed_ordering:
        ordering = 'codigo'
    alumnos = Alumno.objects.all().order_by(ordering)
    contexto = {'alumnos': alumnos, 'ordering': ordering}
    return render(request, 'listar.html', contexto)

def agregar(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.edad = alumno.calcular_edad
            alumno.save()
            return redirect('listar')
    else:
        form = AlumnoForm()
    contexto = {'form': form}
    return render(request, 'agregar.html', contexto)

def editar(request, codigo_alumno):
    alumno = Alumno.objects.get(codigo=codigo_alumno)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.edad = alumno.calcular_edad
            alumno.save()
            return redirect('listar')
    else:
        form = AlumnoForm(instance=alumno)
    contexto = {'form': form}
    return render(request, 'editar.html', contexto)

def eliminar(request, codigo_alumno):
    alumno = Alumno.objects.get(codigo=codigo_alumno)
    alumno.delete()
    return redirect('listar')
