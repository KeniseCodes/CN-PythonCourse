'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
pi = 3.14159265359
radius = 3.14
height = 5
volume = pi * radius**2 * height
sf_area = (2 *pi * radius * height) + (2 * pi * radius**2)
print(volume, sf_area)
