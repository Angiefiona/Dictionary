# Create a dictionary named my_dict with the following key-value pairs:
# "name": "John"
# "age": 25
# "city": "New York"
#"gender": "male"


my_dict = {"name":"John", "age": 25, "city":"New York", "gender":"male"}

# Access the value associated with the key "name" in the dictionary my_dict.
my_dict = {"name":"John", "age": 25, "city":"New York"}
print(my_dict.get("name"))

# Add a new key-value pair to the dictionary my_dict with the key "country" and the value "USA".
my_dict = {"name":"John", "age": 25, "city":"New York"}
my_dict ["country"] = "USA"
my_dict.update({"country":"USA"})
print(my_dict)

# Change the value associated with the key "age" in the dictionary my_dict to 26.
my_dict = {"name":"John", "age": 25, "city":"New York"}
my_dict["age"] = 26
my_dict.update({"age": 26})
print(my_dict)

# Use a loop to iterate over all the keys in the dictionary my_dict and print each key-value pair.
my_dict = {"name":"John", "age": 25, "city":"New York"}
for key, value in my_dict.items():
    print(key, ":", value)

# remove the last item in  my_dict and add key "complexion", value "Dark"
my_dict = {"name":"John", "age": 25, "city":"New York"}
my_dict.popitem()
print(my_dict)

my_dict.update({"complexion": "Dark"})
print(my_dict)




