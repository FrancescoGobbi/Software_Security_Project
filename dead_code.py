import random

candidate_lines = ['while', 'for', 'def', 'if ']

def start(source_path):
    # apro il file da offuscare
    source = open(source_path, "r")
    output = open('./result/output.py', 'w') #creo il risultato 

    lines = source.readlines() #leggo tutte le righe del file aperto

    #indica se le variabili del codice morto sono state inizializzate
    dead_code_variables_is_inizialized = False

    # variabile che indica se sono in un blocco di commenti
    comment = False

    value = ('\t', ' ', '', '\n')

    for line in lines:

        # Verifico se sto entrando in un blocco di commento
        if '"""' in line or "'''" in line:
            # se il blocco non inizia e termina sulla stessa riga, allora imposto comment=True per indicare che sono entrato nel blocco,
            # la variabile comment sarà riportata a False quando verrà trovata la fine del blocco (ovvero la stringa '""""')
            if line.count('"""') or line.count("'''")!= 2:
                comment = not comment #quindi diventa True se sono in un blocco di commento
        else:
            # Se non sono in un blocco di commento
            if comment == False:

                # verifico se ci sono commenti sulla riga, e in tal caso prendo solo la parte di stringa che lo precede
                if '#' in line: #così tolgo i commenti all'attaccante!
                    line = line[:line.find('#')] #dall'inizio della riga al commento escluso

                # verifico che line non sia vuota
                if line != '':
                    # verifico che la line non inizi con spazi o tabulazioni (ovvero non sia nello scope di un costrutto)
                    if (not line[0] == ' ') and (not line[0] == '\t') and is_candidate(line):

                        #se le variabili del codice morto non sono ancora state inizializzate le inizializzo
                        if dead_code_variables_is_inizialized == False:
                            inizialize_dead_code_variables(output) #scrivere le variabili del dead-code nel file di output
                            #indico che le variabili del dead_code sono state inizializzate
                            dead_code_variables_is_inizialized = True
                        
                        choice1 = random.randint(0, 1)
                        #choice1 
                        #0 = inserisco il dead code prima e dopo la line candidata
                        #1 = inserisco il dead code o solo prima o solo dopo la linea candidata                        
                        if choice1 == 0:
                            insert_dead_code(output) #inserisco il dead_code prima
                            #print(line)
                            output.write('\n' + line ) #metto la riga candidata
                            #insert_dead_code_with_tab(output) #inserisco il dead code dopo con tabulazione
                        
                        else: #choice1 == 1
                            insert_dead_code(output)
                            output.write('\n' + line) #vado a capo e riscrivo la riga nell'output
                            '''choice2 = random.randint(0, 1)
                            #choice2
                            #0 = inserisco il codice prima della line candidata
                            #1 = inserisco il codice dopo la line candidata

                            if choice2 == 0:
                                insert_dead_code(output) #inserisco il dead_code prima
                                output.write('\n' + line) #metto la riga candidata
                            else:
                                output.write(line) #metto la riga candidata
                                insert_dead_code_with_tab(output) #inserisco il dead code dopo con tabulazione
                        '''

                        # inserisco il codice morto
                        #insert_dead_code(output)
                        #output.write('\n' + line) #vado a capo e riscrivo la riga nell'output
                        ''' Inserire il discorso del lancio della moneta per definire se mettere il dead_code prima o dopo la riga
                        del codice in sè '''

                    # se sono nello scope di un costrutto oppure line non è una riga candidata
                    else:

                        # verifico che line non sia fatta solo da spazi e tabulazioni
                        if any(c not in value for c in line):
                            # scrivo la line in output
                            output.write(line)
    output.write('\n')
    choice = random.randint(1,10)
    for i in range(1,choice):
        insert_dead_code(output) #inserisco un altro dead_code alla fine del file!

    #chiusura dei file
    output.close()
    source.close()

# funzione che aggiunge codice morto
def insert_dead_code(output):
    # seglie a random un file tra trash_code_(number).py1
    choice = random.randint(1,10)
    ran = random.randint(1, 15) #scenta random del file
    dead_code = open('./Trashcode_New/trash_code_' + str(ran) + '.py', 'r')
    for i in range(1,choice):
        
        ran = random.randint(1, 15) #scenta random del file
        dead_code = open('./Trashcode_New/trash_code_' + str(ran) + '.py', 'r')

        # inserisce il file dead_code_x.py nel file output.py
        for line in dead_code.readlines():
            output.write(line)
        
        output.write('\n')

    dead_code.close()

def inizialize_dead_code_variables(output):

    dead_code_variables = open('./Trashcode_New/trash_code_Variable.py', 'r')
    # inizializzo le variabili del codice morto
    for line in dead_code_variables: #quindi aggiungo al mio file di output tutto le variabili contenute nei vari dead code
        #indipendentemente da quale andrò ad usare
        output.write(line)
    output.write('\n')

# funzione che veriifica se la riga è una riga candidata
def is_candidate(source_string):
    for line in candidate_lines: #rispetto alle righe candidate sopra
        if line in source_string: #se nella riga passata c'è una parola tra quelle candidate!
            return True

    return False
