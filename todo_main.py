def main():
    """
    declares task dict, gets task list, loads up dict, shows table,
    asks for completion, and shows table again
    """
    tasks = {}
    next_id = 1

    task_list = user_input()
    next_id = add_to_dict(tasks, task_list, next_id)  # captures return

    display_dict(tasks)
    task_complete_check(tasks)   # changes completed
    display_dict(tasks)
    remove_from_dict(tasks)
    display_dict(tasks)


def user_input():
    """
    returns a list of strings task names
    """
    task_list = []
    num_of_tasks = input("How many tasks would you like to add?\n").strip()
    try:
        count = int(num_of_tasks)
    except ValueError:
        print("Please enter a number.")
        return task_list

    while count > 0:
        task_name = input("What task would you like to add?\n").strip()
        if task_name:
            task_list.append(task_name) # keeps raw text
            count -= 1
    return task_list


def add_to_dict(tasks, task_list, next_id):
    """
    puts task_list into tasks dict using IDs and completed set to False
    """
    for name in task_list:
        tasks[next_id] = {"task": name, "completed": False}
        next_id += 1
    return next_id

def remove_from_dict(tasks):
    """
    removes task from tasks dict using IDs
    """
    remove_task = prompt_int("ID to remove task:\n")
    if remove_task is None:
        return
    if remove_task in tasks:
        del tasks[remove_task]
        print(f"removed {remove_task}.")
    else:
        print(f"No such task with that ID")

def display_dict(tasks):
    """
    prints a table from dict
    """
    if not tasks:
        print("no tasks yet")
        return

    print(f"{'#':<4}{'Task':<25}{'Completed'}")
    print("-" * 50)
    for tid, item in tasks.items():
        done = "Yes" if item["completed"] else "No"
        print(f"{tid:<4}{item['task']:<25}{done}")


def task_complete_check(tasks):
    """
    asks Y/N then asks for an ID and marks completed as True
    """
    ans = input("Did you complete any tasks? Y/N\n").strip().lower()
    if ans not in {"y", "yes"}:
        return

    task_id = prompt_int("What task did you complete? (enter ID)\n")
    if task_id is None:
        return

    if task_id in tasks:
        if not tasks[task_id]["completed"]:
            tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked complete.")
        else:
            print("That task is already complete.")
    else:
        print("No task with that ID.")


def prompt_int(msg):
    """
    safe int prompts and returns int or None
    """
    safeint = input(msg).strip()
    try:
        return int(safeint)
    except ValueError:
        print("Invalid number.")
        return None


if __name__ == "__main__":
    main()
