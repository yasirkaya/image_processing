#A ) 28x28 boyutlarında içeriği sıfır ve bir olan bir matris üretiniz. 

#B ) A’da üretilen matriste bir leri içeren mbr dikdörtgenini üreten fonksiyonu yazınız. 

#C ) 28x28 lik iki vektörün benzeriliğini ölçen fonksiyon yazınız.

#D ) a ve b deki fonksiyonları kullanarak 100 tane matris üretip, ilk üretilen ile diğerlerinin benzerliği listeleyen fonksiyonu yazınız.

import random
import numpy as np

def matris_create_28_by_38_with_0_1():
    my_matris = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            my_matris[i,j] = random.randint(0,1)
    return my_matris


def mbr_28x28(matrix_a):
    m = matrix_a.shape[0]
    n = matrix_a.shape[1]
    
    x_min=m
    x_max=0         #baslangicta degerleri olası en olumsuz durum
    y_min=n
    y_max=0

#soru 0 a nin cevabı
        
    my_matris = np.zeros((28,28))  #28x28 matris oluşturuldu.
    for i in range(28):
        for j in range(28):
            if(matrix_a[i,j] == 1 and x_min > i): #resim/matris üzerinden
                x_min=i                             #x_min, .... güncelleniyor
            if(matrix_a[i,j] == 1 and x_max < i):
                x_max=i
            
            if(matrix_a[i,j] == 1 and y_min > j):
                y_min=j
            if(matrix_a[i,j] == 1 and y_max < j):
                y_max=j
                    
            my_matris[i,j] = random.randint (0,1)
    
    return (x_min,x_max,y_min,y_max,y_matris)


#c şıkkının cevabı

def get_similarity(character_a,character_b):
    n=m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity = 0
    for i in range(n):
        for j in range(n):
            my_similarity = my_similarity+character_a[i,j]*character_b[i,j]
    
    return my_similarity
    
    
    
def get_similarity_for_100_characters(kac_karater=100):
    characters=[]
    for i in range(kac_karater):
        new_char =matris_create_28_by_38_with_0_1()
        characters.append(new_char)
    
    for i in range(kac_karater):
        benzerlik = get_similarity(characters[0],characters[1])
        print("0 --- "+ i + " benzerlik")

    
def main():
   c1=matris_create_28_by_38_with_0_1()
   c2=matris_create_28_by_38_with_0_1()
   mbr_28x28(c1)
   #a = get_similarity(c1,c2)
    a= get_similarity_for_100_characters(10)
   print(a)
main()