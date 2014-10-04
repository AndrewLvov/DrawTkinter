from math import sqrt
from tkinter import Tk, Canvas, PhotoImage, BOTH

WIDTH = 150
HEIGHT = 120


def draw_gradient(canvas):
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT//2), image=img, state="normal")
    # range(10) => (0, 1, 2, ..., 9)
    # range(5, 10) => (5, 6, 7, 8, 9)
    # range(5, 15, 2) => (5, 7, 9, 11, 13)
    for j in range(0, HEIGHT):
        for i in range(0, WIDTH):
            # RGB = red, green, blue
            # диапазон цвета: 0..255, 0x00..0xFF
            img.put("#%02x%02x%02x" % (i % 128, j % 128, 0), (i, j))
    return img


def draw_danger_levels(canvas, x, y):
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT//2), image=img, state="normal")

    for j in range(0, HEIGHT):
        for i in range(0, WIDTH):
            # RGB = red, green, blue
            # диапазон цвета: 0..255, 0x00..0xFF
            distance = sqrt((i-x)**2 + (j-y)**2) / 5
            # две роли оператора %
            # 1 - форматирование строки
            # 2 - остаток от деления
            img.put("#%02x%02x%02x" % (255/(int(distance) % 256 + 1), 0, 0), (i, j))
    return img


def main():
    root = Tk(className="My graphics!")
    root.geometry("400x400")
    canvas = Canvas()
    canvas.pack(fill=BOTH, expand=1)
    # img = draw_gradient(canvas)

    img = draw_danger_levels(canvas, 50, 50)

    # что бы ограничить число
    # if n > 255:
    #     n = 255

    # хочу: n = 256 => 0
    # n = 257 => 1
    # ...
    # n = 300 => 44
    # 10 // 3 = 3(1)
    # 10 - (10 // 3) * 3
    # 10 % 3
    # a % b < b
    # 10 % 3 = 1
    # 11 % 3 = 2
    # 12 % 3 = 0
    # 13 % 3 = 1

    root.mainloop()

    # print("%02x" % (0))

    # print("{}, type: {}".format(WIDTH/2, type(WIDTH/2)))
    # print("{}, type: {}".format(WIDTH//2, type(WIDTH//2)))

main()