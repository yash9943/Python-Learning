'''
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''

n = 5
for i in range(n):
    for j in range(n):
        if j < i:
            print(' ', end=' ')
        else:
            print('*  ', end=' ')
    print('\n')
    
for i in range(n-1):
    for j in range(n-1):
        if j < n-i-2:
            print(' ', end=' ')
        else:
            print('*  ', end=' ')
    print('\n')