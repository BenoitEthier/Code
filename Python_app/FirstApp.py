class Employee:
    def __init__(self, social_number, first_name, last_name, email, salary):
        self.social_number = social_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        self.hired = False

    def hire(self):
        self.hired = True
        print(f"{self.first_name} {self.last_name} has been hired.")

    def salary_raise(self, percentage):
        if self.hired:
            self.salary += self.salary * (percentage / 100)
            print(f"{self.first_name} {self.last_name}'s salary has been raised to {self.salary}.")
        else:
            print("The employee must be hired first.")
            
           