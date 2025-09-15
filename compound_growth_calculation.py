#We have a Pₙ = P₀ * (1 + r)ⁿ
#With Pₙ is the final population after
#P₀ is the current population 
#r is the population growth % 
#n is the year numbers (like 2021 - 2025 is 4 right? So n is 4)

P_n = 0
P_o = input('Enter your population')
n = input('Enter your numbers of years')
r = input('Enter your population growth %')
P_n += P_o * (1 + r) ** n
print(f'Your answer {P_n}')