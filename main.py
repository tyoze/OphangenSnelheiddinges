import random

trager = 0
braaf = 0
straf_1 = 0
straf_2 = 0
straf_3 = 0

def snelheid(verplaatsing, tijd = 1):
   return verplaatsing/tijd

def straf(snelheid_auto):
  if snelheid_auto <= 50:
      print("Proficiat u rijdt,", round(snelheid_auto, 2), "dit is niet te snel.\n")
      global braaf
      braaf += 1

  elif snelheid_auto > 50 and snelheid_auto <= 55:
      print("U rijdt,", round(snelheid_auto, 2), "gelieve te vertragen.\n")
      global trager
      trager += 1

  elif snelheid_auto > 55 and snelheid_auto <= 65:
      print("U rijdt,", round(snelheid_auto, 2), "u krijgt een boete van 50 euro.\n")
      global straf_1
      straf_1 += 1

  elif snelheid_auto > 65 and snelheid_auto <= 80:
      print("U rijdt,", round(snelheid_auto, 2), "u krijgt een boete van 250 euro.\n")
      global straf_2
      straf_2 += 1

  elif snelheid_auto > 80:
      print("U rijdt,", round(snelheid_auto, 2), "u wordt opgehangen.\n")
      global straf_3
      straf_3 += 1

for _ in range(50):
  tijd = random.randint(100, 500)
  verplaatsing = random.randint(10000, 20000)
  straf(snelheid(verplaatsing, tijd))

tot = braaf + trager + straf_1 + straf_2 + straf_3

s = """{} zijn braaf.
{} moeten een beetje trager rijden.
{} moeten 50 euro boete betalen.
{} moeten 250 euro boete betalen.
{} moeten DOOD!!!""".format(braaf, trager, straf_1, straf_2, straf_3)

print("""STATS VAN DE DAG:""",s,'TOT CARS:',tot,sep='\n')
