import sys

def find_corresponding_prefixes(all_operators, phone_number):

    corresponding_prefixes_list = list()
    phone_number_digits = [int(digit) for digit in str(phone_number)]

    for operator in all_operators:

        max_prefix_length = 0
        corresponding_prefix = 0

        for prefix in list(operator[1].keys()):
            
            prefix_digits = [int(digit) for digit in str(prefix)]
            is_valid_prefix = True
            

            for i in range(len(prefix_digits)):
                if prefix_digits[i] != phone_number_digits[i]:
                    is_valid_prefix = False
                    break
                
            if is_valid_prefix and len(prefix_digits) > max_prefix_length:
                max_prefix_length = len(prefix_digits)
                corresponding_prefix = prefix
        

        if corresponding_prefix != 0:
            corresponding_value = operator[1][corresponding_prefix]
            operator_name = operator[0]
            corresponding_prefixes_list.append((corresponding_value, operator_name, corresponding_prefix))
        
    return corresponding_prefixes_list
    

def find_lowest_value(corresponding_prefixes_list):
    lowest_value = sys.maxsize

    for prefix in corresponding_prefixes_list:
        if(prefix[0] < lowest_value):
            lowest_value = prefix[0]
            lowest_name_operator = prefix[1]
            lowest_prefix = prefix[2]
    return {'operator_name':lowest_name_operator, 'prefix':lowest_prefix, 'value':lowest_value}
