test_tup = (15,20,123,47,26,81)

#1
sum_of_test_tup = sum(test_tup)
print('Here is the sum of all numbers in this tuple.')
print(sum_of_test_tup)

#2
max_of_test_tup = max(test_tup)
print('Here is the largest number in this tuple.')
print(max_of_test_tup)

print('----------')

#3
test_tup2 = ([17,28],[93,11],[20,17])
sum1 = sum(test_tup2[0])
sum2 = sum(test_tup2[1])
sum3 = sum(test_tup2[2])
print('Sum of interger 1: ', sum1)
print('Sum of interger 2: ', sum2)
print('Sum of interger 3: ', sum3)

print('----------')

#4
input_tup = ([2,20],[44,1],[3,13])
print('Original list: ', input_tup)
print('Sorted list: ', sorted(input_tup, key = lambda x:x[0] + x[1]))