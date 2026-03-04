def find_starting_city(distances, fuel, mpg):
    n = len(distances)              # number of cities
    miles_remaining = 0             # current fuel balance
    candidate = 0                   # possible starting city

    for i in range(n):              # loop through cities
                                    # fuel gained - distance traveled
        miles_remaining += fuel[i] * mpg - distances[i]

        if miles_remaining < 0:     # not enough fuel
            candidate = i + 1       # next city becomes candidate
            miles_remaining = 0     # reset fuel balance

    return candidate                # return valid start city


city_distances = [5, 25, 15, 10, 15]
fuel           = [1,  2,  1,  0,  3]
mpg            = 10

result = find_starting_city(city_distances, fuel, mpg)
print(f"Preferred starting city: {result}")   # print result