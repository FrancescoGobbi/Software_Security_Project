import dead_code
import generate_equivalent_instructions_sequence as gen
import obfuscate_variable as ov
import obfuscate_function as of
import replace_constants as rc
import sys
import getopt
import os
from staticfg import CFGBuilder
from fpdf import FPDF

def main(argv):

    if len(argv) == 0: #se non ho passato nulla è un errore
        #print('Error: invalid use.')
        #print('python3.6 pythonCowObfuscator.py <source.py>')
        #sys.exit(2)
        raise IOError( 'Error: invalid use. Please use : "python3.6 pythonCowObfuscator.py <source.py>" ' )

    try:
        opt, arg = getopt.getopt(argv, " ", ["idir="])
    except getopt.GetoptError:
        #print('Error: invalid use.')
        #print('python3.6 pythonCowObfuscator.py <source.py>')
        #sys.exit(2)
        raise IOError( 'Error: invalid use. Please use : "python3.6 pythonCowObfuscator.py <source.py>" ' )

    source = arg[0] #Nome del file passato

    #check se il file è un file .py 
    extension = os.path.splitext(source)[1]  #take extension of file
    
    if (extension != ".py") :
        raise IOError( 'Invalid input file. Please enter python file' )
    
    #check il file è nella cartella
    if os.path.isfile(source):
        print ("File exist")
    else:
        raise IOError( 'File not exist' )

    # create dir result if not exists
    if not os.path.exists('result'):
        os.makedirs('result')

    # 0) create cfg
    cfg = CFGBuilder().build_from_file('Before_Obfuscate', source)
    a = cfg.build_visual('CFG/Before_Obfuscate', format='pdf', calls=True)

    # 1) dead code
    dead_code.start(source)

    # 1.1) create cfg
    cfg = CFGBuilder().build_from_file('After_Insertion_Dead_Code', './result/output.py')
    a = cfg.build_visual('CFG/After_Insertion_Dead_Cod', format='pdf', calls=True)

    '''# 2) gen sequence
    source = './result/output.py' #Apro l'output che ho creato prima nel dead code
    with open('./result/result1.py', 'w') as res: #creo il primo risultato
        for line in gen.replace_instructions(source): #nel file "generate_equivalent_instructions_sequence.py"
            res.write(line)

    # 3) replace constants
    source = './result/result1.py'
    with open('./result/result2.py', 'w') as res:
        for line in rc.replace_constants(source):
            res.write(line)
    # 4) replace variables
    source = './result/result2.py'
    with open('./result/result3.py', 'w') as res:
        lines,dic = ov.obfuscate(source)
        for line in lines:
            res.write(line)

    # 5) replace function
    source = './result/result3.py'
    with open('./result/obfuscated.py', 'w') as res:
        for line in of.obfuscate(source, dic):
            res.write(line)'''


if __name__ == '__main__':
    main(sys.argv[1:]) #passiamo la riga di comando eseguita
