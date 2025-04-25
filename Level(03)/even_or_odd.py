def even_or_odd(number):
    number=str(number)
    check=number[-1]
    final_step= int(check)%2
    if final_step == 0:
        print("even")
    else:
        print("odd")

        