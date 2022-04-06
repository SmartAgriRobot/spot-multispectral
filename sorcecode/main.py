from time import sleep
import board
from sspectral_lib import AS7341

import matplotlib.pyplot as plt
from matplotlib import animation

def bar_graph(read_value):
	scaled = int(read_value / 1000)
	return "%d" % read_value + (scaled * "")

def barlist():
	spectral_val	= [int(bar_graph(sensor.channel_415nm)),
			int(bar_graph(sensor.channel_445nm)),
			int(bar_graph(sensor.channel_480nm)),
			int(bar_graph(sensor.channel_515nm)),
			int(bar_graph(sensor.channel_555nm)),
			int(bar_graph(sensor.channel_590nm)),
			int(bar_graph(sensor.channel_630nm)),
			int(bar_graph(sensor.channel_680nm)),
			int(bar_graph(sensor.channel_clear)),
			int(bar_graph(sensor.channel_nir))
			]
	#print(spectral_val)
	plt.ylim(0, max(spectral_val))
	return spectral_val

def animate(i):
	y=barlist()
	for i, b in enumerate(barcollection):
		b.set_height(y[i])
		
i2c = board.I2C()
sensor = AS7341(i2c)

sensor.led = False
sleep(0.5)
sensor.led_current = 5
sensor.led = True

fig=plt.figure()
plt.title('Spectral Sensor')

x=['415', '445', '480', '515', '555', '590', '630', '680', 'Clear', 'NIR']
barcollection = plt.bar(x,barlist(),color=['violet', 'indigo', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red', 'black', 'black'])

anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,
                             interval=10)

plt.show()
