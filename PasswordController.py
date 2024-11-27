import pyotp
import time
from SecretKey import secret

# Create the TOTP object
totp = pyotp.TOTP(secret)

# Check the code in an infinite loop
while True:
    # Read the code from the generated_code.txt file
    try:
        with open("../pythonProject2/generated_code.txt", "r") as file:
            generated_code = file.read().strip()

        # Ask the user to enter a code
        input_code = input("Please enter the TOTP code: ")

        # Verify the code
        if totp.verify(input_code):
            print("Verification successful!")
        else:
            print("Verification failed!")

    except FileNotFoundError:
        print("Code file not found. Please try again later.")

    # Wait for 1 second and try again
    time.sleep(1)
