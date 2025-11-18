numlist = [ 100, 101, 0, "103", 104 ]


try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print("Fout: Ongeldige invoer, geef een geheel getal op.")
except IndexError:
    print("Fout: Index buiten bereik van de lijst.")
except ZeroDivisionError:
    print("Fout: Delen door nul is niet toegestaan.")
except TypeError:
    print("Fout: Kan niet delen door een niet-numerieke waarde.")