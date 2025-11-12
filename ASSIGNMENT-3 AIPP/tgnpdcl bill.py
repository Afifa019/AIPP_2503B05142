# Electricity Bill Generator for TGNPDCL
# Developed using AI assistance (e.g., GitHub Copilot / Gemini)

# Input section
customer_name = input("Enter Customer Name: ")
customer_type = input("Enter Customer Type (Domestic/Commercial): ")
pu = float(input("Enter Previous Units: "))
cu = float(input("Enter Current Units: "))


# Calculate number of units consumed
units = cu - pu

# Initialize charges
ec = fc = cc = ed = total_bill = 0

# Calculation based on customer type
if customer_type.lower() == "domestic":
    if units <= 100:
        ec = units * 1.5
    elif units <= 200:
        ec = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        ec = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 3.5)
    fc = 50
    cc = 30
    ed = 0.05 * ec
else:
    if units <= 100:
        ec = units * 3.0
    elif units <= 200:
        ec = (100 * 3.0) + ((units - 100) * 4.5)
    else:
        ec = (100 * 3.0) + (100 * 4.5) + ((units - 200) * 5.5)
    fc = 100
    cc = 50
    ed = 0.10 * ec

# Total bill
total_bill = ec + fc + cc + ed

# Bill summary
print("\n------ ELECTRICITY BILL SUMMARY ------")
print(f"Customer Name        : {customer_name}")
print(f"Previous Units       : {pu}")
print(f"Current Units        : {cu}")
print(f"Units Consumed       : {units}")
print(f"Customer Type        : {customer_type}")
print("---------------------------------------")
print(f"Energy Charges (EC)  : ₹{ec:.2f}")
print(f"Fixed Charges (FC)   : ₹{fc:.2f}")
print(f"Customer Charges (CC): ₹{cc:.2f}")
print(f"Electricity Duty (ED): ₹{ed:.2f}")
print("---------------------------------------")
print(f"Total Bill Amount    : ₹{total_bill:.2f}")
print("---------------------------------------")
print("Thank you for using TGNPDCL Bill Generator!")