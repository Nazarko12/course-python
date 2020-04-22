class Farm:
    salary_in_dollars = 800

    def __init__(self, number_of_employees=None, location=None, number_of_animals=None,

                 capacity_fan_in_watts=None,

                 amount_of_sowing_machinery=None, species_of_animals=None, the_company_name=None):
        self.number_of_employees = number_of_employees

        self.location = location

        self.number_of_animals = number_of_animals

        self.capacity_fan_in_watts = capacity_fan_in_watts

        self.amount_of_sowing_machinery = amount_of_sowing_machinery

        self.species_of_animals = species_of_animals

        self.the_company_name = the_company_name

    @staticmethod
    def static_method():
        return Farm.salary_in_dollars

    def __str__(self):
        number_of_employees = "Number_of_employees: {0}\n".format(self.number_of_employees)

        location = "Location: {0}\n".format(self.location)

        number_of_animals = "Number_of_animals: {0}\n".format(self.number_of_animals)

        capacity_fan_in_watts = "Capacity_fan_in_watts: {0}\n".format(self.capacity_fan_in_watts)

        amount_of_sowing_machinery = "Amount_of_sowing_machinery: {0}\n".format(self.amount_of_sowing_machinery)

        species_of_animals = "Species_of_animals: {0}\n".format(self.species_of_animals)

        salary_in_dollars = "Salary_in_dollars: {0}\n".format(

            Farm.salary_in_dollars)

        return number_of_employees + location + number_of_animals + capacity_fan_in_watts + amount_of_sowing_machinery + \
               species_of_animals + salary_in_dollars

        def __del__(self):
            print("Deleted " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
            return
