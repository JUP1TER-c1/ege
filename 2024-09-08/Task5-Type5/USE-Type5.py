for number in range(100, 1, -1):
    bin_number = str(bin(number)[2:])
    bin_number += str(bin_number.count("1") % 2)
    bin_number += str(bin_number.count("1") % 2)
    if int(bin_number, 2) < 100:
        print(int(bin_number, 2))
        break