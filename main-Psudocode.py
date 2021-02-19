test: bool <- False
emergency_stop: bool <- False
sim: bool <- True
blackbox: bool <- True
sensor_data: list[bool] <- [True, False, False, False, False, True]
r1: bool <- False
r2: bool <- False
signal_data: list[bool] <- [False, False, False, False, False, False]
Point_A: int <- 0
Point_B: int <- 0
wait_time: float <- 0.5
date: str <- ''
date_file: str <- ''
Sig_a: str <- ''
Sig_b: str <- ''
Sig_c: str <- ''
Sig_d: str <- ''
Sig_e: str <- ''
Sig_f: str <- ''
power_t1: int <- 0
power_t2: int <- 0
done: bool <- False
                           ENDFOR
FUNCTION sensor_check_1():
    global r1
    r1 <- False
    s2 <- sensor_data[1]
    s4 <- sensor_data[3]
    IF s2 is False AND s4 is False:
        OUTPUT 'Route one clear.'
        r1 <- True
        RETURN r1
    ENDIF
    IF s2 is True OR s4 is True:
        OUTPUT 'Route one not clear.'
        r1 <- False
        RETURN r1
    ENDIF
ENDFUNCTION

                           ENDFOR
FUNCTION sensor_check_2():
    global r2
    r2 <- False
    s3 <- sensor_data[2]
    s5 <- sensor_data[4]
    IF s3 is False AND s5 is False:
        OUTPUT 'Route two clear.'
        r2 <- True
        RETURN r2
    ENDIF
    IF s3 is True OR s5 is True:
        OUTPUT 'Route two not clear.'
        r2 <- False
        RETURN r2
    ENDIF
ENDFUNCTION

FUNCTION point_change():
    global Point_A
    global Point_B
    global emergency_stop
    s1 <- sensor_data[0]
    s2 <- sensor_data[1]
    s3 <- sensor_data[2]
    s4 <- sensor_data[3]
    s5 <- sensor_data[4]
    s6 <- sensor_data[5]
    IF s1 is True:
        Point_A <- 30
    ENDIF
    IF s2 is True:
        Point_B <- 30
    ENDIF
    IF s3 is True:
        Point_A <- 0
    ENDIF
    IF s4 is True:
        Point_B <- 30
    ENDIF
    IF s5 is True:
        Point_A <- 0
    ENDIF
    IF s6 is True:
        Point_B <- 0
    ENDIF
    IF s2 is True AND s4 is True:
        emergency_stop <- True
    ENDIF
    IF s3 is True AND s5 is True:
        emergency_stop <- True
    ENDIF
    IF s1 is True AND s2 is True:
        emergency_stop <- True
    ENDIF
    IF s1 is True AND s3 is True:
        emergency_stop <- True
    ENDIF
    IF s6 is True AND s4 is True:
        emergency_stop <- True
    ENDIF
    IF s6 is True AND s5 is True:
        emergency_stop <- True
    ENDIF
    OUTPUT Point_A
    OUTPUT Point_B
ENDFUNCTION

FUNCTION record_data():
    f <- open('blackbox.txt', 'a')
    f.write('\n\n')
    f.write('*--------------------------------------------*\n')
    f.write('SENSOR DATA:\n')
    find_date()
    f.write(f'Sensor 1 = {sensor_data[0]} at {date}\n')
    find_date()
    f.write(f'Sensor 2 = {sensor_data[1]} at {date}\n')
    find_date()
    f.write(f'Sensor 3 = {sensor_data[2]} at {date}\n')
    find_date()
    f.write(f'Sensor 4 = {sensor_data[3]} at {date}\n')
    find_date()
    f.write(f'Sensor 5 = {sensor_data[4]} at {date}\n')
    find_date()
    f.write(f'Sensor 6 = {sensor_data[5]} at {date}\n')
    f.write('\n')
    f.write('SIGNAL DATA:\n')
    find_date()
    f.write(f'Signal 1 = {signal_data[0]} at {date}\n')
    find_date()
    f.write(f'Signal 2 = {signal_data[1]} at {date}\n')
    find_date()
    f.write(f'Signal 3 = {signal_data[2]} at {date}\n')
    find_date()
    f.write(f'Signal 4 = {signal_data[3]} at {date}\n')
    find_date()
    f.write(f'Signal 5 = {signal_data[4]} at {date}\n')
    find_date()
    f.write(f'Signal 6 = {signal_data[5]} at {date}\n')
    f.write('\n')
    f.write('POINT DATA:\n')
    find_date()
    f.write(f'Point 1 = {Point_A}° at {date}\n')
    find_date()
    f.write(f'Point 2 = {Point_B}° at {date}\n')
    f.close()
ENDFUNCTION

FUNCTION find_date():
    global date
    x <- datetime.datetime.today()
    date <- x.strftime('%a %b %d %Y %H:%M:%S')

ENDFUNCTION

FUNCTION find_date_file_name():
    global date_file
    x <- datetime.datetime.today()
    date_file <- x.strftime('%b%d%Y-%H:%M:%S')
ENDFUNCTION

