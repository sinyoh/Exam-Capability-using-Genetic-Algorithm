from random import randint, random

arr = [1,2,3,4,5,6,7,8,9]

arr2 = [11,12,13,14,15,16,17,18,19]

_len = len(arr)


# #2 point crossover
# for i in range(_len):
#     if(i<(_len*0.25)):
#         print(arr[i])
        
#     elif(i>(_len*0.25) and i<(_len*0.75)):
#         print(arr2[i])
        
#     elif(i > (_len * 0.75)):
#         print(arr[i])   
        
# print()        

# for i in range(_len):
#     if(i<(_len*0.25)):
#         print(arr2[i])
        
#     elif(i>(_len*0.25) and i<(_len*0.75)):
#         print(arr[i])
        
#     elif(i > (_len * 0.75)):
#         print(arr2[i])   
        
        
#random crossover
# coin=[]
# for i in range(_len):
#     coin.append(randint(0, 1))
    
# print(coin)
# print()  
    
# for i in range(_len):
#     if(coin[i] == 1):
#         print(arr[i])
#     elif(coin[i] == 0):
#         print(arr2[i])    

# print()

# for i in range(_len):
#     if(coin[i] == 1):
#         print(arr2[i])
#     elif(coin[i] == 0):
#         print(arr[i])    
