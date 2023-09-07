from django.shortcuts import render
from . import models

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

def GArtikelNominativeUndAkkusative(request):
    AlleBeispiele=models.BeispielFuerArtikel.objects.all()
    return render(request,'BeispieleGrammatik/GArtikelNominativeUndAkkusativehtml.html',context={"AlleBeispiele":AlleBeispiele})

