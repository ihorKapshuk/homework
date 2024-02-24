from bs4 import BeautifulSoup
import requests

wether_url = "https://www.ventusky.com/"

def show_weather(city_name : str):
    html = requests.get(wether_url + city_name.lower()).text
    soup = BeautifulSoup(html, "html.parser")
    result = ""
    result += "Година : " + "".join(soup.css.select("#forecast > div.forecast_block > table > thead > tr > th")[0].contents) + "\n"
    result += "Температура : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[0].contents) + "\n"
    result += "Товщина опадів : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[0].contents) + "\n"
    if len("".join(str(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[1].contents))) > 10:
        result += "Імовірність опадів : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span > span")[0].contents) + "\n"
    else:
        result += "Імовірність опадів : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[1].contents) + "\n"
    result += "Напрям вітру : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[1].contents) + "\n"
    result += "Швидкість вітру : " + "".join(soup.css.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[2].contents) + "\n"
    return result

def checker(condition: str):
    if condition == "1":
        result = "ОДЕСА\n" + show_weather("odessa")
    elif condition == "2":
        result = "КИЇВ\n" + show_weather("kiev")
    elif condition == "3":
        result = "ЛЬВІВ\n" + show_weather("lviv")
    elif condition == "4":
        result = "АНЕНТАЛЬ\n" + show_weather("yuzhne")
    elif condition == "5":
        result = "МИКОЛАЇВ\n" + show_weather("mykolayiv")
    elif condition == "6":
        result = "ХЕРСОН\n" + show_weather("kherson")
    elif condition == "7":
        result = "ЗАПОРІЖЖЯ\n" + show_weather("zaporizhzhya")
    elif condition == "8":
        result = "ДОНЕЦЬК\n" + show_weather("donetsk")
    elif condition == "9":
        result = "ЛУГАНСЬК\n" + show_weather("luhansk")
    elif condition == "10":
        result = "ХАРКІВ\n" + show_weather("kharkiv")
    elif condition == "11":
        result = "ДНІПРО\n" + show_weather("dnipropetrovsk")
    elif condition == "12":
        result = "КРОПИВНИЦЬКИЙ\n" + show_weather("kirovohrad")
    elif condition == "13":
        result = "ВІННИЦЯ\n" + show_weather("vinnytsya")
    elif condition == "14":
        result = "ТЕРНОПІЛЬ\n" + show_weather("ternopil")
    elif condition == "15":
        result = "ЧЕРНІВЦІ\n" + show_weather("chernivtsi")
    elif condition == "16":
        result = "ІВАНО-ФРАНКІВСЬК\n" + show_weather("ivano-frankivsk")
    elif condition == "17":
        result = "УЖГОРОД\n" + show_weather("uzhhorod")
    elif condition == "18":
        result = "ЛУЦЬК\n" + show_weather("lutsk")
    elif condition == "19":
        result = "РІВНЕ\n" + show_weather("rivne")
    elif condition == "20":
        result = "ЖИТОМИР\n" + show_weather("zhytomyr")
    elif condition == "21":
        result = "ЧЕРНІГІВ\n" + show_weather("chernihiv")
    elif condition == "22":
        result = "СУМИ\n" + show_weather("sumy")
    elif condition == "23":
        result = "ПОЛТАВА\n" + show_weather("poltava")
    elif condition == "24":
        result = "ЧЕРКАСИ\n" + show_weather("cherkasy")
    elif condition == "25":
        result = "СІМФЕРОПОЛЬ\n" + show_weather("simferopol")
    elif condition == "26":
        result = "СЕВАСТОПОЛЬ\n" + show_weather("sevastopol")
    return result