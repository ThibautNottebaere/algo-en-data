def hanoi_solver(n,A,C,B,stappen):
    if n == 1:
        stappen[0] += 1
        print(f"Schijf {n} van {A} naar {C}")
    else:
        hanoi_solver(n-1,A,B,C,stappen)
        stappen[0] += 1
        print(f"Schijf {n} van {A} naar {C}")
        hanoi_solver(n-1,B,C,A,stappen)
def hanoi(n):
    stappen = [0]
    hanoi_solver(n,'A','C','B',stappen)
    print(f"{stappen[0]} stappen gedaan")


#Kzou zeggen tekent het eens uit op een blad papier:
#N = 1
#Je verplaatst gewoon één schijf: van de bron (A) naar het doel (C).
#N = 2
#Je wilt eigenlijk twee keer het N=1 principe toepassen.
#Eerst schijf 1 van A naar B (N=1, maar met doel B). Pas derna kun je schijf 2 van A naar C brengen en tot
#slot verplaats je schijf 1 van B naar C (weer N=1), zo heb je N=2 uitgevoerd.
#N = 3
#Voor drie schijven wil je in essentie eerst N=2 uitvoeren, ma nu van A naar B voordaje schijf 3
#van A naar C kunt verplaatsen.
#Je herhaalt dus dezelfde stappen als bij N=2, ma dit keer met: bron: A, doel: B, hulppaal: C
#Da betekent: schijf 1 van A naar C, schijf 2 van A naar B, schijf 1 van C naar B
#Nu hebje N=2 voltooid, ma dan van A naar B (omdat je in de context van N=3 werkt)
#Daarna schijf 3 van A naar C.
#Tot slot moeje opnieuw N=2 uitvoeren, ma dit keer van B (waar schijf 1 en 2 liggen) naar C, met A als
# hulppaal: schijf 1 van B naar A, schijf 2 van B naar C, schijf 1 van A naar C