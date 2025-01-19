import os
from datetime import datetime
import json
import streamlit as st
from hashlib import sha512

# Path to store user_info
USER_DATA_FILE = "user_data.json"

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["current_user"] = None

# Load existing user
if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

def hash_password(password):
    return sha512(password.encode()).hexdigest()


# App Title
st.title("📝 My Gratitude Journal App")

tab = st.radio("Choose an option:", ["Login", "Sign Up"], key="auth_tab")

if tab == "Sign Up":
    st.subheader("Create an Gratitude Journal Account")
    st.text("Your own Gratitude Journal Account")

    # Input fields for username and password
    username = st.text_input("Enter a username: ", placeholder="coolguy123")
    password = st.text_input("Enter a password: ", type="password")
    confirm_password = st.text_input("Confirm your password: ", type="password")

    if st.button("Create Account"):
        if username.strip() and password.strip():
            if username in users:
                st.warning("Username already taken, please choose another username!")
            elif password != confirm_password:
                st.warning("Passwords do not match! Please try again")
            else:
                users[username] = hash_password(password)
                with open(USER_DATA_FILE, "w") as f:
                    json.dump(users, f)
                st.success("Account created successfully! You can now log in.")
        else:
            st.warning("Please fill out the fields")

elif tab == "Login":
    st.subheader("Login to Gratitude Journal")

    username = st.text_input("Enter your Username: ")
    password = st.text_input("Enter you Password: ", type="password")

    if st.button("Login"):
        if username.strip() and password.strip():
            if username in users and users[username] == hash_password(password):
                st.success(f"Welcome back, {username}!")
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = username

            else:
                st.warning("Invalid username or password. Please try again.")
        else:
            st.warning("Please enter both username and password.")



# Input area for the Journal Entry
if st.session_state["logged_in"]:
    st.subheader(f"Hello, {st.session_state['current_user']}")
    user_folder = os.path.join("journal_entries", st.session_state['current_user'])

    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    journal_entry = st.text_area("Write your journal entry here:", height=500, placeholder="I am grateful of...")

    custom_name = st.text_input("Enter a name for your entry (Optional):", placeholder="e.g. MyBeautifulEntry")

    if st.button("logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None

        st.query_params.update(auth_tab="Login")

        st.success("You have successfully logged out. Please manually refresh page if needed")

    # Save button for the journal entry
    if st.button("Save Entry"):
        if journal_entry.strip():
            # Create folder if it doesn't exist
            if not os.path.exists("journal_entries"):
                os.makedirs("journal_entries")

            # Generate a timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Human-readable format
            if custom_name.strip():
                filename = f"{custom_name.strip().replace(' ', '_')}.txt"
            else:
                filename = f"entry_{timestamp}.txt"
            file_path = os.path.join(user_folder, filename)

            # Save the journal entry with the timestamp at the top
            with open(file_path, "w") as file:
                file.write(f"Time and Date: {timestamp}\n\n{journal_entry}")

            st.success(f"Your entry has been saved as {filename}")
        else:
            st.warning("Please write something before saving!")
else:
    st.warning("Please log in before using")

# Display previous entries
if st.session_state.get("logged_in", False):
    if st.button("View Previous Entries"):
        user_folder = os.path.join("journal_entries", st.session_state["current_user"])
        print("Trace 0")
        if os.path.exists(user_folder) and os.listdir(user_folder):
            files = sorted(os.listdir(user_folder))
            print("Trace 1")

            # Display all files as a list
            for file_name in files:
                file_path = os.path.join(user_folder, file_name)
                with open(file_path, "r") as file:
                    content = file.read()

                    # Extract timestamp from the content
                    first_line = content.split("\n")[0].replace("Timestamp: ", "")
                    st.subheader(file_name)
                    st.markdown(f"**Time and Date:** {first_line}")  # Display the timestamp prominently
                    st.write("\n".join(content.split("\n")[2:]))  # Exclude "Timestamp:" and the blank line

        else:
            st.info("No journal entries found.")
