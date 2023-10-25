import tkinter as tk
from tkinter import font
#matplotlib provides OOP API for embedding plots into apps
import matplotlib.pyplot as plt
#import class for embedding figures into tkinter 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import numpy (used in conjunction with matplotlib for visualization)
import numpy as np


def plot():
    x = np.random.randint(0,10,10)
    ax.plot(x)
    canvas.draw()

def clear():
    ax.clear()
    canvas.draw()


#Initialise Tkinter
root = tk.Tk()
root.configure(bg="grey")

#welcome label
bold_font = font.Font(family="Helvetica", size=12, weight="bold")

greeting = tk.Label(root, text="Welcome to CyberScraper",
                    font=bold_font,           
                    fg="blue",
                    bg="#34A2FE",
                    pady=10
                    )
greeting.pack(fill=tk.X)

#create frame for graph to fill
graph_frame = tk.Frame(root, bg="white")  
graph_frame.pack(fill=tk.BOTH)

#create figure for canvas
figure, ax = plt.subplots()
#canvas takes figure and 'frame' parameter)
canvas = FigureCanvasTkAgg(figure, master=graph_frame)
#to integrate in tkinter, get the widget for it first
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


plot_graph_button = tk.Button(graph_frame, text="Plot Graph",padx=10,pady=10, command=plot).pack()

refresh_button = tk.Button(graph_frame, text="Refresh", padx=10,pady=10, command=clear).pack()

root.mainloop()
#window.update()
