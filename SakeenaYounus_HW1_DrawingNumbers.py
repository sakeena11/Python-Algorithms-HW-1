''' 
    * drawing_numbers.py
    * @description Program to track success of 'drawing numbers from a hat' algorithm solution
    * @author Sakeena Younus
    * version 3.0 2022-04-08 
'''

import numpy as np
import random

class Part1:
    hat = np.random.choice(range(1, 1000000), 1000)
    random.shuffle(hat)
    # print(hat)

    set1_max_value = 0
    for i in range (len(hat)//2):
        a = hat[i]
        if a > set1_max_value: 
            set1_max_value = a

    answer = None
    for i in range (len(hat)//2, len(hat)):
        a = hat[i]
        if a > set1_max_value: 
            answer = a      

    if answer == max(hat):
        print(f'''
    You won! Your answer was: {answer} 
    The largest number was: {max(hat)}''')
    
    
    else:
        print(f'''
    You lost. Your answer was: {answer} 
    The largest number was: {max(hat)}''')

#-----------------------------------------------------------    

class Part2:
    num_games = 0
    losses = 0
    wins = 0

    while(num_games < 1001):
        hat = np.random.choice(range(1, 10000), 1000)
        random.shuffle(hat)
        # print(hat)

        set1_max_value = 0
        for i in range (len(hat)//2):
            a = hat[i]
            if a > set1_max_value: 
                set1_max_value = a

        answer = None
        for i in range (len(hat)//2, len(hat)):
            a = hat[i]
            if a > set1_max_value: 
                answer = a      

        if answer == max(hat):
        #     print(f'''
        # You won! Your answer was: {answer} 
        # The largest number was: {max(hat)}''')
            wins+=1
            num_games+=1
           
        else:
        #     print(f'''
        # You lost. Your answer was: {answer} 
        # The largest number was: {max(hat)}''')
            losses+=1
            num_games+=1

    print("wins: " + str(wins))
    print("losses: " + str(losses))
    
    success_rate = (wins/1001) * 100
    rounded_success_rate = round(success_rate, 2)
    print("success rate: " + str(round(rounded_success_rate)) + "%")

#-----------------------------------------------------------    

class Part3:
    ''' Success Rates
        ==============
        K = 2 
        Success Rate: 35%

        K = 3
        Success Rate: 27%

        K = 4
        Success Rate: 20%

        K = 5
        Success Rate: 18%

        ANSWER: K = 2 gives the best success rate
    '''
    
    K = 5
    N = 1000

    NK_num_of_values_in_set = N//K

    NK_start = 1

    r = 1
    wins = 0
    losses = 0
    num_games = 0

    
    while(num_games < 1000):
        max_list_K_minus_1 = []

        r = 0

        while r <= K:
            set = np.random.choice(range(1, 10000), NK_num_of_values_in_set)


            max_set = (max(set))

            if r <= (K-1):
                max_list_K_minus_1.append(max_set)
                max_in_list = max(max_list_K_minus_1)

            if r == K:
                if max_in_list > max_set:
                    print("You lost!")
                    losses+=1
                    print("num games: " + str(num_games))

                    num_games+=1
                else:
                    print("You win!")
                    wins+=1
                    print("num games: " + str(num_games))
                    num_games+=1
                
                print(f"The largest number was: {str(max_set)}")

            r += 1

    print("wins: " + str(wins))
    print("losses: " + str(losses))
    
    success_rate = (wins/1000) * 100
    rounded_success_rate = round(success_rate, 2)
    print("success rate: " + str(round(rounded_success_rate)) + "%")

  