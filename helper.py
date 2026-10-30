def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    try:
        bedrag_pp = bedrag / personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag aan fooien per persoon is {bedrag_pp} euro."

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(ijs_soorten):
    uitkomst = 0
    for v in ijs_soorten.values():
         uitkomst += v
    return uitkomst    








