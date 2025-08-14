def main():
    """
    declares task dict, gets task list, loads up dict, shows table,
    asks for completion, and shows table again
    """
    tasks = {}
    next_id = 1
    next_id = command_room(tasks,next_id)

def add_to_dict(tasks, next_id, cmd_text):
    """
    puts task_list into tasks dict using IDs and completed set to False
    adds tasks
    """
    if cmd_text == "":
        print("add <task text here>")
        return next_id
    tasks[next_id] = {"task": cmd_text, "completed": False}
    print(f"added " + str(next_id)+ " : " + cmd_text)
    next_id += 1
    return next_id

def remove_from_dict(tasks, cmd_text):
    """
    removes task from tasks dict using IDs
    """
    if cmd_text != "":
        t_id = to_int(cmd_text)
    else:
        user_input = to_int(input("ID to remove: ").strip())
        t_id = user_input
    if t_id is None:
        print("ID must be a whole number.")
        return
    if t_id in tasks:
        task_name = tasks[t_id]["task"]
        del tasks[t_id]
        print(f"#" + str(t_id)+ ". " + task_name + " has been removed.")
    else:
        print(f"No task with that ID.")

def display_dict(tasks):
    """
    prints a table from dict
    """
    if len(tasks) == 0:
        print("No tasks to display, yet.")
        return

    print(f"{'Row':<4}{'ID':<4}{'Task':<25}{'Completed'}")
    print("-" * 50)
    row_number = 1

    for t_id, task_checker in tasks.items():
        if task_checker["completed"] == True:
            completed_text = "Yes"
        else:
            completed_text = "No"
        print("{:<4}{:<4}{:<25}{:<10}".format(row_number, t_id, task_checker["task"], completed_text))
        row_number += 1


def task_complete_check(tasks, cmd_text):
    """
    asks Y/N then asks for an ID and marks completed as True
    checks if completed tasks
    """
    if cmd_text != "":
        t_id = to_int(cmd_text)
    else:
        user_input = input("ID to complete: ").strip()
        t_id = to_int(user_input)
    if t_id is None:
        print("ID must be a whole number.")
        return
    if t_id in tasks:
        if tasks[t_id]["completed"] == True:
            print("Task already completed.")
            return
        tasks[t_id]["completed"] = True
        print("Marked " + str(t_id) + " as completed.")
    else:
        print("No task with that ID.")

def to_int(s):
    """
    converts string to int
    if any fail returns None
    """
    try:
        return int(s)
    except Exception:
        return None

def prompt_int(msg):
    """
    safe int prompts and returns int or None
    """
    user_input = input(msg).strip()
    try:
        return int(user_input)
    except ValueError:
        print("Invalid number.")
        return None
def help_prompt():
    print("""commands:
    help                  show help
    list                  show list of tasks
    add <task name here>  add task (text)
    remove <ID # here>    remove task via ID
    completed <ID # here> complete task via ID
    exit                  exit program
    """)

def command_room(task, next_id):
    """
    Lists out commands and allows user to choose where to go next
    commands: help, list, add, remove, completed, help, exit
    """
    commands = {"help": None, "list": None, "add": add_to_dict,
                "remove": remove_from_dict, "completed": task_complete_check, "exit": None}
    print("to-do list - type 'help' to see available commands\n")
    while True:
        user_input = input().strip()
        if user_input == "":
            continue

        readable =  user_input.split(maxsplit=1) #splits string in two max strings
        if len(readable) == 2:
            cmd_input = readable[0].lower()
            cmd_text = readable[1]
        else:
            cmd_input = readable[0].lower()
            cmd_text = ""

        if cmd_input == "help":
            help_prompt()
        elif cmd_input == "list":
            display_dict(task)
        elif cmd_input == "add":
            next_id = add_to_dict(task, next_id, cmd_text) # captures returned next_id
        elif cmd_input == "remove":
            remove_from_dict(task, cmd_text)
        elif cmd_input == "completed":
            task_complete_check(task, cmd_text)
        elif cmd_input == "exit":
            print("Exiting Program.")
            break
        else:
            print("Invalid command. Type ' help' to see available commands")

    return next_id

if __name__ == "__main__":
    main()
