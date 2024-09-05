def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

prem = []
i = 2
while len(prem) < 100:
    if est_premier(i):
        nombres_premiers.append(i)  
    i += 1
  
print(prem)
