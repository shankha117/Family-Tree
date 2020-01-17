
# **`Family Tree`**

![Alt text](resources/tree.png?raw=true "Title")


# **`Description`**

The project models a family tree based on the image above .
All the metadata (name , gender) of every entity is kept as it is given .

# **`Available Operation`**

* ***GET_RELATIONSHIP*** :: Given a _name_ and a _relationship_, output the people corresponding to the relationship in the order in
which they were added to the family tree. *Assume the names of the family members are unique*.

     `**Formart** : GET_RELATIONSHIP ”Name” “Relationship”`

* ***ADD_CHILD*** :: add a child to any family in the tree through the **mother**.
        
        `**Formart** : GET_RELATIONSHIP ”Name” “Relationship”`
        
        Formart** : GET_RELATIONSHIP ”Name” “Relationship”
* example

    :zap:ADD_CHILD Satya Ketu Male
    
    :zap: GET_RELATIONSHIP Chitra Siblings
    
    :zap: GET_RELATIONSHIP Amba Daughter
    
    :zap: GET_RELATIONSHIP Yodhan Paternal-Uncle
    
    :zap: GET_RELATIONSHIP Atya Sister-In-Law


# :rocket:&nbsp;**`Run Project`**

* input format is as below - 

    `python -m geektrust <absolute_path_to_input_file>`