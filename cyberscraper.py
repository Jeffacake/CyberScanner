import tkinter as tk
from tkinter import font
#matplotlib provides OOP API for embedding plots into apps
import matplotlib.pyplot as plt
#import class for embedding figures into tkinter 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import numpy (used in conjunction with matplotlib for visualization)
import numpy as np
#import dummy data
from dummyData import attack_frequency, attack_severity, attack_success_rate, cyber_attacks

#rcParams stands for runtime configuration parameters
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#0047AB", "#6E81D6", "#2E5AAC", "#17325E", "#8CB8E8"]
)


    # def plot():
    #     x = np.random.randint(0,10,10)
    #     ax.plot(x)
    #     canvas.draw()

    # def clear():
    #     ax.clear()
    #     canvas.draw()



#chart1
fig1, ax1 = plt.subplots() 
ax1.bar(attack_frequency.keys(), attack_frequency.values())
ax1.set_title("Attack Frequency")
ax1.set_xlabel("Attack Type")
ax1.set_ylabel("Frequency")


#chart2
fig2, ax2 = plt.subplots()

ax2.barh(list(attack_severity.keys()), attack_severity.values()) #barh must take list object
ax2.set_title("Attack Severity")
ax2.set_xlabel("Attack Type")
ax2.set_ylabel("Severity")


#chart3
fig3, ax3, = plt.subplots()
ax3.pie(attack_success_rate.values(), labels=attack_success_rate.keys())
ax3.set_title("Attack Success Rate")

fig4, ax4, = plt.subplots()
ax4.plot(cyber_attacks.keys(), cyber_attacks.values())
ax4.set_title("Cyber Attacks over 6yr period")




#Initialise Tkinter
root = tk.Tk()
root.config(bg="grey")

#welcome label
bold_font = font.Font(family="Helvetica", size=12, weight="bold")

greeting = tk.Label(root, text="Welcome to CyberScraper",
                    font=bold_font,           
                    fg="blue",
                    bg="#34A2FE",
                    pady=10
                    )
greeting.pack(fill=tk.X)

upper_frame = tk.Frame(root)
upper_frame.pack(fill="both", expand=True)
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.get_tk_widget().pack(side="left", fill="both",expand=True)
canvas1.draw()

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.get_tk_widget().pack(side="left", fill="both", expand="true")
canvas2.draw()

lower_frame = tk.Frame(root)
lower_frame.pack(fill="both",expand="true")

canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
canvas3.get_tk_widget().pack(side="left",fill="both",expand="true")
canvas3.draw()

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.get_tk_widget().pack(side="left", fill="both",expand="true")

root.mainloop()
#window.update()
