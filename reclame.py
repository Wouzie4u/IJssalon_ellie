from algemene_functies import mijn_functie_2

def aanbieding_1 (smaak, prijs, korting):
    antwoord = prijs  - prijs * korting
    tekst_return = str(antwoord).replace(".",",")
    # de '.' naar ',' aanpassen heb ik teruggevonden in eerdere lessen, maar het lukt me niet om 2 getallen na de komma te krijgen
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {tekst_return} euro.")

def inkomsten_totaal(inkomsten,btw_tarief):
    totaal = 0
    for i in inkomsten:
        totaal += i
    btw_bedrag = totaal * btw_tarief
    
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst),min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    gemiddeld =  totaal / len(mijn_lijst)
    return (f"De gemiddelde inkomsten deze week zijn {gemiddeld} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])



#ik heb het argument aangepast, omdat bij het testen van de code een melding komt dat mijn_functie_2, 2 waarden moet bevatten:
#foutmelding: TypeError: mijn_functie_2() missing 1 required positional argument: 'c'


