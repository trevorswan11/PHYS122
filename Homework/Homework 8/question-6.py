import numpy as np
import matplotlib.pyplot as plt

# Constants
B = 2                # Tesla
A = 0.12 ** 2        # m^2
omega = 1            # rad/s
t = np.linspace(0, 7, 1000)  # Time from 0 to 7 seconds

# EMF calculation
emf = B * A * omega * np.sin(omega * t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t, emf, label=r'$\mathcal{E}(t) = 0.0288 \sin(t)$ V', color='blue')
plt.title('Induced EMF in a Rotating Square Loop')
plt.xlabel('Time (s)')
plt.ylabel('EMF (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
