def getinput(inputtext):
    inputtext1 = inputtext + ' IS NOW WITH ME!!!'
    print('got the text '+ str(inputtext1))
    return inputtext1


def get_disease(inputtext):
    import pandas as pd

    dis_symp = pd.read_csv("new_diseases.csv")

    symptoms= list()
    x1= str(inputtext).split(',')
    for ent in x1:
        symptoms.append(str(ent).replace(' ','_'))

    l1=symptoms
    diagnosis={}
    for (row, row_data) in dis_symp1.iterrows():
            cnt = 0
            str1= row_data['final_symp']
            for item in l1:
                if item in str1:
                    cnt=cnt+1
            if cnt > 0:
                diagnosis[row] = cnt

#sorted(diagnosis, reverse = True)

    sorted_diagnosis = sorted(diagnosis.items(), key = lambda x:x[1], reverse = True)
    print (sorted_diagnosis)

    for key, value in sorted_diagnosis:
        #print (key + ' --> ' + str(value))
        outputtext = 'Looks like you are suffering from ' + str(key)  + ' --> ' + str(value)
        break
    return 


TEXT1= get_disease('fever,sneezing,cold,headache,chest pain,restlessness,breathlessness,high BP,swelling,cramps')
print(TEXT1)
