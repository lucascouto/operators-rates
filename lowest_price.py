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
    

def find_lowest_value(prefixes_list):
    lowest_value = sys.maxsize

    for prefix in prefixes_list:
        if(prefix[0] < lowest_value):
            lowest_value = prefix[0]
            lowest_name_operator = prefix[1]
            lowest_prefix = prefix[2]
    return lowest_name_operator, lowest_prefix, lowest_value
