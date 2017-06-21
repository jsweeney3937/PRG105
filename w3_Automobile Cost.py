

# function get_info receives costs per month, calculates total cost per month
# prints monthly cost of automobile, calls function "y_total" and passes monthly total to it
def get_info():
    # gets cost per month of: loan, insurance, gas, oil, tire, maintenance
    m_loan = float(input("How much is your loan payment per month? "))
    m_insurance = float(input("How much is your insurance payment per month? "))
    m_gas = float(input("How much does it cost to fill your car with gas per month? "))
    m_oil = float(input("How much does it cost to replace your oil per month? "))
    m_tire = float(input("How much does it cost to maintain your tires per month? "))
    m_maintenance = float(input("How much is the maintenance per month? "))
    # calculates the total cost per month of automobile
    m_total = m_loan + m_insurance + m_gas + m_oil + m_tire + m_maintenance
    # prints the total cost per month of automobile
    print("The monthly expenses for your car are: $", format(m_total, ",.2f"), "per month.")
    # passes total monthly cost of automobile as argument to function y_total
    y_total(m_total)


# function y_total, takes m_total as parameter renames it as mon_total
def y_total(mon_total):
    # calculates yearly total
    y_cost = mon_total * 12
    # prints the yearly total
    print("Your yearly cost for your automobile is $", format(y_cost, ",.2f"))

# runs function get_info
get_info()
