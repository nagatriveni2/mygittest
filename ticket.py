#OOPR-Assgn-19
#Start writing your code here
class ticket:
    passenger_name=""
    ticket_id=""
    source=""
    c=0
    destination=""
    def __init__(self,passenger_name,source,destination):
        self.passenger_name=passenger_name.upper()
        self.source=source.upper()
        self.destination=destination.upper()
	self.c=0
        
        
    def validate_source_destination(self):
        if(self.source=="delhi".upper() and(self.destination=="mumbai".upper() or self.destination=="chennai".upper() or self.destination=="kolkata".upper() or self.destination=="pune")):
            return True
            
        else:
            return False
            
    def generate_ticket(self,passenger_name,source,destination,c):
        self.passenger_name=passenger_name.upper()
        self.source=source.upper()
        
        self.destination=destination.upper()
        tid=""
        cond=self.validate_source_destination()
        
        if(cond):
            self.c=self.c+1
            
            tid=self.source[0]+self.destination[0]+"0"+str(c)
            self.ticket_id=tid.upper()
            print(self.get_passenger_name())
            print(self.get_source())
            print(self.get_destination())
            print(self.get_ticket_id())
            return c
        else:
            self.ticket_id=None
            return c
        
    
    def get_ticket_id(self):
        return self.ticket_id
    def get_passenger_name(self):
        return self.passenger_name
    def get_source(self):
        return self.source
    def get_destination(self):
        return self.destination
c=0
t1=ticket("triveni","delhi","mumbai")
c=(t1.generate_ticket("mary","delhi","mumbai",c))
c=(t1.generate_ticket("john","delhi","chennai",c))
c=(t1.generate_ticket("mark","delhi","pune",c))


