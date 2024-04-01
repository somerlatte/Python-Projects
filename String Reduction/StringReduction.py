def StringReduction(strParam):
    varOcg = True

    while True:
        reduced = False
        for i in range(len(strParam) - 1):
            if strParam[i] != strParam[i+1]:
                if (strParam[i] == 'a' and strParam[i+1] == 'b') or (strParam[i] == 'b' and strParam[i+1] == 'a'):
                    strParam = strParam[:i] + 'c' + strParam[i+2:]
                elif (strParam[i] == 'a' and strParam[i+1] == 'c') or (strParam[i] == 'c' and strParam[i+1] == 'a'):
                    strParam = strParam[:i] + 'b' + strParam[i+2:]
                elif (strParam[i] == 'b' and strParam[i+1] == 'c') or (strParam[i] == 'c' and strParam[i+1] == 'b'):
                    strParam = strParam[:i] + 'a' + strParam[i+2:]
                reduced = True
                break
        if not reduced:
            break

    return len(strParam)

# keep this function call here 
print StringReduction(raw_input())