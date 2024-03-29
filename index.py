import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('My ToDo App')
st.subheader("This is my ToDo App ")
st.write('This app is to get your shit straight!')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index+1)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label=' ', placeholder='Add new task todo...',
              on_change=add_todo, key='new_todo' )

# st.session_state
