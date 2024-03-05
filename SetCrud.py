nums1 = {1, 2, 3, 4, 5}

# sets are unordered, unchangeable and they do not allow duplicates.

# LENGTH OF SET
print(len(nums1))


# PRINT ITEMS IN A SET
print(nums1)


# ACCESS ITEMS IN A SET.

# set is unorderd, we cannot access the set using index or key. So we use loop with in.
nums2 = {1, 2, 3, 4, 5}
for num in nums2:
    print(num)


# CHECK IF AN ITEM EXISTS IN SET.
nums3 = {1, 2, 3, 4, 5}
if 4 in nums3:
    print("ITEM EXISTS")
else:
    print("ITEM DOES NOT EXISTS")


# ADD ITEMS IN A SET
nums4 = {1, 2, 3, 4, 5}
nums4.add(6)
print(nums4)


# ADD ITEM FROM ANOTHER SET
nums5 = {6, 7, 8, 9}
nums4.update(nums5)
print(nums4)

# ADD ANY ITERABLE IN SET
nums6 = {"abhishek", "sharma", "abhi", 9}
nums7 = ["kiwi", 6, "orange"]
nums6.update(nums7)
print(nums6)


# REMOVE ITEM FROM SET
nums8 = {1, 2, 3, 4, 5, 6, "sharma"}
print(nums8)
# if an element is not present in the set, remove() will raise an error.
nums8.remove("sharma")
print(nums8)
nums8.remove(3)
print(nums8)

# if element is not present in the set, discard() will not raise any error.
nums8.discard(2)
print(nums8)


nums8.pop()
print(nums8)  # pop will remove any random element from the set.

# EMPTY THE SET
nums8.clear()
print(nums8)


# -- LOOP A SET --
nums9 = {1, 2, 3, 4, 5}
for num in nums9:
    print(num)


# JOIN 2 sets
nums10 = {1, 2, 3, 4, 5}
nums11 = {6, 7, 8, 9, 10}
nums10.update(nums11)
print(nums10)


# INTERSECTION
set1 = {"apple", "kiwi", "guava"}
set2 = {"google", "apple", "microsoft"}
# it will return a set with element that is only present in both set1 and set2
x = set1.intersection(set2)
print(x)
