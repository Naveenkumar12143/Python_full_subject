__author__ = "Naveen kumar"
"""
1. set is a heterogeneous unordered collection of unique elements
2. delimited by { elements } ,  single comma separated
3. empty {} makes a dictionary, so for empty set use the set()constructor.
a = {}  
print(type(a))  # <type 'dict'>
a = set() 
print(type(a))   # <type 'set'>
4. set() constructor accepts:
    a. iterable series of values s = set([2,4,16, 4096, 65536])
    b. duplicates are discorded
        t = [2, 4, 16, 4096, 4, 65536, 16]
        print(set(t))  # set([16, 4096, 2, 4, 65536])
    c. often used specifically to remove duplicates - not order preserving.
5. add(item) inserts a single element.
    s.add("Narendra")
6. For multiple elements use update(items) passing any iterable series
    s.update(["Surendra", 34,23])
7. 2 methods are provided to removing elements from set
        a. remove(item) requires that item is present, otherwise raises KeyError
            s.remove(34)  # set([65536, 4096, 2, 4, 'Narendra', 'Surendra', 16, 23])
            s.remove(2323232)  # KeyError: 2323232
        b. discard(item) always succeeds
8. copying 
    ==> s.copy() method
    ==> set(s) constructor
9. Python's set class represents the mathematical notion of a set."""

v = [2, 4, 16, 40.96,"nk", 4, 65536, 16,"rohith"]

v = set(v)
print(v)
v = set[v]
print(v)

n = {2, 4, 16, 40.96,"nk", 4,32, 65536, 16,"rohith"}
print(n)
n.add(454) ### we can able to add integers
print(n)
n.add("teja") ### we can able to add strings
print(n)
n.add(22.4)
print(n)

x = [1, 2, 3.5, 4, "venu"]
n.update(x)  #### list elements we can add to th set (Reason:- set is mutable)
print(n)
print(x)

y = ("Surendra", 3.5, 23, 2)
n.update(y)  # tuple elements we can add to th set (Reason:- set is mutable)
print(n)

z = {"Surendra", 4, "jayanth", 333, 22.5, 2}
n.update(z)
print(n)
print(z)

n = {2, 4, 16, 40.96,"nk", 4,32, 65536}
n.remove(4)
print(n)

n.discard('nk')
print(n)

n.discard(65432789) ## ( if item is not present there is no showing error)
print(n)  #####{32, 65536, 2, 16, 40.96}

"""copy  in 2 ways"""
x = {2, 3, 4, 5,9,11,54, 3, 4, 5.5, "Jai", 5.5, "Abhishek"}
b = x.copy()
print(b)
print(id(x),id(b)) ### deep copy (creates the separate memory location)


h = set(x)
print(h)
print(id(x), (h))    # deep copy (creates the separate memory location)

f = x
print(f)
print(id(x),(f))  #### shallow copy (uses the same memory location)

# #pop()
# #removes and returns an arbitrary set element. The method raises a KeyError if the set is empty
p = {1, 2, 3.5, 4, "venu",65,87,}
print(p)
print(p.pop())

# # True if A is a subset of B
# # False if A is not a subset of B
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B)) # Returns True

print(A.issubset(C))  # # # Returns False

print(B.issuperset(A))  # Returns True

print(B.issuperset(C))  # Returns True

# #Set difference()
h = {'a', 'b', 'c', 'd'}
i = {'c', 'f', 'g'}

# # # Equivalent to h-i
print(h.difference(i))  ##{'a', 'd', 'b'}

### Equivalent to i-h
print(i.difference(h))  # {'g', 'f'}


## intersection()
hi = {2, 3, 5, 4}
i = {2, 5, 100}
u = {2, 3, 8, 9, 10}

# print(i.intersection(hi))  # {2, 5}
# print(i.intersection(u))  # {2}
# print(hi.intersection(u))  # {2}
# print(u.intersection(hi,i)) ## {2}

# print(hi.union(i)) ####  {2, 3, 4, 5, 100}
# print(i.union(u))  ###{2, 3, 100, 5, 8, 9, 10}
# print(i)
# print(hi)
# print(u)

