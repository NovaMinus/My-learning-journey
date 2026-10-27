import os
import csv
import sys
import plotly.express as px
import tkinter as tk
from tkinter import filedialog
def getfile(): # function to get the file path of a selected file in a prompt
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title="Select a File", filetypes=[("All Files", "*.csv")])
    return filepath
def printbanner(title):
    print("------------------------------------")
    print(title)
    print("------------------------------------")
def startup():
    os.system('cls' if os.name == 'nt' else 'clear')
    printbanner("GRAPHER INTERFACE")
    graphtype = ""
    xaxis,yaxis=[],[]
    selectfile = getfile()
    if selectfile:
        print(str(selectfile))
    else:
        print("No File was Selected")
        sys.exit(0)
    title = str(selectfile)
    with open(selectfile, 'r') as file: # open and read the file and turn into variable file
        reader = csv.reader(file)
        for row in reader:
            xaxis.append(row[0]) # add left row which is x value
            yaxis.append(row[1]) # add right row which is y value
    graphtype=input('What graph type would you like? [Bar | Line]\n').lower() # ask which graph type
    if graphtype == "bar":
        print("Making your graph...")
        graph = px.bar(x=xaxis, y=yaxis, title=title)
        graph.update_layout(template="plotly_white")
        # graph.update_layout(xaxis_title=xtitle, yaxis_title=ytitle)

        graph.show()
    elif graphtype == "line":
        print("Making your graph...")
        graph = px.line(x=xaxis, y=yaxis, title=title, markers=True)
        graph.update_layout(template="plotly_white")
        # graph.update_layout(xaxis_title=xtitle, yaxis_title=ytitle)
        graph.show()
    else:
        startup()
os.system('cls' if os.name == 'nt' else 'clear') # way to clear terminal/console text
startup()