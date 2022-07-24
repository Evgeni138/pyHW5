with open('file1_task4.txt', 'r') as file:
    st = file.read()

st_new = ''
count = 1
for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        count +=1
    else:
        st_new = st_new + str(count) + st[i-1]
        count = 1
st_new = st_new + str(count) + st[i]

with open('file2_task4.txt', 'w') as file:
    file.write(st_new)
