testi = int(input())
for i in range(testi):
    distinct_cities = []
    trips = int(input())
    count = 0
    for j in range(trips):
        city = str(input())
        if city not in distinct_cities:
            distinct_cities.append(city)
            count += 1
    print(count)