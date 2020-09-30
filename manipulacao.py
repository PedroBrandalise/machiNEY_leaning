

with open('tuitesDoNey.txt', 'r',  encoding="utf-8") as file:
    data = file.read().replace('\n\n', '\n')




file.close()
# print((tuites))

file = open('tuitesDoNey2.txt', 'w+', encoding= 'utf-8')

file.write(data)
file.close()
print('-- o ousado terminou')



