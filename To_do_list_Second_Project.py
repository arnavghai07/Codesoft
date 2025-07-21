# Task manager with status and importance tracking
todo_items = {}

# Collecting tasks
while True:
    task_input = input("Add a new task (type 'quit' to stop): ")
    if task_input.strip().lower() in ['quit', 'stop']:
        break
    level = input("Priority level? (High/Medium/Low): ")
    todo_items[task_input] = {'importance': level, 'done': False}

# Display current to-do list
print("\n📝 To-Do Overview:")
for task_name, details in todo_items.items():
    completion = "Completed" if details['done'] else "Pending"
    print(f"- {task_name} [{details['importance']}] : {completion}")

# Update completion status
while True:
    finished = input("Which task is now done? (type 'end' to stop): ")
    if finished.lower() == 'end':
        break
    if finished in todo_items:
        todo_items[finished]['done'] = True
    else:
        print(f"'{finished}' not found in your list.")

# Final list output
print("\n✅ Final To-Do Status:")
for title, info in todo_items.items():
    result = "Completed" if info['done'] else "Pending"
    print(f"- {title} | Priority: {info['importance']} | Status: {result}")