from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# py function for home page template.. 
def home(request):  		#(request is a browser request )
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c633a6eb9f964907b4ae56ec6a813661")
	
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})
	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticket Symbol Above..."})

	# pk_c633a6eb9f964907b4ae56ec6a813661




	#return render(request, 'home.html', {'api': api}) #render the home webpage
	
def about(request):
	return render(request, 'about.html', {})

def add_stock(request):

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, "Stock has been added!")
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		return render(request, 'add_stock.html', {'ticker': ticker})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted!"))
	return redirect(add_stock)

