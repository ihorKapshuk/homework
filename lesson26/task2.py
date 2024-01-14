import requests
import json

def get_war_stat(date_from : str, date_to : str):
    """year-month-day"""
    from_stats = requests.get("https://russianwarship.rip/api/v2/statistics/" + date_from).json()["data"]["stats"]
    to_stats = requests.get("https://russianwarship.rip/api/v2/statistics/" + date_to).json()["data"]["stats"]
    new_stats = {
        "personnel_units": to_stats["personnel_units"] - from_stats["personnel_units"],
        "tanks": to_stats["tanks"] - from_stats["tanks"],
        "armoured_fighting_vehicles": to_stats["armoured_fighting_vehicles"] - from_stats["armoured_fighting_vehicles"],
        "artillery_systems": to_stats["artillery_systems"] - from_stats["artillery_systems"],
        "mlrs": to_stats["mlrs"] - from_stats["mlrs"],
        "aa_warfare_systems": to_stats["aa_warfare_systems"] - from_stats["aa_warfare_systems"],
        "planes": to_stats["planes"] - from_stats["planes"],
        "helicopters": to_stats["helicopters"] - from_stats["helicopters"],
        "vehicles_fuel_tanks": to_stats["vehicles_fuel_tanks"] - from_stats["vehicles_fuel_tanks"],
        "warships_cutters": to_stats["warships_cutters"] - from_stats["warships_cutters"],
        "cruise_missiles": to_stats["cruise_missiles"] - from_stats["cruise_missiles"],
        "uav_systems": to_stats["uav_systems"] - from_stats["uav_systems"],
        "special_military_equip": to_stats["special_military_equip"] - from_stats["special_military_equip"],
        "atgm_srbm_systems": to_stats["atgm_srbm_systems"] - from_stats["atgm_srbm_systems"],
        "submarines": to_stats["submarines"] - from_stats["submarines"]
    }
    with open("lesson26/your_stats.json", "w") as w_s:
        json.dump(new_stats, w_s)

get_war_stat("2022-12-01", "2023-03-01")