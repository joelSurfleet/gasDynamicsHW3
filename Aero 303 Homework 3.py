# Aero 303 Homework3

from SurfleetToolbox import *

k = 1.4
R = 287 # J/(kg.K)
Cp = (k * R) / (k - 1)

# Problem 1
P1 = 0.8 * 101325 # Pa
T1 = 273 # K

q = 0.25e6 # J/kg

flow = rayleigh(k)

flow.M(0.4)

rho1 = P1 / (R * T1)

air = isentropic(k)
air.M(0.4)
air.getStag(P1,rho1,T1)

flow.getStar(P1,rho1,T1,air.P0,air.T0)

T02 = (q / Cp) + air.T0

T02ratio = (T02 / flow.T0star)

# print(T02ratio)

# Numbers from Anderson A.3
M2 = linInterp(T02ratio,0.9951,0.9973,0.92,0.94)

print()
print("Problem 1")
print("M2",M2)

flow.M(M2)

flow.getReal(flow.Pstar,flow.rhostar,flow.Tstar,flow.P0star,flow.T0star)

print("P2",flow.P,"Pa")
print("T2",flow.T,"K")
print("rho2",flow.rho,"kg/m**3")
print("P02",flow.P0,"Pa")
print("T02",flow.T0,"K")

# Problem 2
P1 = 100000 # Pa
T1 = 300 # K

q = 0.50e6 # J/kg

flow.M(0.2)

rho1 = P1 / (R * T1)

air.M(0.2)
air.getStag(P1,rho1,T1)

flow.getStar(P1,rho1,T1,air.P0,air.T0)

T02 = (q / Cp) + air.T0

T02ratio = (T02 / flow.T0star)

# print(T02ratio)

# Numbers from Anderson A.3
M2 = linInterp(T02ratio,0.4572,0.4935,0.36,0.38)

print()
print("Problem 2")
print("M2",M2)

flow.M(M2)

flow.getReal(flow.Pstar,flow.rhostar,flow.Tstar,flow.P0star,flow.T0star)

print("P2",flow.P,"Pa")
print("T2",flow.T,"K")
print("rho2",flow.rho,"kg/m**3")
print("P02",flow.P0,"Pa")
print("T02",flow.T0,"K")

# Problem 3
M1 = 0.6
P1 = 150e3 # Pa
T1 = 300 # K

rho1 = P1 / (R * T1)

f = 0.005
L = 0.45 # m
D = 0.03 # m

flow = fanno(1.4)

flow.M(0.6)
air.M(0.6)
air.getStag(P1,rho1,T1)
flow.getStar(P1,rho1,T1,air.P0)

fL4D1 = flow.fL4D

fL4D = (4 * f * L) / D

fL4D2 = fL4D1 - fL4D

print()
print("Problem 3")
# print(fL4D2)

M2 = linInterp(fL4D2,0.2081,0.1721,0.7,0.72)

print("M2",M2)

flow.M(M2)
flow.getReal(flow.Pstar,flow.rhostar,flow.Tstar,flow.P0star)

print("P2",flow.P,"Pa")
print("T2",flow.T,"K")

# Problem 4

V1 = 100 # m/s
T1 = 400 # k
HV = 40e6 # J/kg

a = (k * R * T1) ** (1/2) # m/s

M1 = V1/a

print(M1)

air.M(M1)
air.getStag(1,1,T1)

flow = rayleigh(k)
flow.M(M1)
flow.getStar(1,1,1,1,air.T0)

mDotRatio = (Cp * (flow.T0star - air.T0) / HV)

print()
print("Problem 4")
print("Fuel to Air Ratio",mDotRatio)

qMax = Cp * (flow.T0star - air.T0)

print("Max Heat Addition",qMax,"J/kg")

mDotRatio10 = mDotRatio * 1.1

T0star = (mDotRatio10 * HV) / Cp + air.T0

T0ratio = air.T0/T0star

M2 = linInterp(T0ratio,0.2057,0.2395,0.22,0.24)
# from tables

air10 = isentropic(k)
air10.M(M2)
flow10 = rayleigh(k)
flow10.M(M2)

mDotRatio2 = M2/M1 * air10.Pratio/air.Pratio

percentDiff = (1 - mDotRatio2) * 100

print("Percent Decrease",percentDiff,"%")