def remove_duplicates(OrgList):
    NewList = []
    for x in OrgList:
        if x not in NewList:
            NewList.append(x)
    return NewList
OrgList = []
n = int(input("enter the number of elements: "))
for i in range(n):
    ele = int(input(f"enter {i} element: "))
    OrgList.append(ele)
print(remove_duplicates(OrgList))
