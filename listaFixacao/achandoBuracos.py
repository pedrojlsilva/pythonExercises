cases=int(input())

umBuraco=["A", "D", "O", "P", "Q","R"]
doisBuraco=["B"]

 
for case in range(cases):
    count = 0
    palavra=input()

    for char in palavra:
        for letra in umBuraco:
            if char == letra:
                count+=1
        
        if char == "B":
            count+=2

    print(count)
    
