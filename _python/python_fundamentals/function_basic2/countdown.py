def countdown(num):
    result = [num]
    for i in range(num-1,-1,-1):
      result.append(i)
    return result
print(countdown(5))
