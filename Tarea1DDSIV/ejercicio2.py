#luis Enrique Lopez Chaidez DDSIV
#Solicitar dos números y decir si uno es múltiplo del otro.

print('Numeros multiplos')
print('introduce el primer numero')
no1 = int(input())
print('introduce el segundo numero')
no2 = int(input())

if (no1 % no2) == 0:
    print('%d es multiplo de %d' % (no1,no2))
else:
    print('%d no es multiplo de %d' % (no1,no2))
if (no2 % no1) == 0:
    print('%d es multiplo de %d' % (no2,no1))
else:
    print('%d no es multiplo de %d' % (no2,no1))