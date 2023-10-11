# Format Strings
If we want to evaluate inside of a string, we use *f-strings*.  
To create an f-string, we put an `f` before the open quote

```python
fave_food = input("What's your favourite food? ")

print(f"Ooooooo, {fave_food} sounds good!")
```

We can use string methods to help solve [[Errors#Semantic Errors|semantic errors]]

## `.lower( )`

The `.lower( )` method takes a string and converts all uppercase characters to lowercase

## `.upper( )`

The `.upper( )` method uppercases all the letters.

## `.strip( chars)`

The '.strip( )' method **removes** characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today? ")

#"good!" "good." "Good!" "good!!!!!!!!!!!"
if user_feeling.lower().strip("!.,") == "good":
    print("That's great!")
```


## `.split(str)`
The `.split()` method splits a string into a *list*, separating the string based on the characters you give it.

```python
grovery_str = "eggs milk cheese hotwheels"

grocery_list = grovery_str.split(" ")
```

