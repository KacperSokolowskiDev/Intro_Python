# Tuples are immutable, mostly used for data that's not changed

coordinates = (4, 5)
coordinates[1] = 10  # Will throw an error because tuples are immutable
print(coordinates[0])
