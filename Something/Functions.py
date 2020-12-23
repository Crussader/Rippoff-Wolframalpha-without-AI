##Imports####
from sympy import *
from re import findall
import operator, re, math
#############
global decorators1
decorators1 = "######################"
def simple_cal(user_input):
    res = N(user_input)
    if ((res - int(res)) == 0) == True:
        return print("Result: {} = {}".format(user_input, round(res, 2)))
    if ((res - int(res)) == 0) == False:
        return print("Result: {} = {}".format(user_input, round(res, 2)))
        return print("Sqaure Root of {} = {} , Rounded to {} ".format(res, res**.5, round(res**.5, 4)))
    else:
        if isprime(res)==True:
            return print(f"{res} is a Prime Number")

def percent_cal(user_input):
    
    arr = [int(number) for number in findall("\d+", user_input)]
    a = arr[0]
    b = arr[1]
    a=a/100
    res=a*b
    return print("{} = {}".format(user_input, res))
    return print("{} - {} = {}\n{}{4}".format(user_input, b, (b-res), decorators1))

def fraction_to_percent(user_input):
    arr = [int(number) for number in findall("\d+", user_input)]
    a = arr[0]
    b = arr[1]
    res=(a/b)*100
    return print("{} is {}{}".format(user_input, res,'%'))

def mass_percent1(user_input):
    arr = [float(i) for i in findall("\d*\.\d+", user_input)]
    c = ''.join(re.findall("^\w+", user_input))
    x = str(c)
    gramsofsolute = arr[0]
    gramsofsolution = arr[1]
    res1 = (gramsofsolute/gramsofsolution)*100
    finalres = round(res1, 2)
    string='Mass percent of {}'.format(x)
    return print("Mass {} of {} is {}{}".format('%', x, finalres, '%'))
    return print("{} = {} / {} * 100 = {}{}".format(string, gramsofsolute, gramsofsolution, finalres, '%'))

def mass_percent2(user_input):
    y = user_input.split()
    str2 = y[0]
    z = re.split('\s\,', user_input)
    z.remove(str2)
    new_string = ', '.join(z)
    arr = [float(i) for i in findall("\d*\.?\d+", new_string)]
    mass_percent = arr[0]
    gramsofsolution = arr[1]
    res1 = (mass_percent*gramsofsolution)/100
    finalres = round(res1, 3)
    string = 'Grams of Solute'
    return print("{} {}{}".format(string, finalres,'gms'))
    return print("{} = ({}x{})/{} = {}{}".format(string, mass_percent, gramsofsolution, '100', finalres, "gms"))

def mass_percent3(user_input):
    y = user_input.split()
    str2 = y[0]
    z = re.split('\s\,', user_input)
    z.remove(str2)
    new_string = ', '.join(z)
    arr = [float(i) for i in findall("\d*\.?\d+", new_string)]
    mass_percent = arr[0]
    gramsofsolution = arr[1]
    res1 = (mass_percent*gramsofsolution)/100
    finalres = round(res1, 3)
    string = 'Grams of Solution'
    return print("{} {}{}".format(string, finalres,'gms'))
    return print("{} = ({}x{})/{} = {}{}\n{}{6}".format(string, mass_percent, gramsofsolution, '100', finalres, "gms", decorators1))

def mass_percent4(user_input):
    y = user_input.split()
    str2 = y[0]
    z = re.split('\s\,', user_input)
    z.remove(str2)
    new_string = ', '.join(z)
    arr = [float(i) for i in findall("\d*\.?\d+", new_string)]
    volumeofsolute = arr[0]
    volumeofsolution = arr[1]
    res1 = (volumeofsolute/volumeofsolution)*100
    finalres = round(res1, 3)
    string = 'Volume Percent'
    return print("{} {}{}".format(string, finalres,'gms'))
    return print("{} = ({}x{})/{} = {}{}\n{}{6}".format(string, volumeofsolute, volumeofsolution, '100', finalres, "gms", decorators1))

def vol_percent(user_input):
    y = user_input

