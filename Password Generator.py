import random
import string

def generate_password(complexity):
    if complexity == "mild":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        print("Invalid complexity level")
        return None

    length = 12  # You can change the length of the password as desired

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Complexity Levels:")
    print("1. Mild")
    print("2. Medium")
    print("3. Hard")
    choice = input("Choose complexity (1/2/3): ")

    if choice == "1":
        complexity = "mild"
    elif choice == "2":
        complexity = "medium"
    elif choice == "3":
        complexity = "hard"
    else:
        print("Invalid choice")
        return

    password = generate_password(complexity)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()
