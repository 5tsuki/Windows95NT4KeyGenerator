# XXX–XXXXXXX 
import random

def generate_site():
    rejected_sites = [333, 444, 555, 666, 777, 888, 999]
    new_site = random.randint(0, 999)
    while new_site in rejected_sites:
        new_site = random.randint(0, 999)
    return str(new_site).rjust(3, '0')

def generate_second_segment():
    first_digits = str(random.randint(0, 999999))
    last_digit = random.randint(0, 9)
    while last_digit == 0 or last_digit >= 8:
        last_digit = random.randint(0, 9)
    second_segment = (first_digits + str(last_digit)).rjust(7, '0')
    
    digit_sum = 0
    for digit in second_segment:
        digit_sum += int(digit)
    
    return second_segment, digit_sum

def check_second_segment():
    second_segment, digit_sum = generate_second_segment()
    while digit_sum % 7 != 0:
        second_segment, digit_sum = generate_second_segment()
    
    return second_segment

# XXXXX-OEM-XXXXXXX-XXXXX
def generate_oem_date():
    day = random.randint(0, 366)
    years = ["95", "96", "97", "98", "99" , "00", "01", "02", "03"]
    year = random.choice(years)
    return (str(day) + year).rjust(5, '0')

def generate_oem_second_segment():
    first_digits = str(random.randint(0, 99999))
    last_digit = random.randint(0, 9)
    while last_digit == 0 or last_digit >= 8:
        last_digit = random.randint(0, 9)
    
    second_segment = ("0" + first_digits + str(last_digit)).rjust(7, '0')
    
    digit_sum = 0
    for digit in second_segment:
        digit_sum += int(digit)
    
    return second_segment, digit_sum

def check_oem_second_segment():
    second_segment, digit_sum = generate_oem_second_segment()
    while digit_sum % 7 != 0:
        second_segment, digit_sum = generate_oem_second_segment()
    
    return second_segment

def generate_last_segment():
    return str(random.randint(0, 99999)).rjust(5, '0')
    

if __name__ == "__main__":
    key_file = open("key.txt", "w")
    key_type = input("Insert what key you need (normal, oem): ")
    key = ""

    while not (key_type in ["normal", "oem"]):
        key_type = input("Error, Insert what key you need (normal, oem): ")

    if key_type == "normal":
        key = generate_site() + "-" + check_second_segment()
    else:
        key = generate_oem_date() + "-" + "OEM" + "-" + check_oem_second_segment() + "-" + generate_last_segment()
    
    key_file.write(key)

    print("Key Generated!")