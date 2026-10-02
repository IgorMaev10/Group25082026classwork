numbers = [10, 20, 10, 30, 20, 40, 10, 50]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
print(len(numbers_set))

def is_contains_symbol(symbol, set: set) -> bool:
    if symbol in set:
        return True
    else:
        return False

print(is_contains_symbol(30, numbers_set))
print(is_contains_symbol(100, numbers_set))


data = [15, "Python", 15, True, "Python", 3.14, False, True]
data_set = set(data)
data_set.update(["Redis", 100])
data_set.discard("Python")
print(is_contains_symbol(True, data_set))
print(is_contains_symbol(False, data_set))


python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}
union1 = python_students.union(redis_students)
union2 = python_students | redis_students
print(union1 == union2)


intersection1 = python_students.intersection(redis_students)
intersection2 = python_students & redis_students


all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}
not_learning_python1 = all_students.difference(python_students)
not_learning_python2 =  all_students - python_students


numbers = {10, 20, 30}
numbers.add(40)
numbers.add(40)
numbers.update([50, 60, 70])
numbers.remove(20)
numbers.discard(100)
print(numbers)
print(numbers.pop())
print(numbers)
