from django.shortcuts import render


def startPage(request):
    return render(request, 'startPage/startPage.html', {
        'result': 'lolilol',
    })
