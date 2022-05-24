
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


  
  def wynik(self):
    emerytalna = self.wynagrodzenie_brutt* 0.0976
    rentowa = self.wynagrodzenie_brutt * 0.065
    wypadkowa = self.wynagrodzenie_brutt * 0.0195
    fp = self.wynagrodzenie_brutt * 0.0245
    FGŚP = self.wynagrodzenie_brutt * 0.001
    pracodawca_koszt = round(self.wynagrodzenie_brutt + emerytalna + rentowa + wypadkowa + fp + FGŚP, 2)

    #Tu jest liczona kwota wynagrodzenia netto
    do_odliczenia = self.wynagrodzenie_brutt * 0.23
    kwota_netto = round(self.wynagrodzenie_brutt - do_odliczenia, 2)

  
    print(f'{self.imie} {kwota_netto} {pracodawca_koszt}')
  


for n in range(0,len(second_values)):
  x = first_values_str[n]
  y = second_values[n]
  instance = Pracownik(x,y)
  instance.wynik()

  
'''
person1 = Pracownik("Kuba", 3000)
print(person1.koszt_pracdawcy())
print(person1.netto())
'''