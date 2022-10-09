from django.shortcuts import render


def main_page(request):
    context = {'dishes': {'omlet': 'Омлет',
                          'pasta': 'Паста',
                          'buter': 'Бутерброд'}}
    return render(request, 'calculator/main_page.html', context)


def omlet(request):
    number = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Омлет',
        'recipe': {
            'яйца, шт': 2*number,
            'молоко, л': round(0.1*number, 2),
            'соль, ч.л.': round(0.5*number, 2), }}
    return render(request, 'calculator/index.html', context)


def pasta(request):
    number = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Паста',
        'recipe': {
            'макароны, г': round(number*0.3, 2),
            'сыр, г': round(number*0.05, 2), }}
    return render(request, 'calculator/index.html', context)


def buter(request):
    number = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Бутерброд',
        'recipe': {
            'хлеб, ломтик': number,
            'колбаса, ломтик': number,
            'сыр, ломтик': number,
            'помидор, ломтик': number, }}
    return render(request, 'calculator/index.html', context)

