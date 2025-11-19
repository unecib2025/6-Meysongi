tries=['ok', 'fail', 'fail', 'ok', 'fail']
a=tries.count('fail')
for i in range(a):
    tries.remove('fail')
tries.append('audit_completed')
tries.reverse()
c=tries.index('ok')
print('Колличество неудачных входов: ', a)
print('Итоговый список: ', tries)
print('Первый индекс ok: ', c)