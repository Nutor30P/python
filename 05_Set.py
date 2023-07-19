
# Set is a collection of unique elements
st = set()
my_other_set = {14, 23, 234, 244, 54}

print(type(st))
print(type(my_other_set))


# Add elements to set

st.add(1)
st.add(2)
st.add(3)
st.add(4)
st.add(5)
st.add(5)  # Adding duplicate element

#a set cannot contain duplicate elements

print(st)
print(len(st))

# Remove elements from set

st.remove(5)
print(st)

st2 = st.union(my_other_set)
print(st2)


# Intersection of two sets

st.intersection(my_other_set)
print(st)


# Difference of two sets

st3 = {2,4,6,8,10}
st4 = {2,4}
st4.difference(st3)
print(st4)


# subset and superset

print(st3.issubset(st4))
print(st4.issuperset(st3))

# simmetric difference

print(st3.symmetric_difference(st4))