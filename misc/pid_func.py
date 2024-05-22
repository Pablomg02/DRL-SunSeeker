import matplotlib.pyplot as plt
import numpy as np

threshold = 255

def getfunc(kp):
    xvalues = np.arange(-180, 181, 1)
    yvalues = np.zeros(len(xvalues))

    for i in range(len(xvalues)):
        error = xvalues[i] * kp
        if error > threshold:
            yvalues[i] = threshold
        elif error < -threshold:
            yvalues[i] = -threshold
        else:
            yvalues[i] = error

    return xvalues, yvalues


for i in range(1, 6):
    output1, output2 = getfunc(i)
    plt.plot(output1, output2)

plt.xlabel("Angle")
plt.ylabel("Output")
plt.legend( ["Kp=1", "Kp=2", "Kp=3", "Kp=4", "Kp=5"])
plt.title("PID Output (Limited to 255 and -255)")
plt.show()