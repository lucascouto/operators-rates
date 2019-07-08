import sys

num_operators = int(input('How many operators do you want to register? '))
print("="*30)

all_operators = list()

for i in range(num_operators):
    rates_table = dict()
    operator_name = input(f'Name of operator {i+1}: ')
    operator_entries = int(input(f'How many entries for {operator_name}? '))
    print()
    for j in range(operator_entries):
        prefix = int(input('Prefix: '))
        value = float(input('Value: '))
        rates_table[prefix] = value
        
        print()
    print(f'Rates table for {operator_name}: {rates_table}')
    all_operators.append((operator_name, rates_table))
    print("="*30)

print(all_operators)

phone_number = int(input('Enter the phone number to search the lowest rate: '))
phone_number_digits = [int(digit) for digit in str(phone_number)]

#FIND THE LOWEST RATE
lowest_rate = sys.maxsize
for operator in all_operators:
    for prefix in list(operator[1].keys()):
        
        prefix_digits = [int(digit) for digit in str(prefix)]
        max_prefix_length = 0
        is_valid_prefix = True
        current_prefix = 0

        for i in range(len(prefix_digits)):
            if prefix_digits[i] != phone_number_digits[i]:
                is_valid_prefix = False
                break
            
        if is_valid_prefix and len(prefix_digits) > max_prefix_length:
            max_prefix_length = len(prefix_digits)
            current_prefix = prefix
    
    print(f'Operadora: ${operator[0]}')
    if current_prefix != 0:
        print(f'O prefixo: {current_prefix}')
        print(f'O valor: ${operator[1][prefix]}')
    else:
        print('Sem prefixo correspondente!')
            



      




