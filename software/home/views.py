import math
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def evenodd(request):
    c = ''
    n = ''
    try:
        if request.method == "POST":
            n = eval(request.POST.get('num'))
            if n%2 == 0:
                c = 'even'
            else:
                c = 'odd'
    except:
        c = 'Error...!'

    data = {
        'num' : n,
        'output' : c
    }
    return render(request, 'evenodd.html', data)

def squareOrSquareRoot(request):
    opr = ''
    r = ''
    n = ''
    try:
        if request.method == "POST":
            n = eval(request.POST.get('num'))
            opr = request.POST.get('opr')
            if opr == '*':
                r = n*n
            elif opr == '/':
                r = math.sqrt(n)
            else:
                r = 'Plese select anyone'
    except:
        r = 'Error....!'

    data = {
            'num': n,
            'output': r,
        }
    return render(request, 'squareOrSquareRoot.html',data)


def primeOrNot(request):
    p=''
    n = ''
    try:
        if request.method == "POST":
            n = eval(request.POST.get('num'))
            if n == 2:
                p = 'Number is prime'
            elif n>1:
                for i in range(2, n):
                    if(n%i) == 0:
                        p = 'Not Prime'
                        break
                    else:
                        p = 'Number is Prime'
            else:
                p ='Not Prime'

    except:
        p = 'Error.....!'
    data = {
        'num': n,
        'output':p
    }
    return render(request, 'primeOrNot.html', data)