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


if __name__ == "__main__":
    unittest.main()
