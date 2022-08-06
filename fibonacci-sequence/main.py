fibonacci_sequence = [0,1]

number = int(input('\nFibonacci dizisinin ilk kaç terimi hesaplansın : '))

for i in range(number):

    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print(f'\n{fibonacci_sequence}\n')
