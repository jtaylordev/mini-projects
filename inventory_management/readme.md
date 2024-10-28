# Inventory Management System

## Concepts Covered

### Classes and Objects

Classes are blueprints for creating objects. They encapsulate data for the object, and functions that manipulate that data.
Objects are instances of classes. When you create an object, you are creating an instance of a class with actual values.

### Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data within one unit (class). It restricts direct access to some of the object's components, which is a way of preventing accidental interference and misuse of the data.

Private Attributes/Methods: Prefixing an attribute or method with double underscores __ makes it private.
Protected Attributes/Methods: Prefixing with a single underscore _ suggests that it should be treated as non-public.

### Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability.

### Polymorphism

Polymorphism allows methods to have the same name but behave differently in different contexts. In OOP, this often involves method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class.

The Item class will serve as the parent class for all item types.

Attributes:

name: The name of the item.
price: The price of the item.
quantity: The quantity in stock.

Methods:

apply_discount(): Applies a discount to the item.

Electronics
Unique Attributes:

warranty_period: Duration of the warranty in months.
Methods:

Override apply_discount to provide a different discount mechanism.

Clothing
Unique Attributes:

size: Size of the clothing item.
material: Material of the clothing item.

Groceries
Unique Attributes:

expiration_date: Expiry date of the grocery item.
Methods:

Override apply_discount to handle perishable items.

Polymorphism is achieved through method overriding in the subclasses.

Each subclass (Electronics, Groceries) overrides apply_discount to implement specific discount logic.
The same method name (apply_discount) behaves differently depending on the object's class.


Inventory

Explanation:

items is a list that holds all the item objects.
apply_discounts iterates over all items and applies a discount, demonstrating polymorphism.
