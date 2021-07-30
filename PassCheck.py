# we will be taking a password as a combination of alphanumeric characters along with special
# characters,and check whether the password is valid or not with the help of few conditions.
# Primary conditions for password validation :
# Minimum 8 characters.
# The alphabets must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].
pas = input("enter a pass:")
l, u, d, s = 0, 0, 0, 0
if (len(pas) >= 8):
    for i in pas:
        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            d += 1
        if (i == '@' or i == '$' or i == '_'):
            s += 1
if (l >= 1 and u >= 1 and d >= 1 and s >= 1):
    print("Pass is valid.")
else:
    print("pass is invalid.")
# l, u, p, d = 0, 0, 0, 0
# s = "Vineet@123"
# s=input("Enter pass:")
# if (len(s) >= 8):
#     for i in s:
#
#         # counting lowercase alphabets
#         if (i.islower()):
#             l+=1
#
#             # counting uppercase alphabets
#         if (i.isupper()):
#             u+=1
#
#             # counting digits
#         if (i.isdigit()):
#             d+=1
#
#             # counting the mentioned special characters
#         if(i=='@'or i=='$' or i=='_'):
#             p+=1
# if (l>=1 and u>=1 and p>=1 and d>=1 ):
#     print("Valid Password")
# else:
#     print("Invalid Password")
