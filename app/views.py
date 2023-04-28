from django.shortcuts import render

# Create your views here.
def Built_in_filters(request):
    import datetime
    t=datetime.datetime.now()
    d={'data':'Hai NaReNdRa','t':t,'c':5}

    return render(request,'Built_in_filters.html',d)