FUNCTION signal_check():
    global Sig_a
    global Sig_b
    global Sig_c
    global Sig_d
    global Sig_e
    global Sig_f
    a <- signal_data[0]
    b <- signal_data[1]
    c <- signal_data[2]
    d <- signal_data[3]
    e <- signal_data[4]
    f1 <- signal_data[5]
    IF a is False:
        Sig_a <- 'RED'
    ELSEIF a is True:
        Sig_a <- 'GREEN'
    ENDIF
    IF b is False:
        Sig_b <- 'RED'
    ELSEIF b is True:
        Sig_b <- 'GREEN'
    ENDIF
    IF c is False:
        Sig_c <- 'RED'
    ELSEIF c is True:
        Sig_c <- 'GREEN'
    ENDIF
    IF d is False:
        Sig_d <- 'RED'
    ELSEIF d is True:
        Sig_d <- 'GREEN'
    ENDIF
    IF e is False:
        Sig_e <- 'RED'
    ELSEIF e is True:
        Sig_e <- 'GREEN'
    ENDIF
    IF f1 is False:
        Sig_f <- 'RED'
    ELSEIF f1 is True:
        Sig_f <- 'GREEN'
    ENDIF
    IF Point_A = 0:
        Sig_c <- 'RED'
    ELSEIF Point_A = 30:
        Sig_b <- 'RED'
    ENDIF
    IF Point_B = 0:
        Sig_d <- 'RED'
    ELSEIF Point_B = 30:
        Sig_e <- 'RED'
    ENDIF
ENDFUNCTION

FUNCTION main():
    emergency_stop <- False
    while sim AND emergency_stop is not True:
        OUTPUT '*----------------------------------------------------*'
        OUTPUT '1. Control Panel'
        OUTPUT '2. Black Box'
        OUTPUT '3. Test'
        OUTPUT '4. Quit'
        OUTPUT 'Enter digit to continue:'
        o1 <- input()
        IF o1 = '1':
            o2 <- '1'
            while o2 != '4':
                OUTPUT 'Control Panel'
                OUTPUT '1. Check Sensors'
                OUTPUT '2. Check Points'
                OUTPUT '3. Check Signals'
                OUTPUT '4. Leave'
                OUTPUT ''
                OUTPUT 'HIT ENTER FOR EMERGENCY STOP'
                o2 <- input()
                IF o2 = '1':
                                               ENDFOR
                    sensor_data[1] <- True
                    sensor_check_1()
                    sensor_check_2()
                    OUTPUT f'Route one is clear - {r1} Route two is clear - {r2}'
                    record_data()
                ELSEIF o2 = '2':
                    OUTPUT f'Point A is at {Point_A}°\n'
                          f'Point B is at {Point_B}°\n')
                    record_data()
                ELSEIF o2 = '3':
                    signal_check()
                    OUTPUT f'Signal 1 - {Sig_a}\n'
                          f'Signal 2 - {Sig_b}\n'
                          f'Signal 3 - {Sig_c}\n'
                          f'Signal 4 - {Sig_d}\n'
                          f'Signal 5 - {Sig_e}\n'
                          f'Signal 6 - {Sig_f}\n')
                    record_data()
                ELSEIF o2 = '':
                    record_data()
                    f <- open('blackbox.txt', 'a')
                    find_date()
                    f.write(f'\n\n***EMERGENCY STOP AT {date}***\n')
                    f.close()
                    emergency_stop <- True
                    break
                ENDIF
            ENDWHILE
        ELSEIF o1 = '2':
            OUTPUT 'Black Box Menu'
            OUTPUT '1. Read Last Input'
            OUTPUT '2. Download Black Box'
            OUTPUT '3. Clear Black Box'
            OUTPUT '4. Leave'
            o3 <- input()
            while o3 != '4':
                IF o3 = '1':
                    f <- open("blackbox.txt", "r")
                    file <- f.read()
                    f.close()
                    OUTPUT file[-750:]
                ENDIF
                                ENDFOR
                IF o3 = '2':
                    OUTPUT 'Please input where you want the file downloaded to.'
                    OUTPUT 'i.e C:/Users/johnsmith/'
                    file_dst <- input()
                    src <- 'blackbox.txt'
                    find_date_file_name()
                    dst <- f'{file_dst}blackbox{date_file}.txt'
                    try:
                        f <- open(dst, 'a')
                        f.close()
                        copyfile(src, dst)
                    except Exception as e:
                        OUTPUT 'Error: %s' % str(e)
                ENDIF
                IF o3 = '3':
                    f <- open('blackbox.txt', 'r')
                    x <- f.read()
                    f.close()
                    OUTPUT 'Are you sure you want to delete all data?'
                    OUTPUT 'Once deleted data cannot be restored'
                    OUTPUT f'Last delete was on {x[:24]}'
                    OUTPUT 'y/n'
                    delete <- input().lower()
                    IF delete = 'yes' OR 'y':
                        f <- open('blackbox.txt', 'a')
                        f.truncate(0)
                        find_date()
                        f.write(f'{date}\n')
                        f.close()
                    ELSEIF delete = 'no' OR 'n':
                        pass
                ENDIF
                    ENDIF
            ENDWHILE
        ELSEIF o1 = '3':
            o4 <- ''
            while o4 != 2:
                OUTPUT 'Test Menu'
                OUTPUT '1. Full run'
                OUTPUT '2. Leave'
                o4 <- input()
                IF o4 = '1':
                    OUTPUT 'Starting Simulation'
                    power_t1 <- 10
                    power_t2 <- 10
                    IF power_t1 != 0 AND power_t2 != 0:
                        OUTPUT f'The Scotsman is traveling at {power_t1}'
                        OUTPUT f'The Mallard is traveling at {power_t2}'
                        from run import outward_run
                        test <- True
                        outward_run()
                        point_change()
                        time.sleep(2)
                        from run import return_run
                        return_run()
                    ENDIF
                ELSEIF o4 = '2':
                    break
                ENDIF
            ENDWHILE
        ELSEIF o1 = '4':
            OUTPUT 'Type 1 to quit type 2 to return'
            q1 <- input()
            IF q1 = '1':
                break
            ELSE:
                pass
        ENDIF
            ENDIF
    ENDWHILE
    time.sleep(wait_time)
ENDFUNCTION

IF __name__ = '__main__':
    main()
