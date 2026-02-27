def contact_manager():
    # 1. Initialization
    # Creating a list of phone numbers
    contacts = ["9876543210", "1122334455", "9988776655"]
    
    print("--- Initial State ---")
    print(f"Current Contacts: {contacts}")
    # Printing memory address to demonstrate mutability later
    print(f"Memory Address (ID) before modification: {id(contacts)}")

    # 2. Add a Contact (Demonstrating list.append())
    new_number = "5566778899"
    contacts.append(new_number)
    print(f"\n[+] Added {new_number} using append()")
    
    # 3. Remove a Contact (Demonstrating list.remove())
    remove_number = "1122334455"
    if remove_number in contacts:
        contacts.remove(remove_number)
        print(f"[-] Removed {remove_number} using remove()")
    
    print("\n--- Final State ---")
    print(f"Updated Contacts: {contacts}")
    
    # 4. Mutability Verification
    print(f"Memory Address (ID) after modification:  {id(contacts)}")
    
    # Logic: If IDs match, the object was modified in-place.
    print("\nConclusion: The memory address (ID) remained constant despite changes.")
    print("This proves that Python lists are MUTABLE.")

# Execute the function
contact_manager()