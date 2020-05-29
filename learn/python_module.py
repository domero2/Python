from collections import Counter, defaultdict, OrderedDict, namedtuple
import timeit


#Counter in list
List1 = [1,1,1,2,3,4,4,4,5,6,6,7,8,8,89,99,9,9]
list_counter= Counter(List1)
#return: Counter({1: 3, 4: 3, 6: 2, 8: 2, 9: 2, 2: 1, 3: 1, 5: 1, 7: 1, 89: 1, 99: 1})

#Counter with string
simple_string = 'jajajajaajkkkokokoknmnaman'
count_string = Counter(simple_string)

# count_string = Counter({'a': 7, 'k': 6, 'j': 5, 'o': 3, 'n': 3, 'm': 2})

words_string = 'kaka koko keke kaka koko oko'
counted_words = Counter(words_string.split())

#counted_words = Counter({'kaka': 2, 'koko': 2, 'keke': 1, 'oko': 1})

# Get most common word
most_common_counted = counted_words.most_common(1)[0][0]



##################################  DEFAULT DICTIONARY


#When you want to avoid key error when call key which wasn't deifne yet
default_dict = defaultdict(lambda: 0)

default_dict['two'] = 2
default_dict['one']
default_dict['three']

#ORDER DICTIONARY

order_dict = OrderedDict()
normal_dict = {}
normal_dict['a'] = 1
normal_dict['b'] = 2

normal_dict2 = {}
normal_dict2['b'] = 7
normal_dict2['a'] = 1
normal_dict2['d'] = 0
normal_dict2['c'] = 2


#def sorterdValues():
for m in sorted(normal_dict2.items(), reverse=False):
    pass


print('\n-----')


student_tuples = [
    ('john', 'A', 15),
    ('mane', 'C', 12),
    ('dave', 'B', 20),
]
print(sorted(student_tuples, key=lambda student: student[0], reverse=False))
#sorted by name[('dave', 'B', 20), ('john', 'A', 15), ('mane', 'C', 12)]
print(sorted(student_tuples, key=lambda student: student[1]))
#sorted by second value [('john', 'A', 15), ('dave', 'B', 20), ('mane', 'C', 12)]
print(sorted(student_tuples, key=lambda student: student[2]))
#sorted by numbers [('mane', 'C', 12), ('john', 'A', 15), ('dave', 'B', 20)]




############################  NAMED TUPLE

#classs creation

FirstClass = namedtuple('FirstClass','order firstName')

#object

joe = FirstClass(order=2, firstName='Doe')
#print(joe.order, joe[1])


############################ TimeIt

first_string = '0-1-2-3-...-99'
"-".join(str(n) for n in range(100))

print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
#run as list comprehension
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

#using map much faster
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
