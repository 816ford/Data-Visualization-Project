import requests
import pandas as pd
from bs4 import BeautifulSoup

# Downloading contents of the web page
url = "https://www.cars.com/shopping/results/?makes[]=&maximum_distance=50&models[]=&page=1&page_size=100&stock_type=all&zip=64082"

# Get Request
response = requests.get(url)

# Status Code
response.status_code
 
# Soup Object
soup = BeautifulSoup(response.content, "html.parser")

# Results
results = soup.find_all("div", {"class" : "vehicle-card"})

# Target necessary data. 

# Name
results[0].find("h2").get_text()
# Dealer Name
results[0].find("div", {"class":"dealer-name"}).get_text().strip
# Rating
results[0].find("span", {"class":"sds-rating__count"}).get_text()
# Review Count
results[0].find("span", {"class":"sds-rating__link"}).get_text()
# Price
results[0].find("span", {"class":"primary-price"}).get_text()

# Put everything together inside a For-Loop
name = []
dealer_name = []
rating = []
review_count = []
price = []

for result in results:
    
    # name
    try:
        name.append(result.find("h2").get_text()) 
    except:
        name.append("n/a")
    
    # dealer_name
    try:
        dealer_name.append(result.find("div", {"class":"dealer-name"}).get_text().strip())
    except:
        dealer_name.append("n/a")
        
    # rating
    try:
        rating.append(result.find("span", {"class":"sds-rating__count"}).get_text())
    except:
        rating.append("n/a")
    
    # review_count
    try:
        review_count.append(result.find("span", {"class":"sds-rating__link"}).get_text())
    except:
        review_count.append("n/a")
    
    #price 
    try:
        price.append(result.find("span", {"class":"primary-price"}).get_text())
    except:
        price.append("n/a")

# Create Pandas Dataframe
# dictionary
car_dealer = pd.DataFrame({"Name": name, "Dealer Name":dealer_name,
                                "Rating": rating, "Review Count": review_count, "Price": price})
# Output in Excel
car_dealer.to_excel("output/car_dealer_single_page.xlsx", index=False)

# Pagination
name = []
mileage = []
dealer_name = []
rating = []
review_count = []
price = []

for i in range (1,100):
    
    # website in variable
    website = "https://www.cars.com/shopping/results/?makes[]=&maximum_distance=50&models[]=&page="+str(i)+"1&page_size=100&stock_type=all&zip=64082"
    
    # request to website
    response = requests.get(website)
    
    # soup object
    soup = BeautifulSoup(response.content, "html.parser")
    
    # results
    results = soup.find_all("div", {"class" : "vehicle-card"})
    
    # loop through results
    for result in results:
    
        # name
        try:
            name.append(result.find("h2").get_text()) 
        except:
            name.append("n/a")

        # mileage
        try:
            mileage.append(result.find("div", {"class":"mileage"}).get_text())
        except:
            mileage.append("n/a")

        # dealer_name
        try:
            dealer_name.append(result.find("div", {"class":"dealer-name"}).get_text().strip())
        except:
            dealer_name.append("n/a")

        # rating
        try:
            rating.append(result.find("span", {"class":"sds-rating__count"}).get_text())
        except:
            rating.append("n/a")

        # review_count
        try:
            review_count.append(result.find("span", {"class":"sds-rating__link"}).get_text())
        except:
            review_count.append("n/a")

        #price 
        try:
            price.append(result.find("span", {"class":"primary-price"}).get_text())
        except:
            price.append("n/a")
# dictionary
car_dealer = pd.DataFrame({"Name": name, "Mileage":mileage, "Dealer Name":dealer_name,
                                "Rating": rating, "Review Count": review_count, "Price": price})
car_dealer.to_excel("output/car_dealer_single_page.xlsx", index=False)