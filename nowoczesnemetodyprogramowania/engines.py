class Engine:
    def __init__(self, cylinders: int = 0, power: int = 0, capacity: float = 0., compression: float = 0.) -> None:
        self.cylinders = cylinders
        self.power = power
        self.capacity = capacity
        self.compression = compression

    def __del__(self) -> print:
        return print("the object has been removed!")

    def introduce(self) -> str:
        return ('number of cylinders: ' + str(self.cylinders) +
                '\n power: ' + str(self.power) +
                '\n capacity: ' + str(self.capacity) +
                '\n compression: ' + str(self.compression))

    def set_cylinders(self, cylinders: int) -> None:
        self.cylinders = cylinders

    def set_power(self, power: int) -> None:
        self.power = power

    def set_capacity(self, capacity: float) -> None:
        self.capacity = capacity

    def set_compression(self, compression: float) -> None:
        self.compression = compression


class Gasoline(Engine):
    def __init__(self, valves: int = 0, octane: int = 0):
        super().__init__()
        self.valves = valves
        self.octane = octane

    def __del__(self) -> print:
        return print("gasoline engine has been removed!")

    def introduce(self) -> str:
        return (super().introduce() + '\n number of valves: ' + str(self.valves) +
                '\n number of octanes: ' + str(self.octane))

    def set_valves(self, valves: int) -> None:
        self.valves = valves

    def set_octane(self, octane: int) -> None:
        self.octane = octane


class Diesel(Engine):
    def __init__(self, emission_co2: float = 0., turbo: bool = False) -> None:
        super().__init__()
        self.emission_co2 = emission_co2
        self.turbo = turbo

    def __del__(self) -> print:
        return print("diesel engine has been removed!")

    def introduce(self) -> str:
        return (super().introduce() + '\n emission CO2: ' + str(self.emission_co2) +
                '\n turbocharger: ' + str(self.turbo))

    def set_emission(self, emission: float) -> None:
        self.emission_co2 = emission

    def set_turbo(self, turbo: bool) -> None:
        self.turbo = turbo


# w1 = Diesel(10, True)
# w1.set_compression(10)
# w1.set_capacity(5)
# w1.set_power(150)
# w1.set_cylinders(4)
# w1.set_turbo(False)
# print(w1.introduce())
# 
# w2 = Gasoline(20, 100)
# w2.set_power(200)
# w2.set_cylinders(8)
# w2.set_compression(10)
# w2.set_capacity(6210)
# print(w2.introduce())

