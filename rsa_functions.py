import number_theory_functions
import random
import math

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
        p = number_theory_functions.generate_prime(9)
        q = number_theory_functions.generate_prime(1)
        N = p * q
        phi_N = (p-1) * (q-1)
        
        # generate e and d
        e = 0
        d = 0
        for i in range(0, phi_N):
            if number_theory_functions.modular_inverse(i,phi_N) != None:
                e = i
                d = number_theory_functions.modular_inverse(i,phi_N)
                break
        
        return [(N, e), (N, d)]
        
        
                


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
        return number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])
        #return (easy_exp(m, self.public_key[1]) % self.public_key[0])
        


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
        return number_theory_functions.modular_exponent(c, self.private_key[1], self.private_key[0])
        #return (easy_exp(c, self.private_key[1]) % self.private_key[0])

def easy_exp(num, exp):
    bin_exp = bin(exp)
    sum = 0
    counter = 0
    for digit in bin_exp[2:]:
        if digit == 1:
            sum += pow(num, pow(2,counter))
        counter += 1
    return sum
    
def main():
    p = 7919
    q = 6841
    N = p * q
    phi_N = (p-1) * (q-1)
        
    # generate e and d
    e = 0
    d = 0
    for i in range(2, phi_N):
        if number_theory_functions.modular_inverse(i,phi_N) != None:
            e = i
            d = number_theory_functions.modular_inverse(i,phi_N)
            break
    print(e)
    print(d)
    
    new_RSA = RSA((N, e), (N, d))
    message = 7918
    encrypted_mess = new_RSA.encrypt(message)
    print ("the public key is {0}, {1}".format(new_RSA.public_key[0], new_RSA.public_key[1]))
    print ("the encrypted message is {0}".format(encrypted_mess))
    decrypt_mess = new_RSA.decrypt(encrypted_mess)
    print ("the decrypted message is {0}".format(decrypt_mess))
    
  
if __name__ == "__main__":
    main()