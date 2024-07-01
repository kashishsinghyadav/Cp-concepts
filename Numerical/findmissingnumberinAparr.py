#tc=o(logn)
def findmissing(arr):
    l=0
    r=len(arr)
    diff=(arr[r-1]+arr[l])//r
    while l<r:
        mid=(l+r)//2
        if arr[mid]-arr[mid-1]!=diff and mid>0:
            return arr[mid-1]+diff
        if arr[mid+1]-arr[mid]!=diff:
            return arr[mid]+diff
        nthval=diff*arr[mid]+arr[0]
        if arr[mid]==nthval:
            l=mid+1
        else:
            r=mid-1
arr=[2,4,8,10,12]
print(findmissing(arr))
        
    
