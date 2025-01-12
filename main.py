import time
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import requests

# SPI init
spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10
reset_pin = board.D11

DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 320
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=reset_pin)
display = ST7789(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rotation=90)

splash = displayio.Group()
display.show(splash)


def update_display(content):
    splash.pop()
    # todo: display contents


def get_leetcode_stats(username):
    api_url = f"https://leetcode-stats-api.herokuapp.com/{username}"

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "totalSolved" in data:
            return {
                "username": username,
                "total_solved": data["totalSolved"],
                "easy_solved": data["easySolved"],
                "medium_solved": data["mediumSolved"],
                "hard_solved": data["hardSolved"],
            }
        else:
            raise ValueError("User Not Found！")
    else:
        raise Exception(f"Request Failed with Status Code：{response.status_code}")


username = "Jiang17832"
try:
    stats = get_leetcode_stats(username)
    print(f"LeetCode User {stats['username']}：")
    print(f"Problem Solved：{stats['total_solved']}")
    print(f"Easy：{stats['easy_solved']}")
    print(f"Medium：{stats['medium_solved']}")
    print(f"Hard：{stats['hard_solved']}")
except Exception as e:
    print(f"Error：{e}")
