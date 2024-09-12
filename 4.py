#Nested to Flattened List

L=[1,[2,3,4],5,[6,7,8]]

def Nested_to_Flattened(L):
    Flattened=[]
    for i in L:
        if isinstance(i,list):
            Flattened.extend(i)
        else:
            Flattened.append(i)
    return Flattened

print(Nested_to_Flattened(L))
