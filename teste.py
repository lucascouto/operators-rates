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


phone_number = int(input('Enter the phone number to search the lowest rate: '))
phone_number_digits = [int(digit) for digit in str(phone_number)]



#FIND THE CORRESPONDING PREFIXES FOR THE GIVEN NUMBER
prefixes_list = list()

for operator in all_operators:

    max_prefix_length = 0
    current_prefix = 0

    for prefix in list(operator[1].keys()):
        
        prefix_digits = [int(digit) for digit in str(prefix)]
        is_valid_prefix = True
        

        for i in range(len(prefix_digits)):
            if prefix_digits[i] != phone_number_digits[i]:
                is_valid_prefix = False
                break
            
        if is_valid_prefix and len(prefix_digits) > max_prefix_length:
            max_prefix_length = len(prefix_digits)
            current_prefix = prefix
    
    
    #print(f'Operator: {operator[0]}')
    if current_prefix != 0:
        #print(f'The prefix: {current_prefix}')
        #print(f'The value: ${operator[1][current_prefix]}')
        current_value = operator[1][current_prefix]
        operator_name = operator[0]
        prefixes_list.append((current_value, operator_name, current_prefix))
    

#FIND THE LOWEST RATE
lowest_value = sys.maxsize

for prefix in prefixes_list:
    if(prefix[0] < lowest_value):
        lowest_value = prefix[0]
        lowest_name_operator = prefix[1]
        lowest_prefix = prefix[2]

print(f'\nThe operator that offers the lowest price for the number {phone_number} is Operator {lowest_name_operator}')
print(f'Correspoding prefix: {lowest_prefix}')
print(f'Value: ${lowest_value}')

    



      




