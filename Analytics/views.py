from django.shortcuts import render
from .charts import create_chart

def dashboard(request):
    chart = create_chart()
    return render(request, "pages/dashboard.html",{"chart": chart})