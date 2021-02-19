# imports
import time
import itertools
import threading
import sys
from track import *
from main import sensor_data
from main import point_change
from main import record_data
v <- 0.2  # This number should be 17.8 for correct timings but is lower for testing purposes
                                      ENDFOR
route_1 <- section_a + section_c + section_d
route_two <- section_a + section_b + section_d
route_2 <- route_two[::-1]
FUNCTION outward_run():
    scotsman_current_position <- route_1[0]
    mallard_current_position <- route_2[0]
    l1: bool <- True
    x <- 0
    while l1:
        sensor_data[1] <- False
        sensor_data[2] <- False
        sensor_data[3] <- False
        sensor_data[4] <- False
        arrived <- False
        OUTPUT f'Scotsman is at position - {scotsman_current_position}'
        OUTPUT f'Mallard is at position - {mallard_current_position}'
        FUNCTION traveling():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                IF arrived:
                    break
                ENDIF
                sys.stdout.write('\rtraveling ' + c)
                sys.stdout.flush()
                time.sleep(0.3)
            ENDFOR
            sys.stdout.write('\r \n')
        ENDFUNCTION

        t <- threading.Thread(target=traveling)
        t.start()
        time.sleep(v)
        arrived <- True
        time.sleep(0.2)
        x += 1
        IF x = 30:
            break
        ENDIF
        scotsman_current_position <- route_1[x]
        mallard_current_position <- route_2[x]
        IF scotsman_current_position = '3':
            sensor_data[0] <- not sensor_data[0]
        ELSEIF scotsman_current_position = '7b':
            sensor_data[1] <- True
        ELSEIF scotsman_current_position = '7c':
            sensor_data[2] <- True
        ELSEIF scotsman_current_position = '22b':
            sensor_data[3] <- True
        ELSEIF scotsman_current_position = '22c':
            sensor_data[4] <- True
        ELSEIF scotsman_current_position = '28':
            sensor_data[5] <- not sensor_data[5]
        ENDIF
        IF mallard_current_position = '3':
            sensor_data[0] <- not sensor_data[0]
        ELSEIF mallard_current_position = '7b':
            sensor_data[1] <- True
        ELSEIF mallard_current_position = '7c':
            sensor_data[2] <- True
        ELSEIF mallard_current_position = '22b':
            sensor_data[3] <- True
        ELSEIF mallard_current_position = '22c':
            sensor_data[4] <- True
        ELSEIF mallard_current_position = '28':
            sensor_data[5] <- not sensor_data[5]
        ENDIF
        OUTPUT sensor_data
        point_change()
        record_data()
ENDFUNCTION

    ENDWHILE
FUNCTION return_run():
    mallard_current_position <- route_1[0]
    scotsman_current_position <- route_2[0]
    l2 <- True
    x <- 0
    while l2:
        sensor_data[1] <- False
        sensor_data[2] <- False
        sensor_data[3] <- False
        sensor_data[4] <- False
        arrived <- False
        OUTPUT f'Scotsman is at position - {scotsman_current_position}'
        OUTPUT f'Mallard is at position - {mallard_current_position}'
        FUNCTION traveling():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                IF arrived:
                    break
                ENDIF
                sys.stdout.write('\rtraveling ' + c)
                sys.stdout.flush()
                time.sleep(0.3)
            ENDFOR
            sys.stdout.write('\r \n')
        ENDFUNCTION

        t <- threading.Thread(target=traveling)
        t.start()
        time.sleep(v)
        arrived <- True
        time.sleep(0.2)
        x += 1
        IF x = 30:
            break
        ENDIF
        scotsman_current_position <- route_2[x]
        mallard_current_position <- route_1[x]
        IF scotsman_current_position = '3':
            sensor_data[0] <- not sensor_data[0]
        ELSEIF scotsman_current_position = '7b':
            sensor_data[1] <- True
        ELSEIF scotsman_current_position = '7c':
            sensor_data[2] <- True
        ELSEIF scotsman_current_position = '22b':
            sensor_data[3] <- True
        ELSEIF scotsman_current_position = '22c':
            sensor_data[4] <- True
        ELSEIF scotsman_current_position = '28':
            sensor_data[5] <- not sensor_data[5]
        ENDIF
        IF mallard_current_position = '3':
            sensor_data[0] <- not sensor_data[0]
        ELSEIF mallard_current_position = '7b':
            sensor_data[1] <- True
        ELSEIF mallard_current_position = '7c':
            sensor_data[2] <- True
        ELSEIF mallard_current_position = '22b':
            sensor_data[3] <- True
        ELSEIF mallard_current_position = '22c':
            sensor_data[4] <- True
        ELSEIF mallard_current_position = '28':
            sensor_data[5] <- not sensor_data[5]
        ENDIF
        OUTPUT sensor_data
        point_change()
        record_data()
