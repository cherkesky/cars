showroom = set()
showroom.add("Mazda")
showroom.add("Subaru")
showroom.add("BMW")
showroom.add("Fisker")
showroom.add("Fisker")

print(len(showroom))

moreCars = {"Mercedes Benz", "Dacia"}
showroom.update(moreCars)
showroom.discard("BMW")
print(f'Showroom {showroom}')

junkyard = {"Hyundai", "Renualt", "Citruen", "Subaru", "Mazda", "Fisker"}
print(f'Junkyard {junkyard}')

intersectionCars = showroom.intersection(junkyard)
print (f'Cross Inventory{intersectionCars}')

showroom.discard("Mazda")
print(f'Showroom2 {showroom}')
