from collections import Counter
import math
def get_numbers():
    while True:
        try:
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            if not numbers:
                print("Error: The list cannot be empty.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter a list of integers.")



def find_min(numbers):
   min_val=numbers[0]
   for minimum in numbers:
       if minimum < min_val:
           min_val = minimum
   return min_val



def find_max(numbers):
   max_val=numbers[0]
   for maximum in numbers:
       if maximum > max_val:
           max_val = maximum
   return max_val



def find_mean(numbers):
   sum=0
   for mean in numbers:
       sum+=mean
   return sum/len(numbers)



def find_modes(numbers):
    freq = Counter(numbers)  
    #conter=>is the dictionary must deal with the numbers as key and their frequency as value
   
    max_freq = 0
    for value in freq.values():
        if value > max_freq:
            max_freq = value

    
    modes = []
    for key, value in freq.items():
        if value == max_freq:
            modes.append(key)
    
    return modes
    


def find_median(numbers):
    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    else:
        return numbers[middle_index]


def find_range(numbers):
    return max(numbers) - min(numbers)



def find_population_variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance


def find_sample_variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers)-1)
    return variance



def find_standard_deviation_sample(numbers):
    variance = find_sample_variance(numbers)
    return math.sqrt(variance)

def find_standard_deviation_population(numbers):
    variance = find_population_variance(numbers)
    return math.sqrt(variance)

def find_quartiles(numbers):
    
    Q2 = find_median(numbers)
    mid = len(numbers) // 2
    
    
    Q1 = find_median(numbers[:mid])
    
    if len(numbers) % 2 == 0:
        Q3 = find_median(numbers[mid:])
    else:
        Q3 = find_median(numbers[mid + 1:])
    
    return Q1, Q2, Q3
#automatically when any function return multiple values it return as tuple so we can use tuple with index

def find_IQR(numbers):
    return find_quartiles(numbers)[2] - find_quartiles(numbers)[0]





if __name__ == "__main__":
    numbers = get_numbers()
    print(f"The minimum number is: {find_min(numbers)}")
    print(f"The maximum number is: {find_max(numbers)}")
    print(f"The mean is: {find_mean(numbers)}")
    print(f"The modes are: {find_modes(numbers)}")
    print(f"The median is: {find_median(numbers)}")
    print(f"The range is: {find_range(numbers)}")
    print(f"The population variance is: {find_population_variance(numbers):.2f}")
    print(f"The sample variance is: {find_sample_variance(numbers):.2f}")
    print(f"The standard deviation (sample) is: {find_standard_deviation_sample(numbers):.2f}")
    print(f"The standard deviation (population) is: {find_standard_deviation_population(numbers):.2f}")
    print(f"The quariles are: {find_quartiles(numbers)}")
    print(f"The IQR is: {find_IQR(numbers)}")
   