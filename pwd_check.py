# import re
# password = input("Enter string to test: ")
# # if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
# #     print("match")
# # else:
# #     print("mismatch")
# True if (re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.[@#$%^&+=])[A-Za-z0-9@#$%^&+=]{8,}$', password)):

import re

while True:
    print('Input a strong password.')
    password = input()
    if re.match(r'[A-Z and a-z and 0-9 and #$%^&+=]{8,}', password):
        print('Very nice password. Much secure')
        break
    else:
        print('Not a valid password')