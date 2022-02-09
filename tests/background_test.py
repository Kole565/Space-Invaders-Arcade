import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.environment.background import Background


class TestBackground(unittest.TestCase):

    def test_image_load(self):
        back = Background("./resource/image/static/test_back.png")
        
        self.assertTrue(back.surface)
    
    def test_image_load_fail(self):
        try:
            back = Background("./resource/image/static/miss.error")
        except:
            pass
        else:
            self.fail()
    
    # def test_image_safe_load(self):
    #     try:
    #         back = Background("./resource/image/static/miss.error")
    #     except:
    #         self.fail()
    #     else:
    #         pass

            