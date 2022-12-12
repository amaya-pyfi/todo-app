import functions
import time
now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
user_prompt="Type add,edit,complete,show or exit: "

while True:
    user_action=input(user_prompt)
    user_action=user_action.strip()
    if  user_action.startswith('add'):
        todo = user_action[4:]
        todos=functions.get_todos()


        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()
        todo=todo+'\n'
        todos.append(todo)
        # file=open('todos.txt','w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)
    elif user_action.startswith('show'):
        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()

        todos=functions.get_todos()
        # new_todos=[]
        # for item in todos:
        #     new_item=item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])
            print(number)
            number=number-1
            todos=functions.get_todos()
                # print('existing todos', todos)

            todos[number]=input("Kindly enter new todo item : ")+'\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            index=int(user_action[9:])
            todos=functions.get_todos()
            todo_to_remove=todos[index-1].strip('\n')
            todos.pop(index-1)
            functions.write_todos(todos)
            message=f"Todo {todo_to_remove} was removed form the list"
            print(message)
        except IndexError:
            print('There is no item with that number. ')
            continue
    elif 'exit' in user_action:
        break
        # case _:
        #     print("Hey, you entered an unknown command")
    else:
        print("Command is not valid")

print("Bye")