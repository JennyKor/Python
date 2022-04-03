##Jenny Korkeamäki
##ika = int(input("Anna ikäsi:"))

def tarkista_ika(ika):
    if ika < 18:
        return "Olet lapsi"
        
    if ika >= 18 and ika < 70:
        return "Olet aikuinen"

    if ika >= 70:
        return "Olet eläkeläinen"


##result = tarkista_ika(ika)
##print(result)
