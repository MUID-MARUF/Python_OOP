fineSystem = dict()

fineSystem['ABC-123'] = [200, 300]

while 1:
    car_code = input("Enter a car regestration number : ")
    fine_amount = int(input("Enter the fine amount : "))

    if(car_code in fineSystem):
        fineSystem[car_code].append(fine_amount)
        print(f"Car {car_code} fined {fine_amount}")
    else:
        fineSystem[car_code] = [fine_amount]
        print(f"Car {car_code} fined {fine_amount}")

    ch = input("Do you want to add more? Y/N : ")
    if ch == "Y":
        continue
    else :
        break

for x, y in fineSystem.items():
    print(x)
    print(sum(y))







