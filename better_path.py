path = input('Pase your file path:')
finale_path = ''
for i in path:
    if i == '\\':
        finale_path = finale_path + '/'
    else:
        finale_path = finale_path + i
print(finale_path)