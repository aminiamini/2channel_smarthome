from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import LED_States

def Control_page(request):
    Last_LED_States = LED_States.objects.all()[0]
    Latest_LED1_Status = Last_LED_States.LED1
    Latest_LED2_Status = Last_LED_States.LED2

    #template = loader.get_template('control_template.html')
    #return HttpResponse(template.render(context=))
    context = {"Latest_LED1_Status" : Latest_LED1_Status,
               "Latest_LED2_Status" : Latest_LED2_Status,}
    
    return render(request, "control_template.html", context)


def get_data(request):
    #data = str(LED_States.LED1) + str(LED_States.LED2)
    data = LED_States.objects.all()[0]
    resp_payload = str(data.LED1) +"1" + str(data.LED2) + "2"
    return HttpResponse(resp_payload)

def LED1_ON(request):

    Last_LED_States = LED_States.objects.all()[0]
    Last_LED_States.LED1 = True
    Last_LED_States.save()

    Latest_LED1_Status = Last_LED_States.LED1
    Latest_LED2_Status = Last_LED_States.LED2

    context = {"Latest_LED1_Status" : Latest_LED1_Status,
               "Latest_LED2_Status" : Latest_LED2_Status,}
    
    return render(request, "control_template.html", context)

def LED1_OFF(request):
    
    Last_LED_States = LED_States.objects.all()[0]
    Last_LED_States.LED1 = False
    Last_LED_States.save()

    Latest_LED1_Status = Last_LED_States.LED1
    Latest_LED2_Status = Last_LED_States.LED2

    context = {"Latest_LED1_Status" : Latest_LED1_Status,
               "Latest_LED2_Status" : Latest_LED2_Status,}
    
    return render(request, "control_template.html", context)

def LED2_ON(request):
    
    Last_LED_States = LED_States.objects.all()[0]
    Last_LED_States.LED2 = True
    Last_LED_States.save()

    Latest_LED1_Status = Last_LED_States.LED1
    Latest_LED2_Status = Last_LED_States.LED2

    context = {"Latest_LED1_Status" : Latest_LED1_Status,
               "Latest_LED2_Status" : Latest_LED2_Status,}
    
    return render(request, "control_template.html", context)

def LED2_OFF(request):

    Last_LED_States = LED_States.objects.all()[0]
    Last_LED_States.LED2 = False
    Last_LED_States.save()

    Latest_LED1_Status = Last_LED_States.LED1
    Latest_LED2_Status = Last_LED_States.LED2

    context = {"Latest_LED1_Status" : Latest_LED1_Status,
               "Latest_LED2_Status" : Latest_LED2_Status,}
    
    return render(request, "control_template.html", context)