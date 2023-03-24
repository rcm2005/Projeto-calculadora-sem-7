print('Insira apenas números entre 0 a 99')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite outro número: '))

if a < 0 or a > 99 or b < 0 or b > 99:
    print('Por favor, apenas números inteiros de 0 a 99')

   
car1 = a // 10    
car2 = a % 10
 
if car1 == 7:
    car1 = 0
else: car1 = car1
    
if car2 == 7:
    car2 = 0
else: car2 = car2

car1 = car1 *10

numero1 = car1 + car2


car3 = b // 10
car4 = b % 10  


if car3 == 7:
    car3 = 0
else:car3 = car3
    
    
if car4 == 7:
    car4 = 0
else:car4 = car4
    
    
car3 = car3 * 10


numero2 = car3 + car4


soma = numero1 + numero2

print(soma)