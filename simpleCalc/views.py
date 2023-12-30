from django.shortcuts import render

# simpleCalc view as a function
def simpleCalc(request):
    """function to implement the logic of the view for simpleCalc"""
    return render(
        request,
        'simpleCalc/simpleCalc/calc.html')
