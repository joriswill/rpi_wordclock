class time_german1212:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a german WCA in alternative layout german1212
    Credits to Joris
    """

    def __init__(self):
        self.prefix = range(0,2) +  range(3,6)
        self.minutes=[[], \
            range(8,12) + range(44,48), \
            range(12,16) + range(44,48), \
            range(29,36) + range(44,48), \
            range(17,24) + range(44,48), \
            range(8,12) + range(36,39) + range(49,53), \
            range(49,53), \
            range(8,12) + range(44,48) + range(49,53), \
            range(17,24) + range(36,39), \
            range(29,36) + range(36,39), \
            range(12,16) + range(36,39), \
            range(8,12) + range(36,39) ]
        self.hours= [range(96,101), \
            range(60,63), \
            range(104,108), \
            range(72,76), \
            range(108,112), \
            range(92,96), \
            range(115,120), \
            range(66,72), \
            range(84,88), \
            range(80,84), \
            range(128,132), \
            range(90,93), \
            range(96,101)]
        self.full_hour= range(141,144)

    def get_time(self, time, purist):
        hour=time.hour%12+(1 if time.minute/5 > 4 else 0)
        minute=time.minute/5
        # Assemble indices
        return  \
            (self.prefix if not purist else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            ([63] if (hour == 1 and minute != 0) else []) + \
            (self.full_hour if (minute == 0) else [])

