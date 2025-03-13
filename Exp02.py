  {
   "cell_type": "markdown",
   "id": "996bfca3-da7f-4831-8b14-1174fdef77f3",
   "metadata": {},
   "source": [
    "### Abhishek Singh (Roll No 57)"
   ]
  }

'''
General case represents that developer working on 
frontend cannot work backend development unless he/she is fullstack dev.

Write a method named verifier () that checks this condition.

The method should check that if frontend is True and backend is True,
the method returns Fullstack as string. If one of them is True, it should return
the respective desgination, and if none of them are true, it returns,
not a developer respetively.
'''

class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self):
        if(self.frontend==True and self.backend==True):
            return 'Fullstack'
        elif(self.frontend==True):
            return '{}'.format(self.designation,self.frontend, self.backend)
        elif(self.backend==True):
            return '{}'.format(self.designation,self.frontend, self.backend)
        else:
            return 'Not a developer'
    def printData(self):
        print(self.designation,self.frontend,self.backend)
        return ''

if __name__ == '__main__':
    firstEmployee = Employee ()
    secondEmployee = Employee (designation="Manager",frontend=True,backend=False)

    firstEmployee.printData()
    secondEmployee.printData()

    # Call the method here to display output.
