max = 100
seats = [1,2,3]

x = 1
while x:
    inp_seat = int(input("Enter seat number to book (1-100): "))
    if inp_seat in seats:
        print(f"Seat {inp_seat} is already booked.")
    else:
        seats.append(inp_seat)
        print(f"Seat {inp_seat} successfully booked.")

    condi = input("Do you want to book more seats? Y/N :: ")
    if condi == "Y":
        continue
    else :
        break

print(len(seats))
