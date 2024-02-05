import requests

def get_date_stat(your_date : str):
    """year-month-day (after 2022-04-14)"""
    try:
        data = requests.get("https://russianwarship.rip/api/v2/statistics/" + your_date).json()
        date = data["data"]["date"]
        day = data["data"]["day"]
        status = data["data"]["war_status"]["alias"]
        print(f"date : {date}\nday : {day}\nstatus : {status}")
        stats = data["data"]["stats"]
        for k, v in stats.items():
            print(k + " : " + str(v))
    except KeyError:
        print("Не вірно введено дату!")

get_date_stat("2023-01-01")
print("---------------------------")
get_date_stat("2024-01-01")