from freq_dev import FreqDev


class Signal(FreqDev):
    def __init__(self, ip):
        super(Signal, self).__init__(ip)

    def set_amp(self, amp):
        return self.visa_write(':POW {}'.format(amp))

    def get_amp(self):
        return self.visa_query(':POW?')

    def set_freq(self, freq):
        return self.visa_write(':FREQ {}'.format(freq))

    def get_freq(self):
        return self.visa_query(':FREQ?')

    def set_ext_ref(self, freq):
        pass

    def set_rf_on_off(self, rf):
        return self.visa_write(':OUTP {}'.format(rf))

    def set_mod_on_off(self, rf):
        pass