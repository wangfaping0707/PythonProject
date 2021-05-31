while True:
    try:
        x = int(input("Enter the first number:"))
        y = int(input("Enter the second number:"))
        value = x / y
        print('x / y is', value)
    except Exception as e:
        print("Invalid input:", e)
        print('Please try again')
    else:
        print("一切都结束了。。。。")
        break
