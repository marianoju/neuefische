[neuefische] randomized allocation of objects of two classes 

# randomized allocation of objects of two classes 

## Goals/Limitations 
- Randomized allocation of objects of two classes without repetition over several iterations. 
- All objects of the class 'Person' will be allocated an object of the class 'Seat' on a randomised basis. 
- These allocations will be repeated over n iterations. 
- No object of the class 'Person' will be allocated the same object of the class 'Seat' 
    - in two consecutive iterations, 
    - more than (+1) times compared to any other object of the same class. 
---

### Klassen: 
- Person 
- Seat 

### Objekte der Klasse "Person" (n=12): 
- Andreas
- Britta
- Dima
- Fabrice
- Johanna
- Katharina
- Katie
- Mariano
- Nathalie
- Sarah
- Sophie
- Thomas

<- allocation --

### Objekte der Klasse "Seat" (n=12): 
- 1:12 

### Iterationen = Wochen (n=17) 
- 32:48


## Entwurf 

### Rotation 

32	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 01 02 03 04 05 06 07 08 09 10 11 12 

33	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 12 01 02 03 04 05 06 07 08 09 10 11

34	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 11 12 01 02 03 04 05 06 07 08 09 10

...

Nachteil: bei 17 Iterationen werden die Personen nicht gleichmäßig allen Sitzen zugeordnet. 

### Lotterie ohne Wiederholung 

import secrets
foo = ['a', 'b', 'c', 'd', 'e']
print(secrets.choice(foo))

To print a random index:

print(secrets.randbelow(len(foo)))


# class Student: 
    def __init__(self, self.name, 

17 / 12 =< 2 
n  / s(P) 

### Siehe 

- How to randomly select an item from a list? <https://stackoverflow.com/questions/306400/>
- Assigning Values to an Array <https://rosettacode.org/wiki/Assigning_Values_to_an_Array#Python>
- How to assign a class object to a item in a list? (python) <https://stackoverflow.com/questions/19307169/>
- Assigning Tasks to People <https://stackoverflow.com/questions/23590389/>
- random.shuffle(x[, random]) <https://docs.python.org/2/library/random.html#random.shuffle>
- Python: take the content of a list and append it to another list <https://stackoverflow.com/questions/8177079/>
- Concatenating two one-dimensional NumPy arrays <https://stackoverflow.com/questions/9236926/>

*nicht hilfreich* 
- How to concatenate two lists in Python? <https://stackoverflow.com/questions/1720421/>
- Python: take the content of a list and append it to another list <https://stackoverflow.com/questions/8177079/>
- Python - Create an array from columns in file <https://stackoverflow.com/questions/23769007/>



### Klassen: 
- Person 
- Seat 

### Objekte der Klasse "Person" (n=12): 
- Andreas
- Britta
- Dima
- Fabrice
- Johanna
- Katharina
- Katie
- Mariano
- Nathalie
- Sarah
- Sophie
- Thomas

<- allocation --

### Objekte der Klasse "Seat" (n=12): 
- 1:12 

### Iterationen = Wochen (n=17) 
- 32:48


## Entwurf 

### Rotation 

32	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 01 02 03 04 05 06 07 08 09 10 11 12 

33	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 12 01 02 03 04 05 06 07 08 09 10 11

34	(S) 01 02 03 04 05 06 07 08 09 10 11 12 
	(P) 11 12 01 02 03 04 05 06 07 08 09 10

...

Nachteil: bei 17 Iterationen werden die Personen nicht gleichmäßig allen Sitzen zugeordnet. 

### Lotterie ohne Wiederholung 

import secrets
foo = ['a', 'b', 'c', 'd', 'e']
print(secrets.choice(foo))

To print a random index:

print(secrets.randbelow(len(foo)))


# class Student: 
    def __init__(self, self.name, 

17 / 12 =< 2 
n  / s(P) 

### Siehe 

- How to randomly select an item from a list? <https://stackoverflow.com/questions/306400/>
- Assigning Values to an Array <https://rosettacode.org/wiki/Assigning_Values_to_an_Array#Python>
- How to assign a class object to a item in a list? (python) <https://stackoverflow.com/questions/19307169/>
- Assigning Tasks to People <https://stackoverflow.com/questions/23590389/>
- random.shuffle(x[, random]) <https://docs.python.org/2/library/random.html#random.shuffle>
- Python: take the content of a list and append it to another list <https://stackoverflow.com/questions/8177079/>
- Concatenating two one-dimensional NumPy arrays <https://stackoverflow.com/questions/9236926/>
- How to draw N elements of random indices from numpy array without repetition? <https://stackoverflow.com/questions/29563788/>

*nicht hilfreich* 
- How to concatenate two lists in Python? <https://stackoverflow.com/questions/1720421/>
- Python: take the content of a list and append it to another list <https://stackoverflow.com/questions/8177079/>
- Python - Create an array from columns in file <https://stackoverflow.com/questions/23769007/>

