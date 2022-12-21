def convert_str_to_int(str_num_list):
    new_list = []
    for item in str_num_list:
        int_num= int(item)
        new_list.append(int_num)
    return new_list
str_num_list = input("Enter Array Seperated By Comma").split(",")
rotate_times = int(input("Enter No.Of Times To Rotate:"))
int_list = convert_str_to_int(str_num_list)
rotate_times = rotate_times % len(int_list)

first_part=int_list[0:rotate_times]
second_part=int_list[rotate_times:]
second_part.extend(first_part)
print(second_part)
