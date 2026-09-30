# SG4 - Understanding Classes and Objects

## Class Name
Gun

## Class Description
The Gun class represents a weapon in a game like Call of Duty: Mobile. It stores basic information about a gun and the actions that a player can do with it.

## Properties

| Property | Data Type | Description |
|---|---|---|
| gunName | string | The name of the gun, such as VMP or USS 9 |
| damage | int | The amount of damage the gun can deal |
| magazineSize | int | The number of bullets the gun can hold |
| automatic | boolean | Shows whether the gun can fire automatically |

## Methods

| Method | Description |
|---|---|
| reload() | Reloads the gun when it runs out of bullets |
| aim() | Allows the player to aim the gun |
| changeDamage(amount: int) | Changes the damage value of the gun |

## Class Diagram

```text
+-------------------------------------------+
|                    Gun                    |
+-------------------------------------------+
| gunName : string                          |
| damage : int                              |
| magazineSize : int                        |
| automatic : boolean                       |
+-------------------------------------------+
| reload()                                  |
| aim()                                     |
| changeDamage(amount : int)                |
+-------------------------------------------+

## Design Revision
No major changes were needed from my original design.
