from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

password = '0000'
hash = context.hash(secret=password)
print(hash)

user_pass = '0000'
is_valid = context.verify(user_pass, hash)
print(is_valid)