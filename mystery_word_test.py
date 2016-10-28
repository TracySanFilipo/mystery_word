from mystery_word import obtain_words_of_appropriate_difficulty

def test_easy_words():
    word_list = obtain_words_of_appropriate_difficulty("1")
    for word in word_list:
        assert 4 <= len(word) <=6

def test_normal_words():
    word_list = obtain_words_of_appropriate_difficulty("2")
    for word in word_list:
        assert 6 <= len(word) <=8

def test_hard_words():
    word_list = obtain_words_of_appropriate_difficulty("3")
    for word in word_list:
        assert len(word) >8

from mystery_word import check_for_complete_word

def test_comparison_False():
    assert check_for_complete_word(["c", "e", "l", "i", "o", "c", "y", "e", "s", "i", "s"], ["c", "e", "l", "i", "o", "s"]) == False

def test_comparison_True():
    assert check_for_complete_word(["f", "l", "a", "v", "o", "r"], ["r", "o", "v", "a", "l", "f"]) == None

def test_comparison_False2():
    assert check_for_complete_word(["d", "i", "h", "e", "r", "o", "n"], ["d", "i", "e", "o", "n"]) == False

def test_comparison_True2():
    assert check_for_complete_word(["f", "i", "n", "a", "n", "c", "i", "a", "l", "i", "s", "t"], ["a", "t", "i", "n", "s", "l", "f", "c"]) == None

def test_comparison_False3():
    assert check_for_complete_word(["k", "e", "r", "f", "l", "u", "m", "m", "o", "x"], ["l"]) == False

def test_comparison_True3():
    assert check_for_complete_word(["n", "u", "c", "l", "e", "o", "n", "e"], ["e", "u", "o", "n", "c", "l"]) == None

def test_comparison_False4():
    assert check_for_complete_word(["h", "a", "r", "d", "i", "l", "y"], ["a", "r", "i"]) == False

def test_comparison_True4():
    assert check_for_complete_word(["p", "y", "r", "i", "m", "i", "d", "y", "l"], ["i", "l", "m", "d", "p", "r", "y"]) == None
