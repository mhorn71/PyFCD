__author__ = 'mark'

## Note for hid to work you need to install cython from repos and cython-hidapi from https://github.com/bazuchan

import hid
import struct
import re

##  Funcube Dongle Pro Command Line Control Interface.
##  This library is based upon work by X X X X X
##


class PyFcdCtrl(object):
    def __init__(self):
        """ Set some default settings to start with lna_gain, mixer_gain, if_gain, init_frequency and ppm_offset

            All Errors raise Exception """

        self.vendorid = 0x04d8
        self.productid = 0xfb56
        self.lna_gain = 4
        self.mixer_gain = 0
        self.if_gain = 4
        self.init_freq = 64000000
        self.ppm_offset = -120

    def set_khz(self, freq, ppm_offset):

        """
            set_khz(int(frequency), int(ppm_offset))

            returns True or False

            NOTE: There is no checking of whether or not the frequency being set is within range of the device.
        """

        corrected_freq = freq + int((float(freq)/1000000.0)*float(ppm_offset))

        nfreq = hex(corrected_freq)

        _bytes = [hex(int(nfreq, 16) >> i & 0xff) for i in (16,8,0)]  ## convert frequency into 3 bytes

        lbytechars = []

        for i in reversed(_bytes):  # Reverse order bytes for little endian.
            lbytechars.append(chr(int(i, 16)))

        try:
            d = hid.device(self.vendorid, self.productid)
            n = [0, 100] + map(ord, lbytechars)
            d.write(n)
            x = d.read(65)[0:6]
            d.close()
        except IOError as e:
            raise Exception('IOError ' + str(e))
        else:
            if x[0] == 100 and x[1] == 1:
                return True
            else:
                return False

    def set_hz(self, freq, ppm_offset):

        """
            set_hz(int(frequency), int(ppm_offset))

            returns True or False

            NOTE: There is no checking of whether or not the frequency being set is within range of the device.
        """

        corrected_freq = freq + int((float(freq)/1000000.0)*float(ppm_offset))

        try:
            d = hid.device(self.vendorid, self.productid)
            n = [0, 101] + map(ord, struct.pack('<I', corrected_freq))
            d.write(n)
            x = d.read(65)[0:6]
            d.close()
        except IOError as e:
            raise Exception('IOError ' + str(e))
        else:
            if x[0] == 101 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_mode(self, gainmode):
        """
            Where gainmode is a string consisting of :

            lin or sen

            returns True or False
        """
        if re.match('^lin$', gainmode):
            gainmodeenum = 0
        elif re.match('^sen$', gainmode):
            gainmodeenum = 1
        else:
            raise Exception('Gain Mode string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 118, gainmodeenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 118 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_1(self, gain):
        """
            Where gain in db is a string consisting of :

            -3.0 or +6.0

            returns True of False
        """
        if re.match('^\-3\.0$', gain):
            gainoneenum = 0
        elif re.match('\+6\.0', gain):
            gainoneenum = 1
        else:
            raise Exception('IF Gain One string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 117, gainoneenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 117 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_2(self, gain):
        """
            Where gain in db is a string consisting of :

            +0.0, +3.0, +6.0 or +9.0

            returns True of False
        """
        if re.match('^\+0\.0$', gain):
            gaintwoenum = 0
        elif re.match('\+3\.0', gain):
            gaintwoenum = 1
        elif re.match('\+6\.0', gain):
            gaintwoenum = 2
        elif re.match('\+9\.0', gain):
            gaintwoenum = 3
        else:
            raise Exception('IF Gain Two string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 120, gaintwoenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 120 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_3(self, gain):
        """
            Where gain in db is a string consisting of :

            +0.0, +3.0, +6.0 or +9.0

            returns True of False
        """
        if re.match('^\+0\.0$', gain):
            gainthreeenum = 0
        elif re.match('\+3\.0', gain):
            gainthreeenum = 1
        elif re.match('\+6\.0', gain):
            gainthreeenum = 2
        elif re.match('\+9\.0', gain):
            gainthreeenum = 3
        else:
            raise Exception('IF Gain Three string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 121, gainthreeenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 121 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_4(self, gain):
        """
            Where gain in db is a string consisting of :

            +0.0, +1.0 or +2.0

            returns True of False
        """
        if re.match('^\+0\.0$', gain):
            gainfourenum = 0
        elif re.match('\+1\.0', gain):
            gainfourenum = 1
        elif re.match('\+2\.0', gain):
            gainfourenum = 2
        else:
            raise Exception('IF Gain Four string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 123, gainfourenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 123 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_5(self, gain):
        """
            Where gain in db is a string consisting of :

            +3.0, +6.0, +9.0, +12.0 or +15.0

            returns True of False
        """
        if re.match('^\+3\.0$', gain):
            gainfiveenum = 0
        elif re.match('\+6\.0', gain):
            gainfiveenum = 1
        elif re.match('\+9\.0', gain):
            gainfiveenum = 2
        elif re.match('\+12\.0', gain):
            gainfiveenum = 3
        elif re.match('\+15\.0', gain):
            gainfiveenum = 4
        else:
            raise Exception('IF Gain Five string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 124, gainfiveenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 124 and x[1] == 1:
                return True
            else:
                return False

    def set_if_gain_6(self, gain):
        """
            Where gain in db is a string consisting of :

            +3.0, +6.0, +9.0, +12.0 or +15.0

            returns True of False
        """
        if re.match('^\+3\.0$', gain):
            gainsixenum = 0
        elif re.match('\+6\.0', gain):
            gainsixenum = 1
        elif re.match('\+9\.0', gain):
            gainsixenum = 2
        elif re.match('\+12\.0', gain):
            gainsixenum = 3
        elif re.match('\+15\.0', gain):
            gainsixenum = 4
        else:
            raise Exception('IF Gain Six string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 125, gainsixenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 125 and x[1] == 1:
                return True
            else:
                return False

    def set_lna_enhance(self, lna_enhance):
        """
            Where lna_enhance is a string consisting of :

            OFF, 0, 1, 2, 3

            returns True or False
        """
        if re.match('^OFF$', lna_enhance):
            lnaenum = 0
        elif re.match('^0$', lna_enhance):
            lnaenum = 1
        elif re.match('^1$', lna_enhance):
            lnaenum = 3
        elif re.match('^2$', lna_enhance):
            lnaenum = 5
        elif re.match('^3$', lna_enhance):
            lnaenum = 7
        else:
            raise Exception('LNA Enhance string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 111, lnaenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 111 and x[1] == 1:
                return True
            else:
                return False

    def set_lna_gain(self, lna_gain):
        """
            Where lna_gain is a string consisting of :

            -5.0, -2.5, +0.0, +2.5, +5.0, +7.5, +10.0, +12.5, + 15.0, +17.5, +20.0, +25.00, +30

            returns True or False
        """
        if re.match('^\-5.0$', lna_gain):
            gainenum = 0
        elif re.match('^\-2.5$', lna_gain):
            gainenum = 1
        elif re.match('^\+0.0$', lna_gain):
            gainenum = 4
        elif re.match('^\+2.5$', lna_gain):
            gainenum = 6
        elif re.match('^\+5.0$', lna_gain):
            gainenum = 7
        elif re.match('^\+7.5$', lna_gain):
            gainenum = 8
        elif re.match('^\+10.0$', lna_gain):
            gainenum = 9
        elif re.match('^\+12.5$', lna_gain):
            gainenum = 10
        elif re.match('^\+15.0$', lna_gain):
            gainenum = 11
        elif re.match('^\+17.5$', lna_gain):
            gainenum = 12
        elif re.match('^\+20.0$', lna_gain):
            gainenum = 13
        elif re.match('^\+25.0$', lna_gain):
            gainenum = 14
        elif re.match('^\+30.0$', lna_gain):
            gainenum = 15
        else:
            raise Exception('LNA Gain string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 110, gainenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception(e)
        else:
            if x[0] == 101 and x[1] == 1:
                return True
            else:
                return False

    def set_band(self, band):
        """
            Where band is a string consisting of:

            VHF2, VHF3, UHF, LBAND

            returns True or False
        """

        bandcenum = ['VHF2', 'VHF3', 'UHF', 'LBAND']

        bandenum = None

        for i in bandcenum:
            if re.match(i, band):
                bandenum = bandcenum.index(i)

        if bandenum is None:
            raise Exception('Band string mismatch!!')
        else:
            try:
                d = hid.device(self.vendorid, self.productid)
                d.write([0, 112, int(bandenum)])
                x = d.read(65)[0:3]
                d.close()
            except IOError as e:
                raise Exception("IOError " + str(e))
            else:
                if x[0] == 112 and x[1] == 1:
                    return True
                else:
                    return False

    def set_rf_filter(self, rf_filter):
        """
        Where rf_filter is a string consisting for:

        (Band 0, VHF II) - LPF268MHz, LPF299MHz

        (Band 1, VHF III) - LPF509MHz, LPF656MHz

        (Band 2, UHF) - BPF360MHz, BPF380MHz, BPF405MHz, BPF425MHz, BPF450MHz, BPF475MHz, BPF505MHz, BPF540MHz
           BPF575MHz, BPF615MHz, BPF670MHz, BPF720MHz, BPF760MHz, BPF840MHz, BPF890MHz, BPF970MHz

        (Band 3, L Band) - BPF1300MHz, BPF1320MHz, BPF1360MHz, BPF1410MHz, BPF1445MHz, BPF1460MHz, BPF1490MHz
           BPF1530MHz, BPF1560MHz, BPF1590MHz, BPF1640MHz, BPF1660MHz, BPF1680MHz, BPF1700MHz, BPF1720MHz, BPF1750MHz

        set_rf_filter('BPF360MHz')

        returns True or False

        Wrong Band to RF Filter match raises Exception.
        """

        band0 = ['LPF268MHz', 'LPF299MHz']

        band1 = ['LPF509MHz', 'LPF656MHz']

        band2 = ['BPF360MHz', 'BPF380MHz', 'BPF405MHz', 'BPF425MHz', 'BPF450MHz', 'BPF475MHz', 'BPF505MHz',
                 'BPF540MHz', 'BPF575MHz', 'BPF615MHz', 'BPF670MHz', 'BPF720MHz', 'BPF760MHz', 'BPF840MHz',
                 'BPF890MHz', 'BPF970MHz']

        band3 = ['BPF1300MHz', 'BPF1320MHz', 'BPF1360MHz', 'BPF1410MHz', 'BPF1445MHz', 'BPF1460MHz', 'BPF1490MHz',
                 'BPF1530MHz', 'BPF1560MHz', 'BPF1590MHz', 'BPF1640MHz', 'BPF1660MHz', 'BPF1680MHz', 'BPF1700MHz',
                 'BPF1720MHz', 'BPF1750MHz']

        band = self.get_band()

        rffilterenum = None

        if band == 'VHF2':
            for i in band0:
                if re.match(i, rf_filter):
                    rffilterenum = band0.index(i)
                    if rffilterenum == '2':  # Fudge as we're using list index and FCD expects index 2 to be 8
                        rffilterenum = 8
        elif band == 'VHF3':
            for i in band1:
                if re.match(i, rf_filter):
                    rffilterenum = band1.index(i)
                    if rffilterenum == '2':
                        rffilterenum = 8
        elif band == 'UHF':
            for i in band2:
                if re.match(i, rf_filter):
                    rffilterenum = band2.index(i)
        elif band == 'LBAND':
            for i in band3:
                if re.match(i, rf_filter):
                    rffilterenum = band3.index(i)
        else:
            raise Exception('RF Filter unable to get current set band')

        if rffilterenum is None:
            raise Exception('RF Filter and Band mismatch!!')
        else:
            try:
                d = hid.device(self.vendorid, self.productid)
                d.write([0, 113, int(rffilterenum)])
                x = d.read(65)[0:3]
                d.close()
            except IOError as e:
                raise Exception("IOError " + str(e))
            else:
                if x[0] == 113 and x[1] == 1:
                    return True
                else:
                    return False

    def set_bias_current(self, bias):
        """
            Where bias is a string consisting of:

            LBAND, 01, 10, VUBAND

            returns True or False
        """
        biascenum = ['LBAND', '01', '10', 'VUBAND']

        biasenum = None

        for i in biascenum:
            if re.match(i, bias):
                biasenum = biascenum.index(i)

        if biasenum is None:
            raise Exception('Bias string mismatch!!')
        else:
            try:
                d = hid.device(self.vendorid, self.productid)
                d.write([0, 115, biasenum])
                x = d.read(65)[0:3]
                d.close()
            except IOError as e:
                raise Exception("IOError " + str(e))
            else:
                if x[0] == 115 and x[1] == 1:
                    return True
                else:
                    return False

    def set_if_filter(self, if_filter):
        """
            Where bias is a string consisting of:

            5.50, 5.30, 5.00, 4.80, 4.60, 4.40, 4.30, 4.10, 3.90, 3.80, 3.70, 3.60, 3.40, 3.30, 3.20, 3.10, 3.00
            2.95, 2.90, 2.80, 2.75, 2.70, 2.60, 2.55, 2.50, 2.45, 2.40, 2.30, 2.28, 2.24, 2.20, 2.15

            returns True or False
        """

        _filter = ['5.50', '5.30', '5.00', '4.80', '4.60', '4.40', '4.30', '4.10', '3.90', '3.80', '3.70', '3.60',
                   '3.40', '3.30', '3.20', '3.10', '3.00', '2.95', '2.90', '2.80', '2.75', '2.70', '2.60', '2.55',
                   '2.50', '2.45', '2.40', '2.30', '2.28', '2.24', '2.20', '2.15']

        iffilterenum = None

        for f in _filter:
            if re.match(f, if_filter):
                iffilterenum = _filter.index(f)
            else:
                iffilterenum = None
        else:
            if iffilterenum is None:
                raise Exception('IF Filter string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 115, iffilterenum])
            x = d.read(65)[0:3]
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 115 and x[1] == 1:
                return True
            else:
                return False

    def set_if_rc_filter(self, if_rc_filter):
        """
            Where if_rc_filter in MHz is a string consisting of :

            21.4, 21.0, 17.6, 14.7, 12.4, 10.6, 9.0, 7.7, 6.4, 5.3, 4.4, 3.4, 2.6, 1.8, 1.2 or 1.0

            returns True or False
        """
        if re.match('^27\.0$', if_rc_filter):
            ifrcfilterenum = 0
        elif re.match('^21\.0$', if_rc_filter):
            ifrcfilterenum = 1
        elif re.match('^17\.6$', if_rc_filter):
            ifrcfilterenum = 2
        elif re.match('^14\.7$', if_rc_filter):
            ifrcfilterenum = 3
        elif re.match('^12\.4$', if_rc_filter):
            ifrcfilterenum = 4
        elif re.match('^10\.6$', if_rc_filter):
            ifrcfilterenum = 5
        elif re.match('^9\.0$', if_rc_filter):
            ifrcfilterenum = 6
        elif re.match('^7\.7$', if_rc_filter):
            ifrcfilterenum = 7
        elif re.match('^6\.4$', if_rc_filter):
            ifrcfilterenum = 8
        elif re.match('^5\.3$', if_rc_filter):
            ifrcfilterenum = 9
        elif re.match('^4\.4$', if_rc_filter):
            ifrcfilterenum = 10
        elif re.match('^3\.4$', if_rc_filter):
            ifrcfilterenum = 11
        elif re.match('^2\.6$', if_rc_filter):
            ifrcfilterenum = 12
        elif re.match('^1\.8$', if_rc_filter):
            ifrcfilterenum = 13
        elif re.match('^1\.2$', if_rc_filter):
            ifrcfilterenum = 14
        elif re.match('^1\.0$', if_rc_filter):
            ifrcfilterenum = 15
        else:
            raise Exception('IF RC Mixer Filter string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 119, ifrcfilterenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception(e)
        else:
            if x[0] == 119 and x[1] == 1:
                return True
            else:
                return False

    def set_mixer_filter(self, mixer_filter):
        """
            Where mixer_filter in MHz is a string consisting of :

            27.0, 4.6, 4.2, 3.8, 3.4, 3.0, 2.7, 2.3 or 1.9

            returns True or False
        """
        if re.match('^27\.0$', mixer_filter):
            mixerfilterenum = 0
        elif re.match('^4\.6$', mixer_filter):
            mixerfilterenum = 8
        elif re.match('^4\.2$', mixer_filter):
            mixerfilterenum = 9
        elif re.match('^3\.8$', mixer_filter):
            mixerfilterenum = 10
        elif re.match('^3\.4$', mixer_filter):
            mixerfilterenum = 11
        elif re.match('^3\.0$', mixer_filter):
            mixerfilterenum = 12
        elif re.match('^2\.7$', mixer_filter):
            mixerfilterenum = 13
        elif re.match('^2\.3$', mixer_filter):
            mixerfilterenum = 14
        elif re.match('^1\.9$', mixer_filter):
            mixerfilterenum = 15
        else:
            raise Exception('Mixer Filter string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 116, mixerfilterenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception(e)
        else:
            if x[0] == 116 and x[1] == 1:
                return True
            else:
                return False

    def set_mixer_gain(self, mixer_gain):
        """
            Where mixer_gain in db is a string consisting of :

            +4.0 or +12.0

            returns True of False
        """
        if re.match('^\+4\.0$', mixer_gain):
            mixergainenum = 0
        elif re.match('\+12\.0', mixer_gain):
            mixergainenum = 1
        else:
            raise Exception('Mixer Gain string mismatch!!')

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 114, mixergainenum])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 114 and x[1] == 1:
                return True
            else:
                return False

    def set_mode(self, mode):
        """ Sets the mode of the Funcube FCDAPP or FCDBL
        """
        pass

    def firmware(self, mode):
        """ Upload or Verify Firmware
        """
        pass

    def set_iq(self, phase, gain):
        """
            Where phase and gain are floats.

            returns True or False
        """

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 108,]) + map(ord, struct.pack('h', (phase * 32768.0))) + \
            map(ord, struct.pack('h', (gain * 32768.0)))
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 108 and x[1] == 1:
                return True
            else:
                return False

    def set_dc(self, i, q):
        """
            Where i and q are floats.

            returns True or False
        """

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 106,]) + map(ord, struct.pack('h', (i * 32768.0))) + \
            map(ord, struct.pack('h', (q * 32768.0)))
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception('IOError' + str(e))
        else:
            if x[0] == 106 and x[1] == 1:
                return True
            else:
                return False

    def defaults(self):
        """
            Sets the following default parameters:

            Frequency : 144430000   (GB3VHF 2m Beacon)
            ppm : -120
            LNA Gain : +12.0db
            Mixer Gain : +12.0db
            RF Filter : 268MHz LPF
            Mixer Filter : 1.9MHz
            IF RC Filter : 1.0MHz
            IF Filter : 2.15MHz
            IF Gain 1 : +6db
            IF Gain 2 : 0db
            IF Gain 3 : 0db
            IF Gain 4 : 0db
            IF Gain 5 : +3db
            IF Gain 6 : +3db
            LNA Enhance : OFF
            Band : VHF II
            Bias Current : II V/U band
            IF Gain Mode : Linearity
            PLL Lock : True
            DC I : 0.00000
            DC Q : 0.00000
            Gain : 1.00000
            Phase: 0.00000
        """

        if self.set_hz(144430000, -120) is not True:
            raise Exception('Unable to set defaults (Frequency)!')

        if self.set_lna_gain('+12.0') is not True:
            raise Exception('Unable to set defaults (LNA Gain)!')

        if self.set_mixer_gain('+12.0') is not True:
            raise Exception('Unable to set defaults (Mixer Gain)!')

        if self.set_mixer_filter('1.9') is not True:
            raise Exception('Unable to set defaults (Mixer Filter)!')

        if self.set_rf_filter('LPF268MHz') is not True:
            raise Exception('Unable to set defaults (RF Filter)!')

        if self.set_if_rc_filter('1.0') is not True:
            raise Exception('Unable to set defaults (IF RC Filter)!')

        if self.set_if_filter('2.15') is not True:
            raise Exception('Unable to set defaults (IF Filter)!')

        if self.set_if_gain_1('+6.0') is not True:
            raise Exception('Unable to set defaults (IF Gain One)!')

        if self.set_if_gain_2('+0.0') is not True:
            raise Exception('Unable to set defaults (IF Gain Two)!')

        if self.set_if_gain_3('+0.0') is not True:
            raise Exception('Unable to set defaults (IF Gain Three)!')

        if self.set_if_gain_4('+0.0') is not True:
            raise Exception('Unable to set defaults (IF Gain Four)!')

        if self.set_if_gain_5('+3.0') is not True:
            raise Exception('Unable to set defaults (IF Gain Four)!')

        if self.set_if_gain_6('+3.0') is not True:
            raise Exception('Unable to set defaults (IF Gain Four)!')

        if self.set_lna_enhance('OFF') is not True:
            raise Exception('Unable to set defaults (LNA Enhance)!')

        if self.set_band('VHF2') is not True:
            raise Exception('Unable to set defaults (LNA Enhance)!')

        if self.set_bias_current('VUBAND') is not True:
            raise Exception('Unable to set defaults (BIAS Current)!')

        if self.set_if_gain_mode('lin') is not True:
            raise Exception('Unable to set defaults (IF Gain Mode)!')

        if self.set_iq(0.00000, 1.00000) is not True:
            raise Exception('Unable to set defaults (I/Q Correction)!')

        if self.set_dc(0.00000, 0.00000) is not True:
            raise Exception('Unable to set defaults (DC Correction)!')
        else:
            return True

    ####################
    ### Get Commands ###
    ####################

    def get_hz(self):
        """
            Returns current set frequency in Hz as reported by the Funcube, if no frequency is found None is returned.
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 1, 101])
            x = d.read(65)[0:6]
            d.close()
        except IOError as e:
            raise Exception(e)
        else:
            if x[0] == 101 and x[1] == 1:
                xn = re.sub('[(),]', '', str(struct.unpack('<I', ''.join(map(chr, x[2:6])))))
                return xn
            else:
                return None

    def get_band(self):
        """
            Returns a string consisting of:

            VHF2, VHF3, UHF, LBAND
        """

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 152])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 152 and x[1] == 1:
                if x[2] == 0:
                    return 'VHF2'
                elif x[2] == 1:
                    return 'VHF3'
                elif x[2] == 2:
                    return 'UHF'
                elif x[2] == 3:
                    return 'LBAND'
                else:
                    raise Exception('Funcube reponse not recognised!!')
            else:
                raise Exception('Funcube reponse not recognised!!')

    def get_lna_gain(self):
        """
            Returns a string consisting of :

            -5.0, -2.5, +0.0, +2.5, +5.0, +7.5, +10.0, +12.5, + 15.0, +17.5, +20.0, +25.00, +30
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 150])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 150 and x[1] == 1:
                if x[2] == 0:
                    return '-5.0'
                elif x[2] == 1:
                    return '-2.5'
                elif x[2] == 4:
                    return '+0.0'
                elif x[2] == 6:
                    return '+2.5'
                elif x[2] == 7:
                    return '+5.0'
                elif x[2] == 8:
                    return '+7.5'
                elif x[2] == 9:
                    return '+10.0'
                elif x[2] == 10:
                    return '+12.5'
                elif x[2] == 11:
                    return '+15.0'
                elif x[2] == 12:
                    return '+17.5'
                elif x[2] == 13:
                    return '+20.0'
                elif x[2] == 14:
                    return '+25.0'
                elif x[2] == 15:
                    return '+30.0'
                else:
                    raise Exception('Funcube reponse not recognised!!')
            else:
                raise Exception('Funcube reponse not recognised!!')

    def get_lna_enhance(self):
        """
            Returns a string consisting of :

            OFF, 0, 1, 2, 3
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 151])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 151 and x[1] == 1:
                if x[2] == 0:
                    return 'OFF'
                elif x[2] == 1:
                    return '0'
                elif x[2] == 3:
                    return '1'
                elif x[2] == 5:
                    return '2'
                elif x[2] == 7:
                    return '3'
            else:
                raise Exception('Funcube reponse not recognised!!')

    def get_rf_filter(self):
        """
        Returns a string consisting of :

        (Band 0, VHF II) - LPF268MHz, LPF299MHz

        (Band 1, VHF III) - LPF509MHz, LPF656MHz

        (Band 2, UHF) - BPF360MHz, BPF380MHz, BPF405MHz, BPF425MHz, BPF450MHz, BPF475MHz, BPF505MHz, BPF540MHz
           BPF575MHz, BPF615MHz, BPF670MHz, BPF720MHz, BPF760MHz, BPF840MHz, BPF890MHz, BPF970MHz

        (Band 3, L Band) - BPF1300MHz, BPF1320MHz, BPF1360MHz, BPF1410MHz, BPF1445MHz, BPF1460MHz, BPF1490MHz
           BPF1530MHz, BPF1560MHz, BPF1590MHz, BPF1640MHz, BPF1660MHz, BPF1680MHz, BPF1700MHz, BPF1720MHz, BPF1750MHz.
        """

        band0 = ['LPF268MHz', '', '', '', '', '', '', '', 'LPF299MHz']

        band1 = ['LPF509MHz', '', '', '', '', '', '', '', 'LPF656MHz']

        band2 = ['BPF360MHz', 'BPF380MHz', 'BPF405MHz', 'BPF425MHz', 'BPF450MHz', 'BPF475MHz', 'BPF505MHz',
                 'BPF540MHz', 'BPF575MHz', 'BPF615MHz', 'BPF670MHz', 'BPF720MHz', 'BPF760MHz', 'BPF840MHz',
                 'BPF890MHz', 'BPF970MHz']

        band3 = ['BPF1300MHz', 'BPF1320MHz', 'BPF1360MHz', 'BPF1410MHz', 'BPF1445MHz', 'BPF1460MHz', 'BPF1490MHz',
                 'BPF1530MHz', 'BPF1560MHz', 'BPF1590MHz', 'BPF1640MHz', 'BPF1660MHz', 'BPF1680MHz', 'BPF1700MHz',
                 'BPF1720MHz', 'BPF1750MHz']

        band = self.get_band()

        enum = None

        if band == 'VHF2':
            enum = band0
        elif band == 'VHF3':
            enum = band1
        elif band == 'UHF':
            enum = band2
        elif band == 'LBAND':
            enum = band3
        else:
            raise Exception("Funcube response not recognised!!")

        if enum is None:
            raise Exception("Funcube response not recognised!!")
        else:
            try:
                d = hid.device(self.vendorid, self.productid)
                d.write([0, 153])
                x = d.read(65)
                d.close()
            except IOError as e:
                raise Exception("IOError " + str(e))
            else:
                if x[0] == 153 and x[1] == 1:
                    return enum[x[2]]
                else:
                    raise Exception("Funcube response not recognised!!")


    def get_mixer_gain(self):
        """
            Returns a string in db consisting of :

            +4.0 or +12.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 154])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 154 and x[1] == 1:
                if x[2] == 0:
                    return '+4.0'
                elif x[2] == 1:
                    return '+12.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_bias_current(self):
        """
            Returns a string consisting of:

            LBAND, 01, 10, VUBAND
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 155])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 155 and x[1] == 1:
                if x[2] == 0:
                    return 'LBAND'
                elif x[2] == 1:
                    return '01'
                elif x[2] == 2:
                    return '10'
                elif x[2] == 3:
                    return 'VUBAND'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_mixer_filter(self):
        """
            Returns a string in MHz consisting of :

            27.0, 4.6, 4.2, 3.8, 3.4, 3.0, 2.7, 2.3 or 1.9
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 156])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 156 and x[1] == 1:
                if x[2] == 0:
                    return '27.0'
                elif x[2] == 8:
                    return '4.6'
                elif x[2] == 9:
                    return '4.2'
                elif x[2] == 10:
                    return '3.8'
                elif x[2] == 11:
                    return '3.4'
                elif x[2] == 12:
                    return '3.0'
                elif x[2] == 13:
                    return '2.7'
                elif x[2] == 14:
                    return '2.3'
                elif x[2] == 15:
                    return '1.9'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_1(self):
        """
            Returns a string in db consisting of :

            -3.0 or +6.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 157])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 157 and x[1] == 1:
                if x[2] == 0:
                    return '-3.0'
                elif x[2] == 1:
                    return '+6.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_2(self):
        """
            Returns a string in db consisting of :

            +0.0, +3.0, +6.0 or +9.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 160])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 160 and x[1] == 1:
                if x[2] == 0:
                    return '+0.0'
                elif x[2] == 1:
                    return '+3.0'
                elif x[2] == 2:
                    return '+6.0'
                elif x[2] == 3:
                    return '+9.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_3(self):
        """
            Returns a string in db consisting of :

            +0.0, +3.0, +6.0 or +9.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 161])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 161 and x[1] == 1:
                if x[2] == 0:
                    return '+0.0'
                elif x[2] == 1:
                    return '+3.0'
                elif x[2] == 2:
                    return '+6.0'
                elif x[2] == 3:
                    return '+9.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_4(self):
        """
            Returns a string in db consisting of :

            +0.0, +1.0 or +2.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 163])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 163 and x[1] == 1:
                if x[2] == 0:
                    return '+0.0'
                elif x[2] == 1:
                    return '+1.0'
                elif x[2] == 2:
                    return '+2.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_5(self):
        """
            Returns a string in db consisting of :

            +3.0, +6.0, +9.0, +12.0 or +15.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 164])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 164 and x[1] == 1:
                if x[2] == 0:
                    return '+3.0'
                elif x[2] == 1:
                    return '+6.0'
                elif x[2] == 2:
                    return '+9.0'
                elif x[2] == 3:
                    return '+12.0'
                elif x[2] == 4:
                    return '+15.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_6(self):
        """
            Returns a string in db consisting of :

            +3.0, +6.0, +9.0, +12.0 or +15.0
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 165])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 165 and x[1] == 1:
                if x[2] == 0:
                    return '+3.0'
                elif x[2] == 1:
                    return '+6.0'
                elif x[2] == 2:
                    return '+9.0'
                elif x[2] == 3:
                    return '+12.0'
                elif x[2] == 4:
                    return '+15.0'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_gain_mode(self):
        """
            Returns a string consisting of :

            lin or sen
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 158])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 158 and x[1] == 1:
                if x[2] == 0:
                    return 'lin'
                elif x[2] == 1:
                    return 'sen'
                else:
                    raise Exception("Funcube response not recognised!!")
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_rc_filter(self):
        """
            Returns a string in MHz consisting of :

            21.4, 21.0, 17.6, 14.7, 12.4, 10.6, 9.0, 7.7, 6.4, 5.3, 4.4, 3.4, 2.6, 1.8, 1.2 or 1.0
        """
        rcfilter = ['21.4', '21.0', '17.6', '14.7', '12.4', '10.6', '9.0', '7.7', '6.4', '5.3', '4.4', '3.4', '2.6',
                    '1.8', '1.2', '1.0']
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 169])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 169 and x[1] == 1:
                return rcfilter[x[2]]
            else:
                raise Exception("Funcube response not recognised!!")

    def get_if_filter(self):
        """
            Returns a string in MHz consisting of :

            5.50, 5.30, 5.00, 4.80, 4.60, 4.40, 4.30, 4.10, 3.90, 3.80, 3.70, 3.60, 3.40, 3.30, 3.20, 3.10, 3.00
            2.95, 2.90, 2.80, 2.75, 2.70, 2.60, 2.55, 2.50, 2.45, 2.40, 2.30, 2.28, 2.24, 2.20, 2.15
        """

        _filter = ['5.50', '5.30', '5.00', '4.80', '4.60', '4.40', '4.30', '4.10', '3.90', '3.80', '3.70', '3.60',
                   '3.40', '3.30', '3.20', '3.10', '3.00', '2.95', '2.90', '2.80', '2.75', '2.70', '2.60', '2.55',
                   '2.50', '2.45', '2.40', '2.30', '2.28', '2.24', '2.20', '2.15']

        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 162])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 162 and x[1] == 1:
                return _filter[x[2]]
            else:
                raise Exception("Funcube response not recognised!!")

    def get_iq(self):
        """
            Returns phase correction followed by gain correction as tuple.
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 109])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 162 and x[1] == 1:
                rphase = x[2:4]
                rgain = x[4:6]

                phase = '{:.5f}'.format(struct.unpack('h', ''.join(rphase))[0] / 32768.0)
                gain = '{:.5f}'.format(struct.unpack('h', ''.join(rgain))[0] / 32768.0)

                return phase, gain
            else:
                raise Exception("Funcube response not recognised!!")

    def get_dc(self):
        """
            Returns I DC correction followed by Q DC correction
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 107])
            x = d.read(65)
            d.close()
        except IOError as e:
            raise Exception("IOError " + str(e))
        else:
            if x[0] == 162 and x[1] == 1:
                ri = x[2:4]
                rq = x[4:6]

                i = '{:.5f}'.format(struct.unpack('h', ''.join(ri))[0] / 32768.0)
                q = '{:.5f}'.format(struct.unpack('h', ''.join(rq))[0] / 32768.0)

                return i, q
            else:
                raise Exception("Funcube response not recognised!!")

    def get_mode(self):
        """
            gets the mode of the Funcube FCDAPP or FCDBL
        """
        pass

    def get_firmware_version(self):
        """
            Returns the current firmware version as a string.
        """
        try:
            d = hid.device(self.vendorid, self.productid)
            d.write([0, 1])
            xx = d.read(65)[2:16]
            verstring = []
            for i in xx:
                verstring.append(chr(i))  # Convert return data into chars and append to list

            charsv = ''.join(verstring)  # join the list together this will be in format of FCDAPP / FCDBL xx.xx B..
            ##  Next we need to create a new list from all the joined chars in version.
            version = charsv.split()
            d.close()
        except IOError as e:
            raise Exception("IOError" + str(e))
        else:
            return version[1]







