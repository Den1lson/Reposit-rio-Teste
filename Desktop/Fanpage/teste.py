num1 = int(input("Digite um número:"))
num2 =  int(input("Digite outro número:"))

s = num1 + num2
sb = num1 - num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
rd = num1 % num2
e = num1 ** num2

print("A soma é {}, \n -subtração {}, \n -mutiplicação {}, \n -divisão {}, \n -divisão de inteiro {}, \n -reto da divisão {}, \n -exponenciação {} "
      .format(s, sb, m, d, di, rd, e))
