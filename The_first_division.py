
for i in range(0,10):

    New_Num = float(input())
    
    # detect all prime division of input number
    all_prime_deviation = []
    for j in range(2,New_Num):

        if New_Num%j==0:

            if len(all_prime_deviation)!=0:

                for div_ind in all_prime_deviation:

                    if j%div_ind!=0:
                        all_prime_deviation.append(j)
    
