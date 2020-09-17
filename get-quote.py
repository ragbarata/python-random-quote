import random

def main():
  print("Keep it logically awesome.")

  f = open("C:\python-random-quote\quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  second = len(quotes) - 3
  rnd = random.randint(0, last)
  rnd_1 = random.randint(0, second)

  print(quotes[rnd], end='')    # O parâmetro end='' é utilizado para remover a linha em branco entre os dois prints
  print(quotes[rnd_1])

if __name__== "__main__":
  main()
