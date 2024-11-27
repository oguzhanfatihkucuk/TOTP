import pyotp
import time
from SecretKey import secret

# Create the TOTP object
totp = pyotp.TOTP(secret)

# Continuously generate the code and write it to a file
while True:
    # Generate the current TOTP code
    current_code = totp.now()

    # Write the code to the file
    with open("../pythonProject6/generated_code.txt", "w") as file:
        file.write(current_code)

    print(f"Current TOTP code: {current_code} (Written to file)")

    # Wait for 30 seconds
    time.sleep(30)
