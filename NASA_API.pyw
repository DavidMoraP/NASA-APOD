import requests
import ctypes
import pathlib


class Wallpaper:
    def __init__(self, path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


def main():
    # requesting data from API link
    raw_response = requests.get("https://api.nasa.gov/planetary/apod?api_key=SIcyYtjr7ewrzHp76MfMghQGVtsNf1TlShsdIyNb")

    # turning data into json file and extracting values from keys hdurl and date
    json_response = raw_response.json()
    hdurl = json_response['hdurl']
    date = json_response['date'].replace('-','_')

    # requesting data from hdurl
    image_data = requests.get(hdurl)

    # creating path and name of image
    current_dir = str(pathlib.Path(__file__).parent.resolve())
    image_path = current_dir + '/APOD_images/%s_NASA_APOD.png' %date

    # saving data from hdurl into a png file
    with open(image_path, 'wb') as f:
        f.write(image_data.content)

    Wallpaper(image_path)


if __name__ == '__main__':
    main()
