import unittest
import pyotp
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


if __name__ == '__main__':
    unittest.main()
