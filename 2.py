def conversion(binary):
    convert1=int(binary, 2)
    print("Binary into Number: ", convert1)
    convert2=bin(convert1)[2:]
    print("Converted Back to Binary: ", convert2)
binary=input("Enter binary to convert into number: ")
conversion(binary)