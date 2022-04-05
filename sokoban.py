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

    #Controladores
    #a-Izquierda 
    #d-Derecha
    #w-Arriba
    #s-Abajo
    #q-Salir
    #mapa = [3,1,1,1,0,1,1,1,3]#Define el mapa de juego

  mapa =[
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,4,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,0,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,2,1,1,1,2,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,4,1,1,1,1,1,1,1,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
      ]#Define el mapa de juego
  mapa = np.array(mapa)
  result = np.where(mapa == 0)
  muneco_fila=result[0] 
  muneco_columna=result[1] #estas lineas muestran que simbolo son

  def __init__(self): #Pone en modo privdo el comando
    pass #Permite seguir corriendo nuestro comando
      
  def imprimirMapa(self): #Metodo para imprimir el mapa
      for j in range(9):#Recorre cada caracterer del juego
        for i in range(14):
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

    #12 muneco_meta,meta [5,4] -> [4,5] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.muneco_columna+=1

    #13 muneco_meta,caja,espacio [5,2,1] -> [4,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1

    #14 muneco_meta,caja,meta [5,2,4] -> [4,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1

    #15 muneco_meta,caja_meta,espacio [5,6,1] -> [4,5,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1

    #16 muneco_meta,caja_meta,meta [5,6,4] -> [4,5,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
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
        
    #23 muneco_meta,espacio [5,1] -> [4,0] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.muneco_columna-=1

    #24 muneco_meta,meta [5,4] -> [4,5] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.muneco_columna-=1

    #25 muneco_meta,caja,espacio [5,2,1] -> [4,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.mapa[self.muneco_fila,self.muneco_columna-2]=2
        self.muneco_columna-=1

    #26 muneco_meta,caja,meta [5,2,4] -> [4,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=0
        self.mapa[self.muneco_fila,self.muneco_columna-2]=6
        self.muneco_columna-=1

    #27 muneco_meta,caja_meta,espacio [5,6,1] -> [4,5,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.mapa[self.muneco_fila,self.muneco_columna-2]=2
        self.muneco_columna-=1

    #28 muneco_meta,caja_meta,meta [5,6,4] -> [4,5,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna-1]=5
        self.mapa[self.muneco_fila,self.muneco_columna-2]=6
        self.muneco_columna-=1

  def moverArriba(self):
    #29 muneco,espacio [1,0] -> [0,1]
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila-1,self.muneco_columna]=0
        self.muneco_fila-=1

    #30 muneco,meta [0,4] -> [1,5] 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila-1,self.muneco_columna]=5
        self.muneco_fila-=1

    #31 muneco,caja,espacio [0,2,1] -> [1,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and self.mapa[self.muneco_fila-2,self.muneco_columna]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila-1,self.muneco_columna]=0
        self.mapa[self.muneco_fila-2,self.muneco_columna]=2
        self.muneco_fila-=1

    #32 muneco,caja,meta [0,2,4] -> [1,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila-1,self.muneco_columna]=0
        self.mapa[self.muneco_fila-2,self.muneco_columna]=6
        self.muneco_fila-=1

  def moverAbajo(self):
    #41 muneco,espacio [1,0] -> [0,1]
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila+1,self.muneco_columna]=0
        self.muneco_fila+=1

    #42 muneco,meta [0,4] -> [1,5] 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila+1,self.muneco_columna]=5
        self.muneco_fila+=1

    #43 muneco,caja,espacio [0,2,1] -> [1,0,2] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and self.mapa[self.muneco_fila+2,self.muneco_columna]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila+1,self.muneco_columna]=0
        self.mapa[self.muneco_fila+2,self.muneco_columna]=2
        self.muneco_fila+=1

    #44 muneco,caja,meta [0,2,4] -> [1,0,6] 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila+1,self.muneco_columna]=0
        self.mapa[self.muneco_fila+2,self.muneco_columna]=6
        self.muneco_fila+=1
                   
juego = Mi_primer_juego()#Crea un objeto para jugar
juego.imprimirMapa()#Imprime el mapa

while True: #Bucle para jugar N veces
    instrucciones = "d-Derecha\na-Izquierda\nw-Arriba\ns-Abajo\nq-Salir" #instrucciones de juego
    print(instrucciones) #Imprime las intrucciones del juego
    movimientos = input("Mover a: ") #Lee el movimiento del muñco
    if movimientos == "d": #Si es d - mover a la derecha
        juego.moverDerecha() #Mueve el muñeco a la derecha
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "a": #Si es a - mover a la izquierda
        juego.moverIzquierda() #Mueve el muñeco a la izquierda
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "w": #Si es w - mover hacia arriba
        juego.moverArriba() #Mueve el muñeco hacia arriba
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "s": #Si es s - mover hacia abajo
        juego.moverAbajo() #Mueve el muñeco hacia abajo
        juego.imprimirMapa() #Imprime el mapa
    elif movimientos == "q": #Si es q-salir
        print("Saliste del juego") #Imprime mensaje de salida
        break #Rompe el while