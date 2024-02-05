import requests

def last_war_stat():
    data = requests.get("https://russianwarship.rip/api/v2/statistics/latest").json()
    date = data["data"]["date"]
    day = data["data"]["day"]
    status = data["data"]["war_status"]["alias"]
    print(f"date : {date}\nday : {day}\nstatus : {status}")
    stats = data["data"]["stats"]
    for k, v in stats.items():
        print(k + " : " + str(v))

last_war_stat()