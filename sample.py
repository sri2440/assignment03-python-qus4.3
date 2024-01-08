import re

password_pattern = re.compile(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
)

# Test the pattern with passwords
valid_passwords = ['StrongPwd1!', 'AnotherPwd@2022', 'Secure123$']
invalid_passwords = ['weakpassword', 'noSpecialCharacter123', 'Short1!']

print("Valid Passwords:")
for password in valid_passwords:
    if password_pattern.match(password):
        print(password)

print("\nInvalid Passwords:")
for password in invalid_passwords:
    if not password_pattern.match(password):
        print(password)
