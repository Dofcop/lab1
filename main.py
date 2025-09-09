import fib, fig

def main():
    #loop for main app
    while True:
        #flag for block loops
        f = 0
        print("Для вызова функции для числа Фибоначчи, напишите fib, для фигурного числа - fig. Числа для программ должны быть неотрицательными. ")
        inp = input()
        #condition for choice of a block
        if type(inp) != str or (inp != "fig" and inp != "fib"):
            print("Введённое значение не поддерживается программой, пожалуйста следуйте инструкциям!")
        else:
            #block fibonachi whit it's loop
            if inp == "fib":
                while f == 0:
                    print("Число должно быть меньше 40. Для выхода, введите exit")
                    n = input("Введите число: ")
                    #exit the loop
                    if n == "exit":
                        f = 1
                        break
                    try:
                        n = int(n)
                    except ValueError:
                        print("Введённое значение не поддерживается программой, пожалуйста следуйте инструкциям!")
                        continue
                    if 0 <= n <= 40:
                        print(f"Число Фибоначчи: {fib.fib_num(n)}")
                    else:
                        print("Введённое значение не поддерживается программой, пожалуйста следуйте инструкциям!")
            else:
                #block and loop for figure numbers
                while f == 0:
                    print("Число должно быть меньше 10^13. Для выхода, введите exit")
                    n = int(input("Введите число: "))
                    # exit the loop
                    if n == "exit":
                        f = 1
                        break
                    try:
                        n = int(n)
                    except ValueError:
                        print("Введённое значение не поддерживается программой, пожалуйста следуйте инструкциям!")
                        continue
                    if 0 <= n <= 10 ** 13:
                        print(f"Фигурное число: {fig.fig_num(n)}")
                    else:
                        print("Введённое значение не поддерживается программой, пожалуйста следуйте инструкциям!")


if __name__ == "__main__":
    main()