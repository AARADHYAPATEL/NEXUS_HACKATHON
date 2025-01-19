# NEXUS_HACKATHON
This is my repository of the nexus hackathon.

## Gratitude Journal App
**Project summary:** This is a gratitude journal app that allows users to enter entries about what they are grateful about. This app uses streamlit as its base of development. This app includes User authentication, area to enter the entry, option to Sign Up and Login, option to Logout, option to save an entry and an option to view the previous entries. Each entry is user specific so only the user who made the entries can view them and can’t view any other users entries.

**Key Features:** 
- The app will allow users to enter their entries and save them.
- It will correspond specific entries with the user that entered them.
- It will give two options in the form of Radio buttons: One to Sign-Up and one to Login.
- In the Sign Up tab, the user will be asked to enter their username and password, with a password reconfirmation. Then after Signing Up the 
  user should click on the Login tab to log-in, with their same credentials.
- After writing the entry, the user must click on the save entry button to save their entry. This entry will be saved onto a folder named 
  according to the user’s username.
- The user can view all their entries if they click the “View Previous entries” button.
- The user can Logout by clicking on the “Logout” button.
- The user can’t enter any entries after they log out.
- A nice, presentable UI.
- The user can give a custom name to their entry.
- Has a timestamp with the user entry.
- Stores all user directories in a folder called “Journal_entries”.

**User Instructions:**
- If the user is new, they must first Sign Up by entering the credentials like their username and password. Their password must be reconfirmed.
- Then they must click on the Login button and Login to start using their personalized Gratitude Journal!
- The user will be able to write whatever they want in a big sized text box with no limit to how much can they write.
- After writing, the user can save their entry to whatever name they want. If they don’t then a name is automatically generated.
- They can view their previous entries by clicking on the view previous entries button.
- Finally, if the user is done writing their entries, they can click on the logout button. After clicking, they will no longer be able to     
  write their entries without logging in again.

**System requirements:**
 - Good internet, preferably 5G.
 - System with minimum 8GB RAM and 256 GB ssd minimum
 - An IDLE (Pycharm recommended) to execute
 - Python (Miniconda or Anaconda recommended).
 - A web browser (Opera GX recommended)

**Limitations:**
 - Cannot remember users due to no caching.
 - All files are accessible to the creator.
 - The entries will keep on getting listed, which will make the page go on for very long.
 - Does not include authentication with google and others.
 - Has a very basic JSON database.
 - Does not include detailed AI analysis or user data analysis.

**Tools/Frameworks used:**
 - JetBrains Pycharm Community Edition 2024.3.1.1 (IDLE)
 - Python Miniconda distribution
 - Streamlit web development framework.
 - Hashlib’s Sha512 for password Hashing.
 - JSON Database to store user data.
 - Text files to store user entries with Timestamp.
 - Uses the Datetime library to show Timestamp.
 - Usage of Command Prompt to run.
