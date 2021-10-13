cpf_cnpj = input("Digite o CPF ou CNPJ: ")

x = cpf_cnpj.find('.')
y = cpf_cnpj.find('/')
if (x == 2) or (x == 3):
    cpf = cpf_cnpj.split('.')
    a, b, c = cpf
    cpf = a + b + c
    if y == 10:
        cnpj = cpf_cnpj.split('/')
        d, e = cnpj
        cnpj = str((cpf)[:8]) + str(e)

if len(cpf_cnpj) == 9:
    cpf = cpf_cnpj

    num1 = int(str(cpf)[:1])
    num2 = int(str(cpf)[:2]) - (num1 * 10)
    if num2 <= 0:
        num2 = 0
    num3 = int(str(cpf)[:3]) - (int(str(cpf)[:2]) * 10)
    if num3 <= 0:
        num3 = 0
    num4 = int(str(cpf)[:4]) - (int(str(cpf)[:3]) * 10)
    if num4 <= 0:
        num4 = 0
    num5 = int(str(cpf)[:5]) - (int(str(cpf)[:4]) * 10)
    if num5 <= 0:
        num5 = 0
    num6 = int(str(cpf)[:6]) - (int(str(cpf)[:5]) * 10)
    if num6 <= 0:
        num6 = 0
    num7 = int(str(cpf)[:7]) - (int(str(cpf)[:6]) * 10)
    if num7 <= 0:
        num7 = 0
    num8 = int(str(cpf)[:8]) - (int(str(cpf)[:7]) * 10)
    if num8 <= 0:
        num8 = 0
    num9 = int(str(cpf)[:9]) - (int(str(cpf)[:8]) * 10)
    if num9 <= 0:
        num9 = 0
    num10 = ((num1 * 1) + (num2 * 2) + (num3 * 3) + (num4 * 4) + (num5 * 5) + (num6 * 6) + (num7 * 7) + (num8 * 8) + (num9 * 9)) % 11
    num11 = ((num1 * 0) + (num2 * 1) + (num3 * 2) + (num4 * 3) + (num5 * 4) + (num6 * 5) + (num7 * 6) + (num8 * 7) + (num9 * 8) + (num10 * 9)) % 11
    if num11 == 10:
        num11 = 0

    print("CPF: %d%d%d.%d%d%d.%d%d%d-%d%d" % (num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11))

if len(cpf_cnpj) == 12:
    cnpj = cpf_cnpj

    num1 = int(str(cnpj)[:1])
    num2 = int(str(cnpj)[:2]) - (num1 * 10)
    if num2 <= 0:
        num2 = 0
    num3 = int(str(cnpj)[:3]) - (int(str(cnpj)[:2]) * 10)
    if num3 <= 0:
        num3 = 0
    num4 = int(str(cnpj)[:4]) - (int(str(cnpj)[:3]) * 10)
    if num4 <= 0:
        num4 = 0
    num5 = int(str(cnpj)[:5]) - (int(str(cnpj)[:4]) * 10)
    if num5 <= 0:
        num5 = 0
    num6 = int(str(cnpj)[:6]) - (int(str(cnpj)[:5]) * 10)
    if num6 <= 0:
        num6 = 0
    num7 = int(str(cnpj)[:7]) - (int(str(cnpj)[:6]) * 10)
    if num7 <= 0:
        num7 = 0
    num8 = int(str(cnpj)[:8]) - (int(str(cnpj)[:7]) * 10)
    if num8 <= 0:
        num8 = 0
    num9 = int(str(cnpj)[:9]) - (int(str(cnpj)[:8]) * 10)
    if num9 <= 0:
        num9 = 0
    num10 = int(str(cnpj)[:10]) - (int(str(cnpj)[:9]) * 10)
    num11 = int(str(cnpj)[:11]) - (int(str(cnpj)[:10]) * 10)
    num12 = int(str(cnpj)[:12]) - (int(str(cnpj)[:11]) * 10)
    num13 = ((num1 * 6) + (num2 * 7) + (num3 * 8) + (num4 * 9) + (num5 * 2) + (num6 * 3) + (num7 * 4) + (num8 * 5) + (num9 * 6) + (num10 * 7) + (num11 * 8) + (num12 * 9)) % 11
    num14 = ((num1 * 5) + (num2 * 6) + (num3 * 7) + (num4 * 8) + (num5 * 9) + (num6 * 2) + (num7 * 3) + (num8 * 4) + (num9 * 5) + (num10 * 6) + (num11 * 7) + (num12 * 8) + (num13 * 9)) % 11

    print("CNPJ: %d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % (num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14))

elif cpf != 9:
    print("CPF INVÁLIDO")
elif cnpj != 12:
    print("CNPJ INVÁLIDO")