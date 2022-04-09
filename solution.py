def decodeBinarySeq(binarySeq):
    binarySeq = str(binarySeq)
    invalid = "Invalid input"
    if len(binarySeq) < 8:
        return invalid

    if len(binarySeq) > 24:
        return invalid

    mapping = {
        "00": "C",
        "01": "G",
        "10": "A",
        "11": "T"
    }

    
    result = ""

    for i in range(0, len(binarySeq), 2):
        result += mapping[binarySeq[i]+binarySeq[i+1]]

    return result



    