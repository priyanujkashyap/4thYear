import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.extras import average
from scipy.interpolate import make_interp_spline
from scipy.optimize import curve_fit

# Data section


conc = [98.44,96.88,93.75,87.5,75.0,50.0, 25.0, 12.5, 6.25, 3.125, 1.5625, 0.78125]

Absorbance= [ 0.310,0.310,0.309,0.308,0.304,0.296, 0.288 , 0.285 , 0.283 , 0.282  ,0.281 , 0.280   ]

wavelengths  = [400, 420, 440, 460, 480, 500, 560, 580, 600, 620, 640, 660, 680, 700,720, 740, 760, 780, 800, 820, 840, 860, 880, 900]

Transmittance= [31.0, 31, 31, 31, 31, 31, 31.2, 31.9, 42.5, 59.2, 75.6, 86.3, 95.5, 95.2, 80.1, 59.2, 50.4, 64.5, 82.7, 93.9, 96, 92.1, 83, 70.4]


print(len(wavelengths),len(Transmittance))

log_errors = 0.02 / np.log10(Absorbance)  # +1 ensures denominator > 0
log_errors = np.clip(log_errors, 0.001, 0.1)  # Constrain between reasonable bounds


plt.subplot(2, 1, 2)
findgen = np.linspace(0, 100, 1000)
curve = np.poly1d(np.polyfit(conc,Absorbance, 1))
#print('the slope and intercept',(np.polyfit(conc,Absorbance, 1)[0])/(0.01))
plt.scatter(conc,Absorbance,color='#cc241d') # my points
plt.plot(findgen, curve(findgen),  color='#282828') # The curve of best fit
plt.title("Beer Lamberts Law",family='Latin Modern Roman',size=18)
plt.xlabel("Concentration %",family='Latin Modern Roman',size=12)
plt.ylabel("Absorbance",family='Latin Modern Roman',size=12)
plt.grid(True)
plt.subplot(2, 1, 1)
grid2= np.linspace(400, 900, 1000)
plt.scatter(wavelengths,Transmittance,color='#cc241d')
spline = make_interp_spline(wavelengths,Transmittance)
abspec=spline(grid2)
plt.plot(grid2,abspec, color='#282828')
#plt.errorbar(wavelengths,Transmittance, yerr=0.4, fmt='none', ecolor='gray', elinewidth=0.8, capsize=3, alpha=0.7, zorder=2)
plt.annotate('local absorption maxima', xy=(760,50.4), xytext=(770, 35),
             arrowprops=dict(arrowstyle='->', color='red'),family='Latin Modern Roman',size=10)
print(len(abspec),len(grid2))
plt.title('Absorption spectra',family='Latin Modern Roman',size=18)
plt.xlabel('$ \\lambda $ in nm',family='Latin Modern Roman',size=12)
plt.ylabel('Transmittance %',family='Latin Modern Roman',size=12)
plt.grid(True)


plt.show()
