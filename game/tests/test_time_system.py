import time
from systems.time_system import TimeSystem


def test_tick_measures_elapsed_time():
    time_system = TimeSystem()
    time_system.reset()

    dt1 = time_system.tick()
    time.sleep(1)
    dt2 = time_system.tick()

    print("TimeSystem test :")
    print("dt1:", dt1)
    print("dt2:", dt2)

    assert dt1 < 0.01            
    assert 0.9 <= dt2 <= 1.1 
    

if __name__ == "__main__":
    test_tick_measures_elapsed_time()