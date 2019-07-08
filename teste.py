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

#FIND THE LOWEST RATE
lowest_rate = sys.maxsize
for operator in all_operators:
    for prefix in list(operator[1].keys()):
        if operator[1][prefix] < lowest_rate:
            lowest_rate = operator[1][prefix]
            lowest_prefix = prefix
            lowest_operator = operator[0]


print(f'The lowest rate is {lowest_rate} for prefix {lowest_prefix} from {lowest_operator}')


