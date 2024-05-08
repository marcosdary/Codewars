# Fazer um programa para ler 10 valores e os armazene em um vetor. Em seguida, mostre a posição onde
# se encontram o maior e o menor valor.
nums = []

try:
    maximo = int(input("Máximo de valores: "))
    for i in range(maximo):
        num = float(input(f"{i+1}° número: "))
        nums.append(num)
    maior_num = 0
    menor_num = nums[0]
    for num in nums:
        if maior_num < num:
            maior_num = num
        if menor_num > num:
            menor_num = num
         
    print(f'Na lista {nums}, o maior número é {maior_num}, enquanto o menor número, {menor_num}')
except ValueError:
        print("\n\tNúmero incorreto\n")