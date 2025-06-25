def plusOne(digits):
    if digits[-1] !=9:
        digits[-1] +=1
        return digits
    else:
        if len(digits) == 1:
            return [1,0]
        else:
            res = plusOne(digits[:-1])
            res.append(0)
            return res