from nowoczesnemetodyprogramowania.engines import Gasoline, Diesel


class TestEngine:
    def test_gasoline(self):
        engine_gasoline = Gasoline()

        assert (
            isinstance(engine_gasoline, Gasoline) and engine_gasoline.capacity,
            engine_gasoline.cylinders,
            engine_gasoline.compression,
            engine_gasoline.octane,
            engine_gasoline.power,
            engine_gasoline.valves == 0,
        )

        engine_gasoline.set_valves(4)
        engine_gasoline.set_capacity(10)
        engine_gasoline.set_compression(12)
        engine_gasoline.set_cylinders(4)
        engine_gasoline.set_octane(98)
        engine_gasoline.set_power(150)
        assert (
            engine_gasoline.capacity == 10
            and engine_gasoline.cylinders == 4
            and engine_gasoline.compression == 12
            and engine_gasoline.octane == 98
            and engine_gasoline.power == 150
            and engine_gasoline.valves == 4
        )

    def test_diesel(self):
        engine_diesel = Diesel()

        assert (
            isinstance(engine_diesel, Diesel) and engine_diesel.capacity,
            engine_diesel.cylinders,
            engine_diesel.compression,
            engine_diesel.power == 0,engine_diesel.turbo == False
        )
        engine_diesel.set_turbo(True)
        engine_diesel.set_capacity(10)
        engine_diesel.set_compression(12)
        engine_diesel.set_cylinders(4)
        engine_diesel.set_power(150)
        engine_diesel.set_emission(100)
        assert (
            engine_diesel.capacity == 10
            and engine_diesel.cylinders == 4
            and engine_diesel.compression == 12
            and engine_diesel.power == 150
            and engine_diesel.emission_co2 == 100
            and engine_diesel.turbo 
        )
