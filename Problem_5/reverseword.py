

def reverseInput(uInput):
    sInput = uInput.split()
    rInput = reversed(sInput)
    output = " ".join(str(x) for x in rInput)
    return output
    
    
