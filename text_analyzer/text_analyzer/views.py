from django.http import HttpResponse
from django.shortcuts import render


#HOME PAGE
def index(request):
    return render(request, 'index.html')


#ANALYZE TEXT
def analyze(request):
    djtext = request.POST.get('text', 'default')
    rp = request.POST.get('removepunc', 'off')
    uc = request.POST.get('uppercase', 'off')
    nlr = request.POST.get('newlineremover', 'off')
    esr = request.POST.get('exspaceremover', 'off')
    cc = request.POST.get('charcount', 'off')
    print(djtext)

#REMOVE PUNCTUATIONS
    if rp == "on":
        punctuations = '''?'-(){}[]_/.,:=+*&!@#$%^;!'''
        analyzed = ""
        for c in djtext:
            if c not in punctuations:
                analyzed = analyzed + c
        djtext = analyzed

#UPPERCASE
    if uc == "on":
        analyzed = ""
        for c in djtext:
            analyzed = analyzed + c.upper()
        djtext = analyzed

#NEW LINE REMOVER
    if nlr == "on":
        analyzed = ""
        for c in djtext:
            if c != "\n":
                analyzed = analyzed + c
        djtext = analyzed

#EXTRA SPACE REMOVER
    if esr == "on":
        analyzed = ""
        for c in djtext:
            if c != " ":
                analyzed = analyzed + c
        djtext = analyzed

#CHARACTER COUNT
    if cc == "on":
        count = 0
        for c in djtext:
            count = count + 1

        params2 = {'count': count}
        return render(request, 'text_analyzed.html', params2)

#IF NO BUTTON IS ON
    if rp != "on" and uc != "on" and nlr != "on" and esr != "on":
        return HttpResponse("Error")

    djtext = analyzed
    params = {'analyzed_text': analyzed}
    return render(request, 'text_analyzed.html', params)



    # params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
    # return render(request, 'text_analyzed.html', params)