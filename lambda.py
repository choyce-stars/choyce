# # 람다 표현식

# def p_ten(x):    # 일반적인 함수
#     return x + 10

# print(p_ten(1))

# lambda x: x + 10    # 람다 표현식은 함수 객체를 돌려줌
# <function <lambda> at 0x00000207D4A43EC0>    # 람다 표현식은 이름이 없음 - 익명 함수로도 부름

# plus_ten = lambda x: x + 10    # 람다로 만든 익명함수 호출하려면
# print(plus_ten(1))    # 변수에 함수를 할당해주면 됨

# print((lambda x: x + 10)(1))    # 람다 표현식 자체를 호출하려면 람다 식을 괄호로 묶어서 사용

# print((lambda x: y = 10; x + y)(1))    # 람다 표현식 안에서 변수 생성 못함

# y = 10
# print((lambda x: x + y)(1))    # 바깥에 있는 변수는 끌어와 쓸 수 있음
# print((lambda x, y: x + y)(1, 2))    # 애초에 변수를 2개 가지고 있어도 됨

# def p_ten(x):
#     return x + 10

# a = list(map(p_ten, [1, 2, 3]))
# print(a)    # map 함수에 직접 만든 함수를 넣어도 됨

# b = list(map(lambda x: x + 10, [1, 2, 3]))
# print(b)    # 함수 대신 람다 표현식을 사용

# 람다 표현식으로 매개 변수가 없는 함수 만들기
# a = (lambda: 1)()
# print(a)

# x = 10
# b = (lambda: x)()
# print(b)

# def hello():    # 매개변수가 없는 함수
#     return 10

# x = hello()
# print(x)


# # 람다 표현식과 map, filter, reduce 함수 활용

# map 사용하기

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# print(b)    # 람다 표현식에서 if 사용했다면 else도 같이 사용해야함

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []

# for i in a:
#     if i % 3 == 0:
#         b.append(str(i))
#     else:
#         b.append(i)
# print(b)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# print(b)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def f(x):
#     if x == 1:
#         return str(x)
#     elif x == 2:
#         return float(x)
#     else:
#         return x + 10

# b = list(map(f, a))
# print(b)

# a = [1, 2, 3, 4, 5]
# b = [2, 4, 6, 8, 10]
# x = list(map(lambda x, y: x * y, a, b))    # 객체 여러 개 넣기
# print(x)


# filter 사용하기

# def f(x):
#     return x > 5 and x < 10

# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# b = list(filter(f, a))    # 함수를 적용하여 참인 값만 가져오고 거짓인 값은 버림
# print(b)

# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# b = list(filter(lambda x: x > 5 and x < 10, a))
# print(b)

# reduce 사용하기

# from functools import reduce

# def f(x, y):
#     return x + y

# a = [1, 2, 3, 4, 5]
# print(reduce(f, a))

# a = [1, 2, 3, 4, 5]
# b = reduce(lambda x, y: x + y, a)
# print(b)

# 람다 표현식과 리스트 표현식

# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# b = [i for i in a if i > 5 and i < 10]
# print(b)


# a = [1, 2, 3, 4, 5]
# x = a[0]

# for i in range(len(a) - 1):
#     x = x + a[i + 1]

# print(x)


# 32.4
# files = ['font', '1.png', '10.png', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docs']

# print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))



# # 32. 5
# 문자열 그 자체를 보고 변경시키는 코드
files = input().split()

print(list(map(lambda x: '{:0>7}'.format(x) if len(x) <= 6 else '{:0>8}'.format(x), files)))



# 숫자와 문자열을 따로 보고 변경시키는 코드
# filst = input().split()

# print(list(map(lambda x : '{0:03d}'.format(int(x.split('.')[0])) + '.' +  x.split('.')[1], filst)))
