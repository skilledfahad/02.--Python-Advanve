# # print(x / y)
# try:
#     print(x / y)
# except:
#     print("Something is not right")
#
# # get details by specifying error type
# try:
#     print(x / y)
# except NameError as e:
#     print("The error cause")
#     print(e)

# # try,except,finally
# try:
#     x = 5
#     y = 0
#     print(x / y)
# except :
#     print(y/x)
# finally:
#     print("problem need to resolved")
#
# try:
#     x = 5
#     print(x)
# except ZeroDivisionError as e:
#     print("The error cause")
#     print(e)
# finally:
#     print("any massage")

# Create your won error with "raise"
def five_ele_list(data):
    if len(data) != 5:
        raise "Must have 5 element in Data"
    print(data)


five_ele_list("apple")
five_ele_list([1, 2, 3, 4])
