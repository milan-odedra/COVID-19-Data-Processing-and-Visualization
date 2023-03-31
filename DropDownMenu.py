#!/usr/bin/python
import tkinter
import csv

window = tkinter.Tk()
clicked = tkinter.StringVar()

with open('Dataset\Covid-19 Dataset\\country_wise_latest.csv', 'r') as x:
    read = csv.reader(x)
    header = next(read)
    countryStatistics = {}
    for line in read:
       countryStatistics[line[0]] = {header[i]: line[i] for i in range(1, len(line))}

window.title("Countries' Covid-19 Statistics")

clicked.set("Select a country")
drop = tkinter.OptionMenu(window, clicked, *countryStatistics)
drop.pack()

confirmedLabel = tkinter.Label(window, text="Confirmed: ")
confirmedLabel.pack()

deathsLabel = tkinter.Label(window, text="Deaths: ")
deathsLabel.pack()

recoveredLabel = tkinter.Label(window, text="Recovered: ")
recoveredLabel.pack()

activeLabel = tkinter.Label(window, text="Active: ")
activeLabel.pack()

newCasesLabel = tkinter.Label(window, text="New cases: ")
newCasesLabel.pack()

newDeathsLabel = tkinter.Label(window, text="New deaths: ")
newDeathsLabel.pack()

newRecoveredLabel = tkinter.Label(window, text="New recovered: ")
newRecoveredLabel.pack()

deaths100CasesLabel = tkinter.Label(window, text="Deaths / 100 Cases: ")
deaths100CasesLabel.pack()

recovered100CasesLabel = tkinter.Label(window, text="Recovered / 100 Cases: ")
recovered100CasesLabel.pack()

deaths100RecoveredLabel = tkinter.Label(window, text="Deaths / 100 Recovered: ")
deaths100RecoveredLabel.pack()

confirmedLastWeekLabel = tkinter.Label(window, text="Confirmed last week: ")
confirmedLastWeekLabel.pack()

weekChangeLabel = tkinter.Label(window, text="1 week change: ")
weekChangeLabel.pack()

weekPercentIncreaseLabel = tkinter.Label(window, text="1 week % increase: ")
weekPercentIncreaseLabel.pack()

whoRegionLabel = tkinter.Label(window, text="WHO Region: ")
whoRegionLabel.pack()


def displayData():
    country = clicked.get()
    data = countryStatistics[country]

    confirmedLabel.config(text=f"Confirmed: {data['Confirmed']}")
    deathsLabel.config(text=f"Deaths: {data['Deaths']}")
    recoveredLabel.config(text=f"Recovered: {data['Recovered']}")
    activeLabel.config(text=f"Active: {data['Active']}")
    newCasesLabel.config(text=f"New cases: {data['New cases']}")
    newDeathsLabel.config(text=f"New deaths: {data['New deaths']}")
    newRecoveredLabel.config(text=f"New recovered: {data['New recovered']}")
    deaths100CasesLabel.config(text=f"Deaths / 100 Cases: {data['Deaths / 100 Cases']}")
    recovered100CasesLabel.config(text=f"Recovered / 100 Cases: {data['Recovered / 100 Cases']}")
    deaths100RecoveredLabel.config(text=f"Deaths / 100 Recovered: {data['Deaths / 100 Recovered']}")
    confirmedLastWeekLabel.config(text=f"Confirmed last week: {data['Confirmed last week']}")
    weekChangeLabel.config(text=f"1 week change: {data['1 week change']}")
    weekPercentIncreaseLabel.config(text=f"1 week % increase: {data['1 week % increase']}")
    whoRegionLabel.config(text=f"WHO Region: {data['WHO Region']}")



button = tkinter.Button(window, text="Display Data", command=displayData)
button.pack()
window.mainloop()
