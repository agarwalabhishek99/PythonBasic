class id:
    def __init__(self,name,email,contact):

        self.name = name;
        self.email = email;
        self.contact = contact;

        def method(demo):
            print("your name is"+demo.email)

        i = id("Abhi", "Abhi@gmail.com", 8329568797)
        del i.email
        i.method()