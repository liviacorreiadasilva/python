from datetime import datetime

# Obtendo a data de nascimento do usuário
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
mes_nascimento = int(input("Digite o mês em que você nasceu: "))
dia_nascimento = int(input("Digite o dia em que você nasceu: "))

# Criando um objeto datetime para a data de nascimento
data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)

# Obtendo a data atual
data_atual = datetime.today()

# Calculando a diferença em dias
diferenca_em_dias = (data_atual - data_nascimento).days

print("Vocêjá viveu aproximadamente", diferenca_em_dias, "dias.")
