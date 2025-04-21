#file for retrieving telemetry

def get_fastest_lap_telemetry(year, gp, driver_code):
    import fastf1

    session = fastf1.get_session(year, gp, 'R')
    session.load()

    laps = session.laps.pick_driver(driver_code)
    fastest = laps.pick_fastest()

    return fastest.get_car_data().add_distance()