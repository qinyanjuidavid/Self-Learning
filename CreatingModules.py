#Check the script myFunctions in the folder named myDirectory
from myDirectory import myFunctions
# import myDirectory.myFunctions #Another way of importing scripts
#import myDirectory.myFunctions as func #Another alternative
#from myDirectory import myFunctions as func #Alternative
import myModule
print("Add:",myModule.add(2,3))
print("Multiplication:",myModule.Multipy(2,3))

#Files from a different folder
print(myFunctions.Divide(6,2))
print(myFunctions.Substraction(6,2))