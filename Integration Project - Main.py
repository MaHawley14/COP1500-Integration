# Matthew Hawley
# Integration Project - Florida Earnings & Savings calculator
# Allows an estimate or exact amount that you earn and save in one week

# Define the main function
def main():

# Introduction & Name input
    print("Welcome to the Florida Earnings & Savings Calculator!")
    name = input("Who are you? ")

#Begin the loop
    calculate_ess = "YES"
    while calculate_ess.upper() == "YES":

# Beginning Variables
        apparel_total = 0
        accessories_total = 0
        entertainment_total = 0
        food_total = 0
        utilities_total = 0
        transportation_total = 0

# Earning inputs: asks for input, & formats question response
        hourly_wage = float(input("What is your hourly wage? "))
        work_time = int(input("How many hours did you work? "))
        cash_question = input("Did you earn any extra cash this week, yes or no? ")
        if cash_question.upper() == "YES":
            extra_cash = float(input("How much did you earn? "))
        else:
            extra_cash = 0

# Spending inputs: asks for input, & formats question response
        apparel_question = input("Did you purchase any apparel this week, yes or no? ")
        if apparel_question.upper() == "YES":
            clothes_question = input("Did you spend anything on clothes this week, yes or no? ")
            if clothes_question.upper() == "YES":
                clothes_amount = float(input("How much did you spend? "))
                apparel_total += clothes_amount
            shoes_question = input("Did you spend anything on shoes this week, yes or no? ")
            if shoes_question.upper() == "YES":
                shoes_amount = float(input("How much did you spend? "))
                apparel_total += shoes_amount

        accessories_question = input("Did you purchase any accessories this week, yes or no? ")
        if accessories_question.upper() == "YES":
            bracelet_question = input("Did you spend anything on bracelets this week, yes or no? ")
            if bracelet_question.upper() == "YES":
                braclet_amount = float(input("How much did you spend? "))
                accessories_total += bracelet_amount
            earring_question = input("Did you spend anything on earrings this week, yes or no? ")
            if earring_question.upper() == "YES":
                earring_amount = float(input("How much did you spend? "))
                accessories_total += earring_amount
            necklace_question = input("Did you spend anything on necklaces this week, yes or no? ")
            if necklace_question.upper() == "YES":
                necklace_amount = float(input("How much did you spend? "))
                accessories_total += necklace_amount
            ring_question = input("Did you spend anything on rings this week, yes or no? ")
            if ring_question.upper() == "YES":
                ring_amount = float(input("How much did you spend? "))
                accessories_total += ring_amount

        entertainment_question = input("Did you purchase any entertainment this week, yes or no? ")
        if entertainment_question.upper() == "YES":
            book_question = input("Did you spend anything on books this week, yes or no? ")
            if book_question.upper() == "YES":
                book_amount = float(input("How much did you spend? "))
                entertainment_total += book_amount
            game_question = input("Did you spend anything on games this week, yes or no? ")
            if game_question.upper() == "YES":
                game_amount = float(input("How much did you spend? "))
                entertainment_total += game_amount
            movie_question = input("Did you spend anything on movies this week, yes or no? ")
            if movie_question.upper() == "YES":
                movie_amount = float(input("How much did you spend? "))
                entertainment_total += movie_amount
            sport_question = input("Did you spend anything on sports this week, yes or no? ")
            if sport_question.upper() == "YES":
                sport_amount = float(input("How much did you spend? "))
                entertainment_total += sport_amount

        food_question = input("Did you purchase any food this week, yes or no? ")
        if food_question.upper() == "YES":
            grocery_question = input("Did you spend anything on groceries this week, yes or no? ")
            if grocery_question.upper() == "YES":
                grocery_amount = float(input("How much did you spend? "))
                food_total += grocery_amount
            restaurant_question = input("Did you spend anything at restaurants this week, yes or no? ")
            if restaurant_question.upper() == "YES":
                restaurant_amount = float(input("How much did you spend? "))
                food_total += restaurant_amount

        utilities_question = input("Did you pay any utilities this week, yes or no? ")
        if utilities_question.upper() == "YES":
            air_question = input("Did you spend anything on A/C and/or heat this week, yes or no? ")
            if air_question.upper() == "YES":
                air_amount = float(input("How much did you spend? "))
                air_utilities_total += air_amount
            cable_question = input("Did you spend anything on cable this week, yes or no? ")
            if cable_question.upper() == "YES":
                cable_amount = float(input("How much did you spend? "))
                utilities_total += cable_amount
            electricity_question = input("Did you spend anything on electricity this week, yes or no? ")
            if electricity_question.upper() == "YES":
                electricity_amount = float(input("How much did you spend? "))
                utilities_total += electicity_amount
            internet_question = input("Did you spend anything on internet this week, yes or no? ")
            if internet_question.upper() == "YES":
                internet_amount = float(input("How much did you spend? "))
                utilities_total += internet_amount
            phone_question = input("Did you spend anything on phone this week, yes or no? ")
            if phone_question.upper() == "YES":
                phone_amount = float(input("How much did you spend? "))
                utilities_total += phone_amount
            water_question = input("Did you spend anything on water this week, yes or no? ")
            if water_question.upper() == "YES":
                water_amount = float(input("How much did you spend? "))
                utilities_total += water_amount

        transportation_question = input("Did you pay for transportation this week, yes or no? ")
        if transportation_question.upper() == "YES":
            ticket_question = input("Did you spend anything on bus tickets this week, yes or no? ")
            if ticket_question.upper() == "YES":
                ticket_amount = float(input("How much did you spend? "))
                transportation_total += ticket_amount
            gas_question = input("Did you spend anything on gas this week, yes or no? ")
            if gas_question.upper() == "YES":
                gas_amount = float(input("How much did you spend? "))
                transportation_total += gas_amount
            repair_question = input("Did you spend anything on vehicle repairs this week, yes or no? ")
            if repair_question.upper() == "YES":
                repair_amount = float(input("How much did you spend? "))
                transportation_total += repair_amount

# Calculation of the total earnings, spendings, & savings
        total_spent = apparel_total + accessories_total + entertainment_total + food_total + utilities_total + transportation_total         
        total_earned = (hourly_wage * work_time) + extra_cash
        total_saved = total_earned - total_spent

# Outputs the total earnings, spendings, & savings
        print(name + " this week you earned $" + format(total_earned, ".2f") + "\n and spent a total of $" + format(total_spent, ".2f") +
          "\n which as left a total of $" + format(total_spent, ".2f") + " saved.")
        print("Warning: No state or federal taxes have been accounted for.")

# Ask about calculating another earnings, spendings, & savings
        calculate_ess = input("Would you like to calculate another earnings, spendings, & savings, Yes or No? ")
        if calculate_ess.upper() == "YES":
            print("Accepted. Program recommencing.")
        else:
            print("Okay, Goodbye!")

# Call the main function
main()
