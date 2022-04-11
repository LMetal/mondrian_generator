import numpy as np
from random import randint as rand
from PIL import Image

lato = 52
n_immagini = 5
n_linee = 12
colore_linee = [0, 0, 0]

def gen_oriz(x, y, right):
   if right: #verso destra
       delta_y = 0
       while True:
           delta_y = delta_y + 1

           if(array[x][y + delta_y] == colore_linee).all():
               break
           else:
               array[x][y + delta_y] = colore_linee
   else: #verso sinistra
       delta_y = 0
       while True:
           delta_y = delta_y + 1
           if (array[x][y - delta_y] == colore_linee).all():
               break
           else:
               array[x][y - delta_y] = colore_linee

def gen_vert(x, y, up):
   if up: #verso l'alto
       delta_x = 0
       while True:
           delta_x = delta_x - 1

           if(array[x + delta_x][y] == colore_linee).all():
               break
           else:
               array[x + delta_x][y] = colore_linee
   else: #verso in basso
       delta_x = 0
       while True:
           delta_x = delta_x + 1
           if (array[x + delta_x][y] == colore_linee).all():
               break
           else:
               array[x + delta_x][y] = colore_linee


def analisi_punto(x, y): #ritorna [sopra, sotto, destra, sinistra]
   intorno_punto = [(array[x-1][y] == colore_linee).all(), (array[x+1][y] == colore_linee).all(), (array[x][y+1] == colore_linee).all(), (array[x][y-1] == colore_linee).all()]
   #print(intorno_punto)
   return intorno_punto


def nuova_linea():
   while True:
       x = rand(1, lato-2)
       y = rand(1, lato-2)
       if (array[x][y] == colore_linee).all():
           intorno_punto = analisi_punto(x,y)
           if(intorno_punto == [True, True, True, True]):
               continue
           else:
               array[x][y] = [255, 0, 0]
               while True:
                   rand_direction = rand(0,3)
                   if(intorno_punto[rand_direction] == False):
                       if(rand_direction == 0): #verso l'alto
                           gen_vert(x, y, True)
                       elif(rand_direction == 1):  # verso basso
                               gen_vert(x, y, False)
                       elif (rand_direction == 2):  # verso destra
                           gen_oriz(x, y, True)
                       else: # verso sinistra
                           gen_oriz(x, y, False)


                       break
           break



def generation(k):
   # tutto bianco
   for i in range(lato):
       for j in range(lato):
           array[j][i] = [255, 255, 255]

   # bordi
   for i in range(lato):
       array[0][i] = colore_linee
       array[lato - 1][i] = colore_linee
       array[i][0] = colore_linee
       array[i][lato - 1] = colore_linee

       array[1][i-1] = colore_linee
       array[lato - 2][i] = colore_linee
       array[i-1][1] = colore_linee
       array[i-1][lato - 2] = colore_linee

   #linee
   for i in range(n_linee):
       nuova_linea()



   img = Image.fromarray(array)
   img.save(str(k) + '.png')


if __name__ == "__main__":
   for n_immagine in range(n_immagini):
      global array
      array = np.zeros([lato, lato, 3], dtype=np.uint8)
      generation(n_immagine)

