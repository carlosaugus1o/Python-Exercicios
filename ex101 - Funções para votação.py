

def calc_idade(nascimento):
    from datetime import date
    return date.today().year - nascimento


def voto(ano_nasc, calcula_idade):  # Função responsável por verificar se pode ou não votar
    idade = calcula_idade(ano_nasc)
    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano_nascimento = int(input('Informe o ano de seu nascimento: '))

print(voto(ano_nascimento, calc_idade))
# Argumentos passados para a função voto():
#           ano_nascimento = ano informado pelo usuário;
#           calc_idade = função para calcular idade do usuário.