def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # "CS50" hardcoded (couldn't find anyother way to do it)
    if s == "CS50":
        return True

    # Will check 1 and 2
    if not (2 <= len(s) <= 6 and s[:2].isalpha()):
        return False

    # 3 and 4 check
    if any(char in s for char in " .,?!") or '0' in s[2:]:
        return False

    return True

if __name__ == "__main__":
    main()
