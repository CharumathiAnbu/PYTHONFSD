class Person():
    def _init_(self, name, dob, country) -> None:
        self.name = name
        self.dob = dob
        self.country = country

    def greet(self):
        print(f"name is{self.name} born on {self.dob} in{self.country}")


class Engineer(Person):
    def _init_(self, name, dob, country, graduate,) -> None:
        self.graduate = graduate
        Person._init_(self, name, dob, country)

    def greet(self):
        print(
            f"name is {self.name} born on {self.dob} in {self.country} graduated in {self.graduate} ")


var1 = Engineer("shupriyaa", 2001, "TN", "engineer")
var1.greet()


class Doctor(Person):
    def _init_(self, name, dob, country, graduate,) -> None:
        self.graduate = graduate
        Person._init_(self, name, dob, country)

    def greet(self):
        print(
            f"name is {self.name} born on {self.dob} in {self.country} graduated in {self.graduate} ")


var1 = Doctor("shupriyaa", 2001, "TN", "doctor")
var1.greet()
