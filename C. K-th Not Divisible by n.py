# iters= int(input())
# div=[]
# output=[]

# def Binarysearch(arr,key):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if key==arr[mid]:
#             return mid
#         else:
#             if key<arr[mid]:
#                 right=mid-1
#             else:
#                 left=mid+1
#     return mid

# for i in range(iters):
#     n , k=map(int,input().split())
#     for x in range(1,(k*2)+1):
#         if x%n !=0:
#             div.append(x)
#     output.append(Binarysearch(div,k))     

# for a in output:
#     print(a)

# import sys
# iters= int(input())
# div=[]
# output=[]

# def Binarysearch(n, k):
#     left = 1
#     right = sys.maxsize
#     ans = 0
#     while (left <= right):
#         mid = (left + right) // 2
#         sol = mid - mid // n
#         if (sol > k):
#             right = mid - 1
#         elif (sol < k):
#           right = mid + 1
#         else:
#             ans = mid
#             right = mid - 1   
#     return ans

# for i in range(iters):
#     n , k=map(int,input().split())
#     for x in range(1,(k*2)+1):
#         if x%n !=0:
#             div.append(x)
#     index=Binarysearch(div,k)
#     output.append(div[index])   

# for a in output:
#     print(a)


# iters= int(input())
# div=[]
# output=[]

# for i in range(iters):
#     n , k=map(int,input().split())
#     for x in range(1,(k*2)+1):
#         if x%n !=0:
#             div.append(x)  
#     output.append(div[k-1])   

# for a in output:
#     print(a)



# iters= int(input())
# div=[]
# outtput=[]

# for i in range(iters):
#     n , k=list(map(int,input().split()))
#     for x in range((k*2)+1):
#         if x%n !=0:
#             div.append(x) 
#     print(div[k-1])         



iters = int(input())
l = []
for i in range(iters):
    n,k = list(map(int,input().split()))
    div = k // (n-1) 
    ex = k % (n-1) 
    ans = n * div + ex 
    if(ex == 0):
        ans -=1 
    print(ans)


# import sys
# def kthNonDivisible(n, k):
#     left = 1
#     right = sys.maxsize
#     ans = 0
#     while (left <= right):
#         mid = (left + right) // 2
#         sol = mid - mid // n
#         if (sol > k):
#             right = mid - 1
#         elif (sol < k):
#           right = mid + 1
#         else:
#             ans = mid
#             right = mid - 1   
#     print(ans)


# N = 3
# K = 7
# kthNonDivisible(N, K)


# iters= int(input())
# div=[]
# output=[]

# def Binarysearch(n, k):
#     left = 1
#     right = sys.maxsize
#     ans = 0
#     while (left <= right):
#         mid = (left + right) // 2
#         sol = mid - mid // n
#         if (sol > k):
#             right = mid - 1
#         elif (sol < k):
#           right = mid + 1
#         else:
#             ans = mid
#             right = mid - 1   
#     return ans

# for i in range(iters):
#     n , k=map(int,input().split())
#     index=Binarysearch(div,k)
#     print(index)