new_whitelist=[]
whitelist=['192.168.0.1', '192.168.0.3', '192.168.0.2', '192.168.0.4', '192.168.0.5']
deleted_ip=input('Введите IP для удаления: ')
inserted_ip=input('Введите новый IP: ')
for i in whitelist:
    if i==deleted_ip:
        i=inserted_ip
        new_whitelist.append(i)
    else:
        new_whitelist.append(i)
new_whitelist.sort()
print('Обновлённый белый список: ', new_whitelist)
print('Индекс нового IP: ', new_whitelist.index(inserted_ip))