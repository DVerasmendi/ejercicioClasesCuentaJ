from cuenta import Cuenta


def new_user(usuario,new_saldo=0):
    imprimir_usuario=list(user.mostrar())
    print('Nuevo Usuario Creado: ',imprimir_usuario[0])
    print('Saldo Nuevo Usuario: ',imprimir_usuario[1])
    
def depositarDinero(monto_deposito):
    depositar=list(user.ingresar(monto_deposito))
    print('Dinero Depositado: ', depositar[1])
    print('Nuevo Saldo Disponible: ', depositar[0])


def retirarDinero(monto_retirar):
    retirar=list(user.retirar(monto_retirar))
    print('Dinero Retirado: ', retirar[1])
    print('Nuevo Saldo Disponible: ', retirar[0])



print("\nHello, this is the Command Line Interface for a Bank application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: Crear Usuario
- Type 2: Ingrese el monto a depositar en su cuenta.
- Type 3: Ingrese el monto a retirar de su cuenta.
- Type 4: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)    
    try: 
        if option == 1:
            print('Ingrese el Nombre de usuario: ')
            usuario=input()
            print('Desea ingresar dinero de Apertura a su cuenta? \n1.-SI \n2.-NO \n')  
            respuesta=input()
            if '1' in respuesta:    
                print('Ingrese el monto de Apertura: ')  
                monto_apertura=float(input())
                if monto_apertura<0:
                    print('No puedes ingresar numeros negativos we \n')
                    break
            else:
                monto_apertura=0    
                
            print('\n')
            user=Cuenta(titular=usuario,cantidad=monto_apertura) 
            new_user(usuario,monto_apertura)
            
        if option == 2:
            print('Ingrese el monto a Depositar: ')  
            monto_depositar=float(input())
            print('\n')
            depositarDinero(monto_depositar)
        if option == 3:
            print('Ingrese el monto a Retirar: ')  
            monto_retirar=float(input())
            print('\n')
            retirarDinero(monto_retirar)
            
        if option==4:
            print("Bye bye!")
            stop = True             
    except:
        print('Seleccione una opcion valida')
        pass