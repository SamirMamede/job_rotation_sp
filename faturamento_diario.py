'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na 
linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no 
cálculo da média;
'''

import requests
import json

url = 'https://drive.google.com/uc?id=1qXvCPjEL4jerElN-hnScoKkEVmSQ8A2L'
response = requests.get(url)
data = json.loads(response.content)


faturamento_diario = []


for dia in data:
    valor = dia['valor']
    faturamento_diario.append(valor) 


menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)


faturamento_total = sum(faturamento_diario)
dias_com_faturamento = len([f for f in faturamento_diario if f > 0])
media_faturamento = faturamento_total / dias_com_faturamento
dias_acima_da_media = len([f for f in faturamento_diario if f > media_faturamento])


print('Menor faturamento diário:', menor_faturamento)
print('Maior faturamento diário:', maior_faturamento)
print('Dias com faturamento superior à média mensal:', dias_acima_da_media)




