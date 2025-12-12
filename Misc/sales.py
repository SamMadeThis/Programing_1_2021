import organisation 

def main ():
    personal_expenses = ["travel", "food", "cosmetics"]
    work_expenses = [ "tools", "travel"]
    functions = ["snacks", "coffee", "food"]
    
    

    organisation.identify_common_items(personal_expenses, work_expenses)
    organisation.identify_food(personal_expenses, work_expenses, functions)

main()
