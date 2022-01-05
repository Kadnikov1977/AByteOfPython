import sys

print('Аргументы командной строки')

for i in sys.argv:
    print(i)

print(sys.path)
print(sys.api_version)
print(sys.int_info)
