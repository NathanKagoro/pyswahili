import io
import unittest
from pyswahili.swahili_node import PySwahili


def translate(swahili_code):
    """Helper: translate a Swahili-Python snippet to English-Python."""
    node = PySwahili()
    node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
    sw_io = io.StringIO(swahili_code).readline
    tokens = node.create_english_tokens(sw_io)
    import tokenize
    return tokenize.untokenize(tokens)


class TestExistingKeywords(unittest.TestCase):
    def test_andika_translates_to_print(self):
        result = translate("andika('hello')")
        self.assertIn("print", result)

    def test_wakati_translates_to_while(self):
        result = translate("wakati x > 0:")
        self.assertIn("while", result)

    def test_ikiwa_translates_to_for(self):
        result = translate("ikiwa x imo orodha:")
        self.assertIn("for", result)
        self.assertIn("in", result)

    def test_kama_translates_to_if(self):
        result = translate("kama x == 1:")
        self.assertIn("if", result)


class TestMinBuiltin(unittest.TestCase):
    def test_ndogo_translates_to_min(self):
        result = translate("ndogo([3, 1, 2])")
        self.assertIn("min", result)

    def test_ndogo_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = ndogo([5, 2, 8, 1])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 1)


class TestMaxBuiltin(unittest.TestCase):
    def test_kubwa_translates_to_max(self):
        result = translate("kubwa([3, 1, 2])")
        self.assertIn("max", result)

    def test_kubwa_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = kubwa([5, 2, 8, 1])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 8)


class TestTypeBuiltin(unittest.TestCase):
    def test_aina_translates_to_type(self):
        result = translate("aina(x)")
        self.assertIn("type", result)

    def test_aina_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = aina(42)"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], int)


class TestEnumerateBuiltin(unittest.TestCase):
    def test_orodhesha_translates_to_enumerate(self):
        result = translate("orodhesha([1, 2, 3])")
        self.assertIn("enumerate", result)

    def test_orodhesha_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = list(orodhesha(['a', 'b', 'c']))"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], [(0, "a"), (1, "b"), (2, "c")])


class TestSumBuiltin(unittest.TestCase):
    def test_jumlisha_translates_to_sum(self):
        result = translate("jumlisha([1, 2, 3])")
        self.assertIn("sum", result)

    def test_jumlisha_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = jumlisha([1, 2, 3, 4])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 10)


class TestLenBuiltin(unittest.TestCase):
    def test_urefu_translates_to_len(self):
        result = translate("urefu([1, 2, 3])")
        self.assertIn("len", result)

    def test_urefu_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = urefu([1, 2, 3])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 3)


class TestZipBuiltin(unittest.TestCase):
    def test_unganisha_translates_to_zip(self):
        result = translate("unganisha([1, 2], [3, 4])")
        self.assertIn("zip", result)

    def test_unganisha_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = list(unganisha([1, 2], ['a', 'b']))"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], [(1, "a"), (2, "b")])


class TestSortedBuiltin(unittest.TestCase):
    def test_panga_translates_to_sorted(self):
        result = translate("panga([3, 1, 2])")
        self.assertIn("sorted", result)

    def test_panga_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = panga([3, 1, 2])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], [1, 2, 3])


class TestAnyBuiltin(unittest.TestCase):
    def test_yoyote_translates_to_any(self):
        result = translate("yoyote([True, False])")
        self.assertIn("any", result)

    def test_yoyote_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = yoyote([False, True, False])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertTrue(env["x"])


class TestAllBuiltin(unittest.TestCase):
    def test_yote_translates_to_all(self):
        result = translate("yote([True, True])")
        self.assertIn("all", result)

    def test_yote_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = yote([True, True, True])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertTrue(env["x"])


class TestAbsBuiltin(unittest.TestCase):
    def test_kamili_translates_to_abs(self):
        result = translate("kamili(-5)")
        self.assertIn("abs", result)

    def test_kamili_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = kamili(-7)"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 7)


class TestRoundBuiltin(unittest.TestCase):
    def test_karibia_translates_to_round(self):
        result = translate("karibia(3.7)")
        self.assertIn("round", result)

    def test_karibia_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = karibia(3.7)"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], 4)


class TestMapBuiltin(unittest.TestCase):
    def test_badilisha_translates_to_map(self):
        result = translate("badilisha(str, [1, 2, 3])")
        self.assertIn("map", result)

    def test_badilisha_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = list(badilisha(str, [1, 2, 3]))"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], ["1", "2", "3"])


class TestFilterBuiltin(unittest.TestCase):
    def test_chuja_translates_to_filter(self):
        result = translate("chuja(None, [0, 1, 2])")
        self.assertIn("filter", result)

    def test_chuja_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = list(chuja(None, [0, 1, 2, 0, 3]))"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], [1, 2, 3])


class TestReversedBuiltin(unittest.TestCase):
    def test_kinyume_translates_to_reversed(self):
        result = translate("kinyume([1, 2, 3])")
        self.assertIn("reversed", result)

    def test_kinyume_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = list(kinyume([1, 2, 3]))"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], [3, 2, 1])


class TestSetBuiltin(unittest.TestCase):
    def test_seti_translates_to_set(self):
        result = translate("seti([1, 2, 2])")
        self.assertIn("set", result)

    def test_seti_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = seti([1, 2, 2, 3])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], {1, 2, 3})


class TestTupleBuiltin(unittest.TestCase):
    def test_fungu_translates_to_tuple(self):
        result = translate("fungu([1, 2, 3])")
        self.assertIn("tuple", result)

    def test_fungu_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = fungu([1, 2, 3])"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertEqual(env["x"], (1, 2, 3))


class TestIsinstanceBuiltin(unittest.TestCase):
    def test_niaina_translates_to_isinstance(self):
        result = translate("niaina(x, int)")
        self.assertIn("isinstance", result)

    def test_niaina_execution(self):
        node = PySwahili()
        node.sw_to_en = __import__("pyswahili.sw_to_en", fromlist=["dictionary"]).dictionary
        code = "x = niaina(42, int)"
        english = node.convert_to_english(code)
        env = {}
        exec(english, env)
        self.assertTrue(env["x"])


if __name__ == "__main__":
    unittest.main()
