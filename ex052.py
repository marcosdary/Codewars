def contador_caractere(texto:str):
    
    texto_editado = texto.split()
    
    numero_total_palavras = 0
    dicionario = {}
    for palavra in texto_editado:
        
        dicionario[palavra] = dicionario.setdefault(palavra, 0) + 1
        numero_total_palavras += 1
            
    dicionario = {k:v for k, v in sorted(dicionario.items(), key=lambda item: item[1])}
    dicionario_quantidade_mais_frequentes = {}
    dicionario_quantidade_menos_frequentes = {}
    
    
    for item in list(dicionario.items())[:10]:
    
        dicionario_quantidade_menos_frequentes[item[0]] = item[1]
        
    for item in list(dicionario.items())[-10:]:
    
        dicionario_quantidade_mais_frequentes[item[0]] = item[1]  
        
    dicionario_quantidade_mais_frequentes = {k: v for k, v in sorted(dicionario_quantidade_mais_frequentes.items(), key= lambda item: item[1], reverse=True)}  
    
    return {'maisfrequentes': dicionario_quantidade_mais_frequentes, 'menosfrequentes': dicionario_quantidade_menos_frequentes}

text = '''
Norberto Bobbio, cientista político italiano, afirma que a democracia
é um processo que tem, em seu cerne, o objetivo de garantia a representatividade 
política de todas as pessoas. Para que o mecanismo democrático funcione, então, 
é fundamental apresentar uma rede estatal que dê acesso a diversos recursos, 
como alimentação, moradia, educação, segurança, saúde e participação eleitoral. 
Contudo, muitos brasileiros, por não terem uma certidão de nascimento, 
são privados desses direitos básicos e têm seus próprios papéis de cidadãos invisibilizados. 
Logo, deve-se discutir as raízes históricas desse problema e as suas consequências nocivas.
'''