ENDFUNCTION

    ENDWHILE
FUNCTION constant_run():
    from main import emergency_stop
    from main import record_data
    from main import point_change
    scotsman_current_position <- route_1[0]
    mallard_current_position <- route_2[0]
    l3: bool <- True
    while l3 is True:
        x <- 0
        y <- 0
        l4: bool <- True
        l5: bool <- True
        while l4 is True AND emergency_stop is False:
            sensor_data[1] <- False
            sensor_data[2] <- False
            sensor_data[3] <- False
            sensor_data[4] <- False
            arrived <- False
            OUTPUT f'Scotsman is at position - {scotsman_current_position}'
            OUTPUT f'Mallard is at position - {mallard_current_position}'
            FUNCTION traveling():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    IF arrived:
                        break
                    ENDIF
                    sys.stdout.write('\rtraveling ' + c)
                    sys.stdout.flush()
                    time.sleep(0.3)
                ENDFOR
                sys.stdout.write('\r \n')
            ENDFUNCTION

            t <- threading.Thread(target=traveling)
            t.start()
            time.sleep(v)
            arrived: bool <- True
            time.sleep(0.2)
            x += 1
            IF x = 30:
                break
            ENDIF
            scotsman_current_position <- route_1[x]
            mallard_current_position <- route_2[x]
            IF scotsman_current_position = '3':
                sensor_data[0] <- not sensor_data[0]
            ELSEIF scotsman_current_position = '7b':
                sensor_data[1] <- True
            ELSEIF scotsman_current_position = '7c':
                sensor_data[2] <- True
            ELSEIF scotsman_current_position = '22b':
                sensor_data[3] <- True
            ELSEIF scotsman_current_position = '22c':
                sensor_data[4] <- True
            ELSEIF scotsman_current_position = '28':
                sensor_data[5] <- not sensor_data[5]
            ENDIF
            IF mallard_current_position = '3':
                sensor_data[0] <- not sensor_data[0]
            ELSEIF mallard_current_position = '7b':
                sensor_data[1] <- True
            ELSEIF mallard_current_position = '7c':
                sensor_data[2] <- True
            ELSEIF mallard_current_position = '22b':
                sensor_data[3] <- True
            ELSEIF mallard_current_position = '22c':
                sensor_data[4] <- True
            ELSEIF mallard_current_position = '28':
                sensor_data[5] <- not sensor_data[5]
            ENDIF
            OUTPUT sensor_data
            point_change()
            record_data()
        ENDWHILE
        while l5 is True AND emergency_stop is False:
            sensor_data[1] <- False
            sensor_data[2] <- False
            sensor_data[3] <- False
            sensor_data[4] <- False
            arrived <- False
            OUTPUT f'Scotsman is at position - {scotsman_current_position}'
            OUTPUT f'Mallard is at position - {mallard_current_position}'
            FUNCTION traveling():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    IF arrived:
                        break
                    ENDIF
                    sys.stdout.write('\rtraveling ' + c)
                    sys.stdout.flush()
                    time.sleep(0.3)
                ENDFOR
                sys.stdout.write('\r \n')
            ENDFUNCTION

            t <- threading.Thread(target=traveling)
            t.start()
            time.sleep(v)
            arrived <- True
            time.sleep(0.2)
            y += 1
            IF y = 30:
                break
            ENDIF
            scotsman_current_position <- route_2[y]
            mallard_current_position <- route_1[y]
            IF scotsman_current_position = '3':
                sensor_data[0] <- not sensor_data[0]
            ELSEIF scotsman_current_position = '7b':
                sensor_data[1] <- True
            ELSEIF scotsman_current_position = '7c':
                sensor_data[2] <- True
            ELSEIF scotsman_current_position = '22b':
                sensor_data[3] <- True
            ELSEIF scotsman_current_position = '22c':
                sensor_data[4] <- True
            ELSEIF scotsman_current_position = '28':
                sensor_data[5] <- not sensor_data[5]
            ENDIF
            IF mallard_current_position = '3':
                sensor_data[0] <- not sensor_data[0]
            ELSEIF mallard_current_position = '7b':
                sensor_data[1] <- True
            ELSEIF mallard_current_position = '7c':
                sensor_data[2] <- True
            ELSEIF mallard_current_position = '22b':
                sensor_data[3] <- True
            ELSEIF mallard_current_position = '22c':
                sensor_data[4] <- True
            ELSEIF mallard_current_position = '28':
                sensor_data[5] <- not sensor_data[5]
            ENDIF
            OUTPUT sensor_data
            point_change()
            record_data()
