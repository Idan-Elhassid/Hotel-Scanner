# Hotel-Scanner
A unique automation script that scrapes data from booking.com to reveal the cheapest dates for a given hotel in a given period. 

using Selenium, the script will go to booking.com and simulate a search for many dates in a gives time period range, all according to our parameters.
after it finished scraping the data, it will create a customized Pandas DataFrame from which it will create a colorful and customized Seaborn Chart presenting us  with the best and cheapest dates for our desired hotel within out parameters. 

the inspiration for this project came from my wife.
for one of our holiday's, she wanted to book us a hotel with booking.com, but had to go through many different dates manually to find the best and cheapest ones.

I wanted to be able to help her and get the cheapest dates for hotels just like you can get the cheapest dates for flights in sites like skyscanner and airline website's.

***in this branch there are extra steps to collect and store monthly and seasonal data and prices. it can also display the summery of this added data in the end chart. 

***requirements: install and import the following python libraries: Selenium, pandas, seaborn. matplotlib.pyplot, datetime.


