while True:
    liczba = int(input("podaj liczbę dodatnią, zero kończy: "))
    if liczba == 0: #warunek wyjścia z pętli
        break
    if liczba < 0:
        print("miała być dodatnia...")
        continue
    print("  .....przetwarzanie")
print("Koniec")
