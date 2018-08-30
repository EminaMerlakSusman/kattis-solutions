N, b = list(map(float, input().split()))
'''Preveri, če je N manjši ali enak številu možnih bitstringov dolžine od 0 do b
znakov.'''
print('yes' if N <= 2**(b + 1) - 1 else 'no')
