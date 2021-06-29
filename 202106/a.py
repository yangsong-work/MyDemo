

my_tuple = ('小明', 'name','eat')
print(my_tuple,type(my_tuple))

my_dict = {'name':5,'小明':6}

print(my_dict ,type(my_dict))

my_list = [1,2,2,3,4]
print(my_list ,type(my_list))

my_set = {1,2,3,3,4}
print(my_set , type(my_set))

#对任意序列进行排序，不会影响原来的对象
#sorted()
l = [2,5,'1',3,'6','4']
print(l)
print(sorted(l,key=int))

#闭包 将函数作为返回值返回

def fn():
    a=10
    def inner():
        print('我是inner')
        print(a)

    return inner()

r = fn()
print(r)