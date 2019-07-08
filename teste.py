from lowest_price import *

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


phone_number = int(input('Enter the phone number to search the lowest rate: '))

#FIND THE CORRESPONDING PREFIXES FOR THE GIVEN NUMBER
prefixes_list = find_corresponding_prefixes(all_operators, phone_number)

#FIND THE LOWEST RATE
lowest_value = find_lowest_value(prefixes_list)

print(f'\nThe operator that offers the lowest price for the number {phone_number} is Operator {lowest_value[0]}')
print(f'Correspoding prefix: {lowest_value[1]}')
print(f'Value: ${lowest_value[2]}')
