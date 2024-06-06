from datetime import date
class Funcionario:
    
    def __init__(self, nome:str, cpf:str, salario:float, data_adimissao:str) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._data_adimissao = date.fromisoformat(data_adimissao)
    
    @property
    def salario(self):
        return self._salario
    
    def tempo_servico(self):
        hoje = date.today()
        tempo_servico = hoje - self._data_adimissao
        return tempo_servico.days
    
    def atualizar_salario(self, novo_salario:float):
        if novo_salario > self._salario:
            self._salario = novo_salario
            return "Salário Atualizado com sucesso!!"
        raise ValueError("Atualizar o salário está inválido")

class Vendedor(Funcionario):
    
    def __init__(self, nome: str, cpf: str, salario: float, data_adimissao: str, meta_vendedor:float, comissao:float) -> None:
        super().__init__(nome, cpf, salario, data_adimissao)
        self.__valor_total_vendido = 0
        self.__meta_vendedor = meta_vendedor
        self.__comissao = comissao
    @property
    def meta_vendedor(self):
        return self.__meta_vendedor
    
    def total_vendido(self):
        return self.__valor_total_vendido
    
    @property
    def comissao(self):
        return self.__comissao
    
    def calcularComissao(self, valor_vendas:float):
        if valor_vendas > 0:
            return self.__comissao * valor_vendas
        raise ValueError("Valor Inválido")
    
    def registrar_venda(self, preco:float, quantidade: int):
        if quantidade > 0 and preco > 0:
            valor = preco * quantidade
            self.__valor_total_vendido += valor
            if self.__meta_vendedor <= self.__valor_total_vendido:
                return "META CUMPRIDA"
            return True
        raise ValueError("Quantidade de venda inválida ou Preço do produto")

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, salario: float, data_adimissao: str, nome_departamento:str, equipe:list) -> None:
        super().__init__(nome, cpf, salario, data_adimissao)
        self.__nome_departamento = nome_departamento.nome
        self.__equipe = equipe
    
    @property
    def equipe(self):
        return self.__equipe
    def gerenciar_equipe(self):
        metas_trimestrais = {'venda': 10_000, 'atendimento': 95}
        vendedores_nao_atingiu_metas = []
        for membro in self.__equipe:
            dado_membro = {}
            if membro.total_vendido() < metas_trimestrais['venda']:
                dado_membro['nome'] = membro._nome 
                dado_membro['cpf'] = membro._cpf 
                vendedores_nao_atingiu_metas.append(dado_membro)
        return "Todos Atingiu a Meta" if vendedores_nao_atingiu_metas == [] else vendedores_nao_atingiu_metas

class Tecnico(Funcionario):
    
    def __init__(self, nome: str, cpf: str, salario: float, data_adimissao: str, area_atuacao: str, habilidade_tecnicas:list) -> None:
        super().__init__(nome, cpf, salario, data_adimissao)
        self.__area_atuacao = area_atuacao
        self.__habilidade_tecnicas = habilidade_tecnicas
        
    @property
    def area_atuacao(self):
        return self.__area_atuacao
    
    @property
    def habilidade_tecnicas(self):
        return self.__habilidade_tecnicas
    
    def atualizacao_tecnica(self, habilidade:str):
        self.__habilidade_tecnicas.append(habilidade)
        