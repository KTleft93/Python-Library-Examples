import ephem
# An instance of Mars location in 2021
m = ephem.Mars('2021')

#Distance between earth and mars in astronomical units
d = m.earth_distance

#Distance between the sum and mars in astronomical units
sun_d = m.sun_distance

# % of surface illuminated
phase_m = m.phase

# size of mars diameter in arcseconds
m_size = m.size

# size of mars radius as an angle
m_radius = m.radius

# the constellation mars is located in
print('\n')
print('The constellation Mars is located in 2021 is:')
print(ephem.constellation(m))
print('\n')
print('The distance of Mars in 2021 from Earth is:')
print(d)
print('\n')
print('The distance of Mars in 2021 from the Sum is:')
print(sun_d)
print('\n')
print('The percentage of Mars that is illuminated:')
print(phase_m)
print('\n')
print('The size of Mars diameter in arcseconds:')
print(m_size)
print('\n')
print('The radius of Mars as an angle:')
print(m_radius)