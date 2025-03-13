def add(a,b):
    return a + b

def sub(a,b):
    print('결과는 ',a-b)
    # return a - b

def mul(a,b):
    return a * b

def indata():
    a = int(input("숫자를 입력하세요 >> "))
    return a

def add_many(*args,mode=;'k'):
    print(type(args))
    result = 0
    for i in args:
        # print(i)
        result += i

print(add_many(1,2,3,4,5,6,7,8,9))
print(add_many(1,2,3,4,5,6,7,8,mode='yy'))

def item_print(**items):
    print(types(items))
    print(items
          
          item_print(a='hnng',b=22)