import time, json, requests
	
def gdaxExLastTradePrice(coin):
	gdaxExTick = requests.get('https://api.gdax.com/products/'+coin+'/ticker')
	return gdaxExTick.json()['price'] #last trade price
	
#This loop will update the data in every 5sec
crytpocoins = ["BTC-USD","ETH-USD","LTC-USD"] #A list of all the crytpo products 

while True:
	for coin in crytpocoins:
		gdaxExLastPrice = float(gdaxExLastTradePrice(coin))
		print ("GDAX Price of ", coin, gdaxExLastPrice)
	print("==============================")
	time.sleep(5) #sleep time in sec