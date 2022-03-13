

#
# Requirement is to check password strength
#
# Iength should be greater than 10
#
# 2. It should have one upper case one lower case, numberic and special character
# 3. it should not have special character @


# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
    SpecialSym = ['$', '#', '%']
    invalid = ['@']
    val = True

    if not len(passwd) > 10:
        print('length should be  be greater than 10')
        val = False

    # if not any(char.isdigit() for char in passwd):
    #     print('Password should have at least one numeral')
    #     val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@# ')
        val = False

    if any(char in invalid for char in passwd):
        print('Password should not have @ ')
        val = False


    if val:
        return val


# Main method
def main():
    passwd = 'eek12reyrfsfdse'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")


# Driver Code
if __name__ == '__main__':
    main()