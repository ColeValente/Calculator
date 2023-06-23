import tkinter as tk
window = tk.Tk()

strg1 = ""
strg2 = ""

def button1_click():
	global strg1
	strg1 = strg1 + '1'
	print(strg1)

def button2_click():
	global strg1
	strg1 = strg1 + '2'
	print(strg1)

def button3_click():
	global strg1
	strg1 = strg1 + '3'
	print(strg1)

def button4_click():
	global strg1
	strg1 = strg1 + '4'
	print(strg1)

def button5_click():
	global strg1
	strg1 = strg1 + '5'
	print(strg1)

def button6_click():
	global strg1
	strg1 = strg1 + '6'
	print(strg1)

def button7_click():
	global strg1
	strg1 = strg1 + '7'
	print(strg1)

def button8_click():
	global strg1
	strg1 = strg1 + '8'
	print(strg1)

def button9_click():
	global strg1
	strg1 = strg1 + '9'
	print(strg1)

def button0_click():
	global strg1
	strg1 = strg1 + '0'
	print(strg1)

frame = tk.Frame()

greetings = tk.Label(master=frame, text="Hello, Tkinter")
greetings.pack()

button1 = tk.Button(
	master = frame,
	text = "1",
	command = button1_click
	)
button2 = tk.Button(
	master = frame,
	text = "2",
	command = button2_click
	)
button3 = tk.Button(
	master = frame,
	text = "3",
	command = button3_click
	)
button4 = tk.Button(
	master = frame,
	text = "4",
	command = button4_click
	)
button5 = tk.Button(
	master = frame,
	text = "5",
	command = button5_click
	)
button6 = tk.Button(
	master = frame,
	text = "6",
	command = button6_click
	)
button7 = tk.Button(
	master = frame,
	text = "7",
	command = button7_click
	)
button8 = tk.Button(
	master = frame,
	text = "8",
	command = button8_click
	)
button9 = tk.Button(
	master = frame,
	text = "9",
	command = button9_click
	)
button0 = tk.Button(
	master = frame,
	text = "0",
	command = button0_click
	)



button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button0.pack()

frame.pack()



window.mainloop()

