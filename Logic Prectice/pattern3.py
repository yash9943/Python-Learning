'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

n = 5
for i in range(n):
    for j in range(n):
        count = n - i -1
        if j < count:
            print(' ', end=' ')
        else:
            print('*  ', end=' ')
    print('\n')