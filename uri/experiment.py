N=int(input())
total, total_rabbit, total_rat, total_frog= 0, 0, 0, 0
for i in range(N):
    amount, aniType=input().split()
    amount=int(amount)
    if (aniType=='C'):
        total_rabbit+=amount
    if(aniType=='R'):
        total_rat+=amount
    if(aniType=='S'):
        total_frog+=amount
total= total_rabbit + total_rat + total_frog

perRab=(total_rabbit/total)*100
perRat=(total_rat/total)*100
perFrog=(total_frog/total)*100

print(f"Total: {total} cobaias\nTotal de coelhos: {total_rabbit}\nTotal de ratos: {total_rat}\nTotal de sapos: {total_frog}")
print(f"Percentual de coelhos: {perRab:.2f} %")
print(f"Percentual de ratos: {perRat:.2f} %")
print(f"Percentual de sapos: {perFrog:.2f} %")