from device import Device


class PowDev(Device):
    def __init__(self, ip):
        super(PowDev, self).__init__(ip)

    def set_voltage(self, voltage):
        pass

    def set_current(self, current):
        pass

    def get_voltage(self):
        pass

    def get_current(self):
        pass
