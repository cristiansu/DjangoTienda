from django.shortcuts import render
from .models import Category, Products,Contact
from .forms import ProductoForm,CategoryForm,ContactoForm
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q,Count
from django.contrib.auth.models import User

# Create your views here.

#home dashboard


def home(request):

    productos=Products.objects.count()

    categorias=Category.objects.count()
    
    users=User.objects.count()

    #lista de categorias
    prueba=Category.objects.all()
    lir=[]
    ids=[]
    for it in prueba.iterator():
        lir.append(it.nombre)
        ids.append(it.id)
    print(lir)
    #productos por categoria
    cant=[]    
    for c in ids:
        datos=Products.objects.filter(categoria=c).count()
        cant.append(datos)

    print(cant)
    print('-------------')
    print(ids)
    

    data={'productos':productos,'categorias':categorias,'etiquetas':lir,'cant_pxcat':cant,'usuarios':users}
    return render(request, 'admin_templates/home.html', data)


#Categorías

def agregar_categoria(request):
    data={

        'form': CategoryForm()
    }
    if request.method == 'POST':
        formulario=CategoryForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría registrado')
        else:
            data['form']=formulario
    return render(request, 'admin_templates/category_create.html', data)

# def listar_categorias(request):
#     categorias=Category.objects.all()
#     data={
#         'categorias':categorias
#     }
#     return render(request, 'admin_templates/categories_list.html', data)


class CategoriesListView(ListView):
    model=Category
    template_name='admin_templates/categories_list.html'
    paginate_by=10

    def get_queryset(self):
        filter_val=self.request.GET.get('filter', '')
        order_by=self.request.GET.get('orderby', 'id')
        if filter_val != '':
            cat=Category.objects.filter(Q(nombre__contains=filter_val)).order_by(order_by)
        else:
            cat=Category.objects.all().order_by(order_by)
        return cat

    def get_context_data(self, **kwargs):
        context=super(CategoriesListView, self).get_context_data(**kwargs)
        context['filter']=self.request.GET.get('filter', '')
        context['order_by']=self.request.GET.get('order_by', '')
        context['all_table_fields']=Category._meta.get_fields()
        return context


#Productos

def agregar_producto(request):
    data={

        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto registrado')
        else:
            data['form']=formulario
    return render(request, 'admin_templates/product_create.html', data)

class ProductsListView(ListView): #se puede iterar en el template como products_list  es decir nombre de la vista sin ListView más _list
    model=Products
    template_name='admin_templates/product_list.html'

