# Assuming remove_list is predefined somewhere in the script or imported
remove_list = [...]  # List of IP addresses to be removed

# Assign the filename to the import_file variable
import_file = "allow_list.txt"

# Open the file that contains the allow list
with open(import_file, 'r') as file:
    # Read the content of the file into a string
    ip_addresses = file.read()

    # Convert the string into a list using newline as the delimiter
    ip_addresses = ip_addresses.split("\n")

# Iterate through the remove list
for element in remove_list:
    # Remove IP addresses that are on the remove list
    if element in ip_addresses:
        ip_addresses.remove(element)  # Remove the IP address from the allow list

# Convert the list back into a string
updated_ip_addresses = "\n".join(ip_addresses)

# Open the file in write mode to update it with the revised list of IP addresses
with open(import_file, 'w') as file:
    # Write the updated string back to the file
    file.write(updated_ip_addresses)

