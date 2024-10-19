# math genrateing problems
import random
import time
from sty import RgbFg,Style,RgbBg,rs,ef,fg,bg
fg.gold=Style(RgbFg(255,215,0))
fg.tomato=Style(RgbFg(255,99,71))
bg.lime=Style(RgbBg(0,255,0))
opertar=["+","-","*","/","%"]
max_value=int(input(f"{fg.gold}Enter maximam value: {fg.rs}"))
min_value=int(input(f"{fg.gold}Enter minmum value: {fg.rs}"))
total_problem=int(input(f"{fg.gold}Enter number of problems you wanted to play: {fg.rs}"))
def problem():
    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    choice=random.choice(opertar)
    exp=str(left)+" "+choice+" "+str(right)
    
    # print(exp)
    answer=eval(exp)
    return exp,answer
exp,answer=problem()
# print(exp,answer)

wrong=0
right_q=0
enter=input(f"{fg.gold}press enter: {fg.rs}")
print(f"{bg.lime}{fg.li_blue}___________{rs.all}")
start_time=time.time()
    # start_time=time.time()
for i in range(total_problem):
    exp,answer=problem()
    while True:
        user=input(f"{fg.gold}problem #{fg.rs} {i+1}: {exp} = ")
        if user==str(answer):
            print(f"{fg.tomato}right{fg.rs}")
            right_q+=1
            break
        elif user!=str(answer):
            print(f"{fg.tomato}wrong{fg.rs}")
            print(f"{fg.red}Loding....{fg.rs}")
            time.sleep(2)
            print(f"{fg.green}{answer}{fg.rs}")
            wrong+=1
            break



end_time=time.time()        
print(f"{bg.lime}{fg.blue}...........{rs.all}")
print(f"{fg.green}nice work{fg.rs}")
total_time=round(start_time-end_time,2)
print(f"total time {total_time} secondes")
print(f"your wrong questions {wrong}\nyour right questions {right_q}")