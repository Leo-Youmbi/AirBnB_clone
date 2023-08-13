# AirBnB Clone
This repository contains an AirBnB clone project, which aims to replicate some of the core functionalities of the popular AirBnB website. The project includes a command interpreter that allows users to interact with the application through a text-based interface. By following the instructions below, you can start the command interpreter and explore its features.

## Description of the Command Interpreter
The command interpreter provides a Shell-like interface for managing properties, users, bookings, and other aspects of the AirBnB clone. It allows users to execute commands and perform operations such as creating, updating, deleting, and retrieving data. The command interpreter supports various commands and follows a specific syntax for input.

## How to Start the Command Interpreter
To start the command interpreter, follow these steps:  
1. Clone this repository to your local machine using the following command:
```
git clone https://github.com/Leo-Youmbi/AirBnB_clone.git
```

2. Navigate to the cloned repository's directory:
```
cd AirBnB_clone
```

3. Run the command interpreter by executing the console.py file:
```
python console.py
```

After executing these steps, you should see the command prompt of the AirBnB clone's command interpreter, indicating that it is ready for user input.

## How to Use the Command Interpreter
Once the command interpreter is running, you can execute various commands to interact with the AirBnB clone. The general syntax for a command is as follows:

```
command_name [arguments] [options]
```
Here are some essential commands that you can use:

* `create`: Create a new instance of a class (e.g., property, user).
* `update`: Update the attributes of an instance.
* `show`: Display the details of a specific instance.
* `destroy`: Delete a particular instance.
* `all`: Display all instances of a given class or all classes.
* `quit` or `EOF`: Exit the command interpreter.  

For a complete list of commands and their usage, you can type `help` or `help [command_name]` within the command interpreter.

## Examples
Here are a few examples of how to use the command interpreter:

1. Create a new property:
```
(hbnb) create City
```

2. Show the details of a specific user:
```
(hbnb) show User 987654
```

3. Display all instances of the User class:
```
(hbnb) all User
```

Feel free to explore and experiment with the available commands to get familiar with the functionality of the AirBnB clone.

With this command interpreter, you can manage properties, users, and bookings, mimicking some of the core features of the actual AirBnB website. Enjoy exploring and developing your own version of the AirBnB clone!