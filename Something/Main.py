import Functions
from sympy.simplify.simplify import simplify
decorators1 = "####################"
try:
    print("{}\npress ctrl c to exit \n1.Simple Maths\n2.Simple Algebra\n3.Complex Maths\n4.Geometry\n5.Probablity".format(decorators1))
    user_input=input("Enter Choice[1/2/3/4/5]:  ")
    #Simple Maths
    if user_input=='1':
        print("{}\n1.Simple Maths\n2.Percentage\n3.Place Values".format(decorators1))
        user_input=input("Enter Choice[1/2/3]:  ")

        if user_input=='1':
            user_input=input("Enter Question:  ")
            Functions.simple_cal(user_input)

        if user_input=='2':
            print("#For finding percent from fractions just type fractions\n#For finding percent from number type:\n(percentage) of (number)(optional-distance)-->syntax\n")
            print("\n1.Fraction to Percent\n2.Money '%'\n3.Mass '%'\n4.Volume '%'")
            user_input=input("Enter Choice[1/2/3/4]:  ")
            #Fraction
            if user_input=='1':
                print("Format: \nJust Fraction")
                user_input=input("Enter Question:  ")
                Functions.fraction_to_percent(user_input)
            #Money %
            if user_input=='2':
                print("{0}\nFormat: x% of n\n{0}".format(decorators1))
                user_input=input("Enter Question:  ")
                Functions.percent_cal(user_input)
            #Mass %
            if user_input=='3':
                print("{0}\n1.Mass percent\n2.Grams of solute\n3.Grams of Solution\n{0}\n".format(decorators1))
                choice_user=input("Enter Choice[1/2/3]: ")
                if choice_user=='1':
                    print("#Format: \n(name of solute), Grams of solute, Grams of Solution\n{0}".format(decorators1))
                    user_input=input("Enter Question:  ")
                    Functions.mass_percent1(user_input)

                if choice_user=='2':
                    print("#Format: \n(Grams of solute), mass percent, Grams of Solution\n{0}".format(decorators1))
                    user_input=input("Enter Question:  ")
                    Functions.mass_percent2(user_input)

                if choice_user=='3':
                    print("#Format: \n(Grams of solution), mass percent, Grams of Solute\n{0}".format(decorators1))
                    user_input=input("Enter Question:  ")
                    Functions.mass_percent3(user_input)
            # Volume %
            if user_input=='4':
                user_input=input("Enter Question:  ")
                Functions.mass_percent4(user_input)
                

        if user_input=='3':
            user_input=list(input("Enter Number For Placements:  "))
            user_input.reverse()
            Functions.placements_cal(user_input)
    #Simple Alegebra
    if user_input=='2':
        print("{0}\n1.Equation Solving\n2.Polynomials\n3.Simplification\n{0}\n".format(decorators1))
        user_input=input("Enter Choice[1/2/3]: ")

        if user_input=='1':
            print("{0}\n#Format: \na*x + b*x + c (a, b, c are optional*)\n{0}")
            user_input= input("Enter Question:  ")

        if user_input=='2':
            pass

        if user_input=='3':
            print("{}\n#Format: for square root its 'sqrt(number)'\n{}")
            try:
                user_input = input("Enter Question:  ")
                res = simplify(user_input)
            except TypeError:
                print("{0}\nWrong Format\n#Format: for square root its 'sqrt(number)'{0}\n{0}".format(decorators1))
                user_input = input("Enter Question:  ")
                res = simplify(user_input)
    #Complex Maths
    if user_input=='3':
        print("{0}\n1.Geometry(Coordinates)\n2.Plotting and Graphics\n3.Differential\n4.Derivaties and Limits\n5.Conversion\n6.Trignometry\n7.AP(Arthmetic Progression)&GP(Geometric Progression)\n8.Mathmatical Functions\n9.Continued Fractions\n10.Probablity\n11.Statistics\n{0}".format(decorators1))
        user_input = input("Enter Choice[1/2/3/4/5/6/7/8/9/10/11]:  ")
        #Geometry
        if user_input == '1':
            print("{0}\n1.Triangles\n2.Area or Perimeter of circle types(Tangent, Cocentric,etc)\n3.Rotation to Radians\n4.Coordinate Geometry\n5.Get Info on Curves and Surfaces{0}".format(decorators1))
            user_input = input("Enter Choice[1/2/3/4/5]:  ")
            if user_input == '1':
                #Triangle
                print("{0}\n1.Find Area and Perimeter\n2.Find Sides of Triangles\n3.Compare Triangles\n{0}".format(decorators1))
                user_input = input("Enter Choice[1/2]: ")
                #Area and Perimeter
                if user_input == '1':
                    print("{0}\n#Format: 1st side, 2nd side, 3rd side\n {0}".format(decorators1))
                    # user_input = input("Enter [1/2]: ")
                    # if user_input == '1':
                    user_input = input("Enter Question:  ")
                    Functions.compute_triangle()
                #Find Side of triangle if two are given
                if user_input == '2':
                    print("{0}\n#Format: Enter Opposite, Adjacent, Hypotnuse##(side to be calulated must have a # or %)\n{0}".format(decorators1))
                    user_input = input("Enter Question: ")
                    Functions.get_side_triangle(user_input)
                if user_input == '3':
                    print("{}\n#Format:((t1side1,t1side2,t1side3), (t1angle1,t1angle2,t1angle3)),((t2side1,t2side2,t2side3), (t2angle1,t2angle2,t2angle3))")
                    user_input = input("Enter Question: ")
                    
                    

except KeyboardInterrupt:
    print("\nThank You!!")
