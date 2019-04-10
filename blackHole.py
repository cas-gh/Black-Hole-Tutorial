from decimal import Decimal
from math import sqrt


#### CONSTANTS ####
G = 6.674 * 10**-11 # in m^3 * kg^-1 * s^-2
c = 299792458       # in m/s

def blackHole():
    # Uses formula for Schwarzschild radius to give size of
    # black hole, photon sphere, 
    M = input("Enter a mass in kg: ")
    rs = (2 * G * float(M)) / c**2
    photonRad = 1.5 * rs
    ve = sqrt((2 * G * float(M)) / rs)

    rounded_pR = '%.2E' % Decimal(str(photonRad))
    rounded_rs = '%.2E' % Decimal(str(rs))
    rounded_ve = '%.2E' % Decimal(str(ve))

    print("The Schwarzschild radius of your black hole would be: " + rounded_rs + " meters.")
    print("The radius of the photon sphere would be: " + rounded_pR + " meters.")
    print("Escape velocity at the Schwarzschild radius is: " + rounded_ve + "m/s.")

if __name__ == '__main__':
    blackHole()
