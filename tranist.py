
import numpy as np
import matplotlib.pyplot as plt

# Constants

R_sun = 6.957e8       # Radius of Sun in metres
R_earth = 6.378e6     # Radius of Earth in metres
R_jup = 6.991e7       # Radius of Jupiter in metres

AU = 1.496e11         # 1 AU in metres
M_sun = 1.988e30      # Mass of Sun in kg
G = 6.67e-11          # Gravitational constant (m^3 kg^-1 s^-2)

# Orbital radius range

a_range = np.linspace(0.01 * AU, 2 * AU, 500)

# Function to calculate orbital period
# Using Kepler's Third Law

def Period(a):
    P = 2 * np.pi * np.sqrt(a**3 / (G * M_sun)) / (60 * 60 * 24)
    return P  # Orbital period in days

# Function to calculate transit duration

def Transit(P, a, Rp, i):
    val = ((1 + Rp / R_sun)**2) - ((a / R_sun * np.cos(i))**2)

    # Avoid square root of negative values
    val = np.maximum(val, 0)

    T = (P / np.pi) * np.arcsin((R_sun * np.sqrt(val)) / (a * np.sin(i)))
    return T * 24  # Transit duration in hours

# Plotting

plt.figure(figsize=(8, 6))

# 1. Earth-size planet around a Sun-like star
#    Inclination = 90 degrees

Earth_inclination_deg = 90
Earth_inclination_rad = np.radians(Earth_inclination_deg)

T_vals_earth = []

for a in a_range:
    P = Period(a)
    T_vals_earth.append(Transit(P, a, R_earth, Earth_inclination_rad))

plt.plot(a_range / AU, T_vals_earth, 'b-', linewidth=2, label='Earth-size, i = 90°')

# 2. Jupiter-size planet around a Sun-like star
#    Different orbital inclinations

Jup_inclination_degrees = [90, 89.9, 89.5, 89]
line_styles = ['r--', 'g-.', 'm:', 'c-']

for i in range(len(Jup_inclination_degrees)):
    Jup_inclination_rad = np.radians(Jup_inclination_degrees[i])
    T_vals_jup = []

    for a in a_range:
        P = Period(a)
        T_vals_jup.append(Transit(P, a, R_jup, Jup_inclination_rad))

    plt.plot(a_range / AU, T_vals_jup, line_styles[i], linewidth=2, label=f'Jupiter-size, i = {Jup_inclination_degrees[i]}°')

# Plot labels and formatting

plt.xlabel("Orbital Radius (AU)", fontsize=13)
plt.ylabel("Transit Duration (Hours)", fontsize=13)

plt.title("Transit Duration vs Orbital Radius for a Sun-like Star", fontsize=15)

plt.grid(True, alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()
