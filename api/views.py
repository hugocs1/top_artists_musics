from django.shortcuts import render

from api import genius_api


def search(request):
    if request.POST:
        term = request.POST.get('term')
        if term:
            api_response = genius_api.search(term)
            if api_response.ok:
                data = genius_api.create_response(api_response)
                return render(request, 'index.html', {'data': data})

    return render(request, 'index.html')
