def calculate_floor(string):
    floor = 0
    array = []
    string = string.upper()
    if len(string) == 4:
        for i in string:
            array.append(i)
        for words in array:
            if words == 'U':
                floor += 1
            elif words == 'D':
                floor -= 1
        return floor
    else:
        print("index out of range")
