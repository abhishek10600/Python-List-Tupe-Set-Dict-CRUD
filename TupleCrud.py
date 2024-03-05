nums1 = (1, 2, 3, 4, 5, 6)

# -- TUPLE WITH JUST ONE ITEM --
nums2 = (1,)
print(nums2)

# tuples are unchangeable, allow duplicates and ordered.

# -- LENGTH OF TUPLE
print(len(nums1))

# -- PRINT ITEMS IN A TUPLE --


print(nums1)


# -- GET TUPLE ITEM WITH THE ITEM INDEX --
print(nums1[2])

# -- TUPLE ITEMS BY RANGE OF INDEXED --
print(nums1[1:4])  # 4 not included.


# -- TUPLE ITEMS BY NEGATIVE INDEXES --
print(nums1[-4:-1])  # -1 not included.


# CHECK IF A TUPLE ITEM EXISTS
if 2 in nums1:
    print("ITEM FOUND.")
else:
    print("ITEM NOT FOUND.")


# -- UPDATE TUPLE ITEMS --

nums3 = (1, 2, 4, 5, 6, 7, 8, 9, 10)

# as tuples are unchangle, we cannot update item directly. So we convert tuple to list and the update the item in the list. Then we conver the list back to tuple.

nums3_list = list(nums3)  # converting tuple to list
nums3_list[2] = 9  # updating element at index 2
nums3 = tuple(nums3_list)  # coverting list nums3_list to tuple nums3.
print(nums3)


# -- INSERT ITEMS IN TUPLE --

nums4 = (1, 2, 3, 4, 5, 6)
nums4_list = list(nums4)
nums4_list.insert(2, 20)
nums3_list.append(98)
nums4 = tuple(nums3_list)
print(nums4)


# ADD TUPLE IN A TUPLE

nums5 = (1, 2, 3, 4, 5)
nums6 = (7,)
nums5 += nums6
print(nums5)

# ------------------------


# REMOVE ITEM FROM A TUPLE

# as tuples are unchangle, we cannot update item directly. So we convert tuple to list and the update the item in the list. Then we conver the list back to tuple.
nums7 = (1, 2, 3, 4)
nums7_list = list(nums7)
nums7_list.remove(3)
nums7 = tuple(nums7_list)
print(nums7)


# -- UNPACKING A TUPLE --
nums8 = (1, 2, 3)
one, two, three = nums8
print(one, two, three)

# UNPACKING A TUPLE WITH * --
nums9 = (1, 2, 3, 4, 5, 6)
one, two, *three = nums9  # 1 in one, 2 in two and 3,4,5,6 in three
print(one)
print(two)
print(three)


one, *two, three = nums9  # 1 in one, 2,3,4,5 in two and 6 in three.
print(one)
print(two)
print(three)


# loop through tuples

# loop through the elements of tuple
nums10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in nums10:
    print(num)


# loop through index of tuple
for i in range(len(nums10)):
    print(nums10[i])


# while loop
i = 0
while i < len(nums10):
    print(nums10[i])
    i += 1
