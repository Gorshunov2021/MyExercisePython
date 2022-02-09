# file = open("test2.txt", "w")
# file.close()
#
# file = open("test.txt", "w")
# file.write("Hello World")
# file.close()

# file = open("test.txt", "a")
# file.write(" 33")
# file.close()

# try:
#     file = open("test.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("Not Found")
# except IOError:
#     print("Something else")

# with open('test.txt', 'r') as file:
#     print(file.read())

#
# import os
# print(os.path.exists("D:\\test.txt"))
# print(os.path.exists("D:\\test10.txt"))


# try:
#     with open("D:\\test.txt") as file:
#         print("file is open")
# except:
#     print('no open')


# import shutil
# shutil.copyfile("D:\\test.txt", "D:\\test2.txt")

# import shutil
# shutil.copy("D:\\test.txt", "D:\\folder")


# import shutil
# shutil.copy2("D:\\test.txt", "D:\\folder\\test2.txt")

#
# import os
# print(os.path.getsize("D:\\test.txt"))


# import os
# with open("D:\\test.txt") as file:
#     file.seek(0, os.SEEK_END)
#     print(file.tell())


#
# import os
# os.rename("D:\\test333.txt", "D:\\test.txt")


import shutil
shutil.move("D:\\test3336.txt", "D:\\test.txt")






# file = open(r"D:\test2.txt", "w")
# file.close()


# f = open(r"D:\test.txt", "w")
# print(f.name)
# f.close()
