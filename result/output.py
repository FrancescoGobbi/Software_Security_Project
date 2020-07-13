def PromessiSposi(x, y):
    while x>y:
        y = y + 1

    if y>x:
        x = x + 5
        y = y + 5
    

def Università(Indirizzo):
    if Indirizzo>=10:
        Indirizzo = Indirizzo + 10
    else:
        Indirizzo = Indirizzo + 2
    

def William(Romeo,Giulietta):
    if Romeo > Giulietta:
        Giulietta = Giulietta + 5

    else:
        Romeo = Romeo + 5


#variabili
Sicurezza = 10
Visual = 10
Embedded = 10

Univr = 10
Didattica = 10
Progetto = 10

Riccardo = 10
Francesco = 10

Giulietta = 10
Romeo = 10
Montecchi = 10
Balcone = 0

def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
Riccardo = 5
Francesco = 3

i = 0
while i<Riccardo:
    Francesco = Francesco + 1
    i = i + 1

Riccardo+=5

def qualcosa(n):
	if n==1 :
		return 1
	if n==2 :
		return 1
	return qualcosa(n-1) + qualcosa(n-2)
fib_gen = fib()
for _ in range(10):
    next(fib_gen)
if Univr >= 10:
    if Visual >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Balcone == 1:
    Giulietta = 0
else:
    Giulietta = 20
if Romeo > Giulietta:
    PromessiSposi(Giulietta, Romeo)
else:
    William(Romeo, Giulietta)
if Univr >= 10:
    if Embedded >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Sicurezza > Visual:
    Univr = Univr + 3
else:
    Unvir = Univr - 5

if Univr >= 10:
    Sicurezza = Sicurezza + 1
    Visual = Visual + 3
    Embedded = Embedded + 3 
if Univr >= 10:
    if Embedded >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Univr >= 10:
    if Embedded >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Univr >= 10:
    if Sicurezza >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Sicurezza > Embedded:
    Univr = Univr + 3
else: 
    Univr = Univr - 10
Università(Sicurezza)

if Univr>=10:
    Sicurezza = Sicurezza + 1
    Embedded = Embedded + 1
    Visual = Visual + 1  
if Univr >= 10:
    if Sicurezza >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Univr >= 10:
    if Embedded >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
UniVr = 10
Didattica = 5
Progetto = 0

if UniVr >= Didattica:
    if Riccardo > Francesco:
        if Romeo > Giulietta:
            Progetto = 1
        
        else:
            Progetto = 2
    else:
        Progetto = 3
else:
    Progetto = 4
if Univr >= 10:
    if Visual >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Montecchi > 10:
    Romeo = 0
else:
    Romeo = 20
if Riccardo >= Francesco:
    PromessiSposi(Riccardo, Francesco)
else:
    PromessiSposi(Francesco, Riccardo)
if Montecchi > 10:
    Romeo = 0
else:
    Romeo = 20
if Balcone == 1:
    Giulietta = 0
else:
    Giulietta = 20
if Sicurezza > Visual:
    Univr = Univr + 3
else:
    Unvir = Univr - 5

if Univr >= 10:
    Sicurezza = Sicurezza + 1
    Visual = Visual + 3
    Embedded = Embedded + 3 
if Riccardo >= Francesco:
    PromessiSposi(Riccardo, Francesco)
else:
    PromessiSposi(Francesco, Riccardo)
UniVr = 10
Didattica = 5
Progetto = 0

if UniVr >= Didattica:
    if Riccardo > Francesco:
        if Romeo > Giulietta:
            Progetto = 1
        
        else:
            Progetto = 2
    else:
        Progetto = 3
else:
    Progetto = 4
if Sicurezza > Embedded:
    Univr = Univr + 3
else: 
    Univr = Univr - 10
if Balcone == 1:
    Romeo = 20
else:
    Romeo = 0
Università(Sicurezza)

if Univr>=10:
    Sicurezza = Sicurezza + 1
    Embedded = Embedded + 1
    Visual = Visual + 1  
if Univr >= 10:
    if Sicurezza >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
UniVr = 10
Didattica = 5
Progetto = 0

if UniVr >= Didattica:
    if Riccardo > Francesco:
        if Romeo > Giulietta:
            Progetto = 1
        
        else:
            Progetto = 2
    else:
        Progetto = 3
else:
    Progetto = 4
if Univr >= 10:
    if Embedded >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Univr >= 10:
    if Sicurezza >= 5:
        Univr = Univr + 1
    else:
        Univr = Univr - 2
    
if Montecchi >= 10:
    Romeo-=2
    Giulietta-=1

else:
    Romeo+=Giulietta
if Balcone == 1:
    Giulietta = 0
else:
    Giulietta = 20
UniVr = 10
Didattica = 5
Progetto = 0

if UniVr >= Didattica:
    if Riccardo > Francesco:
        if Romeo > Giulietta:
            Progetto = 1
        
        else:
            Progetto = 2
    else:
        Progetto = 3
else:
    Progetto = 4
if Montecchi > 10:
    Romeo = 0
else:
    Romeo = 20
if Balcone == 1:
    Giulietta = 0
else:
    Giulietta = 20
Università(Sicurezza)

if Univr>=10:
    Sicurezza = Sicurezza + 1
    Embedded = Embedded + 1
    Visual = Visual + 1  
UniVr = 10
Didattica = 5
Progetto = 0

if UniVr >= Didattica:
    if Riccardo > Francesco:
        if Romeo > Giulietta:
            Progetto = 1
        
        else:
            Progetto = 2
    else:
        Progetto = 3
else:
    Progetto = 4
if Romeo > Giulietta:
    PromessiSposi(Giulietta, Romeo)
else:
    William(Romeo, Giulietta)
if Sicurezza > Embedded:
    Univr = Univr + 3
else: 
    Univr = Univr - 10
