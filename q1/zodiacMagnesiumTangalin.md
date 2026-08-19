# Chinese Zodiac Coding Exercise

## Requirements

### a. Input
Ask the user to enter a year of birth. The baseline year is 1900.

### b. Validation
Validate that the year entered is not earlier than 1900.

### c. Invalid Year
If the user enters a year earlier than 1900, display an appropriate message and stop the program.

Example:

Enter your birth year: 1800

Invalid Year, it should not be earlier than 1900

### d. Chinese Zodiac
If the year is valid, determine the Chinese Zodiac sign. The zodiac signs repeat every 12 years, starting with Rat in 1900.

1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Mǎ)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

### e. Year of Birth
Only the year of birth is considered.

---

## Python Code

```python
birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    zodiac_index = (birth_year - 1900) % 12
    zodiac = zodiac_signs[zodiac_index]

    print("Your Chinese Zodiac Sign is:", zodiac)

```
## Screenshots

### Valid Year Output

![Valid Year Output](Screenshot(6).png)

### Invalid Year Output

![Invalid Year Output](Screenshot(3).png)
