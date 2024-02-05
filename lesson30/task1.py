import requests

def show_war_stat_en():
    data = requests.get("https://russianwarship.rip/api/v2/war-info/status/en").json()
    status = data["data"]["war_status"]["alias"]
    description = data["data"]["description"]
    return f"War status : {status}\nDescription : {description}"

def show_war_stat_ua():
    data = requests.get("https://russianwarship.rip/api/v2/war-info/status/ua").json()
    status = data["data"]["war_status"]["alias"]
    description = data["data"]["description"]
    return f"Статус війни : {status}\nОпис : {description}"

print(show_war_stat_en())
print(show_war_stat_ua())