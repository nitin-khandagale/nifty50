from django.shortcuts import render

def record_sheet_view(request):
	return render(request, 'record_sheet.html')

def trading_plan_view(request):
	return render(request, 'trading_plan.html')

	