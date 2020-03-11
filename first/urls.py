from django.urls import path
from . import views

urlpatterns = [
		path('record_sheet', views.record_sheet_view, name='record_sheet'),
		path('trading_plan', views.trading_plan_view, name='trading_plan_sheet'),
]