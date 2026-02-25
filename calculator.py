import csv
from tabulate import tabulate
def main():
    print("---CalC v1.0\n")
    print("Let's begin 🏁\n")
    x = get_number("Enter a number")
    with open("file",'w+') as file:
        writer = csv.DictWriter(file,fieldnames=["x","operation","y","Result"])
        writer.writeheader()
        while True:
            print("Choose Operation:\n+ - * / % p r\n(h for help)" )
            while True:
                match input().strip():
                    case "+":
                        x = add(x,writer)
                    case "-":
                        x= sub(x,writer)
                    case "*":
                        x= mul(x,writer)
                    case "/":
                        x= div(x,writer)
                    case "%":
                        x= modulus(x,writer)
                    case "p"|"P":
                        x=power(x,writer)
                    case "r"|"R":
                        x= root(x,writer)
                    case "h"|"H":
                        help()
                        continue
                    case _:
                        print("INVALID Operation")
                        continue
                break
            print(f"\nAns: {x}")
            print("\n🧮 Continue calculation --> Space\n📝 Print Recipt & exit --> Enter\n🛑 Exit --> Q")
            match input(): 
                case " ":
                    continue
                case "Q"|"q":
                    print("\n\n--Thank you")
                    return
                case _:                     #We asked Enter for printing but in reality we cant read enter, here anything else except space and q triggers print including Enter(Gives empty character)
                    receipt(file)
                    return



def help():
    print(
        "\n+ ---> Addition\n- ---> Subtraction\n* ---> Multiplication\n\\ ---> Division\n% ---> Modulus\np ---> Power\nr ---> Root"
        )

def get_number(s):
    print(s,end=" ")
    while True:
        y = input()
        try:
            y = float(y)
            return y
        except ValueError:
            print("INVALID\nEnter valid number",end =" ")

def add(x,writer):
    y = get_number("Number")
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x+y
def sub(x,writer):
    y = get_number("Number")
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x-y
def mul(x,writer):
    y = get_number("Number")
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x*y
def div(x,writer):
    y = get_number("Number")
    if y == 0:
        print("Syntax Error (ans retained)")
        return x
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x/y
def modulus(x,writer):
    y = get_number("Number")
    if y == 0:
        print("Syntax Error (ans retained)")
        return x
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x%y

def power(x,writer):
    y = get_number("Number")
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x**y
def root(x,writer):
    y = get_number("Number")
    if y == 0:
        print("Syntax Error (ans retained)")
        return x
    writer.writerow({"x":x,"operation":"+","y":y,"Result":x+y})
    return x**1/y

def receipt(file):
    file.seek(0)
    reader = csv.DictReader(file)
    history = list(reader)
    print(tabulate(history,tablefmt="tsv"))



if __name__ == "__main__":
    main()