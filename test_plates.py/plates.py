def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str):
    if len(s) < 2 or len(s) > 6 or s[0].isdigit() or s[1].isdigit():
        return False

    num_found = False
    for each in s[2:]:
        if each.isdigit():
            if not num_found:
                if each == '0':
                    return False
                num_found = True
        elif num_found:
            return False
    return True
main()
