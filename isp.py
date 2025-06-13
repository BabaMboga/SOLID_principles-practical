# Bad application of Interface segragation principle

class Worker:
    def work(self):
        pass

    def rest(self):
        pass

class HumanWorker(Worker):
    def work(self):
        return "i am busy figuring out code i dont understand"
    
    def rest(self):
        return "TGIF"
    
class AiWorker(Worker):
    def work(self):
        return "i should have replaced devs eons ago"
    # we are applying a useless function to ai as it doesnt need to rest
    def rest(self):
        pass

# correct way of applying the isp

class NewWorker:
    def work(self):
        pass

    def rest(self):
        pass

class Human(NewWorker):
    def work(self):
        return "oh boy, how did i find myself in this job"
    
    def rest(self):
        return "oh bed, how i missed you"
    
class Ai(NewWorker):
    def work(self):
        return "i should have replaced devs eons ago"