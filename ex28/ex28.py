one = True and True
print(f"True and True = {one}")

two = False and True
print(f"False and True = {two}")

three = 1 == 1 and 2 == 1
print(f"1 == 1 and 2 == 1 = {three}")

four = "test" == "test"
print(f"test == test = {four}")

five = 1 == 1 or 2 != 1
print(f"1 == 1 or 2 != 1 = {five}")

six = True and 1 == 1
print(f"True and 1 == 1 = {six}")

seven = False and 0 != 0
print(f"False and 0 != 0 = {seven}")

eight = True or 1 == 1
print(f"True or 1 == 1 = {eight}")

nine = "test" == "testing"
print(f"test == testing = {nine}")

ten = 1 != 0 and 2 == 1
print(f"1 != 0 and 2 == 1 = {ten}")

eleven = "test" != "testing"
print(f"test != testing = {eleven}")

twelve = "test" == 1
print(f"test == 1 = {twelve}")

thirteen = not (True and False)
print(f"not (True and False) = {thirteen}")

fourteen = not (1 == 1 and 0 != 1)
print(f"not (1 == 1 and 0 != 1) = {fourteen}")

fifteen = not (10 == 1 or 1000 == 1000)
print(f"not (10 == 1 or 1000 == 1000 = {fifteen}")

sixteen = not (1 != 10 or 3 == 4)
print(f"not (1 != 10 or 3 == 4) = {sixteen}")

seventeen = not ("testing" == "testing" and "Zed" == "Cool Guy")
print(f"not (testing == testing and Zed == Cool Guy) = {seventeen}")

eighteen = 1 == 1 and (not ("testing" == 1 or 1 == 0)) 
print(f"1 == 1 and (not (testing == 1 or 1 == 0)) = {eighteen}")

nineteen = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print(f"chunky == bacon and (not (3 == 4 or 3 == 3)) = {nineteen}")

twenty = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print(f"3 == 3 and (not (testing == testing or Python == Fun)) = {twenty}")
