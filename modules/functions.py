FILEPATH = "todos.txt"


def get_todos(path=FILEPATH):
    """Read a text file and return the list of
        to-do items."""
    with open(path, "r") as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(local_todos, path=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(path, "w") as file:
        file.writelines(local_todos)


older_version = """no need to close stream

                     file = open(r"files/todos.txt", "r")
                     todos = file.readlines()
                     file.close()

             todos.append(todo)

                     file = open(r"files/todos.txt", "w")
                     file.writelines(todos)
                     file.close()
        """

# print(__name__)
if __name__ == "__main__": # this condition is valid only when runnable from the class itself, if u run it inside
    # other class(imported) it will print the name of package.class
    print(get_todos())
