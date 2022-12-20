# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('Data_output.txt', 'w') as data:
    data.write('AAAAAgBBBBBtttRRRYGGGaaaaaaaaaaaaaaaaaaabbbbbbbbbbkkkkgilkkkkk')

with open('Data_output.txt', 'r') as data:
    string = data.readline()

def coding(txt):
     count = 1
     res = ''
     for i in range(len(txt)-1):
         if txt[i] == txt[i+1]:
             count += 1
         else:
             res = res + str(count) + txt[i]
             count = 1
     if count > 1 or (txt[len(txt)-2] != txt[-1]):
         res = res + str(count) + txt[-1]
     return res

def decoding(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            num += txt[i]
        else:
            res = res + txt[i] * int(num)
            num = ''
    return res


with open('Data_output.txt', 'r') as file:
    decoded_string = file.read()

with open('Data_encoding.txt', 'w') as file:
    encoded_string = coding(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + coding(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')