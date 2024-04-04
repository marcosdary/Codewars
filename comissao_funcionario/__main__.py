from armazenar_salario_empregado import ler_json, escrever_json

salarios = ler_json([])
class Empregado:
    def __init__(self, matricula, total_vendas, salario):
        self.matricula = matricula
        self.total_vendas = total_vendas
        self.salario = salario
        self.salario_total = None
    
    def novo_salario(self):
        if 5_000 <= self.total_vendas <= 10_000:
            self.salario_total = self.total_vendas * 0.05 + self.salario
        
        elif 10_000 < self.total_vendas <= 20_000:
            self.salario_total = self.total_vendas * 0.07 + self.salario
            
        elif 20_000 < self.total_vendas:
            self.salario_total = self.total_vendas * 0.09 + self.salario
        
        else:
            self.salario_total = self.salario
        
    
for i in range(10):
    try:
        matricula_empregado = int(input("Matrícula: "))
        valor_vendas = float(input("Total de vendas: "))
        salario_empregado = float(input("Salário: "))
        print('\n\n')
        empregado = Empregado(matricula_empregado, valor_vendas, salario_empregado)
        empregado.novo_salario()
        salarios.append(empregado.__dict__)
        escrever_json(salarios)
    except ValueError:
        print("\n\tPor favor, insira um valor válido para a matrícula, total de vendas e salário\n")
    
maior_salario = sorted(salarios, key=lambda key: key ['salario_total'], reverse=True)[0]['salario_total']
maior_venda = sorted(salarios, key=lambda key: key ['total_vendas'], reverse=True)[0]['matricula']

print(f'MAIOR SALÁRIO: {maior_salario}\nMAIOR VENDA: {maior_venda}')