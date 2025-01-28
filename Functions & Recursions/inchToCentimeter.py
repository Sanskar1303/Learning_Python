def measurement(inch):
    cms =  inch * 2.54
    return cms
inch = float(input("Enter length in inches :"))
print(f"converts {inch} inch into cms is :", measurement(inch))
