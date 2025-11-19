cleaned_journal=[]
journal=['alert', 'spam', 'login', 'error', 'spam', 'alert']
for i in journal:
    if i == 'spam':
        continue
    else:
        cleaned_journal.append(i)
cleaned_journal.append('END_LOG')
cleaned_journal.reverse()
counts=journal.count('alert')
print(cleaned_journal)
print('Колличество alers: ', counts)
