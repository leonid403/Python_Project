# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import visa

SIG_GEN = '10.18.134.209'


class Visa(object):
    def __init__(self, ip):
        self.ip = ip
        self.rm = visa.ResourceManager()
        self.device = None

    def visa_open(self):
        print(self.ip)
        print(type(self.rm))

        self.device = self.rm.open_resource('TCPIP::{}'.format(SIG_GEN))

    def visa_write(self, command):
        return self.device.write(command)

    def visa_read(self, command):
        return self.device.read(command)

    def visa_query(self, command):
        return self.device.query(command)

    def visa_close(self):
        return self.device.close()


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


class PowerSupply(PowDev):
    def __init__(self, ip):
        super(PowerSupply, self).__init__(ip)


class Spectrum(FreqDev):
    def __init__(self, ip):
        super(Spectrum, self).__init__(ip)

    def peak_search(self):
        pass

    def set_band_pow_span(self):
        pass


class Network(FreqDev):
    def __init__(self, ip):
        super(Network, self).__init__(ip)

    def set_sparam(self, sparm):
        pass

    def set_meas_format(self, meas_format):
        pass


class Signal(FreqDev):
    def __init__(self, ip):
        super(Signal, self).__init__(ip)

    def set_amp(self, amp):
        return self.visa_write(':POW {}'.format(amp))

    def get_amp(self):
        return self.visa_query(':POW?')

    def set_ext_ref(self, freq):
        pass

    def set_rf_on_off(self, rf):
        pass

    def set_mod_on_off(self, rf):
        pass


sg = Signal(SIG_GEN)
sg.visa_open()
print(sg.info())



