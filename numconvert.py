conversionDict = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD',
        100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL',
        10  : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV',
        1 : 'I'}

# Function for converting arabic number input to roman numeral output string
def arabicToRomanConverter(arabicInput):
    try:
        int(arabicInput)
    except(ValueError):
        print("Please input a valid arabic integer")
        return -1

    if(isinstance(arabicInput, int) == False):
        print("Floats are not allowed!")
        return -1
    romanString = ''
    # Iterate through all the keys in the dictionary
    for romanKey in conversionDict.keys():
        while arabicInput >= romanKey:
            arabicInput -= romanKey
            # Append the value at the integer key to the result string
            romanString += conversionDict[romanKey]
    return romanString