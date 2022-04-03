##Jenny Korkeamäki
def LueSivut(sivu1, sivu2, sivu3):
    if sivu1 == sivu2 == sivu3:
        return "tasasivuinen"
    
    if sivu1 == sivu2 or sivu1 == sivu3 or sivu2 == sivu3:
        return "tasakylkinen"

    if sivu1 != sivu2 != sivu3:
        return "epäsäännöllinen"
