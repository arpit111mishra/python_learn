#collection of unordered items,unique,immutable
col={1,2,2,3,4}
print(col)
print(len(col))
null_set=set()
print(null_set)
null_set.add(1)
null_set.add(2)
null_set.add((1,2,3))#add tuple
print(null_set)
print(col.union(null_set))
print(col.intersection(null_set))
