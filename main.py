from taskmanager import TaskManager
import sys

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments provided")
        print("Usage: task-cli [add|update|delete|list] [arguments]")
        sys.exit(1)

    command = args[0].lower()

    # debug
    print("COMMAND:", command, args)

    
    manager = TaskManager()

    if command == "add":
        if len(args) < 2:
            print("Please specify the task description to add")
            sys.exit(1)
        task_description = args[1]
        manager.add_task(task_description)
    elif command == "list":
        status = args[1] if len(args) > 1 else None
        manager.list_tasks(status)
    elif command == "update":
        if len(args) < 3:
            print("Please specify the task ID and the new description")
            sys.exit(1)
        task_id = int(args[1])
        new_description = args[2]
        manager.update_task(task_id, new_description)
    elif command == "delete":
        if len(args) < 2:
            print("Please specify the task ID to delete")
            sys.exit(1)
        manager.delete_task(int(args[1]))
    elif command == "mark_in_progress":
        if len(args) < 2:
            print("Please specify the task ID to mark as in progress")
            sys.exit(1)
        manager.mark_in_progress(int(args[1]))
    elif command == "mark_done":
        if len(args) < 2:
            print("Please specify the task ID to mark as done")
            sys.exit(1)
        manager.mark_done(int(args[1]))
    else:
        print("Invalid command")
        sys.exit(1)
if __name__ == "__main__":
    main()