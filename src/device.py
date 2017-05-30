from my_visa import Visa


class Device(Visa):
    def __init__(self, ip):
        super(Device, self).__init__(ip)

    def info(self):
        full_name = self.visa_query('*IDN?')
        return full_name  # .split(",")[0]
        #       return SN     = self.full_name.split(',')[1]
        #       return PN     = self.full_name.split(',')[2]

    def preset(self):
        return self.visa_write('SYST:PRES')
