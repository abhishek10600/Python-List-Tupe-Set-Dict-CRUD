nums = [1, 2, 3, 4, 5, 6]

# Lists are changeable, allow duplicates and ordered.

# length of list.
print(len(nums))

# --- PRINT ITEMS IN A LIST ---

# print a list
print(nums)

# print a particular item by it's index in a list
print(nums[4])


# print a range of items in a list
print(nums[1:4])  # index 4 not included


# print item by negative index
print(nums[-4:-2])


# check if a item exists in a list
if 4 in nums:
    print("Exists")
else:
    print("Does not exists")

# ----------------------------------


# --- UPDATE ITEMS IN A LIST ---

nums2 = [1, 2, 3, 4, 5, 6, 7]


# update an item in a list by it's index
nums[2] = 8
print(nums)

# update items in a list by a range of indexes
nums2[3:6] = [11, 12, 13]  # 6 is is not inlcuded
print(nums2)


# -------------------------------


# --- ADD NEW ITEMS IN A LIST ---


nums3 = [1, 2, 3, 4, 5, 6, 7, 8]


# inserting a new item at a specific index in a list. We need to specify the index and the element to insert.
nums3.insert(3, 9)
print(nums3)


# inserting a new item at the end of the list. We just need to specify the element.
nums3.append(10)
print(nums3)


# append element of one list into another list we use extend.
nums3temp = [87, 45, 23, 97, 22]
nums3.extend(nums3temp)  # it will append nums3temp to the end of list nums3.
print(nums3)


# -----------------------------------


# --- DELETE ELEMENT FROM A LIST ---

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# removing a specific element from the list. We just need to provide the item to be removed.

nums4.remove(9)
print(nums4)


# remove an item from a list by it's index. We need to provide the index of the item we want to remove.
nums4.pop(2)
print(nums4)


# removing the last item from a list.
nums4.pop()
print(nums4)


# deleting a list using "del" keyword
# del nums4
# print(nums4)  # it will give an error as nums4 is deleted

# make a list empty
nums4.clear()
print(nums4)


# -------------------------------------


# -- LOOP A LIST --


nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# looing throught the elements in a list.
for num in nums5:
    print(num)


# looping throught the index of a list
for i in range(len(nums5)):
    print(nums5[i])


# loop using while loop
i = 0
while i < len(nums5):
    print(nums5[i])
    i += 1


# looping using list comprehension
[print(num) for num in nums5]

# -------------------------------------


# -- LIST COMPREHENSION --
nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for num in nums6:
#     if 6 == num:
#         new_list.append(num)

# print(new_list)

# performing the above operation using list comprehension
new_list = [num for num in nums6 if num == 8 or num == 4]
print(new_list)


# -----------------------------------

# -- SORT A LIST --

nums7 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
nums7.sort()  # sorting in ascending order.
print(nums7)

nums8 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
nums8.sort(reverse=True)  # sorting in descending order.
print(nums8)

# ----------------------------------------


# -- REVERSE A LIST --
nums9 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nums9.reverse()
print(nums9)

# -----------------------------------------


# -- COPY LIST --

nums10 = [1, 2, 3, 4, 5, 6, 7]
nums11 = nums10.copy()
print(nums10)

# -----------------------------------------
