'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
n = 5

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(' ', end=' ')
        else:
            print('*',end=' ')
    print('\n')
    
for i in range(n-1):
    for j in range(n):
        if j <= i:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print('\n')

# n = 5

# # 🔹 Upper half
# for i in range(n):
#     print(" " * (n - i - 1), end="")     # spaces
#     print("* " * (i + 1))                # stars

# # 🔹 Lower half
# for i in range(n-1):
#     print(" " * (i + 1), end="")         # spaces
#     print("* " * (n - i - 1))            # stars
