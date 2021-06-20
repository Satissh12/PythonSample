# a=[7,8,9]
# b=[2,5,6]
# c = a+b
# c.sort()
# print (c)
# print (c[:-1])
# for items in c:
#     # range (0,c.__len__()):
# #     print (items)

# multi_arr = [[0,2,3,4], [5,6,7,8]]
# for items in multi_arr :
#     print (items[3])



collect = {}
x = "bisonssons"
for items in x:
    if items in collect.keys():
        collect[items] = collect[items]+1
    else:
        collect[items]=1
print(collect)

