# Daily
Track and Read Your Habits Everyday. Available on IOS and Android.


# High Level Overview
## Backend
### What are your features?
- Users have to register, and login (signup and authenticated with gmail)
- Users must be able to create tasks, update them, read, delete them
- What's your data looking like?
- User object
- Instance variables
- AllTasks = []
- CurrentTasks = [Not Done]
### Functions
- Task object
- Instance variable
- Category Type (DO, Won’t Do)
- Task Name (string)
- Done or Not Done (status type)
- Timestamp of created at (date created)
- Updated at timestamp (change text or complete task)

### What are the actions we want to do on that data?
- Create user
- Update user
- Delete user
- Read user
- Display a list of the user’s tasks in a graph form (react component), only completed tasks displayed
- Share graph (export graph as png/jpeg)
- display username under profile
- Update username under profile (change name)

# App Structure

### components
#### Reader
  - Reader.js
    - AddTask
    - TaskDone
    - RemoveTask
  - index.js
  - styles.js
#### SignIn
- SignIn.js
- index.js
- styles.js
#### Statistics
- Statistics.js
- styles.js
#### Profile
- Profile.js
- index.js
  - users --> display username 
  - emblem --> display user profile
  - logout --> redirect to login pag
- styles.js
- actions.js
- store.js
- index.js

### screens
### navigation
### screens
### yarn.lock
### package.json
### babel.config.js
### App.js (main)
### assets
  - store tab logos etc.
## backend
### src
#### api
#### backend
- daily
  - init.py
  - urls.py
  - wsgi.py
  - settings.py
#### database
- PostgreSQL
