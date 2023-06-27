from tkinter import *
from tkinter.ttk import *
from time import strftime, time, gmtime

def update_clock():
    string = strftime('%H:%M:%S:%p')
    lbl_time.config(text=string)
    lbl_time.after(1000, update_clock)

def start_stopwatch():
    stopwatch['running'] = True
    stopwatch['start_time'] = time()

def stop_stopwatch():
    stopwatch['running'] = False

def reset_stopwatch():
    stopwatch['start_time'] = time()

def update_stopwatch():
    if stopwatch['running']:
        current_time = time()
        elapsed_time = current_time - stopwatch['start_time']
        time_string = strftime('%H:%M:%S', gmtime(elapsed_time))
        lbl_stopwatch.config(text=time_string)
    lbl_stopwatch.after(1000, update_stopwatch)

root = Tk()
root.title('Clock')

lbl_time = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
lbl_time.pack(anchor='center')

stopwatch = {'running': False, 'start_time': None}

btn_start = Button(root, text='START', command=start_stopwatch)
btn_start.pack()

btn_stop = Button(root, text='STOP', command=stop_stopwatch)
btn_stop.pack()

btn_reset = Button(root, text='RESET', command=reset_stopwatch)
btn_reset.pack()

lbl_stopwatch = Label(root, font=('calibri', 20), background='lightgray', foreground='black')
lbl_stopwatch.pack()

update_clock()
update_stopwatch()

root.mainloop()
