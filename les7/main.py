def inText(text):
    textLow = text.lower()
    if textLow[-1::-1]==textLow:
        return print('Yes')
    else: 
        return print('No')