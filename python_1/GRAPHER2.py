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
def printbanner(title): # prints a banner header with text param title
    print("------------------------------------")
    print(title)
    print("------------------------------------")
def startup(): # program to run, could be in a while true loop for repeated
    os.system('cls' if os.name == 'nt' else 'clear')
    printbanner("GRAPHER INTERFACE")
    graphtype = "" # string variable type
    xaxis,yaxis=[],[] # list variable type
    selectfile = getfile()
    if selectfile:
        print(str(selectfile))
    else:
        print("No File was Selected")
        sys.exit(0)
    title = str(selectfile)
    with open(selectfile, 'r') as file: # open and read the file and turn into variable file
        reader = csv.reader(file) # READER is a list of rows
        
        # Separate the first row, to then be tested
        header = next(reader) 
        
        try:
            float(header[1]) # checks y so text x values are accepted
            # If this goes through, it's a number. Put it in the list
            # this is a float to accept decimal values as well
            xaxis.append(header[0])
            yaxis.append(header[1])
            x_label = "X Axis"
            y_label = "Y Axis"
        except ValueError: # if first part fails
            # If it fails, its a text, so use for labels
            x_label = header[0]
            y_label = header[1]

        # Loop through the remaining rows
        for row in reader: 
            xaxis.append(row[0]) 
            yaxis.append(row[1])
        maximum = max(yaxis) # maximum of y, int data type here
        minimum = min(yaxis) # minimum of y, also a int var

    graphtype = input('What graph type would you like? [Bar | Line]\n').lower() 
    if graphtype == "bar":
        print("Making your graph...")
        # graph creating with params
        graph = px.bar(x=xaxis, y=yaxis, title=title, labels={'x': x_label, 'y': y_label})
        graph.update_layout(template="plotly_white")
        graph.show()
    elif graphtype == "line":
        print("Making your graph...")
        # graph creating with params
        graph = px.line(x=xaxis, y=yaxis, title=title, markers=True, labels={'x': x_label, 'y': y_label})
        graph.update_layout(template="plotly_white")
        graph.show()
    else:
        startup()
    print("Set Data:\nMax:" + str(maximum) + "\nMin:" + str(minimum))

os.system('cls' if os.name == 'nt' else 'clear') # way to clear terminal/console text
startup()