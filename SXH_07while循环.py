# i = 1
#
# while i <= 5:
#     print(i)
#     i = i + 1  # i += 1

# i = 1
#
# while i <= 100:
#     print(i)
#     i += 1
# print('循环结束')

#1+。。。+100
# i = 1
# j = 0
# while i <= 100:
#     j = j + i
#     i += 1
# print(j)

# i = 1
# j = 0
# while i <= 100:
#     if i%2 == 0:
#         j = j + i
#     i = i + 1
# print(j)

# i = 1
# while i <= 5:
#     if i == 4:
#         print('我吃饱了')
#         break
#     print(f'吃了第{i}个苹果')
#     i += 1

# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'有大虫子，第{i}个我不吃了')
#         i = i + 1
#         continue
#     print(f'我吃了第{i}个苹果')
#     i += 1

# 循环的嵌套
# j = 1
# while j <= 5:
#
#     i  = 1
#     while i <= j:
#         print('*',end = "")
#         i += 1
#     print() #换行
#     j = j + 1


# 打印九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end =" \t")
        i += 1
    print()
    j += 1







































































