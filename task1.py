# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

st = 'адрьд вджыпьд дьабв лпьыдлв лабвлдь льлд'
st = list(st.split())
st2 = []
for i in st:
    if 'абв' in i:
        continue
    else:
        st2.append(i)
for i in st2:
    print(i, end= ' ')
