# TICKY Project - Stevan Ramon

# 1) Importar bibliotecas;
import pandas as pd
import csv

# 1.1) Convertendo CSV para HTML;
a = pd.read_csv("Data_Ticky.csv")
a.to_html("Data_Ticky.html")
html_file = a.to_html()

# 2) Receber Aquivo CSV como INPUT;
tabela = open(r"Data_Ticky.csv", "r").read().split('\n')

dict_error = {}
dict_code = {}
count_ticket = 0
count_error = 0

for line in tabela[1:-1]:
    if "ERROR:" in line:
        _,_,_,_,_,_,message,_,name = line.split(',')

        count_error +=1 #Contador para quantidade de erros;

        if message in dict_error.keys():
            dict_error[message].append(name)

        else:
            dict_error[message] = [name]
    else:
        _,_,_,_,_,_,_,code, name = line.split(',')

        count_ticket +=1 #Contador para quantidade de tickets;

        if code in dict_code.keys():
            dict_code[code].append(name)

        else:
            dict_code[code] = [name]

total_reports = count_error + count_ticket

# Mostre quantas pessoas tem por erro;
print("1) Quantidade de pessoas por erros:")
for erros in dict_error:
    print(erros,len(dict_error[erros]))

print("\n2) Ordem dos erros de forma Rankeada:")
# Mostre quantas pessoas tem por erro de forma Rankeada;
print(sorted(dict_error, key=lambda k: len(dict_error[k]), reverse=True))

print("\n3) Lista de usuários que enviaram os tickets")
# Mostre quais usuários enviaram o ticket e seu código;
print(dict_code)

print("\n4) Lista de usuários separados por erros gerados pelo sistema:")
# Mostre quais usuários tiveram erro em seu ticket e sua mensagem;
print(dict_error)

print("\nA quantidade de ERROS totais gerados:",count_error)
print("A quantidade de TICKETS totais gerados:",count_ticket)
print("\n5) A precisão do programa é de:",(count_ticket/total_reports)*100,"%")

