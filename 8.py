def flatten_depth(nested_list):
    def flatten(nested_list, depth):
        firstdepth=depth
        for items in nested_list:
            if isinstance(items, list):
                firstdepth=max(firstdepth, flatten(items, depth+1))
            else:
                flatten_list.append(items)
        return firstdepth
    flatten_list=[]
    maxdepth=flatten(nested_list, 1)
    return flatten_list, maxdepth

nested_list = [1, [2, [3, 4], 5], [6, [7, [8]]]]
flatten, depth=flatten_depth(nested_list)
print("Flatten List: ", flatten)
print("Depth of Nested List: ", depth)