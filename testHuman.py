#!/usr/bin/env python
__author__ = "Arana Fireheart"

from datetime import datetime

from human import Human, Person, Student

human1 = Human(64, 125, "Mindy")
human1.setHeight(123)
human1.setWeight(133)
human1.speak("Hello")
human1.speak("Good Bye")
human1.speak("What?")
human1.speak("Nothing!")
human1.speak("Why?")
print(human1)
print("---------")
print(human1.pastPhrases())
print("---------")
print(human1.pastPhrases(4))
print("---------")
try:
    print(human1.pastPhrases(-10))
except ValueError:
    print("Usage error: numberOfSteps must be positive.")

person1 = Person(71, 185, "George")
person1.setHeight(345)
person1.setWeight(220)
print(person1)
person1.setName("Mickey")
print(person1.getName())
print(person1)
print(f"Gender: {person1.getGender()}")
person1.setDateOfBirth(datetime.fromisoformat('2001-11-04'))
print(f"DOB: {person1.getDateOfBirth()}")
print(f"Age: {person1.getAge()}")
person2 = Person(69, 143, "Martha")
person2.setHeight(70)
print(f"Height: {person2.getHeight()}")
person2.setWeight(176)
print(f"Weight: {person2.getWeight()}")
print(person2.getGender())
try:
    person2.setEyeColor("brown")
    person2.setEyeColor("blue")
    person2.setEyeColor(None)
    person2.setEyeColor("green")
    person2.setEyeColor("hazel")
    person2.setEyeColor("red")
except ValueError:
    print("Can't set red eyes")
    print(person2.getEyeColor())
try:
    person2.setHairColor("blonde")
    person2.setHairColor("brunette")
    person2.setHairColor(None)
    person2.setHairColor("black")
    person2.setHairColor("red")
    person2.setHairColor("blue")
except ValueError:
    print("Can't set blue hair")
    print(person2.getHairColor())
print(person2)
person2.setGender("male")
print(person2)
person2.setPregnant(True)
try:
    person2.setPregnant("Fred")
except ValueError:
    print("Not a boolean value")
print(person2.isPregnant())

student1 = Student(65, 119, "Mindy")
student1.setSchoolAttended("SNHU")
print(student1.getSchoolAttended())
student1.setSubjectStudied("CompSci")
print(student1.getSubjectStudied())
print(f"Graduated: {student1.didGraduate()}")
student1.setGraduated()
print(f"Graduated: {student1.didGraduate()}")
print(student1)
