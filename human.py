__author__ = 'arana'
from datetime import datetime

validHairColors = ("blonde", "brunette", "red", "black", None)
validEyeColors = ("brown", "blue", "green", "hazel", None)


class Human(object):
    def __init__(self, startingHeight, startingWeight, startingName=None, startingEyeColor="Brown", startingHairColor="Blonde"):
        self.name = startingName
        self.dateOfBirth = datetime.date(datetime.now())
        self.age = datetime.date(datetime.now()).year - self.dateOfBirth.year
        self.height = startingHeight
        self.weight = startingWeight
        self.eyeColor = self.setEyeColor(startingEyeColor)
        self.hairColor = self.setHairColor(startingHairColor)
        self.phrases = []

    def __str__(self):
        return "Name: {0} Height:  {1} Weight: {2} Age: {3} Number of past phrases: {4}".format(self.name, self.height, self.weight, self.age, len(self.phrases))

    def speak(self, phraseToSpeak):
        self.phrases.append(phraseToSpeak)
        print(phraseToSpeak)

    def pastPhrases(self, numberOfSteps=1):
        if numberOfSteps > 0:
            return self.phrases[-numberOfSteps:]
        else:
            raise ValueError

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setDateOfBirth(self, newDate):
        self.dateOfBirth = datetime.date(newDate)
        self.age = datetime.date(datetime.now()) - self.dateOfBirth

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getAge(self):
        return self.age

    def setHeight(self, newHeight):
        self.height = float(newHeight)

    def getHeight(self):
        return self.height

    def setWeight(self, newWeight):
        self.weight = float(newWeight)

    def getWeight(self):
        return self.weight

    def setEyeColor(self, newEyeColor):
        if newEyeColor is not None and newEyeColor.lower() in validEyeColors:
            self.eyeColor = newEyeColor.lower()
        else:
            raise ValueError

    def getEyeColor(self):
        return self.eyeColor

    def setHairColor(self, newHairColor):
        if newHairColor is not None and newHairColor.lower() in validHairColors:
            self.hairColor = newHairColor.lower()
        else:
            raise ValueError

    def getHairColor(self):
        return self.hairColor


class Person(Human):
    def __init__(self, startingHeight, startingWeight, startingName=None, startingEyeColor="Brown", startingHairColor="Blonde"):
        super().__init__(startingHeight, startingWeight, startingName, startingEyeColor, startingHairColor)
        self.gender = "female"
        self.pregnant = False

    def setGender(self, newGender):
        self.gender = newGender

    def getGender(self):
        return self.gender

    def setPregnant(self, newBaby):
        if newBaby in (True, False):
            self.pregnant = newBaby
        else:
            raise ValueError

    def isPregnant(self):
        return self.pregnant


class Student(Person):
    def __init__(self, startingHeight, startingWeight, startingName=None, startingEyeColor="Brown", startingHairColor="Blonde"):
        super().__init__(startingHeight, startingWeight, startingName, startingEyeColor, startingHairColor)
        self.schoolAttended = []
        self.subjectStudies = None
        self.graduated = False

    def setSchoolAttended(self, newSchool):
        self.schoolAttended.append(newSchool)

    def getSchoolAttended(self):
        return self.schoolAttended

    def setSubjectStudied(self, newSubject):
        self.subjectStudies = newSubject

    def getSubjectStudied(self):
        return self.subjectStudies

    def setGraduated(self):
        self.graduated = True

    def didGraduate(self):
        return self.graduated
