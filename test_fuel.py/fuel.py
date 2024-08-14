def main():
    fraction = input('enter :')
    convert(fraction)
def convert(fraction):
    x , y = map(int , fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    elif x > y :
        raise ValueError
    percentage = round((x /y) * 100)
    gauge(percentage)
def gauge(percentage):
    try:
        if percentage <= 1 :
            return "E"
        elif percentage >= 99 :
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise ValueError
    except ValueError:
        pass
    except ZeroDivisionError:
        print("y must not be 0")
if __name__ == "__main__":
    main()
