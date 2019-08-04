import os
import unittest
import math
from brlcad.primitives import Sketch

import brlcad.wdb as wdb


class SketchTestCase(unittest.TestCase):

    TEST_FILE_NAME = "test_sketch.g"

    DEBUG_TESTS = "DEBUG_TESTS"

    @classmethod
    def setUpClass(cls):
        # create the test DB:
        if os.path.isfile(cls.TEST_FILE_NAME):
            os.remove(cls.TEST_FILE_NAME)
        with wdb.WDB(cls.TEST_FILE_NAME, "BRL-CAD geometry for testing sketch primitive") as brl_db:
            brl_db.sketch("sketch.s")
        # load the DB and cache it in a class variable:
        cls.brl_db = wdb.WDB(cls.TEST_FILE_NAME)

    @classmethod
    def tearDownClass(cls):
        # close the test DB
        cls.brl_db.close()
        # delete the test DB except the DEBUG_TESTS environment variable is set
        if not os.environ.get(cls.DEBUG_TESTS, False):
            os.remove(cls.TEST_FILE_NAME)

    def test_default_sketch(self):
        sketch = Sketch("sketch.s")
        self.assertTrue(sketch.base.is_same((0, 0, 0)))
        self.assertTrue(sketch.u_vec.is_same((1, 0, 0)))
        self.assertTrue(sketch.v_vec.is_same((0, 1, 0)))
        self.assertEqual(0, len(sketch))
        self.assertEqual(0, len(sketch.vertices))

    def test_wdb_default_sketch(self):
        sketch = self.brl_db.lookup("sketch.s")
        self.assertTrue(sketch.base.is_same((0, 0, 0)))
        self.assertTrue(sketch.u_vec.is_same((1, 0, 0)))
        self.assertTrue(sketch.v_vec.is_same((0, 1, 0)))
        self.assertEqual(0, len(sketch))
        self.assertEqual(0, len(sketch.vertices))

    def test_example_sketch(self):
        sketch = Sketch("example.s", u_vec=(0, 1, 0), v_vec=(0, 0, 1))
        sketch.add_curve_segment(sketch.circle((0.5, 0), (0, 0)))
        sketch.add_curve_segment(sketch.line((-1, -1), (-1, 1)))
        sketch.add_curve_segment(sketch.line((-1, 1), (1, 1)))
        sketch.add_curve_segment(sketch.line((1, 1), (1, -1)))
        sketch.add_curve_segment(sketch.line((1, -1), (-1, -1)))
        sketch.add_curve_segment(
            sketch.bezier((
                (-2, 0), (-2, 6), (0, -4), (2, 6), (2, 0)
            ))
        )
        sketch.add_curve_segment(
            sketch.nurb(
                [(-2, 0), (-2, -3), (0, -1), (2, -3), (2, 0)],
                order=4,
                reverse=True
            ),
        )
        self.brl_db.save(sketch)
        result = self.brl_db.lookup(sketch.name)
        self.assertTrue(sketch.is_same(result))

    def test_extrude(self):
        sketch = Sketch("extrude_sketch.s")
        sketch.add_curve_segment(sketch.circle((0, 1), (0, 0)))
        self.brl_db.save(sketch)
        shape = sketch.extrude("extrude.s")
        self.brl_db.save(shape)
        result = self.brl_db.lookup(shape.name)
        self.assertTrue(shape.is_same(result))
        self.assertTrue(sketch.is_same(result.sketch))

    def test_revolve(self):
        sketch = Sketch(
            "revolve_sketch.s",
            # u_vec=(0, 1, 0), v_vec=(0, 0, 1)
        )
        sketch.add_curve_segment(
            sketch.line(
                start=(0.5, -1), end=(1, 0)
            ),
        )
        sketch.add_curve_segment(
            sketch.line(
                start=(1, 0), end=(0.5, 1)
            ),
        )
        sketch.add_curve_segment(
            sketch.arc(
                start=(0.5, 1), end=(1, 2), radius=0.7, center_is_left=True,
            )
        )
        self.brl_db.save(sketch)
        shape = sketch.revolve(
            "revolve.s", angle=2*math.pi, radius=(1, 0, 0), revolve_axis=(0, 1, 0), revolve_center=(0, 0, 0)
        )
        self.brl_db.save(shape)
        result = self.brl_db.lookup(shape.name)
        self.assertTrue(shape.is_same(result))
        self.assertTrue(sketch.is_same(result.sketch))

if __name__ == "__main__":
    unittest.main()
