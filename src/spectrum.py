from freq_dev import FreqDev


class Spectrum(FreqDev):
    def __init__(self, ip):
        super(Spectrum, self).__init__(ip)

    def set_mark_on_off(self, mark):
        return self.visa_write(":CALC:MARK1:STAT {}".format(mark))

    def set_mark_freq(self, freq):
        return self.visa_write(":CALC:MARK1:X {}".format(freq))

    def get_mark_freq(self):
        return self.visa_query(":CALC:MARK1:Y?")

    def peak_search(self):
        pass

    def set_band_pow_span(self):
        pass