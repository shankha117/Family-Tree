![Alt text](resources/tree.png?raw=true "Title")


#**`Description`**

The project models a family tree based on the image above .
All the metadata (name , gender) of every entity is kept as it is given .

#**`Available Operation`**

* Given a _name_ and a _relationship_, output the people corresponding to the relationship in the order in
which they were added to the family tree. `Assume the names of the family members are unique.`

* add a child to any family in the tree through the **mother**.

* example

```diff
ADD_CHILD Satya Ketu Male
GET_RELATIONSHIP Chitra Siblings
GET_RELATIONSHIP Amba Daughter
GET_RELATIONSHIP Yodhan Paternal-Uncle
GET_RELATIONSHIP Atya Sister-In-Law
   ``` 

