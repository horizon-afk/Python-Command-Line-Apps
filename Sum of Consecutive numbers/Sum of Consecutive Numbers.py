-class SumNumbers:

    def __init__(self):
        self.function = True
        while self.function:
            SumNumbers.inputNumber(self)
            if self.x.isdigit():
                SumNumbers.myline(self)

            elif self.x == "exit":
                self.function = False
                print("Thank You for using! Glad we could help you!")
                input()

            else:
                print("Invalid Input!\n")
                SumNumbers.__init__(self)

    def inputNumber(self):
        self.x = input("Enter the last number you want to find the sum of or type exit to quit: ")

    def myline(self):

            self.a,self.b = 1,2
            self.times = 2

            while self.b <= int(self.x):
                self.a = self.a + self.b

                print(f"{self.times}. {self.a}")
                self.b += 1
                self.times += 1


if __name__ == "__main__":

    print("WELCOME TO UMESH'S COMMAND LINE APPS FOR YOUR DAILY USE.")
    print("This one will help you to find your sum for consecutive numbers starting from 1 and ends till where you want it!\n")
    SumNumbers()
