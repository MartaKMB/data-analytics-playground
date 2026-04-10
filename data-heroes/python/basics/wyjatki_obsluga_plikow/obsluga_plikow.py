# file = open("./hello.txt", "w", encoding="utf-8")
# file.write("Hello file!\n")
# file.write("534")
# file.close()

# file = open("./hello.txt", "r", encoding="utf-8")
# content = file.read()
# file.close()

# print(content)

with open("hello2.txt", "w", encoding="utf-8") as file:
    file.write("Hello again\n")
    file.write("This is safer using with\n")
    file.write("Third line\n")

with open("hello2.txt", "r", encoding="utf-8") as file:
    content = file.read()

# print(content.splitlines())
print(content.split())

with open("hello2.txt", "r", encoding="utf-8") as file:
    # content = file.readline()
    content = file.readlines()

print(content)
