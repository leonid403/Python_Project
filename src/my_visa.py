import visa


class Visa(object):
    def __init__(self, ip):
        self.ip = ip
        self.rm = visa.ResourceManager()
        self.device = None

    def visa_open(self):
        # print(self.ip)
        # print(type(self.rm))
        self.device = self.rm.open_resource('TCPIP::{}'.format(self.ip))

    def visa_write(self, command):
        return self.device.write(command)

    def visa_read(self, command):
        return self.device.read(command)

    def visa_query(self, command):
        return self.device.query(command)

    def visa_close(self):
        return self.device.close()
