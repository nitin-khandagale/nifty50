from django.shortcuts import render
from .models import Pistol

def record_sheet_view(request):
	data = Pistol.objects.get(sr=5)
	return render(request, 'record_sheet.html', {'data':data})

def trading_plan_view(request):
	return render(request, 'trading_plan.html')

	