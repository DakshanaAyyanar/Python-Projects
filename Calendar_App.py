import tkinter as tk
from time import strftime
from datetime import datetime
import pytz
from tkinter import messagebox

root = tk.Tk()
root. title("Advanced Clock App")
root.geometry("500x400")

bg_color = "black"
fg_color = "cyan"

zones = {
    "India": "Asia/Kolkata",
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo"
}

def update_time():
    selected = zone_var.get()
    tz = pytz. timezone(zones[selected])
    time_now = datetime.now(tz).strftime("%H:%M:%S")
    clock_label.config(text=time_now)
    root.after(1000, update_time)

def check_alarm():
    alarm_time = alarm_entry.get()
    current = strftime("%H:%M:%S")
    if alarm_time == current:
        messagebox. showinfo("Alarm", "Time's up!")
        
    root.after(1000, check_alarm)
        

def toggle_theme():
    global bg_color, fg_color
    if bg_color == "black":
        bg_color = "white"
        fg_color = "black"
    else:
        bg_color = "black"
        fg_color = "cyan"
        
        root.configure(bg=bg_color)
        clock_label.config(bg=bg_color, fg=fg_color)

clock_label = tk.Label(root, font=("Arial", 40, "bold"), bg=bg_color, fg=fg_color)
clock_label.pack(pady=20)

zone_var = tk.StringVar(value="India")
menu = tk.OptionMenu(root, zone_var, *zones.keys())
menu.pack()

alarm_entry = tk.Entry(root)
alarm_entry.pack(pady=10)
alarm_entry.insert(0, "HH:MM:SS")

alarm_btn = tk.Button(root, text="Set Alarm", command=check_alarm)
alarm_btn.pack()

theme_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_btn.pack(pady=10)

root.mainloop()