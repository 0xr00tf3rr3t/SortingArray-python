#Implementacion del selection sort

A = [64, 25, 12, 11, 22]

#Busque entre los elementos

for i in range(len(A)):

#Busca el minimo en el array desordenado

    min_idx = i 
    for j in range(i + 1, len(A)):
        if A[min_idx]>A[j]:
            min_idx = j
            
    #Una vez que encuentre elemento menor
    A[i], A[min_idx]  =A[min_idx], A[i]
    
#Test el code
print("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ")
