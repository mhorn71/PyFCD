# PyFCD
Python FCD Interface.

For testing.

class PyFcdCtrl(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |
 |      All Errors raise Exception
 |
 |  defaults(self)
 |      Sets the following default parameters:
 |
 |      Frequency : 144430000   (GB3VHF 2m Beacon)
 |      ppm : -120
 |      LNA Gain : +12.5db
 |      Mixer Gain : +12.0db
 |      RF Filter : 268MHz LPF
 |      Mixer Filter : 1.9MHz
 |      IF RC Filter : 1.0MHz
 |      IF Filter : 2.15MHz
 |      IF Gain 1 : +6db
 |      IF Gain 2 : 0db
 |      IF Gain 3 : 0db
 |      IF Gain 4 : 0db
 |      IF Gain 5 : +3db
 |      IF Gain 6 : +3db
 |      LNA Enhance : OFF
 |      Band : VHF II
 |      Bias Current : II V/U band
 |      IF Gain Mode : Linearity
 |      PLL Lock : True
 |      DC I : 0.00000
 |      DC Q : 0.00000
 |      Gain : 1.00000
 |      Phase: 0.00000
 |
 |  firmware(self, mode)
 |      Upload or Verify Firmware
 |
 |      TO BE WRITTEN ONCE I UNDERSTAND HOW TO. :-)
 |
 |  get_band(self)
 |      Returns a string consisting of:
 |
 |      VHF2, VHF3, UHF, LBAND
 |
 |  get_bias_current(self)
 |      Returns a string consisting of:
 |
 |      LBAND, 01, 10, VUBAND
 |
 |  get_bootloader_query(self)
 |      Returns the bootload query string.
 |
 |      'FCDAPP 18.10 Brd 1.0 No blk' or 'FCDBL'
 |
 |  get_dc(self)
 |      Returns DC I correction followed by DC Q correction as float tuple.
 |
 |  get_firmware_version(self)
 |      Returns the current firmware version as a string.
 |
 |  get_hz(self)
 |      Returns current set frequency in Hz as reported by the Funcube, if no frequency is found None is returned.
 |
 |  get_if_filter(self)
 |      Returns a string in MHz consisting of :
 |
 |      5.50, 5.30, 5.00, 4.80, 4.60, 4.40, 4.30, 4.10, 3.90, 3.80, 3.70, 3.60, 3.40, 3.30, 3.20, 3.10, 3.00
 |      2.95, 2.90, 2.80, 2.75, 2.70, 2.60, 2.55, 2.50, 2.45, 2.40, 2.30, 2.28, 2.24, 2.20, 2.15
 |
 |  get_if_gain_1(self)
 |      Returns a string in db consisting of :
 |
 |      -3.0 or +6.0
 |
 |  get_if_gain_2(self)
 |      Returns a string in db consisting of :
 |
 |      +0.0, +3.0, +6.0 or +9.0
 |
 |  get_if_gain_3(self)
 |      Returns a string in db consisting of :
 |
 |      +0.0, +3.0, +6.0 or +9.0
 |
 |  get_if_gain_4(self)
 |      Returns a string in db consisting of :
 |
 |      +0.0, +1.0 or +2.0
 |
 |  get_if_gain_5(self)
 |      Returns a string in db consisting of :
 |
 |      +3.0, +6.0, +9.0, +12.0 or +15.0
 |
 |  get_if_gain_6(self)
 |      Returns a string in db consisting of :
 |
 |      +3.0, +6.0, +9.0, +12.0 or +15.0
 |
 |  get_if_gain_mode(self)
 |      Returns a string consisting of :
 |
 |      lin or sen
 |
 |  get_if_rc_filter(self)
 |      Returns a string in MHz consisting of :
 |
 |      21.4, 21.0, 17.6, 14.7, 12.4, 10.6, 9.0, 7.7, 6.4, 5.3, 4.4, 3.4, 2.6, 1.8, 1.2 or 1.0
 |
 |  get_iq(self)
 |      Returns phase correction followed by gain correction as tuple.
 |
 |  get_lna_enhance(self)
 |      Returns a string consisting of :
 |
 |      OFF, 0, 1, 2, 3
 |
 |  get_lna_gain(self)
 |      Returns a string consisting of :
 |
 |      -5.0, -2.5, +0.0, +2.5, +5.0, +7.5, +10.0, +12.5, + 15.0, +17.5, +20.0, +25.00, +30
 |
 |  get_mixer_filter(self)
 |      Returns a string in MHz consisting of :
 |
 |      27.0, 4.6, 4.2, 3.8, 3.4, 3.0, 2.7, 2.3 or 1.9
 |
 |  get_mixer_gain(self)
 |      Returns a string in db consisting of :
 |
 |      +4.0 or +12.0
 |
 |  get_mode(self)
 |      Returns the current mode as FCDAPP or FCDBL
 |
 |  get_pll(self)
 |      Returns True if locked and False if unlocked.
 |
 |  get_rf_filter(self)
 |      Returns a string consisting of :
 |
 |      (Band 0, VHF II) - LPF268MHz, LPF299MHz
 |
 |      (Band 1, VHF III) - LPF509MHz, LPF656MHz
 |
 |      (Band 2, UHF) - BPF360MHz, BPF380MHz, BPF405MHz, BPF425MHz, BPF450MHz, BPF475MHz, BPF505MHz, BPF540MHz
 |         BPF575MHz, BPF615MHz, BPF670MHz, BPF720MHz, BPF760MHz, BPF840MHz, BPF890MHz, BPF970MHz
 |
 |      (Band 3, L Band) - BPF1300MHz, BPF1320MHz, BPF1360MHz, BPF1410MHz, BPF1445MHz, BPF1460MHz, BPF1490MHz
 |         BPF1530MHz, BPF1560MHz, BPF1590MHz, BPF1640MHz, BPF1660MHz, BPF1680MHz, BPF1700MHz, BPF1720MHz, BPF1750MHz.
 |
 |  get_rssi(self)
 |      Returns an int -35dBm ~=0, -10dBm ~=70.
 |
 |  set_band(self, band)
 |      Where band is a string consisting of:
 |
 |      VHF2, VHF3, UHF, LBAND
 |
 |      returns True or False
 |
 |  set_bias_current(self, bias)
 |      Where bias is a string consisting of:
 |
 |      LBAND, 01, 10, VUBAND
 |
 |      returns True or False
 |
 |  set_dc(self, i, q)
 |      Where i and q are floats.
 |
 |      returns True or False
 |
 |  set_hz(self, freq, ppm_offset)
 |      set_hz(int(frequency), int(ppm_offset))
 |
 |      returns True or False
 |
 |      NOTE: There is no checking of whether or not the frequency being set is within range of the device.
 |
 |  set_if_filter(self, if_filter)
 |      Where if_filter is a string consisting of:
 |
 |      5.50, 5.30, 5.00, 4.80, 4.60, 4.40, 4.30, 4.10, 3.90, 3.80, 3.70, 3.60, 3.40, 3.30, 3.20, 3.10, 3.00
 |      2.95, 2.90, 2.80, 2.75, 2.70, 2.60, 2.55, 2.50, 2.45, 2.40, 2.30, 2.28, 2.24, 2.20, 2.15
 |
 |      returns True or False
 |
 |  set_if_gain_1(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      -3.0 or +6.0
 |
 |      returns True of False
 |
 |  set_if_gain_2(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      +0.0, +3.0, +6.0 or +9.0
 |
 |      returns True of False
 |
 |  set_if_gain_3(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      +0.0, +3.0, +6.0 or +9.0
 |
 |      returns True of False
 |
 |  set_if_gain_4(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      +0.0, +1.0 or +2.0
 |
 |      returns True of False
 |
 |  set_if_gain_5(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      +3.0, +6.0, +9.0, +12.0 or +15.0
 |
 |      returns True of False
 |
 |  set_if_gain_6(self, gain)
 |      Where gain in db is a string consisting of :
 |
 |      +3.0, +6.0, +9.0, +12.0 or +15.0
 |
 |      returns True of False
 |
 |  set_if_gain_mode(self, gainmode)
 |      Where gainmode is a string consisting of :
 |
 |      lin or sen
 |
 |      returns True or False
 |
 |  set_if_rc_filter(self, if_rc_filter)
 |      Where if_rc_filter in MHz is a string consisting of :
 |
 |      21.4, 21.0, 17.6, 14.7, 12.4, 10.6, 9.0, 7.7, 6.4, 5.3, 4.4, 3.4, 2.6, 1.8, 1.2 or 1.0
 |
 |      returns True or False
 |
 |  set_iq(self, phase, gain)
 |      Where phase and gain are floats.
 |
 |      returns True or False
 |
 |  set_khz(self, freq, ppm_offset)
 |      set_khz(int(frequency), int(ppm_offset))
 |
 |      returns True or False
 |
 |      NOTE: There is no checking of whether or not the frequency being set is within range of the device.
 |
 |  set_lna_enhance(self, lna_enhance)
 |      Where lna_enhance is a string consisting of :
 |
 |      OFF, 0, 1, 2, 3
 |
 |      returns True or False
 |
 |  set_lna_gain(self, lna_gain)
 |      Where lna_gain is a string consisting of :
 |
 |      -5.0, -2.5, +0.0, +2.5, +5.0, +7.5, +10.0, +12.5, + 15.0, +17.5, +20.0, +25.00, +30
 |
 |      returns True or False
 |
 |  set_mixer_filter(self, mixer_filter)
 |      Where mixer_filter in MHz is a string consisting of :
 |
 |      27.0, 4.6, 4.2, 3.8, 3.4, 3.0, 2.7, 2.3 or 1.9
 |
 |      returns True or False
 |
 |  set_mixer_gain(self, mixer_gain)
 |      Where mixer_gain in db is a string consisting of :
 |
 |      +4.0 or +12.0
 |
 |      returns True of False
 |
 |  set_mode(self, mode)
 |      Where mode is a string consisting of :
 |
 |      FCDAPP (Application) or FCDBL (Bootloader)
 |
 |      returns True or False
 |
 |  set_rf_filter(self, rf_filter)
 |      Where rf_filter is a string consisting for:
 |
 |      (Band 0, VHF II) - LPF268MHz, LPF299MHz
 |
 |      (Band 1, VHF III) - LPF509MHz, LPF656MHz
 |
 |      (Band 2, UHF) - BPF360MHz, BPF380MHz, BPF405MHz, BPF425MHz, BPF450MHz, BPF475MHz, BPF505MHz, BPF540MHz
 |         BPF575MHz, BPF615MHz, BPF670MHz, BPF720MHz, BPF760MHz, BPF840MHz, BPF890MHz, BPF970MHz
 |
 |      (Band 3, L Band) - BPF1300MHz, BPF1320MHz, BPF1360MHz, BPF1410MHz, BPF1445MHz, BPF1460MHz, BPF1490MHz
 |         BPF1530MHz, BPF1560MHz, BPF1590MHz, BPF1640MHz, BPF1660MHz, BPF1680MHz, BPF1700MHz, BPF1720MHz, BPF1750MHz
 |
 |      set_rf_filter('BPF360MHz')
 |
 |      returns True or False
 |
 |      Wrong Band to RF Filter match raises Exception.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
