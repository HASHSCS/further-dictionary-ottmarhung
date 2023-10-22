# 1. Get Length and Type
def get_length(my_dict):
    """
    TODO: Implement a function that returns the number of items (key-value pairs) in `my_dict`.
    """
    return(len (my_dict))

def get_type(my_dict):
    """
    TODO: Implement a function that returns the type of `my_dict`.
    """
    return (type(my_dict))

# 2. Access Items
def access_by_key(my_dict, key):
    """
    TODO: Implement a function that returns the value for key `key` in `my_dict` using bracket notation.
    """
    return (my_dict[key])

def access_by_get(my_dict, key):
    """
    TODO: Implement a function that returns the value for key `key` in `my_dict` using the get() method.
    """
    return my_dict.get(key)

# 3. Change Items
def update_value_directly(my_dict, key, value):
    """
    TODO: Implement a function that updates the value of `key` in `my_dict` to `value` using bracket notation and returns the updated dictionary.
    """
    my_dict[key] = value
    return my_dict

def update_value_with_update(my_dict, key, value):
    """
    TODO: Implement a function that updates the value of `key` in `my_dict` to `value` using the update() method and returns the updated dictionary.
    """
    my_dict.update({key: value})
    return my_dict

# 4. Add Items
def add_item_directly(my_dict, key, value):
    """
    TODO: Implement a function that adds a new item with key `key` and value `value` to `my_dict` using bracket notation and returns the updated dictionary.
    """
    my_dict[key] = value
    return my_dict  

def add_item_with_update(my_dict, key, value):
    """
    TODO: Implement a function that adds a new item with key `key` and value `value` to `my_dict` using the update() method and returns the updated dictionary.
    """
    my_dict.update({key:value})
    return my_dict
# 5. Remove Items
def remove_item_by_pop(my_dict, key):
    """
    TODO: Implement a function that removes the item with key `key` from `my_dict` using the pop() method and returns the updated dictionary.
    """
    
    my_dict.pop(key)
    return my_dict

def remove_item_by_del(my_dict, key):
    """
    TODO: Implement a function that removes the item with key `key` from `my_dict` using del statement and returns the updated dictionary.
    """
    del my_dict[key]
    return my_dict

# 6. Looping through Dictionaries
def get_keys(my_dict):
    """
    TODO: Implement a function that returns all keys in `my_dict`.
    """
    a = []
    for key in my_dict:
        a.append(key)
    return a     
    
def get_values(my_dict):
    """
    TODO: Implement a function that returns all values in `my_dict`.
    """
    a = []
    for key in my_dict:
        a.append(my_dict[key])
    return a     

def get_items(my_dict):
    """
    TODO: Implement a function that returns all items (key-value pairs) in `my_dict`.
    """
    return my_dict.items()

# 7. Copying Dictionaries
def copy_with_copy_method(my_dict):
    """
    TODO: Implement a function that returns a copy of `my_dict` using the copy() method.
    """
    return my_dict.copy()

def copy_with_dict_constructor(my_dict):
    """
    TODO: Implement a function that returns a copy of `my_dict` using the dict() constructor.
    """
    new_dict =  dict(my_dict)
    return new_dict
# 8. Find Values
def find_values(input_dict, keys):
    """
    TODO: Implement a function that returns a list of values from `input_dict`. 
    For each key in `keys`, get its value in `input_dict` and append it to the list. 
    If a key is not present, append None.
    """
    
    lst = [] 
    for key in keys:
        if key in input_dict:
            lst.append(input_dict[key])
        else:
            lst.append(None)
    return lst