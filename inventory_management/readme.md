# Inventory Management System

## Key Concepts

### Classes and Objects

Classes serve as blueprints for creating objects, encapsulating both the data and the functions that operate on that data. Objects are instances of these classes, representing specific entities with defined attributes and behaviors.

### Encapsulation

Encapsulation involves bundling data (attributes) and methods (functions) within a single unit (class) to restrict direct access, thus preventing accidental interference or misuse of data.

- **Private Attributes/Methods**: Attributes or methods prefixed with double underscores (`__`) are made private, limiting their accessibility.
- **Protected Attributes/Methods**: Attributes or methods prefixed with a single underscore (`_`) are treated as non-public, suggesting they should not be accessed directly outside the class.

### Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reuse and modularity.

### Polymorphism

Polymorphism allows different classes to define methods with the same name but distinct behaviors. In object-oriented programming, this is often achieved through method overriding, where a child class provides a specific implementation of a method inherited from the parent class.

## Item Categories

### Items

- **Attributes**:
  - `name`: The name of the item.
  - `price`: The price of the item.
  - `quantity`: The quantity in stock.

- **Methods**:
  - `apply_discount()`: Applies a discount to the item.

### Electronics

- **Unique Attributes**:
  - `warranty_period`: The warranty period for the electronic item (in months).

- **Methods**:
  - Override `apply_discount()`: Implements a different discount mechanism for electronics.

### Clothing

- **Unique Attributes**:
  - `size`: The size of the clothing item.
  - `material`: The material composition of the clothing item.

### Groceries

- **Unique Attributes**:
  - `expiration_date`: The expiration date of the grocery item.

- **Methods**:
  - Override `apply_discount()`: Provides a specific discount logic to handle perishable items.

### Polymorphism in Action

Polymorphism is demonstrated by overriding the `apply_discount()` method in the subclasses. Each subclass, such as `Electronics` and `Groceries`, provides its own specific implementation of the method, allowing the same method name (`apply_discount()`) to behave differently based on the context of the class instance.

## Inventory Management

- **Inventory**:
  - `items` is a list that holds all item objects.
  - `apply_discounts()`: Iterates over all items and applies the appropriate discount, showcasing polymorphism in action.

