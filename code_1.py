import json

with open("file.json", "r") as file:
    data = json.load(file)
comand = ""
while comand != "exit":
    comand = input("enter: (add/show/completed/exit): ").lower()
    if comand == "add":
        new_chore = input("Enter a new chore: ")
        new_date = input("Enter the due date (MM/DD): ")
        new_priority = input("Enter the priority (high/medium/low): ").lower()
        while new_priority not in ["high", "medium", "low"]:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
            new_priority = input("Enter the priority (high/medium/low): ").lower()
        new_tag = input("Enter a tag for the chore : ").lower()
        while new_tag not in ["academic", "sport", "other"]:
            print("Invalid tag. Please enter 'academic', 'sport', or 'other'.")
            new_tag = input("Enter a tag for the chore : ").lower()
        #saves the new chore and data to the list
        data['tasks'].append({"chore": new_chore, "date": new_date, "priority": new_priority, "tag": new_tag})
        #saves the changes to the json file
        with open("file.json", "w") as file:
            json.dump(data, file, indent=4)
    if comand == "show":
        levels = ["high", "medium", "low"]
        colors = {
            "high": "\033[92m",    # Red
            "medium": "\033[93m",  # Yellow
            "low": "\033[91m"      # Green
        }
        for i in levels:
            for task in data['tasks']:
                if (task['priority'] == i):
                    print(f"{colors[i]}Chore: {task['chore']}, Due Date: {task['date']}, Tag: {task['tag']}")
        print("\033[0m")  # Reset color
    if comand == "completed":
        #Fix Error
        chore_done = input("Enter the chore you completed: ")
        if chore_done in [task['chore'] for task in data['tasks']]:
            data['tasks'].remove({"chore": chore_done})
            with open("file.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Chore '{chore_done}' marked as completed and removed from the list.")
        else:
            print(f"Chore '{chore_done}' not found in the list.")
