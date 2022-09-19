from datetime import *
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from openpyxl import workbook, load_workbook


x = 0
vacation_days = 5

# getting 120 days of dates
date_structure = "%Y-%m-%d"
list_of_dates = []
for number in range(1, 120):
    date_x = datetime.today() + timedelta(days=number)
    date_x_date = str(date_x.strftime(date_structure))
    list_of_dates.append(date_x_date)



service = Service(r"C:\Users\yedidya\PycharmProjects\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

date_price_dictionary = {"dates": [], "prices": []}

for item in list_of_dates:
    try:
        # list of hotels
        stella_crete = f"https://www.booking.com/hotel/gr/stella-island-luxury-resort-amp-spa.he.html?aid=376388&label=booking-name-he-ZjzRvp_RD_yeZ9lEt5OinQS494862991881%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1007978%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcX_GyndjDE1z6LWmEwkC5A&sid=d53fcdf5c54736772c37cbfaac97e2a7&checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=1973549;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;soh=1;sohad=1;sr_order=popularity;srepoch=1659855295;srpvid=8893309d8c4e035d;type=total;ucfs=1&#no_availability_msg"
        mitsis_rhodes = f"https://www.booking.com/hotel/gr/mitsis-laguna-resort-and-spa.he.html?aid=376388&label=booking-name-he-ZjzRvp_RD_yeZ9lEt5OinQS494862991881%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1007978%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcX_GyndjDE1z6LWmEwkC5A&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=33999619_289814699_2_85_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=-820290;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=8;highlighted_blocks=33999619_289814699_2_85_0;hpos=8;matching_block_id=33999619_289814699_2_85_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=33999619_289814699_2_85_0__894000;srepoch=1659977977;srpvid=89eb77768d0d0268;type=total;ucfs=1&#hotelTmpl"
        hotel_1898_barcelona = f"https://www.booking.com/hotel/es/hotel.he.html?label=gog235jc-1DCAsoRkIFaG90ZWxIDlgDaGqIAQGYAQ64ARfIAQzYAQPoAQH4AQKIAgGoAgO4AtagzZcGwAIB0gIkYmIzMjk1NmMtZDZiYy00NzE0LTk0ZDYtYjQwN2JhYThlMWNm2AIE4AIB&sid=d53fcdf5c54736772c37cbfaac97e2a7&aid=356980&ucfs=1&arphpl=1&checkin={list_of_dates[x]}&checkout={list_of_dates[x + vacation_days]}&dest_id=-372490&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=f9572de3d9d70433&srepoch=1660113097&all_sr_blocks=9167502_95123720_0_2_0&highlighted_blocks=9167502_95123720_0_2_0&matching_block_id=9167502_95123720_0_2_0&sr_pri_blocks=9167502_95123720_0_2_0__53618&from_beach_sr=1&beach_sr_walking_distance=1815&beach_rating_score=8.2&from=searchresults#hotelTmpl"
        ikos_aria_kos = f"https://www.booking.com/hotel/gr/ikos-aria.he.html?aid=2248045&sid=d53fcdf5c54736772c37cbfaac97e2a7&checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=3938566;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;soh=1;sohad=1;sr_order=popularity;srepoch=1660118190;srpvid=65fb37d8126100d8;type=total;ucfs=1&#no_availability_msg"
        hard_rock_tenerife = f"https://www.booking.com/hotel/es/hard-rock-tenerife.he.html?aid=376388&label=booking-name-he-ZjzRvp_RD_yeZ9lEt5OinQS494862991881%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1007978%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcX_GyndjDE1z6LWmEwkC5A&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=1597813_279214205_2_1_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=15978;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=1597813_279214205_2_1_0;hpos=1;matching_block_id=1597813_279214205_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=1597813_279214205_2_1_0__95100;srepoch=1660125374;srpvid=462445deb1580195;type=total;ucfs=1&#hotelTmpl"
        creta_maris_crete = f"https://www.booking.com/hotel/gr/creta-maris-beach-resort.he.html?aid=329424&label=creta-maris-beach-resort-L7Ux2q3p9C53_0ygoUAb4gS384177095172%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666555%3Akwd-888982424377%3Alp1007978%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz109Q1KykfDBuU&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=34702022_295803339_0_85_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=-820290;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=34702022_295803339_0_85_0;hpos=1;matching_block_id=34702022_295803339_0_85_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=34702022_295803339_0_85_0__235031;srepoch=1662380227;srpvid=b2835661a139010f;type=total;ucfs=1&#hotelTmpl"
        atrium_platinum_rhodes = f"https://www.booking.com/hotel/gr/atrium-platinum.he.html?aid=318615&label=New_Hebrew_HE_IL_20193534265-WOuEdgyszfdR7jrmwF%2AHCwS217272261743%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=27638102_328261851_2_1_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=-818232;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=27638102_328261851_2_1_0;hpos=1;matching_block_id=27638102_328261851_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=27638102_328261851_2_1_0__226500;srepoch=1662386265;srpvid=f3bd622c1756058f;type=total;ucfs=1&#hotelTmpl"
        hard_rock_london = f"https://www.booking.com/hotel/gb/hard-rock-london.he.html?aid=318615&label=New_Hebrew_HE_IL_20193534265-WOuEdgyszfdR7jrmwF%2AHCwS217272261743%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=382052017_121016652_2_2_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=-2601889;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=382052017_121016652_2_2_0;hpos=1;matching_block_id=382052017_121016652_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=382052017_121016652_2_2_0__206400;srepoch=1662386414;srpvid=6fb16276cc150379;type=total;ucfs=1&#hotelTmpl"
        jaz_vienna = f"https://www.booking.com/hotel/at/jaz-in-the-city-vienna.he.html?aid=318615&label=New_Hebrew_HE_IL_20193534265-WOuEdgyszfdR7jrmwF%2AHCwS78260096545%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg&sid=d53fcdf5c54736772c37cbfaac97e2a7&all_sr_blocks=721405902_348393889_2_2_0;checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=-1995499;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=2;highlighted_blocks=721405902_348393889_2_2_0;hpos=2;matching_block_id=721405902_348393889_2_2_0;nflt=review_score%3D90;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=721405902_348393889_2_2_0__72293;srepoch=1662629095;srpvid=7ae5422cb1980057;type=total;ucfs=1&#hotelTmpl"
        boutique_vienna = f"https://www.booking.com/hotel/at/stephansplatz.he.html?aid=318615&label=New_Hebrew_HE_IL_20193534265-WOuEdgyszfdR7jrmwF%2AHCwS78260096545%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg&sid=d53fcdf5c54736772c37cbfaac97e2a7&checkin={list_of_dates[x]};checkout={list_of_dates[x + vacation_days]};dest_id=70025;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;soh=1;sohad=1;sr_order=popularity;srepoch=1662629179;srpvid=005c425cd4a603aa;type=total;ucfs=1&#no_availability_msg"

        # this section will retrieve the cheapest price of each date for our desired hotel and add it to our list
        # note that you can change which hotel you want to check at the next row.
        chosen_hotel = jaz_vienna
        driver.get(chosen_hotel)
        parent = driver.find_element(By.XPATH, '//*[@id="hprt-table"]')
        date_price_dictionary["dates"].append(item)
        list_of_prices = []
        prices = parent.find_elements(By.CLASS_NAME, "prco-valign-middle-helper")
        for price in prices:
            list_of_prices.append(price.text)
        date_price_dictionary["prices"].append(list_of_prices[0])
        x += 1

    except selenium.common.exceptions.NoSuchElementException:
        x += 1
    except IndexError:
        if item == list_of_dates[-1]:
            df = pd.DataFrame(data=date_price_dictionary)
            # clean our DataFrame numbers
            df["prices"] = df["prices"].str.replace("₪", "")
            df["prices"] = df["prices"].str.replace(",", "")
            df["prices"] = df["prices"].str.strip()
            df["prices"] = df["prices"].astype(float)
            df = df.nsmallest(30, "prices")

            # this section will create the Seaborn chart that will show us the cheapest dates for our desired hotel
            sns.set_style("whitegrid")
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x="prices", y="dates", palette="rocket").set(title=f"hotel prices ({vacation_days} nights)",
                                                             xlabel="price", ylabel="checkin cheapest dates")
            cheapest = df[df["prices"] == df["prices"].min()]
            cheapest_price = cheapest["prices"].min()
            cheapest_date = cheapest.iat[0, 0]
            plt.annotate((f"the cheapest date is: {cheapest_date}\n costing: {cheapest_price} ₪"),
                          xy=(float(df["prices"].max()), 0.5), ha="center",
                           bbox=dict(boxstyle="square,pad=0.3", fc="#FFDEB4" ,ec="#411530"))

            plt.show()

