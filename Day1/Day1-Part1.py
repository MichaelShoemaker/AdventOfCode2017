def make_data(file):
    data = open(file, 'r').read()
    nums = [i for i in data if i != '\n']
    total = 0
    for n, d in enumerate(nums):
        if n == len(nums)-1:
            pass
        elif d == nums[n+1]:
            total += int(d)
        else:
            pass
        
    if nums[0]==nums[-1]:
        total += int(nums[0])
    return total

if __name__ == '__main__':
    print(make_data('test.txt'))
