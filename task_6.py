numbers = [1, 3, 2, 3, 4, 2, 1, 5]



def find_repited_num(numbers):
    seen = set()
    repited = []
    
    for num in numbers:
        if num in seen:
            repited.append(num)
        else:
            seen.add(num)
    return repited

res = find_repited_num(numbers)

print(res)       