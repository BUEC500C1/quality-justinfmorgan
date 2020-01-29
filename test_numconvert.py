import numconvert

conversionDict = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD',
        100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL',
        10  : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV',
        1 : 'I'}

def test_numconvertUnitTest():
    assert numconvert.arabicToRomanConverter(1) == 'I'
    assert numconvert.arabicToRomanConverter(4) == 'IV'
    assert numconvert.arabicToRomanConverter(5) == 'V'
    assert numconvert.arabicToRomanConverter(9) == 'IX'
    assert numconvert.arabicToRomanConverter(10) == 'X'
    assert numconvert.arabicToRomanConverter(40) == 'XL'
    assert numconvert.arabicToRomanConverter(50) == 'L'
    assert numconvert.arabicToRomanConverter(90) == 'XC'
    assert numconvert.arabicToRomanConverter(100) == 'C'
    assert numconvert.arabicToRomanConverter(400) == 'CD'
    assert numconvert.arabicToRomanConverter(500) == 'D'
    assert numconvert.arabicToRomanConverter(900) == 'CM'
    assert numconvert.arabicToRomanConverter(1000) == 'M'
    #assert numconvert.arabicToRomanConverter(4999) == 'MMMMCMXCIX'

