
# Written by Mahnatse, Yanga, Allen, Sibusiso, Thabo and Zweli
# Date    : 11 November 2019
# Cohort  : C17 Data Science
# Leader  : Singi

"""
We assumed that k1, k2, d1 and d2 are all greater or equal to zero
"""
def kangaroo_jump(k1,k2,d1,d2):
    """Summary or Description of the Function

    Parameters:
    k1 (int): Starting point of k1
    k2 (int): Starting point of k2
    d1 (int): Jump steps for k1
    d1 (int): Jump steps for k2
    Returns:
    int:Returning meeting point

   """
    if(k1 % 2 == 0 and k2 % 2 == 0 and d1 == d2):
        return -1

    elif (k1 == k2 and d1 == d2):
        return k1

    elif (k1 != k2 and d1 == d2):
        return -1

    else :
        while (k1 != k2):
            k1 = k1 + d1
            k2 = k2 + d2

    return k1
meeting_point = kangaroo_jump(3,4,3,3)
print(meeting_point)
