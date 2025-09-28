import json

with open("file.json", "r") as file:
    data = json.load(file)
comand = ""
while comand != "exit":
    comand = input("enter: (add/show/completed/exit): ").lower()
    if comand == "add":
        new_chore = input("Enter a new chore: ")
        new_date = input("Enter the due date (MM/DD): ")
        #saves the new chore and data to the list
        data['tasks'].append({"chore": new_chore, "date": new_date})
        #saves the changes to the json file
        with open("file.json", "w") as file:
            json.dump(data, file, indent=4)
    if comand == "show":
        #TODO: add priority levels
        for task in data['tasks']:
            print(f"Chore: {task['chore']}, Due Date: {task['date']}")  
    if comand == "completed":
        chore_done = input("Enter the chore you completed: ")
        if chore_done in [task['chore'] for task in data['tasks']]:
            data['tasks'].remove({"chore": chore_done})
            with open("file.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Chore '{chore_done}' marked as completed and removed from the list.")
        else:
            print(f"Chore '{chore_done}' not found in the list.")
