import numpy as np

def calculate(numbers):

    if not numbers:
        print("Empty List!")
        return
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            print("Not a number!")
            return
        
    changed_list=np.array(numbers)
    min_num=np.min(changed_list)
    max_num=np.max(changed_list)

    if min_num==max_num:
        result=np.zeros_like(changed_list)
    else:
        normalized=(changed_list-min_num)/(max_num-min_num)
    
    mean=np.mean(normalized)
    median=np.median(normalized)
    variance=np.var(normalized)

    return mean, median, variance
try:
    result=calculate([10, 20, 30, 40, 50])
    print(f"Mean: {result[0]}, Median: {result[1]}, Variance: {result[2]}")
except:
    print("Error!!")


    