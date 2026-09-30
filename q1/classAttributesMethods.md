# Class Attributes and Methods

## Previous Design

Link to my previous activity:

[classObjectUML.md](classObjectUML.md)

## Design Revision

No major changes were needed from my original design. I kept the Gun class and improved the visibility of some attributes.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| gunName | string | Public | The gun's name can be viewed and displayed by other parts of the program. |
| damage | int | Public | The damage value can be accessed to show weapon statistics. |
| automatic | bool | Public | Other parts of the program may need to know whether the gun is automatic. |
| magazineSize | int | Private | The bullet count should only be changed through methods like fire() and reload(). |

## Updated UML Class Diagram

![Class Diagram](images/classDiagramSG5.png)

## Python Implementation

[View Python Source](classImplementation.py)

## Test Run

![Test Run](images/classTestRun.png)

## Object Diagram

![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?

I made magazineSize private because it represents the number of bullets currently available. If other parts of the program could change it directly, invalid values such as negative bullets could occur. Keeping it private helps protect the object's data.

### Which method changes the state of your object?

The fire() method changes the state of the object. It decreases the value of magazineSize whenever bullets are fired. This changes the condition of the gun during the program.

### How did your two objects demonstrate that instances are independent?

When I called fire() on gun1, only its bullet count changed. The bullet count of gun2 stayed the same. This shows that each object stores its own data independently.

### What is the difference between your class diagram and your object diagram?

The class diagram shows the blueprint of the Gun class, including its attributes and methods. The object diagram shows actual instances of the class and their current values. The class diagram defines the structure, while the object diagram shows real objects created from that structure.