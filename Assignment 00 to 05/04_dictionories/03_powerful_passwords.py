# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)


# hashlib library se sha256 function import kar rahe hain jo passwords ko encrypt karta hai (hashing)
from hashlib import sha256

# Login function banaya gaya hai jo check karega ke diya gaya password sahi hai ya nahi
def login(email, stored_logins, password_to_check):
    """
    Agar email ke liye stored hashed password aur user ke diye gaye password ka hash match karein,
    to True return karega warna False.
    """

    # stored_logins dictionary se email ka hashed password le rahe hain
    # aur diya gaya password ko bhi hash karke dono ko compare kar rahe hain
    if stored_logins[email] == hash_password(password_to_check):
        return True  # Agar match karta hai to login successful
    return False     # Match nahi karta to login fail

# Ye function ek password ko SHA256 algorithm se hash karta hai (encrypt karta hai)
def hash_password(password):
    """
    Password ko SHA256 mein convert karta hai aur uska hexadecimal (safe) form return karta hai.
    """
    return sha256(password.encode()).hexdigest()  # password ko bytes mein convert kar ke hash banaya

# main function — yahan hum logins ko test kar rahe hain
def main():
    # Ye dictionary pre-defined logins ko store karti hai jismein keys emails hain
    # aur values unke hashed passwords hain (plain text password nahi rakha gaya)
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password = "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # password = "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password = "123!456?789"
    }

    # Neeche login function test kar rahe hain kuch correct aur incorrect passwords ke saath

    # Ye incorrect password hai, output: False
    print(login("example@gmail.com", stored_logins, "word"))

    # Ye correct password hai ("password"), output: True
    print(login("example@gmail.com", stored_logins, "password"))

    # Ye correct password hai ("Karel"), output: True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))

    # Incorrect case-sensitive password (should be "Karel"), output: False
    print(login("code_in_placer@cip.org", stored_logins, "karel"))

    # Incorrect password, output: False
    print(login("student@stanford.edu", stored_logins, "password"))

    # Correct password: "123!456?789", output: True
    print(login("student@stanford.edu", stored_logins, "123!456?789"))

# Ye line Python ka standard hai: jab ye file direct run ho to main() function call ho
if __name__ == '__main__':
    main()
