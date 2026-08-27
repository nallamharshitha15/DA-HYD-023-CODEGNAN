'''
#Polymorphism-->it is also one of the key  feature of OOP,
#poly=many,morph=forms
Methods with same name can take diff parameters (args)
-->Method overloading(compiletime polymorphism)
-->Method overrifding(Run_time)
-->operator overloading(+,*)(__add__,__str__)

HotStar
-->Free User-->can watch movies with adds
-->premium User-->can watch premium content without adds
-->VIP User -->live content,streaming quality,without adds,premium content


##Method overloading :
class HotStar:
    """ usage of polymorphism"""
    def watch(self):
        print(f'user logged into Hotstar..opeing home page')
    def watch(self,movie):
        self.movie=movie
        print(f'user is watching {self.movie}')
app=HotStar()
app.watch("pushpa")
#app.watch() -->it returns error as watch() is overload             


#1)Method usage with default arguments
#2)Method usage with variable lenght arguments(*args)
#3)Method usage with type of arguments

#1)Method usage with default arguments
class HotStar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'user login to hotstar..checking..')
        else:
            self.movie=movie
            self.movie=movie
            print(f'user started watching {self.movie},{self.movie}')
app=HotStar()
app.watch()
app.watch("vikram","arya")                


#2)Method usage with variable lenght arguments(*args)
class HotStar:
    """Method usage with default arguments"""
    def watch(self,*movies):
        print(movies)
        for movie in movies:
            self.movie=movie
            print(f'user watching {self.movie} ')
app=HotStar()
app.watch("arya","arya2","kgf")                

#3)Method usage with type of arguments
#method overloading with type of arguments usage
#Hotstar -->one movie at a time
 #       -->multiple movies at a time

#MethodOverriding

class HotStar:
    """Method usage with type of arguments"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print("playing playlist")
            for movie in content:
                print(f'user watched {movie}')
app=HotStar()
app.watch("arya")
#app.watch()->returns error we did not metion default argument as None
app.watch(['arya','arya2','kgf'])


#Method overriding->It happens in the scenario of inheritance,
#where id child class method name same as parent class thats where overriding happen
#we can use super() or if we create diff objects

class Free_User:
    """uderstanding Method overriding"""
    def watch(self):
        print("user login into homepage...")
class PremiumUser(Free_User):
    """usage of inhertance"""
    def watch(self,movie):
        self.movie=movie
        print(f'user watching {self.movie}')
obj=PremiumUser()
obj.watch('kgf')
o2=Free_User()
o2.watch()    
'''    
#in above usecase we can create diff objs

#but in real  
#using super keyword


class Free_User:
    """uderstanding Method overriding"""
    def watch(self):
        print("user login into homepage...")
        #super().watch()
class PremiumUser(Free_User):
    """usage of inhertance"""
    def watch(self,movie):
        super().watch()
        self.movie=movie
        print(f'user watching {self.movie}')
        #super().watch() #calling superclass method 
obj=PremiumUser()
obj.watch('kgf')
#o2=Free_User()
#o2.watch()        










