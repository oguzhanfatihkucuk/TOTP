import pyotp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from SecretKey import secret

# Create the TOTP object
totp = pyotp.TOTP(secret)


# E-posta gönderme ve dosyaya yazma fonksiyonu
def send_email_and_save_to_file(recipient_email, otp_code):
    sender_email = "oguzhanfatihk@gmail.com"  # Gönderen e-posta adresi
    sender_password = "uxgdqgepqmxabihb"  # Gönderen e-posta şifresi

    # E-posta içeriği
    subject = "Your TOTP Code"
    body = f"Your One-Time Password (TOTP) code is: {otp_code}"

    # MIMEText ile e-posta içeriğini oluşturuyoruz
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # E-posta gönderme işlemi
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Güvenli bağlantı başlat
            server.login(sender_email, sender_password)  # Giriş yap
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)  # E-postayı gönder
            print(f"OTP code sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email or write to file: {e}")


# Ana program döngüsü
while True:
    # Kullanıcıdan şifre üretme isteği alıyoruz
    user_input = input("Do you want to generate a TOTP code? (yes/no): ").strip().lower()

    if user_input == "yes":
        # Şifreyi oluştur
        otp_code = totp.now()

        # Kullanıcıya şifrenin nereye gönderileceğini soruyoruz
        delivery_method = input(
            "Do you want the OTP code sent to your email or displayed in the console? (email/console): ").strip().lower()

        if delivery_method == "email":
            recipient_email = input("Please enter your email address: ").strip()
            send_email_and_save_to_file(recipient_email, otp_code)
        elif delivery_method == "console":
            print(f"Your OTP code is: {otp_code}")

        else:
            print("Invalid option selected.")

        # 30 saniye beklemeden önce kullanıcının isteği doğrultusunda işlem yapılacak
        countdown_time = 30
        print(f"\nPlease wait for {countdown_time} seconds before generating a new OTP code.")

        while countdown_time > 0:
            # Her saniyede bir sayacı güncelle
            print(f"Next OTP in {countdown_time} seconds", end="\r")
            time.sleep(1)
            countdown_time -= 1

        print("\nYou can now generate a new OTP code!")

    elif user_input == "no":
        print("No OTP code generated.")


