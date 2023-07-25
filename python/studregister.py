
class studentregister:
    def __init__(self):
        self.lists = {}
    def register(self,name):
        new_list = []
        self.lists[name] = new_list
        print(f"List '{name}' has been created.")

    def insertnames(registername,n):
        for i in range(n):
            registername.append(str(input().split())) 


def main():
    obj = studentregister()
    while True:
        print("select 1 to create a new register")
        print("select 2 to enter names into the register")
        print("select 3 to add attendance to that register students")
        print("select 4 to insert marks for the students")
        print("select 5 to update any record")
        print("select 6 to delete any record")
        print("select 7 to come out of that register")
        print("select 8 to view available registers")
        print("sleect 9 to quit from the interface")
         
        choice = int(input("enter the number: "))

        if choice == 1:
            name = str(input("please enter the register name: "))
            obj.register(name)

        if choice == 2:
            n = int(input("enter the number of students: "))
            obj.insertnames(name,n)

        if choice == 3:
            pass

main()
