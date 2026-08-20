# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation can be applied by putting a product's data, such as its name, price, and quantity, inside a `Product` object. Methods such as `addStock()` and `sellProduct()` can be used to control changes to the product's quantity instead of allowing other parts of the program to change it directly. This keeps the product's data and related behaviors organized in one place and helps prevent incorrect changes to the inventory.

### 2. Abstraction

Abstraction can be applied by providing simple methods that hide the complicated details of how the inventory works. For example, the store could use methods such as `addProduct()` and `checkStock()` without needing to know all the internal steps involved. This makes the program easier to use and allows the user to focus on the important functions of the inventory system.

### 3. Inheritance

Inheritance can be used by creating a general `Product` class and then creating specialized classes that inherit from it. For example, `FoodProduct` and `DrinkProduct` could inherit properties such as `productName`, `price`, and `quantity` from the `Product` class. This reduces repeated code and makes it easier to add different types of products to the inventory system.

### 4. Polymorphism

Polymorphism can be applied when different types of products use the same method but perform the method in different ways. For example, a `getProductInfo()` method could be used by both `FoodProduct` and `DrinkProduct`, while each class provides its own version of the method. This makes the program more flexible because the same method can work with different types of products.

## Reflection

The four pillars of OOP can improve the sari-sari store inventory system by making the program more organized, reusable, and easier to maintain. Encapsulation keeps data and related methods together, abstraction hides unnecessary details, inheritance allows classes to reuse code, and polymorphism allows different objects to respond to the same method in different ways. Using these concepts would make the inventory system easier to expand as the number and types of products increase.
