This Streamlit application creates a simple, interactive to-do list. Here's what it does:

1. **Initializes Task List**: Creates an empty list in the session state to store tasks if one doesn't already exist.

2. **Adds New Tasks**: 
   - Provides a text input field where users can type new tasks
   - Includes an "Add Task" button that appends the new task to the list
   - Shows success message when a task is added or warning if the input is empty

3. **Displays and Manages Tasks**:
   - Shows all tasks in a list format
   - Each task has a checkbox to mark it as completed
   - Completed tasks are displayed with strikethrough formatting
   - Updates the task status (done/not done) in the session state when checkboxes are toggled

The app maintains state across interactions using Streamlit's session state functionality.
