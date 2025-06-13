"""Bad representation of the liskov substitution principle 
   because the subclass/child changes the behavior
"""
class Bird:
    def fly(self):
        # print ("I am flying")
        return "we flew"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins have never flown before, you crazy")
    
bird = Bird()
kowalski = Penguin()

# print(bird.fly())
# print(kowalski.fly())

# first proper user of abstraction to effect liskov substitution

class NewBird:
    def fly(self):
        return "we are flying you numbskull"
    
class FirstNewPenguin(Bird):
    def fly(self):
        return "Penguins dont fly you guy"
    
# bird = NewBird()
# kowalski = FirstNewPenguin()

# print(kowalski.fly())

# second proper user of abstraction to effect liskov substitution

class FinalBird:
    def fly(self):
        pass
    
class FlyingBird(FinalBird):
    def fly(self):
        return "we up in the air"
    
class FlightlessBird(FinalBird):
    def fly(self):
        return "we never flew a day in our lives"
    
class Penguin(FlightlessBird):
    pass

rico = Penguin()
print (rico.fly())