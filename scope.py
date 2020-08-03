import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import serial


ser = serial.Serial(port = "COM6", baudrate = 115200, timeout = 10)

n = 1000

#ignore first line
zeline = ser.readline().decode("utf-8")

#printf("vout:%6.3f vsol:%6.3f isol:%6.3f power:%6.3f duty:%6.3f\r\n", vo, v, i, p, duty);

vout = []
vsol = []
isol = []
power = []
duty = []

for i in range(n):
    if i % 10 == 0:
        print("progress:" + str(100.0 * i / n) + " %")
    zeline = ser.readline().decode("utf-8")
    
    items = zeline.split(" ")
    vout.append(float(items[1]))
    vsol.append(float(items[3]))
    isol.append(float(items[5]))
    power.append(float(items[7]))
    duty.append(float(items[9]))
    
    #print("vout:" + str(vout))
    #print(zeline, end ="")


# Data for plotting
t = np.arange(0.0, n * 0.01, 0.01)

fig, axs = plt.subplots(4)
#axs[0].plot(t, vout, label = "vout")
axs[0].plot(t, vsol, label = "vsol")
axs[0].set(xlabel='time (s)', ylabel='voltage (V)',
       title='Ze title')
#axs[0].set(ylim=(0, 12.0))       
axs[0].grid()
axs[0].legend(loc = "upper right")


axs[1].plot(t, isol, label = "isol")
axs[1].set(xlabel='time (s)', ylabel='current (A)',
       title='Ze title')
axs[1].grid()
axs[1].legend(loc = "upper right")

axs[2].plot(t, power, label = "power")
axs[2].set(xlabel='time (s)', ylabel='power (W)',
       title='Ze title')
axs[2].grid()
axs[2].legend(loc = "upper right")



axs[3].plot(t, duty, label = "duty")
axs[3].set(xlabel='time (s)', ylabel='duty (%/100)',
       title='Ze title')
axs[3].grid()
axs[3].legend(loc = "upper right")



#fig.savefig("test.png")
plt.show()