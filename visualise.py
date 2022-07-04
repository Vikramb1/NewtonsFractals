import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider
import bokeh

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

min, max = -2, 2
step = 0.01

def cmp(x,y):
    return x + 1j * y

def newton(val, it, roots):
    eq = np.polynomial.polynomial.polyfromroots(roots)
    der = np.polyder(eq)
    li = 0
    still_going = np.zeros(val.shape)
    for i in range(it):
        li = val
        val = val - np.polyval(eq,val)/np.polyval(der,val)
        converged = np.invert(abs(val-li) < 0.0000001)
        still_going[converged] = i
    return still_going

fig, ax = plt.subplots()

a = np.arange(min,max+step,step)
b = np.arange(min,max+step,step)
x, y = np.meshgrid(a, b)

roots = [cmp(1,0), cmp(-0.5,math.sqrt(3)/2),cmp(-0.5,-math.sqrt(3)/2)]
eq = np.polynomial.Polynomial.fromroots(roots)
der = eq.deriv()

ax.imshow(newton(cmp(x,y), 20, roots), cmap = 'inferno')

ax_slider = plt.axes([0.20, 0.01, 0.65, 0.03], facecolor='yellow')
slider = Slider(ax_slider, 'Root 1 real part', valmin=-2, valmax=2)

def update(val):
    roots[0] = cmp(val,roots[0].imag)
    ax.imshow(newton(cmp(x,y), 20, roots), cmap = 'inferno')
    fig.canvas.draw_idle()

slider.on_changed(update)  
plt.show()