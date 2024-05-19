# Dada uma lista de números inteiros, 
# escreva uma função para encontrar 
# a subsequência contínua com a maior soma

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# [4, -1, 2, 1]  => Soma = 6
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray_num(nums):
    
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        # Aqui recebe o valor que o max_global irá receber se o valor em max_current foi maior que ele, por exemplo: 
        # max_current, inicialmente, é -2, assim que começa o loop o valor do num é 1. Quando faz a comparação no max entre -2 e (-2+1) = -1 a saída é -1.
        # Logo, compara-se entre -1 e -2, assim a saída da condicional é True, ai o max_global recebe o -1. 
        if max_current > max_global:
            max_global = max_current
        
    return max_global

def max_subarray(nums):
    
    max_global = max_subarray_num(nums)
    i = 0
    while i < len(nums):
        j = 0
        subarray = []
        while j < len(nums[i:]):
            subarray.append(nums[i:][j])
            
            j += 1
        if sum(subarray) == max_global:  
            break
            
        i += 1
    
    return subarray

print(max_subarray(nums))