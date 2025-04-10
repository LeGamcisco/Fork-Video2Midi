import tempfile
import unittest

from video2midi.prefs import prefs
from video2midi.settings import *


class TestMySettings(unittest.TestCase):

	def test_a_settings_load(self) -> None:
		self.assertEqual(prefs.xoffset_whitekeys, 60)
		loadsettings('./tests/spin.mp4.ini')
		self.assertEqual(prefs.xoffset_whitekeys, 99)

	def test_b_persist_octave(self) -> None:
		ini = tempfile.NamedTemporaryFile(suffix='.ini').name
		prefs.octave = 2
		savesettings(ini)
		prefs.octave = 3
		loadsettings(ini)
		self.assertEqual(prefs.octave, 2)

	def test_c_compatible_size(self) -> None:
		loadsettings('./tests/spin.mp4.ini')
		self.assertEqual(len(prefs.keyp_colors_channel_prog),14);

		colorBtns = []
		for i in range(22):
			colorBtns.append( [0,0,0] )

		compatibleColors(colorBtns)
		self.assertEqual(len(prefs.keyp_colors_channel_prog),22);

if __name__ == '__main__':
	unittest.main()
