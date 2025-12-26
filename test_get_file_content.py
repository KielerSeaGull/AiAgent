from functions.get_file_content import get_file_content

print("Result for current directory, main.py:")
print(get_file_content("calculator", "lorem.txt"))
print("-------------------------------")

print("Result for 'pkg/calculator.py':")
print(get_file_content("calculator", "pkg/calculator.py"))
print("-------------------------------")

print("Result for '/bin/cat'")
print(get_file_content("calculator", "/bin/cat"))
print("-------------------------------")

print("Result for 'pkg/does_not_exist.py' file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("-------------------------------")