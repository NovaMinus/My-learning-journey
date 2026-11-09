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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("No file selected")
        time.sleep(3) # wait 3 seconds before returning so error message can be read
        return
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
            yaxis.append(float(header[1]))
            x_label = "X Axis"
            y_label = "Y Axis"
        except ValueError: # if first part fails
            # If it fails, its a text, so use for labels
            x_label = header[0]
            y_label = header[1]

        # Loop through the remaining rows
        for row in reader: 
            xaxis.append(row[0]) 
            try:
                yaxis.append(float(row[1]))
            except ValueError: # if its a text
                print("This file is not supported")
                print ("Error: Y-Value Text")
                return # ends the function
            
        maximum = max(yaxis) # maximum of y, int data type here
        minimum = min(yaxis) # minimum of y, also a int var
    print("--- Reviewing Extracted Variables ---")
    for x_val, y_val in zip(xaxis, yaxis): # zip() combines xaxis yaxis to a list of tuples, which can be like coordinates
        print(f"({x_val}, {y_val})") # f"" with the {} is a cleaner way to write out variables as strings
    print("-------------------------------------\n")
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
        return
    print("Set Data:\nMax:" + str(maximum) + "\nMin:" + str(minimum))
    loopprompt = input('Press enter to start again or exit to exit.\n').lower()
    if loopprompt == "exit":
        sys.exit(0)
while True: # program loop
    os.system('cls' if os.name == 'nt' else 'clear') # way to clear terminal/console text
    startup()   