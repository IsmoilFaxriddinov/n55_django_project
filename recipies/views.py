from django.shortcuts import render

def recipies_list_view(request):
    return render(request, 'recipies/recipies-list.html')

def recipies_category_list_view(request):
    return render(request, 'recipies/recipies.html')
