import math
import random
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def noise(x, y):
    sc_x = x * random.randint(1, 15)
    sc_y = y * random.randint(70, 80)
    return (math.sin(sc_x + sc_y) * 43758.5453123) % 1


def func(x, y):
    return noise(x, y), noise(x, y), noise(x, y)


def func2(x, y):
    return 0, 0, 255


def update():
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.config(image=img)
    label.pack()
    img.image = img
    root.after(10, update)


root = tk.Tk()
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.config(image=img)
label.pack()
root.after(10, update)
root.mainloop()