def placements_cal(user_input):
    positiondict= {
        1 : 'Ones',
        2 : 'Tens',
        3 : 'Hundreads',
        4 : 'Thousands',
        5 : 'Ten Thousand',
        6 : 'Hundread Thousands',
        7 : 'Millions',
        8 : 'Ten Millions',
        9 : 'Hundread Millions',
        10: 'Billion',
        11: 'Ten Billion',
        12: 'Hundread Billion',
        13: 'Trillion',
        14: 'Ten Trillion',
        15: 'Hundread Trillion',
        16: 'Quadrillion',
        17: 'Ten Quadrillion',
        18: 'Hundread Quadrillion',
        19: 'Ouintillion',
        20: 'Ten Ouintillion',
        21: 'Hundread Quintillion',
        22: 'Sextillion',
        23: 'Ten Sextillion',
        24: 'Hundread Sextillion',
        25: 'Septillion',
        26: 'Ten Septillion',
        27: 'Hundread Septillion',
        28: 'Octillion',
        29: 'Ten Octillion',
        30: 'Hundread Octillion',
        31: 'Nonillion',
        32: 'Ten Nonillion',
        33: 'Hundread Nonillion',
        35: 'Decillion',
        34: 'Ten Decillion',
        37: 'Hundread Decillion',
        38: 'Undecillion',
        36: 'Ten Undecillion',
        39: 'Hundread Undecillion',
        41: 'Duodecillion',
        40: 'Ten Duodecillion',
        42: 'Hundread Duodecillion' ,
        43: 'Tredecillion',
        44: 'Ten Tredecillion',
        45: 'Hundread Tredecillion',
        46: 'Ouattuordecillion',
        48: 'Ten Ouattuordecillion',
        47: 'Hundread Ouattuordecillion',
        49: 'Quindecillion',
        50: 'Ten Quindecillion',
        51: 'Hundread Quindecillion'
    }
    for i in range(len(user_input)+1):
        if i in positiondict:
            place=positiondict.get(i)
            return print(user_input[i-1], place,"\n###\n")

def equ_cal_general_var2(user_input):
    arr = [i for i in findall("[a-z]", user_input)]
    symbol=Symbol(arr[0])
    res = solve(user_input)
    if len(res)>1:
        for i in res:
            return print("The Solutions are:\n{} , {}".format(i, i))
            break
    else:
        return print("The Solution is: \n {}".format(res[0]))
#Polynomials function yet to be done:

#Geometry.Triangles
def compute_triangle(user_input):
    arr = [int(number) for number in findall("\d*\.?\d+", user_input)]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    Perimeter = a+b+c 
    return print("Area = {}\nPerimeter of Triangle = {}".format(Area, Perimeter))

def get_side_triangle(user_input):
    for i in user_input:
        if i == ',':
            res = user_input.split(',', 3)
            a = res[0]
            b = res[1]
            c = res[2]
    if a ==str('x'):
        b = int(b)
        c = int(c)
        res = ((c**2)-(b**2))**.5
        s = (res+b+c)/2
        Area = math.sqrt(s*(s-res)*(s-b)*(s-c))
        Perimeter = res+b+c
        return print("The Opposite Side = {}".format(res))
        return print("Area = {}\nPerimeter of Triangle = {}".format(Area, Perimeter))
    elif b == str('x'):
        a = int(b)
        c = int(c)
        res = ((c**2)-(a**2)**.5)
        s = (a+res+c)/2
        Area = math.sqrt(s*(s-a)*(s-res)*(s-c))
        Perimeter = a+res+c 
        return print("The Adjacent Side = {}".format(res))
        return print("Area = {}\nPerimeter of Triangle = {}".format(Area, Perimeter))
    elif c == str('x'):
        a = int(a)
        b = int(b)
        res = ((a**2)+(b**2)**.5)
        s = (a+b+res)/2
        Area = math.sqrt(s*(s-a)*(s-b)*(s-res))
        Perimeter = a+b+res 
        return print("The Hypotnuse Side = {}".format(res))
        return print("Area = {}\nPerimeter of Triangle = {}".format(Area, Perimeter))
        #not returning the second line 

