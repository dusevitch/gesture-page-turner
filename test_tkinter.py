# tutorial/test with tkinter

import tkinter as tk

window = tk.Tk()




# greeting = tk.Label(text="Hello Tkinter", width=100,height=15) # Label width and height measured in text units
# greeting.pack() # pack sizes the windwo as small as it can while still fully encompassing the widget
    
# text_box = tk.Text(width=100)
# text_box.pack()
# print(text_box.get("1.0",tk.END))

# # #Frame Widgets
# frame_a = tk.Frame()
# frame_b = tk.Frame()

# labela = tk.Label(master=frame_a, text = "Frame a")
# labelb = tk.Label(master=frame_b, text = "Frame b")

# labela.pack()
# labelb.pack()

# frame_b.pack()
# frame_a.pack()


# # Pack Geometry examples
frame1 = tk.Frame(master=window,  height=100, bg="red")
frame1.pack(fill=tk.BOTH)
frame2 = tk.Frame(master=window,  height=50, bg ="yellow")
frame2.pack(fill=tk.BOTH)
frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.BOTH)

# # Pack expand both
frame1 = tk.Frame(master=window,  width = 200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
frame2 = tk.Frame(master=window,  height=50, bg ="yellow")
frame2.pack(fill=tk.BOTH, expand=True)
frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, expand=True)

window.mainloop()