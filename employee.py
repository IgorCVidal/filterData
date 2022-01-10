from loadEmployee import data
from operator import attrgetter



class employee:
    all = []
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])
        employee.all.append(self)



    def __repr__(self) -> str:
        return f"employee({self.nome}, {self.genero} , {self.pais}, {self.salario}) "

    def id_filter(x:int):
        for i in employee.all:
            if i.id == x:
                print(i)

    def country_filter(x:str, DATA=all):
        def countryf(self):
            if self.pais.lower() == x.lower():
                return True
            else:
                return False
        return filter(countryf,DATA)

    def gender_filter(x:str,DATA=all):
        def gens(self):    
            if self.genero.lower() == x.lower():
                return True
            else:
                return False
        return filter(gens,DATA)

    def lower_salary(x=all):
        valor = min(x,key=attrgetter('salario'))
        return valor

    def highest_salary(x=all):
        valor = max(x,key=attrgetter('salario'))
        return valor



def main():
    for x in data:
        employee(x)

    fc = employee.gender_filter('f',employee.country_filter('china'))
    print(employee.lower_salary(fc))
    

if __name__ == '__main__':
    main()