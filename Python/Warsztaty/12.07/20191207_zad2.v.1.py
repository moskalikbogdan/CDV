"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

Liczby={"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6,

       "siedem":7, "osiem":8, "dziewięć":9, "dziesięć":10, "jedenaście":11,

       "dwanaście":12, "trzynaście":13, "czternaście":14, "piętnaście":15,

       "szesnaście":16, "siedemnaście":17, "osiemnaście":18,

 "dziewiętnaście":19, "dwadzieścia":20, "trzydzieści":30,

 "czterdzieści":40, "pięćdziesiąt":50}

   
slownie=input("Wpisz słownie liczbę od 1 do 59>")
sl1 = slownie[:slownie.index(' ')]
sl2 = slownie[slownie.index(' ')+1:]
print(sl1)
print(sl2)
print ("Liczba w zapisie cyframi to:", Liczby[sl1] + Liczby[sl2])