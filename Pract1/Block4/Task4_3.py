import math
import tkinter as tk


# Task 4_1
def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Pacman
def func(x, y):
    if (x - 0.5) ** 2 + (y - 0.6) ** 2 <= (y - 0.54) ** 2:
        return 0, 0, 0
    if (x - 0.7) ** 2 + (y - 0.6) ** 2 <= (math.sqrt(y) - 0.74) ** 2:
        return 0, 0, 0
    if (x - 0.5) ** 2 + y ** 2 <= y - 0.05:
        return 255, 255, 0
    else:
        return 0, 0, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
