# Hotel-Scanner
A unique automation script that scrapes data from booking.com to reveal the cheapest dates for a given hotel in a given period. 

using Selenium, the script will go to booking.com and simulate a search for many dates in a gives time period range, all according to our parameters.
after it finished scraping the data, it will create a customized Pandas DataFrame from which it will create a colorful and customized Seaborn Chart presenting us  with the best and cheapest dates for our desired hotel within out parameters. 

the inspiration for this project came from my wife.
for one of our holiday's, she wanted to book us a hotel with booking.com, but had to go through many different dates manually to find the best and cheapest ones.

I wanted to be able to help her and get the cheapest dates for hotels just like you can get the cheapest dates for flights in sites like skyscanner and airline website's.

***requirements: install and import the following python libraries: Selenium, pandas, seaborn. matplotlib.pyplot, datetime.


here is a little demo: 
we are looking on the Hard Rock hotel in london, at mid december the price was above 8000₪ 
but using my software we found much cheaper dates at january\february - with the cheapest date highlighted at aroung 5000₪ 


![booking3](https://user-images.githubusercontent.com/112956707/207547969-b950a580-56d2-4dca-a7d4-028e1c5b05ea.PNG)

