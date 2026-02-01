# Basically, throughout the labs, we've been living with Python. 
# So we tell Docker: "Hey, I want a computer already set up with 3.9 Python, 
# but keep it slim to save storage and run faster!" Let's go!!
FROM python:3.9-slim

# What is Working Directory?
# Chill plz, lol
# Think of it like setting up a dedicated room, a sort of workspace where our main program will run.
# This keeps everything in one isolated place, 
# which makes it super easy to find and manage files.
WORKDIR /app

# By the way, here someone might wonder: why copy the requirements.txt first?
# Think of it like gathering all the tools and gear (like `flask`) before starting the actual work.
# Gotta make sure everything's ready to roll!
COPY requirements.txt .

# Now that we've got our shopping list (requirements.txt), 
# let's go download and install everything from the internet 
# so our app runs properly.
#
# We'll use '--no-cache-dir' like a broom to sweep away 
# unnecessary leftover files—keeping our image lean and clean!
RUN pip install --no-cache-dir -r requirements.txt

# Now it is time to bring all our app files into the container.
# This is like moving all our furniture and decorations into our new room.
# But we need to be careful here not to bring unnecessary stuff,
# such as jenkins files, git files, passwords, keys, etc.
COPY . .

# In real life, shipping containers are dark and closed—
# no connection to the outside world.
# Here, exposing port 5000 is like building a bridge
# so our inner app can communicate with everyone else.
EXPOSE 5000 

# Yay!! After all those setup steps,
# let’s announce that our baby Python app is ready to roll.
CMD ["python", "app.py"]
