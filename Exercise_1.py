# merge two array and print them

# 3Initlaization
# Create on Web UI
# initalize local
# remote

# Pushing

# Add Files we want to send ( staging the changes )
# commit ( Commiting the changes )
# push git push origin <branch>

def mergearray(arr1, arr2):
    a = arr1
    b = arr2
    c = a+b
    c.sort()
    print(c)
    c.sort(reverse=True)
    print(c)
    for items in c:
        # range (0,c.__len__()):
        print(len(c))
        print (items)

mergearray([7, 8, 9],[2, 5, 6])
