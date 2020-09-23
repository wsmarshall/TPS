# stats 10 day  hackerrank 
# quartiles
# note, don't need to be cute and exclude the quartiles from the list for the even case. Not very well explained...

# get input from stdin
from sys import stdin


# define function to run to get the quartiles (use numpy
def calculate_quartiles(numbers):
    # assumes a sorted array!
    def calculate_median(nums):
        n = len(nums)
        if n % 2 == 1:
            return nums[n//2]
        else:
            return (nums[n//2-1] + nums[n//2]) // 2
            
    median_all = calculate_median(numbers)
    length_ = len(numbers)
    
    if length_ % 2 == 1:
        # odd case, return the medians of the upper and lower, exluding the median overall
        median_low = calculate_median(numbers[:length_//2])
        median_up = calculate_median(numbers[length_//2+1:])
        
    else:
        # even case, return medians of up/low excluding 2 median values
        median_low = calculate_median(numbers[:length_//2])
        median_up = calculate_median(numbers[length_//2:])

    print(median_low)
    print(median_all)
    print(median_up)
            
if __name__ == '__main__':
    lines = stdin.readlines()[1]
    numbers = list(map(int, lines.split()))
    numbers.sort()
    calculate_quartiles(numbers)