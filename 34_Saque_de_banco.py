valor = float(input())
resultado = '\n'

mod50 = valor % 50
if (mod50 == valor):
    resultado += 'Notas de 50: %d\n' % 0
else:
    resultado += 'Notas de 50: %d\n' % (valor / 50)

mod20 = mod50 % 20
if (mod20 == mod50):
    resultado += 'Notas de 20: %d\n' % 0
else:
    resultado += 'Notas de 20: %d\n' % (mod50 / 20)

mod10 = mod20 % 10
if (mod10 == mod20):
    resultado += 'Notas de 10: %d\n' % 0
else:
    resultado += 'Notas de 10: %d\n' % (mod20 / 10)

mod5 = mod10 % 5
if (mod5 == mod10):
    resultado += 'Notas de 5: %d\n' % 0
else:
    resultado += 'Notas de 5: %d\n' % (mod10 / 5)

mod2 = mod5 % 1
if (mod2 == mod5):
    resultado += 'Notas de 1: %d\n' % 0
else:
    resultado += 'Notas de 1: %d\n' % (mod5 / 1)

print(resultado)  

