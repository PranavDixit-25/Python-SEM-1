S1 = {'Red', 'yellow', 'orange', 'blue'}
S2 = {'violet', 'blue', 'purple'}

union_set = S1.union(S2)
print("Union:", union_set)

intersection_set = S1.intersection(S2)
print("Intersection:", intersection_set)

difference_s1_s2 = S1.difference(S2)
print("Difference (S1 - S2):", difference_s1_s2)

difference_s2_s1 = S2.difference(S1)
print("Difference (S2 - S1):", difference_s2_s1)

symmetric_difference_set = S1.symmetric_difference(S2)
print("Symmetric Difference:", symmetric_difference_set)
