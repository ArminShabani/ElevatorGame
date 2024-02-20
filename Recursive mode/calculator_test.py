def calculate_floor():
    floor = 0
    array = []
    inpute = input("Enter 4 charecters(U/D): ")
    inpute = inpute.upper()
    if len(inpute) == 4:
        for i in inpute:
            array.append(i)
        for words in array:
                if words == 'U':
                    floor += 1
                elif words == 'D':
                    floor -= 1
                else: 
                    print("invalid Entry")
                    break
        print(floor)
    else: 
        print("index out of range")
    

calculate_floor()