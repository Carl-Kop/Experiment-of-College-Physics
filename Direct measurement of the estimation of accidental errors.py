import math
data = []
while True:
    user_input = input("Enter an experiment data (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        number = float(user_input)
        data.append(number)
    except ValueError:
        print("Please enter a valid number.")
g0=input("Enter the g0 value selected by you using Grubbs' test:")
g0=float(g0)
delta_yi=input("enter your instrumental error")
delta_yi=float(delta_yi)
Ub=delta_yi/math.sqrt(3)
if data:
    def calculate_data():
        average = sum(data) / len(data)
        max_value = max(data)
        min_value = min(data)
        length=len(data)
        total=0
        for i in range(length):
            total=(data[i]-average)**2
        sigmax=math.sqrt(total/(length))
        sigmaxba = math.sqrt(total/(length*(length-1)))
        gi=(max_value-average)/(sigmaxba)
        if gi>=g0:
            data.pop(data.index(max_value))
            calculate_data()
        else:
            sigma = math.sqrt(sigmaxba**2+Ub**2)
            print(f"Average: {average:.2f}")
            print(f"Max: {max_value}")
            print(f"Min: {min_value}")
            print(f"Location of the maximum data{data.index(max_value)}")
            print(f"Total data equal to{length}")
            print(f"The standard deviation is{sigma}")
            print(f"The measurement results are expressed as{average}±{sigma}")
    calculate_data()

else:
    print("No data collected")