def make_data(file):
    data = open(file, 'r').read()
    nums = [int(i) for i in data if i != '\n']
    offset = int(len(nums)/2)
    total = 0
    for n, d in enumerate(nums):
         
        if n + offset > len(nums) - 1:
            if d == nums[(n+offset) % (len(nums))] and n != ((n+offset) % (len(nums)-1)):
                
                total += d
            else:
                pass
        elif d == nums[n+offset]:
            total += d
    return total

if __name__ == '__main__':
    print(make_data('input.txt'))
