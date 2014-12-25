## module to draw a graphic representation with tkinter
# -*- coding: utf-8 -*-

from Tkinter import *
import board_properties as Config

"""
returns a Tkinter instance for future Tkinter calls
"""

def     get_instance():
    return Tk()

"""
returns a canvas object to draw on
"""

def     get_window(instance):
    canvas = Canvas(instance, width=Config.xmax, height=Config.ymax)
    canvas.pack()
    return canvas

"""
calls Tkinter mainloop() function
"""

def     do_mainloop():
    mainloop()
    return

"""
draw graphic representation function
"""

def     draw_graphic(window, ressources, results, prices, res):
    window.configure(background="black")
    window.create_rectangle(0, Config.ymax * 0.15, Config.xmax, Config.ymax * 0.85, fill="#FFCCFF", stipple="gray75", outline="#FFCCFF")
    window.create_arc(0, Config.ymax * 0.89, Config.xmax, Config.ymax, start=0, extent=210, fill="red", width=3)
    draw_text(window, ressources, results, prices, res)
    draw_prices(window, prices)
    draw_prod(window, results)

"""
draw text in graphic
"""

def     draw_text(window, ressources, results, prices, res):
    tHead = window.create_text(Config.xmax * 0.42, Config.ymax * 0.03, anchor="nw", fill="#%02x%02x%02x" % (244, 226, 156))
    window.itemconfig(tHead, text="Available ressources", font=('Helvetica', '20'))

    tE1 = window.create_text(Config.xmax * 0.05, Config.ymax * 0.1, anchor="nw", fill="#%02x%02x%02x" % (244, 226, 156))
    window.itemconfig(tE1, text="E1 : {}".format(str(int(ressources[0]))), font=('Helvetica', '20'))
    tE2 = window.create_text(Config.xmax * 0.3, Config.ymax * 0.1, anchor="nw", fill="#%02x%02x%02x" % (244, 226, 156))
    window.itemconfig(tE2, text="E2 : {}".format(str(int(ressources[1]))), font=('Helvetica', '20'))
    tE3 = window.create_text(Config.xmax * 0.65, Config.ymax * 0.1, anchor="nw", fill="#%02x%02x%02x" % (244, 226, 156))
    window.itemconfig(tE3, text="E3 : {}".format(str(int(ressources[2]))), font=('Helvetica', '20'))
    tE4 = window.create_text(Config.xmax * 0.9, Config.ymax * 0.1, anchor="nw", fill="#%02x%02x%02x" % (244, 226, 156))
    window.itemconfig(tE4, text="E4 : {}".format(str(int(ressources[3]))), font=('Helvetica', '20'))

    tA = window.create_text(Config.xmax * 0.45, Config.ymax * 0.25, anchor="nw", fill="green")
    window.itemconfig(tA, text="Avoine", font=('Helvetica', '30'))
    tB = window.create_text(Config.xmax * 0.47, Config.ymax * 0.35, anchor="nw", fill="red")
    window.itemconfig(tB, text="Blé", font=('Helvetica', '30'))
    tM = window.create_text(Config.xmax * 0.463, Config.ymax * 0.45, anchor="nw", fill="yellow")
    window.itemconfig(tM, text="Maïs", font=('Helvetica', '30'))
    tO = window.create_text(Config.xmax * 0.463, Config.ymax * 0.55, anchor="nw", fill="blue")
    window.itemconfig(tO, text="Orge", font=('Helvetica', '30'))
    tS = window.create_text(Config.xmax * 0.463, Config.ymax * 0.65, anchor="nw", fill="grey")
    window.itemconfig(tS, text="Soja", font=('Helvetica', '30'))

    tProd = window.create_text(Config.xmax * 0.15, Config.ymax * 0.2, anchor="nw", fill="black")
    window.itemconfig(tProd, text="Production", font=('Helvetica', '20'))

    tPrice = window.create_text(Config.xmax * 0.8, Config.ymax * 0.2, anchor="nw", fill="black")
    window.itemconfig(tPrice, text="Prices", font=('Helvetica', '20'))

    tFoot = window.create_text(Config.xmax * 0.43, Config.ymax * 0.90, anchor="nw", fill="orange")
    window.itemconfig(tFoot, text="Profits : {} €".format(str(res)), font=('Helvetica', '20'))

"""
draw prices
"""

def     draw_prices(window, prices):
    maximum = max(prices)
    if maximum == 0:
        return

    window.create_rectangle(Config.xmax * 0.71, Config.ymax * 0.77, Config.xmax * 0.75, (Config.ymax * 0.77) - (Config.ymax * ((prices[0] / maximum) / 2)), fill="green")
    tA = window.create_text(Config.xmax * 0.71, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tA, text="{}€".format(prices[0]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.76, Config.ymax * 0.77, Config.xmax * 0.80, (Config.ymax * 0.77) - (Config.ymax * ((prices[1] / maximum) / 2)), fill="red")
    tB = window.create_text(Config.xmax * 0.76, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tB, text="{}€".format(prices[1]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.81, Config.ymax * 0.77, Config.xmax * 0.85, (Config.ymax * 0.77) - (Config.ymax * ((prices[2] / maximum) / 2)), fill="yellow")
    tM = window.create_text(Config.xmax * 0.81, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tM, text="{}€".format(prices[2]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.86, Config.ymax * 0.77, Config.xmax * 0.90, (Config.ymax * 0.77) - (Config.ymax * ((prices[3] / maximum) / 2)), fill="blue")
    tO = window.create_text(Config.xmax * 0.86, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tO, text="{}€".format(prices[3]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.91, Config.ymax * 0.77, Config.xmax * 0.95, (Config.ymax * 0.77) - (Config.ymax * ((prices[4] / maximum) / 2)), fill="grey")
    tS = window.create_text(Config.xmax * 0.91, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tS, text="{}€".format(prices[4]), font=('Helvetica', '15'))

"""
draw production
"""

def     draw_prod(window, results):
    maximum = max(results)
    if maximum == 0:
        return

    window.create_rectangle(Config.xmax * 0.06, Config.ymax * 0.77, Config.xmax * 0.10, (Config.ymax * 0.77) - (Config.ymax * ((results[0] / maximum) / 2)), fill="green")
    tA = window.create_text(Config.xmax * 0.06, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tA, text="{}".format(results[0]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.11, Config.ymax * 0.77, Config.xmax * 0.15, (Config.ymax * 0.77) - (Config.ymax * ((results[1] / maximum) / 2)), fill="red")
    tB = window.create_text(Config.xmax * 0.11, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tB, text="{}".format(results[1]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.16, Config.ymax * 0.77, Config.xmax * 0.20, (Config.ymax * 0.77) - (Config.ymax * ((results[2] / maximum) / 2)), fill="yellow")
    tM = window.create_text(Config.xmax * 0.16, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tM, text="{}".format(results[2]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.21, Config.ymax * 0.77, Config.xmax * 0.25, (Config.ymax * 0.77) - (Config.ymax * ((results[3] / maximum) / 2)), fill="blue")
    tO = window.create_text(Config.xmax * 0.21, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tO, text="{}".format(results[3]), font=('Helvetica', '15'))

    window.create_rectangle(Config.xmax * 0.26, Config.ymax * 0.77, Config.xmax * 0.30, (Config.ymax * 0.77) - (Config.ymax * ((results[4] / maximum) / 2)), fill="grey")
    tS = window.create_text(Config.xmax * 0.26, Config.ymax * 0.77, anchor="nw", fill="black")
    window.itemconfig(tS, text="{}".format(results[4]), font=('Helvetica', '15'))
