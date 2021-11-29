def process(selection):
    global major1
    global major2
    global major3
    global nostudy

    if selection==1:

        major1=major1+10
        print("민법총칙의 공부량이 10 증가했다!")
        return
    
    elif selection==2:

        major2=major2+10
        print("상법총론의 공부량이 10 증가했다!")
        return
    
    elif selection==3:

        major3=major3+10
        print("전공영어의 공부량이 10 증가했다!")
        return
    
    elif selection==4:
        
        nostudy=nostudy+1
        print("오늘할 공부를 내일로 미루고 스마트폰을 했다.")
        return
    
    else:
        if nostudy==1:
            major1=major1+3
            major2=major2+3
            major3=major3+3
            print("모든 과목의 공부량이  3 증가했다")
        elif nostudy==2:
            major1=major1+2
            major2=major2+2
            major3=major3+2
            print("모든 과목의 공부량이  2 증가했다")            
        else:
            major1=major1+1
            major2=major2+1
            major3=major3+1
            print("모든 과목의 공부량이  1 증가했다")
        
        return


major1=0
major2=0
major3=0
nostudy=0

print("""시험기간 시뮬레이터 입니다. 당신은 하루에 민법총칙, 상법총론, 전공영어 중 한 과목만을 공부할 수 있습니다.
또한 공부를 안하고 하루종일 놀 수 있습니다.
만약 하루종일 놀아서 공부를 못한 경우 시험 전날에 벼략치기를 통해 못한 공부량 만큼 모든 과목들을 공부할 수 있습니다.
다만 벼락치기의 경우 획득하게 되는 공부량이 적어지게 됩니다.
""")


for d in range(10,1,-1):
    print("시험까지 남은 기간:{}일         민법총칙 공부량:{} 상법총론 공부량:{} 전공영어 공부량:{} 총 공부량:{}".format(d, major1, major2, major3, major1+major2+major3))
    print("""
오늘은 무엇을 할까?
1.민법총칙을 공부한다.
2.상법총론을 공부한다.
3.전공영어를 공부한다.
4.하루종일 논다.
""")

    selection=int(input("선택지 번호를 하나만 입력해주세요"))
    process(selection)

    print()
    print("=========================================================================================================")


print("시험까지 남은 기간:1일         민법총칙 공부량:{} 상법총론 공부량:{} 전공영어 공부량:{} 총 공부량:{}".format(major1, major2, major3, major1+major2+major3))
print("""
오늘은 무엇을 할까?
1.민법총칙을 공부한다.
2.상법총론을 공부한다.
3.전공영어를 공부한다.
4.하루종일 논다.""")
if nostudy>0:
    print("5.모든 과목을 벼락치기 한다. (미룬 공부량 ",nostudy,"일치)")
    

selection=int(input("선택지 번호를 하나만 입력해주세요"))
process(selection)

print()
print("=========================================================================================================")

print("""시험 당일
민법총칙 공부량:{}, 상법총론 공부량:{} 전공영어 공부량:{} 총 공부량:{}""".format(major1, major2, major3, major1+major2+major3))

if 30<=major1:
    print("민법총칙의 학점은 A+")
elif 22<=major1:
    print("민법총칙의 학점은 A")
elif 20<=major1:
    print("민법총칙의 학점은 B")
elif major1==0:
    print("민법총칙의 학점은 F")
else:
    print("민법총칙의 학점은 C")
    
if 30<=major2:
    print("상법총론의 학점은 A+")
elif 22<=major2:
    print("상법총론의 학점은 A")
elif 20<=major2:
    print("상법총론의 학점은 B")
elif major2==0:
    print("상법총론의 학점은 F")
else:
    print("상법총론의 학점은 C")

if 30<=major3:
    print("전공영어의 학점은 A+")
elif 22<=major3:
    print("전공영어의 학점은 A")
elif 20<=major3:
    print("전공영어의 학점은 B")
elif major3==0:
    print("전공영어의 학점은 F")
else:
    print("전공영어의 학점은 C")
