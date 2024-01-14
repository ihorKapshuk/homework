import codecs
import requests

wiki_url = "https://uk.wikipedia.org/"
twitter_url = "https://twitter.com/"
youtube_url = "https://www.youtube.com/"

def get_robot(url : str):
    robot_content = requests.get(url + "robots.txt").text
    try:
        with codecs.open("lesson26/my_robots.txt", "r", "utf-8") as r_r:
            r_r.read()
    except FileNotFoundError:
        with codecs.open("lesson26/my_robots.txt", "w", "utf-8") as a_r:
            a_r.write("====================================================")
            a_r.write(robot_content)
            a_r.write("====================================================")
    else:
        with codecs.open("lesson26/my_robots.txt", "a", "utf-8") as a_r:
            a_r.write("====================================================")
            a_r.write(robot_content)
            a_r.write("====================================================")

get_robot(wiki_url)
get_robot(twitter_url)
get_robot(youtube_url)