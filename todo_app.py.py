import streamlit as st

st.set_page_config(page_title="To Do List", layout="centered")
st.title(" My To Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success(f"Added: {new_task}")
    else:
        st.warning("Please enter a task.")

st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.1, 0.9])
    done = col1.checkbox("", value=task["done"], key=i)
    if done:
        st.session_state.tasks[i]["done"] = True
        col2.markdown(f"{task['task']}")
    else:
        st.session_state.tasks[i]["done"] = False
        col2.markdown(task["task"])