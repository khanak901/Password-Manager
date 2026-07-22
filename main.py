import random
import string

passwords = {}

# ---------------- LOAD PASSWORDS ----------------
try:
    with open("password.txt", "r") as f:
        for line in f:
            if ":" in line:
                website, pwd = line.strip().split(":", 1)
                passwords[website] = pwd
except FileNotFoundError:
    pass


# ---------------- SAVE TO FILE ----------------
def save_file():
    with open("password.txt", "w") as f:
        for website, pwd in passwords.items():
            f.write(f"{website}:{pwd}\n")


# ---------------- GENERATE PASSWORD ----------------
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(10))
    return password


# ---------------- MENU ----------------
while True:

    print("\n========== PERSONAL PASSWORD MANAGER ==========")
    print("1. Save Password")
    print("2. View All Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Generate Password")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # ---------- SAVE ----------
    if choice == "1":
        website = input("Enter Website: ")

        if website in passwords:
            print("Password already exists for this website.")
        else:
            password = input("Enter Password: ")
            passwords[website] = password
            save_file()
            print("Password Saved Successfully!")

    # ---------- VIEW ----------
    elif choice == "2":

        if not passwords:
            print("No passwords saved.")
        else:
            print("\nSaved Passwords")
            print("--------------------------")
            for website, password in passwords.items():
                print(f"{website} : {password}")

    # ---------- SEARCH ----------
    elif choice == "3":

        website = input("Enter Website Name: ")

        if website in passwords:
            print(f"Password : {passwords[website]}")
        else:
            print("Website not found.")

    # ---------- UPDATE ----------
    elif choice == "4":

        website = input("Enter Website Name: ")

        if website in passwords:
            new_password = input("Enter New Password: ")
            passwords[website] = new_password
            save_file()
            print("Password Updated Successfully!")
        else:
            print("Website not found.")

    # ---------- DELETE ----------
    elif choice == "5":

        website = input("Enter Website Name: ")

        if website in passwords:
            del passwords[website]
            save_file()
            print("Password Deleted Successfully!")
        else:
            print("Website not found.")

    # ---------- GENERATE ----------
    elif choice == "6":

        print("Generated Password:", generate_password())

    # ---------- EXIT ----------
    elif choice == "7":

        print("Thank You for Using Password Manager!")
        break

    else:
        print("Invalid Choice! Please try again.")