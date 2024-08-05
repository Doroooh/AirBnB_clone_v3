#!/usr/bin/python3
""" Test .get() and .count() methods """
from models import storage
from models.state import State

# Print the total count of all objects
print(f"All objects: {storage.count()}")

# Print the count of State objects
print(f"State objects: {storage.count(State)}")

# Retrieve the ID of the first State object
states = storage.all(State)
if states:
    first_state_id = list(states.values())[0].id
    # Retrieve and print the first State object using its ID
    print(f"First state: {storage.get(State, first_state_id)}")
else:
    print("No State objects found.")
