somename = 'Biff'

def greet(name):
    global somename
    print 'Hello', name, 'have you met', somename
    somename = 'Doc'
    
def grab():
    print 'The variable value is', somename
    
grab()
greet('Marty')
grab()
