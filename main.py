import module_keypad
clavier = module_keypad.keypad(9,8,7,6,5,4,3,2)
#clavier = module_keypad.keypad_buzzer(9,8,7,6,5,4,3,2,10)

code = clavier.scan_code(4)  #4 pour code à 4 caratères
print('Votre code : ', code )

code_users = ('1234','456B','789C','0123')
autorisation = clavier.check_code(code,code_users )
print ('Autorisation valide : ',autorisation)
