from bs4 import BeautifulSoup
import requests

wether_url = "https://www.ventusky.com/"

def show_weather(city_name : str):
    html = requests.get(wether_url + city_name.lower()).text
    soup = BeautifulSoup(html, "html.parser")
    print("Година : ", "".join(soup.css.select("#forecast > div.forecast_block > table > thead > tr > th")[0].contents))
    print("Температура : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[0].contents))
    print("Товщина опадів : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[0].contents))
    if len("".join(str(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[1].contents))) > 10:
        print("Імовірність опадів : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span > span")[0].contents))
    else:
        print("Імовірність опадів : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[1].contents))
    print("Напрям вітру : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[1].contents))
    print("Швидкість вітру : ", "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[2].contents))

show_weather("winnipeg")