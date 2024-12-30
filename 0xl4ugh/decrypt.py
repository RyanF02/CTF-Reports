import base64
import hashlib
from cryptography.fernet import Fernet

# Function to generate a key from the password
def generate_key(password):
    password_bytes = password.encode('utf-8')
    key = hashlib.sha256(password_bytes).digest()  # SHA256 to get a 32-byte key
    return base64.urlsafe_b64encode(key)  # Fernet requires the key to be in base64 format

# Function to decrypt the file with a given password
def try_decrypt(encrypted_file_name, password):
    try:
        key = generate_key(password)
        cipher = Fernet(key)

        # Read the encrypted file content
        with open(encrypted_file_name, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Attempt to decrypt
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data  # Return the decrypted content if successful
    except Exception:
        return None  # Return None if decryption fails

def main():
    encrypted_file_name = "encrypted_friend3.txt"#input("Enter the encrypted file name: ")
    wordlist_file = "wordlist.txt"#input("Enter the wordlist file name: ")

    # Open the wordlist and iterate through passwords
    with open(wordlist_file, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()  # Remove any extra whitespace
            print(f"Trying password: {password}")

            decrypted_data = try_decrypt(encrypted_file_name, password)
            if decrypted_data:
                # If decryption is successful, save the decrypted file
                original_file_name = encrypted_file_name.replace("encrypted_", "")
                with open(original_file_name, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

                print(f"Success! File decrypted with password: {password}")
                print(f"Decrypted file saved as '{original_file_name}'.")
                return  # Exit after successful decryption

    print("Decryption failed. No valid password found in the wordlist.")

if __name__ == "__main__":
    main()

