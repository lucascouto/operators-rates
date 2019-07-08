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




#FIND THE CORRESPONDING PREFIXES FOR THE GIVEN NUMBER
def find_corresponding_prefixes(all_operators, phone_number):

    prefixes_list = list()
    phone_number_digits = [int(digit) for digit in str(phone_number)]

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
        

        if current_prefix != 0:
            current_value = operator[1][current_prefix]
            operator_name = operator[0]
            prefixes_list.append((current_value, operator_name, current_prefix))
        
    return prefixes_list
    

#FIND THE LOWEST RATE
def find_lowest_value(prefixes_list):
    lowest_value = sys.maxsize

    for prefix in prefixes_list:
        if(prefix[0] < lowest_value):
            lowest_value = prefix[0]
            lowest_name_operator = prefix[1]
            lowest_prefix = prefix[2]
    return lowest_name_operator, lowest_prefix, lowest_value




print(f'\nThe operator that offers the lowest price for the number {phone_number} is Operator {find_lowest_value()[0]}')
print(f'Correspoding prefix: {find_lowest_value()[1]}')
print(f'Value: ${find_lowest_value()[2]}')
