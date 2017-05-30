from device import Device


class FreqDev(Device):
    def __init__(self, ip):
        super(FreqDev, self).__init__(ip)

    def set_freq(self, freq):
        return self.visa_write('FREQ:CENT {}'.format(freq))

    def get_freq(self):
        return self.visa_query('FREQ:CENT?')

    def set_span(self, span):
        return self.visa_write('FREQ:SPAN {}'.format(span))

    def get_span(self):
        return self.visa_query('FREQ:SPAN?')


