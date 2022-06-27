from django.shortcuts import render

# Create your views here.


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})
