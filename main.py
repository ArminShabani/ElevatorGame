from utils import calculator

def main():
    inpute = input("Enter 4 charecters(U/D): ")
    return calculator.calculate_floor(inpute)

if __name__ == "__main__":
    print(main())