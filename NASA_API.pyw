import requests
import ctypes

class Wallpaper:
    def __init__(self, path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

# requesting data from API link
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=SIcyYtjr7ewrzHp76MfMghQGVtsNf1TlShsdIyNb")

# turning data into json file and extracting values from keys hdurl and date
hdurl = response.json()['hdurl']
date = response.json()['date'].replace('-','_')

# requesting data from hdurl
image_data = requests.get(hdurl)

# creating path and name of image
image_path = 'E:/Theseus/Pictures/NASA_APOD/%s_NASA_APOD.png' %date

# saving data from hdurl into a png file
with open(image_path, 'wb') as f:
    f.write(image_data.content)

wallpaper_change = Wallpaper(image_path)