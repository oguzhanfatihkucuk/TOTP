import unittest
import pyotp
from PasswordGenerator import send_email
from SecretKey import secret


class TestTOTPSystem(unittest.TestCase):

    def setUp(self):
        """Test setup: Initialize the TOTP object."""
        self.totp = pyotp.TOTP(secret)

    def test_secret_key(self):
        """Test if the secret key is loaded correctly."""
        self.assertEqual(secret, "JBSWY3DPEHPK3PXP")

    def test_otp_generation(self):
        """Test if the generated OTP is valid and of the correct length."""
        otp = self.totp.now()
        self.assertTrue(otp.isdigit())  # Check if OTP is numeric
        self.assertEqual(len(otp), 6)  # Default length is 6 for TOTP

    def test_otp_verification(self):
        """Test the OTP verification process with a valid and invalid OTP."""
        otp = self.totp.now()
        self.assertTrue(self.totp.verify(otp))  # Should pass with the current OTP

        invalid_otp = "123456"
        self.assertFalse(self.totp.verify(invalid_otp))  # Should fail with incorrect OTP

    def test_custom_otp_length(self):
        """Test OTP generation with a custom length."""
        custom_totp = pyotp.TOTP(secret, digits=8)
        otp = custom_totp.now()
        self.assertEqual(len(otp), 8)

    def test_sha512_algorithm(self):
        """Test OTP generation with SHA-512 algorithm."""
        custom_totp = pyotp.TOTP(secret, digest='sha512')
        otp = custom_totp.now()
        self.assertTrue(otp.isdigit())
        self.assertEqual(len(otp), 6)

    def test_invalid_email_address(self):
        """Test with an invalid email address format."""
        invalid_email = "not_an_email"

        with self.assertRaises(ValueError):
            send_email(invalid_email, "123456")


if __name__ == '__main__':
    unittest.main()
