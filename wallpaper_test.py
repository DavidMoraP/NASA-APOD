import ctypes

class Wallpaper:
    def __init__(self, pp):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, pp, 0)

path = 'e:/Theseus/Pictures/NASA_APOD/2022_02_27_NASA_APOD.png'
application = Wallpaper(path)