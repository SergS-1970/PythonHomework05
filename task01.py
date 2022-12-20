#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

f = open('task_1_text.txt', 'r', encoding = 'utf-8-sig')
sourceText = f.read().lower().split()
f.close()

print(sourceText)

newText = [i for i in sourceText if 'абв' not in i]
print(newText)
