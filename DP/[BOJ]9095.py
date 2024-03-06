import traceback
try: 
    count = int(input())
    for i in range(count):
        num = int(input())
        result = [0, 1, 2, 4]
        if num > 3:
            for j in range(num - 3):
                n = j+4
                result.append(result[n-1] + result[n-2] + result[n-3])
    
        print(result[num])
except:
    print(traceback.format_exc())