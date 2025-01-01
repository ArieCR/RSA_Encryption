import number_theory_functions
from random import randrange
class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        generate_prime = number_theory_functions.generate_prime 
        x,y = generate_prime(digits//2 + 1),generate_prime(digits//2 + 1)
        phi_N = (x-1)*(y-1)
        N = x*y
        e = randrange(N//2,N//2+N//4)
        d = number_theory_functions.modular_inverse(e,phi_N)
        return RSA((N,e),(N,d))
    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        N,e = self.public_key
        c =  number_theory_functions.modular_exponent(m,e,N)

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N,d = self.private_key
        m = number_theory_functions.modular_exponent(c,d,N)
