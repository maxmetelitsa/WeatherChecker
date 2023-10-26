from tkinter import *
from tkinter import messagebox
import requests


def get_weather(unit):
    city = cityName.get()
    key = '2a97878785c9b88a6fbb6276e10d0ec5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':key, 'q':city, 'units': unit}
    try:
        result = requests.get(url, params=params)
        return result.json()
    except requests.RequestException:
        return None

def display_weather():

    units_list = ['metric', 'imperial']
    weather_data = {unit: get_weather(unit) for unit in units_list}
    weatherC = weather_data['metric']
    weatherF = weather_data['imperial']

    if weatherC and 'main' in weatherC:
        info = (f'{str(weatherC["name"])}\n{weatherC["main"]["temp"]} C\n'
              f'{weatherF["main"]["temp"]} F')
        weatherInfo.config(text=info)
    else:
        messagebox.showerror('Error')

window = Tk()

window['bg'] = '#465a8c'
window.title('Weather Checker')
window.geometry('500x400')

window.resizable(width=False, height=False)

frame = Frame(window, bg='white', bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Weather Checker', font=("", 30))
title.place(relx=0.5, rely=0.1, anchor='center')

cityLabel = Label(frame, text='City', font=("", 20))
cityLabel.place(relx=0.5, rely=0.3, anchor='center')

cityName = Entry(frame, bg='#61718f', fg='black')
cityName.place(relx=0.5, rely=0.4, anchor='center')

button_check = Button(frame, text='Check weather', command=display_weather)
button_check.place(relx=0.5, rely=0.53, anchor='center')

info = Label(frame, text='Weather info', font=("", 20))
info.place(relx=0.5, rely=0.66, anchor='center')

weatherInfo = Label(frame, text='', font=("", 18))
weatherInfo.place(relx=0.5, rely=0.83, anchor='center')

window.mainloop()






