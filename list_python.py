#append
 
# apend object to the end of the list. 

# a=[121324,13455,2521,25252,23523523,235235,235235,235235,2525,235235,235235]
# b=["nithya","balaji","user"]
# a.append("balaji")
# print(a)
# print(b)
    

   # clear

   Remove all items from list.

# a.clear()
# print(a)

   # copy
   
   Return a shallow copy of the list.


# b=a;
# print(b)
  
    #count

    Return number of occurrences of value

# print(a.count(121324))

# extend

  Extend list by appending elements from the iterabl

# book_1=[12,34,56,78,90,87,65,43,21]
# book_2=["nithya","balji","bala","volley"]
# book_1.append(book_2)
# print(book_1)
# book_2.append(book_1)
# print(book_2)
# book_1.extend(book_2)
# print(book_1)
# book_2.extend(book_1)
# print(book_2)

     # index


     Return first index of value.
 |      
 |      Raises ValueError if the value is not presen

n=[4,5,6,7,8,8,9,6,7]
m=["j","g","k","n","d"]

print(m.index("k"))

     # insert
m.insert(2,"root")
print(m)
m.insert(m.index("root"),"nithya")
print(m)

     # pop

       Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of ran

print(m)
m.pop()
print(m)
  
    # remove
 
    Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
    

m.remove("k")
print(m)

       # reverse
 |  
    Reverse *IN PLACE*.

m.reverse()
print(m)
    # sort

      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order


m.sort()
print(m)

