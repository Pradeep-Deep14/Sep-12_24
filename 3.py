L=[1,1,[2,2,3,4,5],6,7,8,[8,9]]

#Nested to flattened list without duplicates

def nested_to_flattened_without_duplicates(L):
    seen=set()
    flattened=[]
    for i in L:
        if isinstance(i,list):
            for item in i:
                if item not in seen:
                    flattened.append(item)
                    seen.add(item)
        else: 
            if i not in seen:
                flattened.append(i)
                seen.add(i)
    return flattened

print(nested_to_flattened_without_duplicates(L))
