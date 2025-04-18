from django.test import TestCase
import pickle

# Create your tests here.
        
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

        
class ObjectAPITest(TestCase):
    def setUp(self):
        pass
    
    def test_path(self):
        
        dict = {
            "add": add,
            "sub": sub,
        }
        
        url = "add"
        print(dict[url](1, 2))
        
        url = "sub"
        print(dict[url](1, 2))
            