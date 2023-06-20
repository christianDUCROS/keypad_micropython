# POO keypad
from machine import Pin, PWM
import time

class keypad () : 
    
    def __init__(self,R0,R1,R2,R3,C0,C1,C2,C3) :         
        #connexion  rows et columns
        self.R0 = Pin(R0, Pin.OUT)    
        self.R1 = Pin(R1, Pin.OUT)
        self.R2 = Pin(R2, Pin.OUT)    
        self.R3 = Pin(R3, Pin.OUT)

        self.C0 = Pin(C0, Pin.IN,Pin.PULL_DOWN)
        self.C1 = Pin(C1, Pin.IN,Pin.PULL_DOWN)
        self.C2 = Pin(C2, Pin.IN,Pin.PULL_DOWN)
        self.C3 = Pin(C3, Pin.IN,Pin.PULL_DOWN)

    def scan_key(self) :
        while True : 
            self.R0.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    pass
                return '1'
            elif self.C1.value() :
                while (self.C1.value()):
                    pass
                return '2'
            elif self.C2.value() :
                while (self.C2.value()):
                    pass
                return '3'
            elif self.C3.value() :
                while (self.C3.value()):
                    pass
                return 'A'
            self.R0.off()
            self.R1.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    pass
                return '4'
            elif self.C1.value() :
                while (self.C1.value()):
                    pass
                return '5'
            elif self.C2.value() :
                while (self.C2.value()):
                    pass
                return '6'
            elif self.C3.value() :
                while (self.C3.value()):
                    pass
                return 'B'
            self.R1.off()
            self.R2.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    pass
                return '7'
            elif self.C1.value() :
                while (self.C1.value()):
                    pass
                return '8'
                break
            elif self.C2.value() :
                while (self.C2.value()):
                    pass
                return '9'
            elif self.C3.value() :
                while (self.C3.value()):
                    pass
                return 'C'
            self.R2.off()
            self.R3.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    pass
                return '*'
            elif self.C1.value() :
                while (self.C1.value()):
                    pass
                return '0'
            elif self.C2.value() :
                while (self.C2.value()):
                    pass
                return '#'
            elif self.C3.value() :
                while (self.C3.value()):
                    pass
                return 'D'
            self.R3.off()
   
    #scan avec touches spéciales
    def scan_code(self,n) :
        print('veuillez saisir un code') 
        code =''
        code_mask=''
        i=0
        while i< n : 
            touche = self.scan_key()
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
    def scan_code(self,n) :
        print('veuillez saisir un code') 
        code =''
        code_mask=''
        i=0
        while i< n : 
            touche = self.scan_key()
            code = code + touche
            code_mask = code_mask +'*'
            print('code = ',code_mask)  
            i=i+1
        return code
    '''

    def check_code(self, code, code_users) :
        for  i  in code_users :
            if code == i :
                return True
            else :
                return False 

class keypad_buzzer () : 
    
    def __init__(self,R0,R1,R2,R3,C0,C1,C2,C3,buzzer) :         
        #connexion  rows et columns
        self.R0 = Pin(R0, Pin.OUT)    
        self.R1 = Pin(R1, Pin.OUT)
        self.R2 = Pin(R2, Pin.OUT)    
        self.R3 = Pin(R3, Pin.OUT)

        self.C0 = Pin(C0, Pin.IN,Pin.PULL_DOWN)
        self.C1 = Pin(C1, Pin.IN,Pin.PULL_DOWN)
        self.C2 = Pin(C2, Pin.IN,Pin.PULL_DOWN)
        self.C3 = Pin(C3, Pin.IN,Pin.PULL_DOWN)
        self.buzzer = PWM(Pin(buzzer)) # branchement
       
    def scan_key(self) :
        while True : 
            self.R0.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '1'
            
            elif self.C1.value() :
                while (self.C1.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '2'
            elif self.C2.value() :
                while (self.C2.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '3'
            elif self.C3.value() :
                while (self.C3.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return 'A'
            self.R0.off()
            self.R1.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '4'
            elif self.C1.value() :
                while (self.C1.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '5'
            elif self.C2.value() :
                while (self.C2.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '6'
            elif self.C3.value() :
                while (self.C3.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return 'B'
            self.R1.off()
            self.R2.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '7'
            elif self.C1.value() :
                while (self.C1.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '8'
                break
            elif self.C2.value() :
                while (self.C2.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '9'
            elif self.C3.value() :
                while (self.C3.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return 'C'
            self.R2.off()
            self.R3.on()
            if self.C0.value()  :
                while (self.C0.value()):
                    self.buzzer.freq(1500)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '*'
            elif self.C1.value() :
                while (self.C1.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '0'
            elif self.C2.value() :
                while (self.C2.value()):
                    self.buzzer.freq(2000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return '#'
            elif self.C3.value() :
                while (self.C3.value()):
                    self.buzzer.freq(1000)   
                    self.buzzer.duty_u16(32767)
                self.buzzer.duty_u16(0)   
                return 'D'
            self.R3.off()
   
    #scan avec touches spéciales
    def scan_code(self,n) :
        print('veuillez saisir un code') 
        code =''
        code_mask=''
        i=0
        while i< n : 
            touche = self.scan_key()
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
    def scan_code(self,n) :
        print('veuillez saisir un code') 
        code =''
        code_mask=''
        i=0
        while i< n : 
            touche = self.scan_key()
            code = code + touche
            code_mask = code_mask +'*'
            print('code = ',code_mask)  
            i=i+1
        return code
    '''

    def check_code(self, code, code_users) :
        for  i  in code_users :
            if code == i :
                self.buzzer.freq(500)   
                self.buzzer.duty_u16(32767)
                time.sleep_ms(500)
                self.buzzer.duty_u16(0)   
                self.buzzer.freq(1000)   
                self.buzzer.duty_u16(32767)
                time.sleep_ms(500)
                self.buzzer.duty_u16(0)   
                return True
            
            else :
                self.buzzer.freq(200)   
                self.buzzer.duty_u16(32767)
                time.sleep(1)
                self.buzzer.duty_u16(0)  
                return False 


