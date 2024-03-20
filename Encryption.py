from cryptography.fernet import Fernet
# Step 1: Generate a key using Fernet
key = Fernet.generate_key()
file_path = 'H:/PI/encrypted_password.txt'

# Convert the key to a string for easier handling
key_str = key.decode('utf-8')
choice = input("'1' to login in, '2' for new password")
# Step 2: Use the generated key to encrypt the user's password

def openfile(file_path):
    with open(file_path, 'rb') as file:
        data = file.read().split(b',')
        key = data[0]
        ep = data[1]
    return key,ep
def decrypt(key,ep):
    fernet = Fernet(key)
    dp = fernet.decrypt(ep)
    return dp.decode()
cipher_suite = Fernet(key)
if choice == '1':
    pw = input("Enter Password: ")

    key,ep =  openfile(file_path)
    dpp = decrypt(key,ep)
    if pw == dpp :
     print ("Youre Right!!!")
    else:
      print("Youre Wrong!!")
# Convert the encrypted password to a string for easier handling
if choice == '2':
    npw = input("Enter New Password: ")
    eencrypted_password = cipher_suite.encrypt(npw.encode())
    eeencrypted_password = cipher_suite.decrypt(eencrypted_password).decode('utf-8')
    with open(file_path,'wb') as file:
     file.write(key+ b',' + eencrypted_password)
# Step 3: Save the encrypted password to a text file



