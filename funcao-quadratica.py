import cmath

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = (b ** 2) - (4 * a * c)
bhaskaraMais = (-b + cmath.sqrt(delta)) / (2 * a)
bhaskaraMenos = (-b - cmath.sqrt(delta)) / (2 * a)
bhaskaraZero = bhaskaraMais + bhaskaraMenos

if delta < 0:
    print("Não existem raizes reais")
elif delta == 0:
    print("Há uma única raiz real de valor: x=", bhaskaraZero)
elif delta > 0:
    print("Existem duas raízes reais de valores: x1=", bhaskaraMais, "e x2=", bhaskaraMenos)
