from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")
'''
def write_key():
    try:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Key has been successfully written to key.key")
    except Exception as e:
        print(f"Error: {e}")

write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", 'r') as f:
        for line_number, line in enumerate(f.readlines(), start=1):
            data = line.rstrip()

            # Check if the line has the expected format
            if "|" not in data:
                print(f"Invalid data format in line {line_number}: {line}")
                continue  # Skip to the next iteration

            try:
                user, passw = data.split("|")
                print("User:", user, "| Password:", passw)
            except ValueError:
                print(f"Error in line {line_number}: Too many values to unpack. Expected 'user|password'.")



def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones(view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue