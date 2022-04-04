import numpy as np
class Mi_primer_juego:
    #Representación de componentes de juego
    #0-Muñeco    
    #1-Espacio 
    #2-Cajas
    #3-Paredes
    #4-Meta
    #5-Muneco_meta
    #6-Caja_meta

    #Controles
    #a-Izquierda 
    #d-Derecha
    #w-Arriba
    #s-Abajo
    #q-Salir
    #mapa = [3,1,1,1,0,1,1,1,3]#Define el mapa de juego

  mapa = [
        [3,3,3,3,3,3,3,3],
        [3,1,1,1,1,1,1,3],
        [3,1,0,4,1,1,1,3],
        [3,1,1,1,1,1,1,3],
        [3,3,3,3,3,3,3,3]
      ]#Define el mapa de juego
  mapa = np.array(mapa)
  result = np.where(mapa == 0)
  muneco_fila=result[0]
  muneco_columna=result[1] #estas lineas muestran que simbolo son
    
  def __init__(self): #Pone en modo privdo el comando
    pass #Permite seguir corriendo nuestro comando
      
  def imprimirMapa(self): #Metodo para imprimir el mapa
      for j in range(5):#Recorre cada caracterer del juego
        for i in range(8):
          if self.mapa[j][i] == 1:#Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print(" ", end = "")#Cambiar un 1 por un ""
          elif self.mapa[j][i] == 3: #3-pared
            #for a in range(len(self.mapa)):
            print("#", end = "")#Cambia un 3 por un simbolo
            
          else:
            print(self.mapa[j][i], end="")
        print()
      print() #Imprime una linea vacia
      #mover
  def moverDerecha(self): #5 muneco,espacio [0,1] -> [1,0]
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.muneco_columna+=1
        
    #6 muneco,meta [0,4] -> [1,5] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.muneco_columna+=1

    #7 muneco,caja,espacio [0,2,1] -> [1,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1
        
    #8 muneco,caja,meta [0,2,4] -> [1,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1

    #9 muneco,caja_meta,espacio [0,6,1] -> [1,5,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1

    #10 muneco,caja_meta,meta [0,6,4] -> [1,5,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1

    #11 muneco_meta,espacio [5,1] -> [4,0] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.muneco_columna+=1
        
  def moverIzquierda(self):
    #17 muneco,espacio [1,0] -> [0,1]
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.muneco_columna-=1

    #18 muneco,meta [1,5] -> [0,5] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.muneco_columna-=1

    #19 muneco,caja,espacio [0,2,1] -> [1,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.mapa[self.muneco_fila,self.muneco_columna-2]=2
        self.muneco_columna-=1

    #20 muneco,caja,meta [0,2,4] -> [1,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.mapa[self.muneco_fila,self.muneco_columna-2]=6
        self.muneco_columna-=1

    #21 muneco,caja_meta,espacio [0,6,1] -> [1,5,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.mapa[self.muneco_fila,self.muneco_columna-2]=2
        self.muneco_columna-=1

    #22 muneco,caja_meta,meta [0,6,4] -> [1,5,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.mapa[self.muneco_fila,self.muneco_columna-2]=6
        self.muneco_columna-=1
        
    #11 muneco_meta,espacio [5,1] -> [4,0] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.muneco_columna-=1
                   
juego = Mi_primer_juego()#Crea un objeto para jugar
juego.imprimirMapa()#Imprime el mapa

while True: #Bucle para jugar N veces
    instrucciones = "d-Derecha\na-Izquierda\nq-Salir" #instrucciones de juego
    print(instrucciones) #Imprime las intrucciones del juego
    movimientos = input("mover a: ") #Lee el movimiento del muñco
    if movimientos == "d": #Si es d - mover a la derecha
        juego.moverDerecha() #Mueve el muñeco a la derecha
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "a": #Si es a - mover a la izquierda
        juego.moverIzquierda() #Mueve el muñeco a la izquierda
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "q": #Si es q-salir
        print("Saliste del juego") #Imprime mensaje de salida
        break #Rompe el while