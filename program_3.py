# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
# Constants for tax rates
stateTaxRate = 0.05 
countyTaxRate = 0.025 

def calculate_taxes(total_sales):
    """Calculate the county and state sales tax based on total sales."""
    county_tax = total_sales * countyTaxRate
    state_tax = total_sales * stateTaxRate
    total_tax = county_tax + state_tax
    
    return county_tax, state_tax, total_tax

def main():
    # Ask the user to enter total sales for the month
    total_sales = float(input("Enter the total sales for the month: $"))
    
    # Call the function to calculate taxes
    county_tax, state_tax, total_tax = calculate_taxes(total_sales)
    
    # Display the results
    print(f"county sales tax: ${county_tax:.2f}")
    print(f"state sales tax: ${state_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()




# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
