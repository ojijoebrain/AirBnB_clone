0x00. AirBnB clone - The console Project 

# A project between oji joseph oji and Lovette duke

# introduction: 
 This is the first step towards building your first full web application: the AirBnB clone.
 This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

# This task will help you linked and do the following below: 
>>>put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
>>>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
>>>create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
>>>create the first abstracted storage engine of the project: File storage.
>>>create all unittests to validate all our classes and storage engine

# using command interpreter:
using the command interpreter to be able to manage the objects of our project
---Create a new object (ex: a new User or a new Place)
---Retrieve an object from a file, a database etc…
---Do operations on objects (count, compute stats, etc…)
---Update attributes of an object
---Destroy an object

# How to start  the project proper 
step 1 
---you will need to clone the repository of the project from Github
step 2 
---After cloning the repository you will have a folder called AirBnB_clone
step 3
----In the AirBnB_clone floder all the files  will be created there to enable the program work 

/-------/
--- first, that creating the files like the following below 
--/console.py : the command interpreter. (cmd)
---models/engine/file_storage.py: Serializes instances to JSON file
---models/__ init __.py:  A unique `FileStorage` instance for the application
--models/base_model.py: class that  define all common attributes/methods 
--models/user.py: define User class that inherits from BaseModel
---models/state.py: State all class that inherits from BaseModel
---models/city.py: the City class that inherits from BaseModel
---models/review.py: Review class that inherits from BaseModel
---models/amenity.py: Amenity class that inherits from BaseModel

# How it work 

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


# AUTHORS

Oji joseph oji  |Emial: ojijosephoji@gmail.com 

Lovette Duke  | Emial: qutyluv@gmail.com

