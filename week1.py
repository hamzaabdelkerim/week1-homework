#!/usr/bin/env python
# coding: utf-8

# # ** Python Interview **

# VARIABLES

# In[1]:


#variables

#python temelinde 3 çeşit component var.Bunlar
# 1)variable
# 2)function
# 3)object

#variable pythonda bir kodu organize etmek ve belli değerler tanımlamak için kullanılan kalıplardır.
#variable ismi rakamla başlayamaz.
#variable tanımlanırken ilk harfin küçük harfle başlaması tavsiye edilir.

var1 = 10 #integer
var2 = 15

#burada variablelar tanımlandı.

gun="pazartesi" #string

var3=10.0 #double(float)


# LIST

# In[3]:


#list
#her bir integer,string değeri için bir variable oluşturmak yerine bir list oluşturulur.
#list string,integer,float gibi bir datatype'dır.

var1=10
var2=20
var3=30

list_int=[1,2,3,4,5,6] #her bir variable listenin içine yerleştirilir.
type(list_int) #type listenin içindeki değer değil listenin kendisidir. list gözükür.

list_str=["pazartesi","salı","carsamba"] #liste string değerler de alabilir.
type(list_str)

value = list_int[0] 
print(value) #listenin 0. indeksi 1 olduğundan 1 yazdırılır.

value1 = list_int[-1] 
print(value1) #listede çok eleman olduğunda ve kaç eleman olduğu sayılmıyorsa sonuncu eleman bu şekilde yazdırılır.

list_divide= list_int[0:3] #listenin ilk 3 elemanı yazdırılır. 0'dan 3'e kadar
print(list_divide)

#listenin de kendi built_in_functionları vardır.
dir(list_int) #liste ile kullanılabilecek methodlar yazdırılır.

help(list.append) #append methodunun ne işe yaradığını gösterir.

list_int.append(7) #7'yi listenin sonuna ekler.

list_int.remove(7) #7 listeden çıkartılır.

list_int.reverse() #listeyi ters çevirir.

list_yeni=[3,5,2,6,1,4]
list_yeni.sort()

string_int_list=["sevval","ilhan",15,1,2000] #liste string ve integer değer birlikte alabilir.


# LOOPS

# In[4]:


for each in range (1,11): #1 -> inclusive, 11 -> exclusive
    
    print(each) 

for each in "ankara istanbul":
    
    print(each)
    
#a
#n
#k
#a
#r
#a
 
#i
#s
#t
#a
#n
#b
#u
#l
   
liste= [1,4,6,8,3,5,9,2,43,57]
sum(liste) #liste sum methoduyla kolay yoldan toplanabilir.
    
liste1=[1,2,3,4,5,6,-500,23,451,67,21,23]  
min(liste1)  #listedeki en küçük eleman min methoduyla bulunur.
             #aynı işlem for döngüsüyle de yapılabilir.
             
minimum=100000

for each in liste1:
    
    if(each<minimum):
        
        minimum=each
        
    else:
        
        continue #else durumunda hiçbir şey yapmadan devam edilir.
        
print(minimum)


# CONDITIONALS

# In[14]:


#conditionals
#if else statement

1 == 1 #True

1 == 2 #False

1 != 1 #False

True == True #True

True == False #False

1>0 and 4<5 #True

1>0 or 4<3 #True (tek durumun doğru olması yeterli)

var1=10
var2=20

if (var1 > var2):
    
    print("var 1 büyüktür var 2'den")
    
elif (var1 == var2):
    print("var1 eşittir var2")
    
else :
    
    print("var1 küçüktür var2'den")
    

liste =[1,2,3,4,5]

value = 3

if value in liste:
    
    print("value değeri {} listenin içindedir.".format(value))
    
else:
    print("value değeri {} listenin içinde değildir.".format(value))


# In[ ]:


WHILE LOOP


# In[ ]:


#while_loop

#while loop'ta bir condition vardır.

i=0 

while (i<4):
    
    print(i)
    
    i = i+1 #i=4 olana kadar yazdırır. (0,1,2,3)


# In[ ]:


DEFAULT AND FLEXIBLE FUNCTIONS


# In[17]:


#default and flexible functions

# default function: çember çevresi= 2*pi*r

def cember_cevre(r,pi=3.14): #burada pi sayısının değeri değişmeyeceği için default değer atandı.
    
    """
    cember_cevre
    
    parametre:r,pi
    
    output:çemberin çevresi
    
    """
    
    return 2*pi*r
    
cember_cevre(2) #pi sayısı default olarak tanımlandığından fonksiyonda yeni değer yazılmaz.
#cember cevresi 12.56 olarak hesaplandı. 


# LAMBDA FUNCTION

# In[43]:


#lambda function
#Amaç daha hızlı bir şekilde fonksiyon yazabilmektir.

def hesapla(x):
    
    output= x*x
    
    return output

sonuc = hesapla(3)

sonuc2 = lambda x: x*x  

print(sonuc2(3)) 

#iki fonksiyonda da x'in karesi hesaplanır. lambda ile daha kısa bir yazım olur.

y = 3

z = lambda x:x*y

z(3) #9


# DICTIONARY

# In[41]:


#dictionary

#küçük bir database gibidir.
#multiple return yapılmak istendiğinde hepsinin belli isimleri adı altında dictionary kullanmak yararlı olur.

dictionary = {"sevval":22, "utku":6, "nazli":3}
#küçük bir database oluşturuldu.

type(dictionary) #dict

dictionary["sevval"] #Şevval'in yaşını verir(22).

type(dictionary["sevval"]) #dictionary'deki Şevval'in yaşının type'ı integerdır.

#sevval, nazlı, utku = keys
#22, 6, 3 = value

dictionary.keys() #dictionary'de tanımlı keyler verilir
#dict_keys(['sevval', 'utku', 'nazli'])

dictionary.values() #dictionary'de tanımlı valuelar verilir.
#dict_values([22, 6, 3])

def deneme():
    
    dictionary = {"sevval":22, "utku":6, "nazli":3}
    
    return dictionary

dic = deneme() #dic adında bir dictionary fonksiyon içerisinde oluşturuldu.

dic["sevval"] #sevval adlı key'in value'sunu verir(22).

