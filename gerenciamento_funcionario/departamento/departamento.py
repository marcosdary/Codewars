class Departamento:
    
    def __init__(self, nome:str, codigo: str, funcionarios:list) -> None:
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = funcionarios
        
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        
    def remover_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            del self.funcionarios[self.funcionarios.index(funcionario)]
        raise ValueError("Funcionário não encontrado")
    
    def buscar_funcionario(self, funcionario):
        
        cpfs = [funcionario._cpf for funcionario in self.funcionarios]
        if funcionario._cpf in cpfs:
            return f"Funcionário {funcionario._nome} encontrado"
        raise ValueError("Funcionário não encontrado")
    
    def listar_funcionario(self):
        return [{"nome": funcionario._nome, "cpf": funcionario._cpf} for funcionario in self.funcionarios]
    
    def quantidade_funcionario(self):
        return len(self.funcionarios)
    
    
