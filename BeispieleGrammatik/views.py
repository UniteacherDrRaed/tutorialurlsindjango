from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'BeispieleGrammatik/index.html')

def PrMitDative(request):
    listofprD={
        'listpr':['aus', 'nach', 'bei','mit','zu','von'],
    }
    return render(request,'BeispieleGrammatik/PraepositionsDative.html', context=listofprD)


def PrMitAkk(request):
    listofprA={
        'listpr':['fuer', 'gegen', 'ohne','um','durch'],
    }
    return render(request,'BeispieleGrammatik/PraepositionsAkk.html', context=listofprA)

