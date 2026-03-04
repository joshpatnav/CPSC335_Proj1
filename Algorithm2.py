
def find_starting_city(distances, fuel, mpg):
    n = len(distances)
    miles_remaining = 0
    candidate = 0

    for i in range(n):
        miles_remaining += fuel[i] * mpg - distances[i]

        if miles_remaining < 0:
            candidate = i + 1
            miles_remaining = 0

    return candidate

city_distances = [5, 25, 15, 10, 15]
fuel           = [1,  2,  1,  0,  3]
mpg            = 10

result = find_starting_city(city_distances, fuel, mpg)
print(f"Preferred starting city: {result}")  
