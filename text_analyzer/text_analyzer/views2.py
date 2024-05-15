from django.http import HttpResponse
from django.shortcuts import render

#HOME PAGE
def index(request):
    return render(request, 'index.html')

#ANALYZE TEXT
def analyze(request):
    djtext = request.GET.get('text','default')
    rp = request.GET.get('removepunc','off')
    uc = request.GET.get('uppercase', 'off')
    nlr = request.GET.get('newlineremover', 'off')
    esr = request.GET.get('exspaceremover', 'off')
    cc = request.GET.get('charcount', 'off')
    print(rp)
    print(djtext)

#REMOVE PUNCTUATIONS
    if rp == "on":
        punctuations = '''?'-(){}[]_/.,:=+*&!@#$%^;!'''
        analyzed = ""
        for c in djtext:
            if c not in punctuations:
                analyzed = analyzed + c
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'text_analyzed.html', params)

#UPPERCASE
    if(uc == "on"):
        analyzed = ""
        for c in djtext:
            analyzed = analyzed + c.upper()
        params = {'purpose':'Uppercase', 'analyzed_text': analyzed}
        return render(request, 'text_analyzed.html', params)

#NEW LINE REMOVER
    elif(nlr == "on"):
        analyzed = ""
        for c in djtext:
            if c != "\n":
                analyzed = analyzed + c
        params = {'purpose':'New Line Removed', 'analyzed_text': analyzed}
        return render(request, 'text_analyzed.html', params)

#EXTRA SPACE REMOVER
    elif(esr == "on"):
        analyzed = ""
        for c in djtext:
            if c != " ":
                analyzed = analyzed + c
        params = {'purpose':'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'text_analyzed.html', params)

#CHARACTER COUNT
    elif(cc == "on"):
        analyzed = ""
        count = 0
        for c in djtext:
            # if c != " ": (for discluding space character)
                count = count + 1
        params = {'purpose':'New Line Removed', 'analyzed_text': count}
        return render(request, 'text_analyzed.html', params)






