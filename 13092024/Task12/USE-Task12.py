for i1 in range(100):
    for i2 in range(100):
        for i3 in range(100):
            s = '0'+i1*'1'+i2*'2'+i3*'5'
            while s.find('01') > -1 or s.find('02') > -1 or s.find('03') > -1:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 40 and s.count('2') == 10 and s.count('5') == 8:
                print(i1)
#Ответ: 6