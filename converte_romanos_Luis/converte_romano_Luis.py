import math

tabela = {1:"I", 5: "V",10: "X", 50:"L",100: "C", 500:"D",1000: "M" } 

def valida_numero(num):
  if  0 <= num <=3999 : return num
  
  return False

def numero_para_romano(num):
    
    result = ''
    D = 1
    while num >= D: 
        D *= 10
  
    D /= 10  
  
    while num:   
        Num2 = int(num / D) 
  
        if Num2 <= 3: 
            result += (tabela[D] * Num2)

        elif Num2 == 4: 
            result += (tabela[D] + tabela[D * 5]) 

        elif Num2 >= 5 and Num2 <= 8: 
            result += (tabela[D * 5] + (tabela[D] * (Num2 - 5))) 

        elif Num2 == 9: 
            result += (tabela[D] + tabela[D * 10]) 
  
        num = math.floor(num % D) 
        D /= 10
          
    return result