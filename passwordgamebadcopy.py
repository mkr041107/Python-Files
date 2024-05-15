def separate_numbers_and_letters(input_string):
    numbers = []
    letters = []
    has_v = False

    for char in input_string:
        if char.isdigit():
            numbers.append(int(char))
        elif char.isalpha():
            letters.append(char)
            if char.lower() == 'v':
                has_v = True

    return numbers, letters, has_v
while True:
    print("Rule 1: Make password 5 letters")
    passwordinput = input("Enter Password: ")
    if len(passwordinput)==5:
        print("Rule 2: Numbers in password must multiply to 25")
        passwordinput = input("Enter Password: ")
        has_v, numbers,letters= separate_numbers_and_letters(passwordinput)
        product_of_numbers = 1
        for num in numbers:
            product_of_numbers *= num
        if product_of_numbers == 25: # Check if product equals 25
         print("Rule 3: must include 5 V's")
         passwordinput = input("Enter Password: ")
        if has_v == True:
            print ("you win")
    else:
        print("Rule 2: Numbers in password must multiply to 25")
        passwordinput = input("Enter Password: ")
    
    
