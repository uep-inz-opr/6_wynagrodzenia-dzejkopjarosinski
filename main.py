
i = int(input())

  
lista = []
for x in range(i):
  inputowanie  = list(input().split()) # Tu zawsze w stringach
  lista = lista + inputowanie
  
second_values = lista[1::2]
for z in range(0,len(second_values)):
  second_values[z] = int(second_values[z])

  
first_values_str = lista[::2]
new_list = []

for y in range(0,len(second_values)):
  el_first_values_str = first_values_str[y]
  el_second_values = second_values[y]
  new_list.append(el_first_values_str)
  new_list.append(el_second_values)


class Pracownik:

    def __init__(self, imie, wynagrodzenie_brutt):
      self.imie = imie 
      self.wynagrodzenie_brutt = wynagrodzenie_brutt


    def oblicz_emerytalna(self):
      return round(0.0976 * self.wynagrodzenie_brutt, 2)
    
    def oblicz_rentowa(self, procent):
      return round(procent/100 * self.wynagrodzenie_brutt,2)


    
    
    def netto(self) -> float:
      emerytalna = self.oblicz_emerytalna()
      rentowa = self.oblicz_rentowa(1.5)
      chorobowa = round(self.wynagrodzenie_brutt * 0.0245, 2)
      sk = round(emerytalna + rentowa + chorobowa, 2)
      ubez_społeczne = round(emerytalna+chorobowa+rentowa,2)
      podstawa_na_zdrowotne = round(self.wynagrodzenie_brutt - ubez_społeczne,2)
      zdrowotne_z_wynagrodzenia = round(0.09 * podstawa_na_zdrowotne, 2)
      zdrowotne_z_podatku = round(0.0775*podstawa_na_zdrowotne,2)
      koszty_uzyskania_przychodu = 111.25
      podstawa_zaliczki_na_dochodowy = round(self.wynagrodzenie_brutt - koszty_uzyskania_przychodu - sk, 0)
      zaliczka_na_dochodowy_przed_zdrowotna = round(round(0.18*podstawa_zaliczki_na_dochodowy,2) - 46.33, 2)
      zaliczka_na_dochodowy_pobranie = round(zaliczka_na_dochodowy_przed_zdrowotna - zdrowotne_z_podatku,0)
      kwota_do_wyplaty = round(self.wynagrodzenie_brutt - ubez_społeczne - zdrowotne_z_wynagrodzenia - zaliczka_na_dochodowy_pobranie, 2)
      return kwota_do_wyplaty
      
      

      
    def skladki_pracodawcy(self) -> float:
      sk_emerytalna = self.oblicz_emerytalna()
      sk_rentowa = self.oblicz_rentowa(6.5)
      sk_wypadkowa = round(self.wynagrodzenie_brutt*0.0193, 2)
      sk_FP = round(self.wynagrodzenie_brutt*0.0245, 2)
      FGŚP = round(self.wynagrodzenie_brutt*0.001, 2)
      sk_pracodawcy = round(sk_emerytalna + sk_rentowa + sk_wypadkowa + sk_FP + FGŚP, 2)
      return sk_pracodawcy


    def koszt_pracodawcy(self) -> float:
      koszt_pracodawcy = round(self.wynagrodzenie_brutt + self.skladki_pracodawcy(),2)
      return koszt_pracodawcy




for n in range(0,len(second_values)):
  x = first_values_str[n]
  y = second_values[n]
  instance = Pracownik(x,y)
  print(f'{instance.imie} {instance.netto()} {instance.skladki_pracodawcy()} {instance.koszt_pracodawcy()}')

  
'''
person1 = Pracownik("Kuba", 3000)
print(person1.koszt_pracdawcy())
print(person1.netto())
'''