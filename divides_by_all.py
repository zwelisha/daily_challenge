"""
WRITTEN BY         : Mahnatse, Yanga, Allen, Sibusiso, Thabo and Zweli
DATE               : 13 November 2019
COHORT             : C17 Data Science
COHORT MANAGER     : Singi
GROUP LEADER       : Zweli
"""
#------------------------------------------------------------------------------------
"""
PROBLEM
Given two lists a and b, write a function that returns true if any
of the numbers in list a is divisible by all numbers in list b. Divisible in
for an example, given a = [1, 2, 3] and b = [2 , 1], the function would return True
since one of the elements of list a, which is 2 is divisible by all elements in list b.
"""
def divides_each_element(a,b):
    for i in range(len(a)):
        #the truth list stores True and False values based on whether the number we are currently
        # dividing in list a is divisible or not divisible by the number in list b
        truth_list = []
        n = a[i]
        for j in range(len(b)):
            if n % b[j] == 0:
                truth_list.append(True)
            else:
                if n % b[j] != 0:
                    truth_list.append(False)
        # Here we are checking if the truth list contains only True values
        # if that is the case, we return True immediately because it means
        # the number n in a is divisible by all numbers in b.
        if truth_list.count(False) == 0:
            return True
    #if this line gets executed or reached, it means
    # none of the numbers in a are divisible by all the numbers in b
    return False


# You are more than welcome to modify the two lists we created
# to do your own tests.
ls1 = [3,5,7,9,12]
ls2 = [2, 4, 6, 12]
print(divides_each_element(ls1, ls2))
