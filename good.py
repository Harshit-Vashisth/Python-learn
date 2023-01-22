# Python3 implementation of the approach

# Function to return the minimum number
# of elements that must be removed
# to make the given array good
def minimumRemoval(n, a):
    c = dict.fromkeys(a, 0);

    # Count frequency of each element
    for i in range(n):
        c[a[i]] += 1;

    ans = 0;

    # For each element check if there
    # exists another element that makes
    # a valid pair
    for i in range(n):
        ok = False;
        for j in range(31):

            x = (1 << j) - a[i];
            if (x in c and (c[x] > 1 or
                            (c[x] == 1 and x != a[i]))):
                ok = True;
                break;

        # If does not exist then
        # increment answer
        if (not ok):
            ans += 1;

    return ans;


# Driver Code
if __name__ == "__main__":
    a = [3,1,-1,1];
    n = len(a);

    print(minimumRemoval(n, a));

# This code is contributed by Ryuga
