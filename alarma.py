from time import localtime
from pygame import mixer

H = int(input("Ingrese la hora: "))
M = float(input("Ingrese los minutos: "))

while True:
    if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
        print("Sonando alarma")
        mixer.init()
        mixer.music.load("alarma.mp3")
        mixer.music.play()
        break
    