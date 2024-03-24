# app_name/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Name, Block, Field
from .countries import COUNTRIES

def page1(request):
    return render(request, 'page1.html', {'countries': COUNTRIES})

def save_page1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')

        # Create a Name instance
        name_instance = Name.objects.create(name=name, country=country)

        # Process dynamic Block fields
        blocks = request.POST.getlist('blocks[]')
        for block_name in blocks:
            Block.objects.create(name=block_name, name_fk=name_instance)

        return redirect('page2', name_id=name_instance.id)
    return redirect('page1')

def page2(request, name_id):
    name = get_object_or_404(Name, pk=name_id)
    blocks = Block.objects.filter(name_fk=name)
    print(blocks,'pr....')
    return render(request, 'page2.html', {'name': name, 'blocks': blocks})

def save_page2(request, name_id):
    if request.method == 'POST':
        name = get_object_or_404(Name, pk=name_id)

        # Loop through the posted data to identify blocks and fields
        for key, values in request.POST.lists():
            if key.startswith('fields[') and key.endswith('][]'):
                block_id = key.split('[')[1].split(']')[0]
                block = get_object_or_404(Block, pk=block_id)
                for field_name in values:
                    Field.objects.create(name=field_name, name_fk=name, block_fk=block)

        return redirect('page3', name_id=name_id)
    return redirect('page2', name_id=name_id)

def page3(request, name_id):
    name = get_object_or_404(Name, pk=name_id)
    blocks = Block.objects.filter(name_fk=name)
    fields = Field.objects.filter(name_fk=name)
    return render(request, 'page3.html', {'name': name, 'countries': COUNTRIES, 'blocks': blocks, 'fields': fields})
 