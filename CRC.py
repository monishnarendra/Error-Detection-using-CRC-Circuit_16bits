def Division_Bianry():
    for i in range(0,DataWord_len):
        if(Modified_Data[i] == '1'):
            for j in range(0,poly_len):
                if(Modified_Data[i + j] == poly[j]):
                    Modified_Data[i+j] = '0'
                else:
                    Modified_Data[i+j] = '1'
    return Modified_Data

DataWord = input("Enter the input message in binary")
print("your Entered DataWord = ", DataWord)
# print(type(DataWord))

DataWord_len = len(DataWord)
print("Length DataWord = ", DataWord_len)

poly = "10001000000100001"
print("Given Polynomial= ", poly)
poly_len = len(poly)
print("Length Polynomial = ", poly_len)

Modified_Data = int(str(DataWord) + "0"*16)     # Add poly_len - 1 zeros
print("Modified_DataWord = ", Modified_Data)

Modified_Data = bin(Modified_Data)[2:]          # converting it to Binary and removing 0b
print("your Entered Modified_DataWord in binary = ", Modified_Data)
# print(type(Modified_Data))

Modified_Data = list(Modified_Data)             # Converting to list seance String are immutable

Check_Sum = Division_Bianry()

print("CRC Check Sum is = ",Check_Sum)

for i in range(0,DataWord_len):
    Check_Sum[i] = DataWord[i]                  # joining the result to the DataWord

Transmitted = Check_Sum

print("Transmitted Message = ",Transmitted)

error = int(input("Test Error Detection = "))
if (error == 0):
    i = int(input("Enter the Position to be inserted = "))
    Transmitted[i] = int(not Transmitted[i])    # Creating the error by negating the value at position i

Received = Division_Bianry()

print("Received = ",Received)

for i in Received:
    if(i == "0"):                               # Check if result is zero
        s = 1
    else:
        print("Error")
        s = 0
        break

if (s == 1):
    print("no Change in Data")
