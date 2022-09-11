import pytest

class TestStr:
    @pytest.mark.parametrize("str_input,expected", [("VK", "vk"), ("Yandex", "yandex"), ("google", "google")])
    def test_str_lower(self, str_input, expected):
        assert str_input.lower() == expected
        
    def test_str_strip(self):
        test_input = "  samplemail@yandex.ru   "
        expected = "samplemail@yandex.ru"
        assert test_input.strip() == expected
        
    def test_str_join(self):
        test_input = ["Hello", "world", "!"]
        expected = "Hello world !"
        separator = " "
        assert separator.join(test_input) == expected
        

class TestSet:
    companies = {"vk", "yandex", "google", "ozon", "amazon"}
    
    def test_set_remove_negative(self):
        test_input = self.companies
        try:
            assert test_input.remove("1C")
        except KeyError:
            pass
    
    def test_set_intersect(self):
        test_input = self.companies
        rus_companies = {"vk", "yandex", "ozon", "1С"}
        expected = {"vk", "yandex", "ozon"}
        assert test_input.intersection(rus_companies) == expected
        
    def test_set_discard(self):
        test_input = self.companies
        expected = {"vk", "yandex", "google", "amazon"}
        test_input.discard("ozon")
        assert test_input == expected