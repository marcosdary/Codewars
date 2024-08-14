from json import loads, dump
import os

dados = '''
{
  "funcionarios": [
    {
      "nome": "Ana Silva",
      "departamento": "Desenvolvimento",
      "projetos": [
        {
          "nome": "Sistema de Gestão",
          "status": "Em andamento"
        },
        {
          "nome": "Aplicativo Mobile",
          "status": "Concluído"
        }
      ]
    },
    {
      "nome": "João Oliveira",
      "departamento": "Marketing",
      "projetos": [
        {
          "nome": "Campanha de Verão",
          "status": "Planejamento"
        },
        {
          "nome": "Rebranding da Marca",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Maria Santos",
      "departamento": "Recursos Humanos",
      "projetos": [
        {
          "nome": "Treinamento de Novos Funcionários",
          "status": "Concluído"
        },
        {
          "nome": "Programa de Benefícios",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Carlos Pereira",
      "departamento": "Financeiro",
      "projetos": [
        {
          "nome": "Revisão Orçamentária",
          "status": "Em andamento"
        },
        {
          "nome": "Relatório Anual",
          "status": "Planejamento"
        }
      ]
    },
    {
      "nome": "Laura Martins",
      "departamento": "TI",
      "projetos": [
        {
          "nome": "Atualização de Sistema",
          "status": "Concluído"
        },
        {
          "nome": "Segurança da Informação",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Fernando Lima",
      "departamento": "Logística",
      "projetos": [
        {
          "nome": "Otimização de Armazéns",
          "status": "Planejamento"
        },
        {
          "nome": "Gerenciamento de Estoque",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Juliana Costa",
      "departamento": "Jurídico",
      "projetos": [
        {
          "nome": "Revisão de Contratos",
          "status": "Em andamento"
        },
        {
          "nome": "Compliance Regulatório",
          "status": "Concluído"
        }
      ]
    },
    {
      "nome": "Roberto Almeida",
      "departamento": "Vendas",
      "projetos": [
        {
          "nome": "Campanha de Natal",
          "status": "Em andamento"
        },
        {
          "nome": "Expansão de Mercado",
          "status": "Planejamento"
        }
      ]
    },
    {
      "nome": "Patrícia Gomes",
      "departamento": "Design",
      "projetos": [
        {
          "nome": "Novo Layout do Site",
          "status": "Concluído"
        },
        {
          "nome": "Material Publicitário",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Eduardo Souza",
      "departamento": "Pesquisa e Desenvolvimento",
      "projetos": [
        {
          "nome": "Pesquisa de Mercado",
          "status": "Planejamento"
        },
        {
          "nome": "Desenvolvimento de Novo Produto",
          "status": "Em andamento"
        }
      ]
    },
    {
      "nome": "Isabela Rocha",
      "departamento": "Atendimento ao Cliente",
      "projetos": [
        {
          "nome": "Melhoria do Suporte",
          "status": "Em andamento"
        },
        {
          "nome": "Pesquisa de Satisfação",
          "status": "Concluído"
        }
      ]
    }
  ]
}

'''
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
FILE = os.path.join(DESKTOP, 'Autoconsciência', 'Individuo', 'empresa.json')

dados = loads(dados)

with open(FILE, 'w', encoding='utf-8') as file:
    dump(dados, file, indent=4, ensure_ascii=False)