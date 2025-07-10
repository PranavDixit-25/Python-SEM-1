n = int(input("Enter the number of persons: "))
persons = {input("Enter name: "): input("Enter city: ") for _ in range(n)}
print("Names:", list(persons.keys()))
print("Cities:", list(persons.values()))
for name, city in persons.items():
    print(f"{name} lives in {city}")
from collections import Counter
city_counts = Counter(persons.values())
print("City counts:", city_counts)
