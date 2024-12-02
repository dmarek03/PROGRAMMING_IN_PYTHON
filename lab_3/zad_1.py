# 1. Iterator - przypomnienie
# Iterator to obiekt zawierający policzalną liczbę wartości po którym można iterować, co oznacza że
# można przechodzić przez wszystkie wartości.
# W Pythonie iterator to obiekt, który zawiera metody __iter__() i __next__().
# Przykład:

lista = ["ala","ola", "ula"]
myit = iter(lista)
print(next(myit))
print(next(myit))
print(next(myit))