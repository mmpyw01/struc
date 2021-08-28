def sum (l):
    if len(l) <= 2:
        print('Array Input Length Must More Than 2')
    else:
        preAnswer = []
        finalAnswer = []
        for i in range(len(l)):
            for j in range(len(l)):
                for k in range(len(l)):
                    if i < j < k:
                        if l[i] + l[j] + l[k] == 5:
                            preAnswer.append(l[i])
                            preAnswer.append(l[j])
                            preAnswer.append(l[k])
                            preAnswer.sort()
                            if preAnswer not in finalAnswer:
                                finalAnswer.append(preAnswer)
                                preAnswer = []
                                continue
                            preAnswer = []
        print(finalAnswer)

a = list(map(int,input('Enter Your List : ').split()))
sum(a)
