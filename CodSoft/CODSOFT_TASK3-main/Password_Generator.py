import random
import string
import pyperclip

def get_user_options():
    print("\nCustomize Your Password:")
    length = int(input("Enter the desired length of the password: "))
    
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    return length, include_lowercase, include_uppercase, include_digits, include_special_chars

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    character_pool = ""
    
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    if not character_pool:
        print("Error: No character types selected. Cannot generate password.")
        return None
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def evaluate_strength(password):
    length = len(password)
    categories = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ]
    
    score = length + sum(categories) * 2
    
    if score >= 12:
        return "Strong"
    elif score >= 8:
        return "Medium"
    else:
        return "Weak"

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to 'passwords.txt'.")

def display_history(history):
    if not history:
        print("No history available.")
    else:
        print("\nPassword History:")
        for i, record in enumerate(history, start=1):
            print(f"{i}. {record}")

def main():
    history = []
    
    while True:
        print("\n--- Password Generator Menu ---")
        print("1. Generate Custom Password")
        print("2. Generate Password with Random Preset")
        print("3. View Password History")
        print("4. Clear Password History")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            length, include_lowercase, include_uppercase, include_digits, include_special_chars = get_user_options()
            
            if length < 1:
                print("Error: Password length must be at least 1.")
                continue
            
            password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)
        
        elif choice == '2':
            length = random.randint(8, 16)
            include_lowercase = include_uppercase = include_digits = include_special_chars = True
            password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)
            print(f"\nGenerated Password with Random Preset (Length: {length}):")
        
        elif choice == '3':
            display_history(history)
            continue
        
        elif choice == '4':
            history.clear()
            print("Password history cleared.")
            continue
        
        elif choice == '5':
            print("Exiting the password generator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")
            continue
        
        if password:
            print(f"\nGenerated Password: {password}")
            strength = evaluate_strength(password)
            print(f"Password Strength: {strength}")
            pyperclip.copy(password)
            print("Password copied to clipboard.")
            save_option = input("Would you like to save this password? (yes/no): ").strip().lower()
            if save_option == 'yes':
                save_password(password)
            history.append(password)

if __name__ == "__main__":
    main()
