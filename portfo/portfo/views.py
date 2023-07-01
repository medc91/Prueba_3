from django.shortcuts import render,redirect
from productos.models import Productos

def Renderizar(request):
  return render(request,"crud.html")


def read(request):
     ListadoProductos = Productos.objects.all()
     ctx ={'listado':ListadoProductos}   
     return render(request,"crud.html",ctx)

def create(request,nuevoCodigo,productoNuevo,descripcionNuevo,imagenNuevo,precioNuevo):
  producto = Productos(codigo=nuevoCodigo,nombre=productoNuevo,descripcion=descripcionNuevo,imagen=imagenNuevo,precio=precioNuevo)
  producto.save()
  return redirect(read)

def delete(request,idProducto):
  productoBorrar = Productos.objects.filter(id__icontains=idProducto)
  productoBorrar.delete()
  return redirect(read)

def update(request,idProducto,nuevoCodigo,productoNuevo,descripcionNuevo,imagenNuevo,precioNuevo):
  productoActualizar = Productos.objects.filter(id__icontains=idProducto)
  productoActualizar.update(codigo=nuevoCodigo,nombre=productoNuevo,descripcion=descripcionNuevo,imagen=imagenNuevo,precio=precioNuevo)
  return redirect(read)