from machine import Pin
#connexion  rows et columns
R0 = Pin(9, Pin.OUT)    
R1 = Pin(8, Pin.OUT)
R2 = Pin(7, Pin.OUT)    
R3 = Pin(6, Pin.OUT)

C0 = Pin(5, Pin.IN,Pin.PULL_DOWN)
C1 = Pin(4, Pin.IN,Pin.PULL_DOWN)
C2 = Pin(3, Pin.IN,Pin.PULL_DOWN)
C3 = Pin(2, Pin.IN,Pin.PULL_DOWN)

def scan_key() :
    while True : 
        R0.on()
        if C0.value()  :
            while (C0.value()):
                pass
            return '1'
        elif C1.value() :
            while (C1.value()):
                pass
            return '2'
        elif C2.value() :
            while (C2.value()):
                pass
            return '3'
        elif C3.value() :
            while (C3.value()):
                pass
            return 'A'
        R0.off()
        R1.on()
        if C0.value()  :
            while (C0.value()):
                pass
            return '4'
        elif C1.value() :
            while (C1.value()):
                pass
            return '5'
        elif C2.value() :
            while (C2.value()):
                pass
            return '6'
        elif C3.value() :
            while (C3.value()):
                pass
            return 'B'
        R1.off()
        R2.on()
        if C0.value()  :
            while (C0.value()):
                pass
            return '7'
        elif C1.value() :
            while (C1.value()):
                pass
            return '8'
            break
        elif C2.value() :
            while (C2.value()):
                pass
            return '9'
        elif C3.value() :
            while (C3.value()):
                pass
            return 'C'
        R2.off()
        R3.on()
        if C0.value()  :
            while (C0.value()):
                pass
            return '*'
        elif C1.value() :
            while (C1.value()):
                pass
            return '0'
        elif C2.value() :
            while (C2.value()):
                pass
            return '#'
        elif C3.value() :
            while (C3.value()):
                pass
            return 'D'
        R3.off()
    


#scan avec touches spéciales
def scan_code(n) :
    print('veuillez saisir un code') 
    code =''
    code_mask=''
    i=0
    while i< n : 
        touche = scan_key()
        if touche=='*' and code !='':
            i=i-1
            code = code[:-1]
            code_mask= code_mask[:-1]
            print('touche précédente annulée')
        elif touche=='*' and code ==''  :
            i=0
            print('touche annulation')
        else : 
            code = code + touche
            i=i+1
            code_mask = code_mask +'*'
        if touche=='#' :
            i = 0 
            code =''
            code_mask =''
            print('code annulé')
        print('code = ',code_mask)  
    return code

'''
#scan sans touche spéciale
def scan_code(n) :
    print('veuillez saisir un code') 
    code =''
    code_mask=''
    i=0
    while i< n : 
        touche = scan_key()
        code = code + touche
        code_mask = code_mask +'*'
        print('code = ',code_mask)  
        i=i+1
    return code
'''

def check_code(code, code_users) :
    for  i  in code_users :
        if code == i :
            return True
        else :
            return False 

code = scan_code(4)  #4 pour 4 code à 4 caratères
print('Votre code : ', code )
code_users = ('1234','456B','789C','0123')
autorisation = check_code(code,code_users )
print ('Autorisation valide : ',autorisation)

