# Question 5: Contact Book
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999",
}

print(f"Alice's number: {contacts['Alice']}")

contacts["Diana"] = "555-4321"  # Adding a new contact
contacts["Bob"] = "555-0000"    # Updating Bob's number
del contacts["Charlie"]         # Deleting Charlie's contact

print(f"All names: {contacts.keys()} \n") # list so that it only takes what's in keys and not other info
print(f"All names: {list(contacts.keys())}") 
print(f"All numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")
