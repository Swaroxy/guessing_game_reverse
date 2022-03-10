from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Codemy.com - Learn to Code!')
root.iconbitmap('C:')
root.geometry("600x100")

# Create Zipcode Lookup function
def ziplookup():
    zip.get()
    zipLabel = Label(root, text=zip.get())
    zipLabel.grid(row=1, column=0, columnspan=2)

# https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=44600&date=2022-02-26&distance=5&API_KEY=4885220D-7758-4EE7-B719-D685F49B4853

try:
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=4885220D-7758-4EE7-B719-D685F49B4853")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "Yellow"
        elif category == "Unhealthy for Sensetive Groups":
            weather_color = "Orange"
        elif category == "Unhealthy":
            weather_color = "Blue"
        elif category == "Very Unhealthy":
            weather_color = "Brown"
        elif category == "Hazardous":
            weather_color = "Black"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + "Air Quality" + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(1 )
except Exception as e:
    api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=ziplookup)
zipButton.grid(row=0, column=1)

root.mainloop()