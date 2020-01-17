
# **`Family Tree`**

![Alt text](resources/tree.png?raw=true "Title")


## **`Description`**

The project models a family tree based on the image above .
All the metadata (name , gender) of every entity is kept exactly as it is given .

## **`Available Operation`**

- ***GET_RELATIONSHIP*** ::&nbsp;&nbsp;Given a _name_ and a _relationship_, output the people corresponding to the relationship in the order in
which they were added to the family tree. *Assume the names of the family members are unique*.
    - &nbsp;&nbsp;&nbsp;`Formart : GET_RELATIONSHIP   <Name>   <Relationship>`
>    - **Available RelationShips**
>
>| Relationships 	| Paternal-Uncle    	| Maternal-Uncle    	| Paternal-Aunt    	| Maternal-Aunt    	| Sister-In-Law                       	| Brother-In-Law                          	| Son 	| Daughter 	| Siblings 	|
>|---------------	|-------------------	|-------------------	|------------------	|------------------	|-------------------------------------	|-----------------------------------------	|-----	|----------	|----------	|
>| Definition    	| Father’s brothers 	| Mother’s brothers 	| Father’s sisters 	| Mother’s sisters 	| Spouse’s sisters, Wives of siblings 	| Spouse’s brothers, Husbands of siblings 	|     	|          	|          	|


- ***ADD_CHILD*** ::&nbsp;&nbsp;Add a child to any family in the tree through the **mother**.
    - &nbsp;&nbsp;&nbsp;`Formart : ADD_CHILD <Mother’s-Name>  <Child's-Name>  <Gender>`
        
- example

    :zap:&nbsp;&nbsp;ADD_CHILD Satya Ketu Male
    
    :zap:&nbsp;&nbsp;GET_RELATIONSHIP Chitra Siblings
    
    :zap:&nbsp;&nbsp;GET_RELATIONSHIP Amba Daughter
    
    :zap:&nbsp;&nbsp;GET_RELATIONSHIP Yodhan Paternal-Uncle
    
    :zap:&nbsp;&nbsp;GET_RELATIONSHIP Atya Sister-In-Law


## :rocket:&nbsp;**`Run Project`**

* Input format is as below - 

    &nbsp;&nbsp;&nbsp;&nbsp;`python -m geektrust <absolute_path_to_input_file>`

## :detective:&nbsp;**`Project Modules`**

-   **make_family** holds the interface for initial insertion of the family members and their respective relations 
    
    with other members.

-   **family** handles all actual implementations of the insertion of the family seed data.This module also implements the main singleton object , 
    
    which holds the whole family tree data , to be used across the entire project and updates itself with every add event . 

-   **member** this is the class for every member object which has the fields *name,sex,father,mother,etc.*

    This module also has various methods like *get_father,get_siblings,etc.* to get relations and other related data of the member
    
-   **executor** handles the operations that needs to be performed and maps it to the get_attribute methods of the *member* class

 