def PalindromeCreator(strParam):
    varOcg = True

    if strParam == strParam[::-1]:
        return "palindrome"

    for i in range(len(strParam)):
        if strParam[:i] + strParam[i+1:] == (strParam[:i] + strParam[i+1:])[::-1]:
            return strParam[i]
        elif i < len(strParam) - 1 and strParam[:i] + strParam[i+2:] == (strParam[:i] + strParam[i+2:])[::-1]:
            return "not possible"

# keep this function call here 
print PalindromeCreator(raw_input())