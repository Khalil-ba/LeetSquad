# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(a = ['apple', 'apricot'],b = ['banana', 'berry']) == False
    assert candidate(a = ['cat', 'dog', 'elephant'],b = ['ant', 'bat', 'car']) == True
    assert candidate(a = ['dog'],b = ['cat', 'camel']) == True
    assert candidate(a = ['ant', 'antelope'],b = ['ant', 'anteater']) == True
    assert candidate(a = ['cat'],b = ['dog', 'dolphin']) == False
    assert candidate(a = ['apple', 'apricot', 'banana'],b = ['avocado', 'berry', 'blueberry']) == False
    assert candidate(a = ['hrvatska', 'zastava'],b = ['bijeli', 'galeb']) == True
    assert candidate(a = ['aardvark', 'albatross'],b = ['anteater', 'armadillo']) == False
    assert candidate(a = ['avokado', 'dabar'],b = ['brazil']) == False
    assert candidate(a = ['zebra'],b = ['yak', 'xenon']) == True
    assert candidate(a = ['apple', 'banana'],b = ['apricot', 'blueberry']) == False
    assert candidate(a = ['ananas', 'atlas', 'banana'],b = ['albatros', 'cikla', 'nogomet']) == True
    assert candidate(a = ['antelope', 'antenna'],b = ['ant', 'anteater', 'anemone']) == True
    assert candidate(a = ['apple', 'apricot', 'avocado'],b = ['banana', 'blueberry', 'blackberry']) == False
    assert candidate(a = ['feline', 'felix'],b = ['felidae', 'felinidae', 'felonia']) == False
    assert candidate(a = ['quail', 'quake', 'quack'],b = ['qua', 'quag', 'quagmire']) == True
    assert candidate(a = ['mango', 'melon', 'muskmelon', 'nectarine'],b = ['mangosteen', 'melonade', 'nectar', 'papaya']) == True
    assert candidate(a = ['meerkat', 'melon', 'melt'],b = ['meet', 'meal', 'mean']) == True
    assert candidate(a = ['narwhal', 'nail', 'name'],b = ['nail', 'nanny', 'nap']) == True
    assert candidate(a = ['apple', 'apricot', 'banana', 'blueberry'],b = ['avocado', 'berry', 'blackberry', 'bluegrass']) == False
    assert candidate(a = ['gorilla', 'giraffe', 'goat'],b = ['goose', 'gnome', 'gopher']) == True
    assert candidate(a = ['anaconda', 'anachronism', 'anagram'],b = ['anatomy', 'anaphylaxis', 'anatomist']) == False
    assert candidate(a = ['pelican', 'peak', 'peal'],b = ['pea', 'pear', 'peat']) == True
    assert candidate(a = ['apple', 'apricot', 'avocado'],b = ['apricot', 'avocado', 'banana', 'berry']) == False
    assert candidate(a = ['viper', 'vulture'],b = ['toucan', 'tuna', 'turtle', 'viper', 'vulture', 'walrus']) == False
    assert candidate(a = ['sloth', 'skunk', 'sparrow'],b = ['sloth', 'skunk', 'sparrow', 'squirrel']) == False
    assert candidate(a = ['cat', 'caterpillar', 'caterwaul'],b = ['canary', 'caterpillar', 'catfish']) == False
    assert candidate(a = ['jaguar', 'jackal', 'javelina'],b = ['jaguarundi', 'jackrabbit', 'jay']) == False
    assert candidate(a = ['ostrich', 'otter'],b = ['narwhal', 'octopus', 'orca', 'otter', 'owl']) == False
    assert candidate(a = ['baboon', 'baboonb', 'baboonc'],b = ['babood', 'babooe', 'babooe']) == True
    assert candidate(a = ['abc', 'abcd', 'abcde'],b = ['ab', 'abf', 'ac']) == False
    assert candidate(a = ['xenon', 'xerox', 'xylophone'],b = ['vulcan', 'wasp', 'wyrm', 'xenon', 'xerox', 'xylophone', 'yak', 'yam', 'yak']) == False
    assert candidate(a = ['zebra', 'zephyr'],b = ['yxion', 'yokel']) == True
    assert candidate(a = ['banana', 'bandanna', 'bandito'],b = ['bandanna', 'bandit', 'banjo']) == False
    assert candidate(a = ['umbrella', 'unicorn', 'urial'],b = ['umbrella', 'unicorn', 'urial', 'uakari']) == True
    assert candidate(a = ['blueberry', 'cherry', 'date'],b = ['banana', 'cantaloupe', 'dragonfruit']) == False
    assert candidate(a = ['apple', 'apricot', 'banana', 'blueberry'],b = ['avocado', 'berry', 'blackberry', 'bluefish']) == False
    assert candidate(a = ['antelope', 'antenna'],b = ['anemone', 'antelope', 'anteater']) == True
    assert candidate(a = ['antelope', 'ant', 'ape'],b = ['bat', 'bear', 'beetle']) == False
    assert candidate(a = ['iguana', 'impala', 'indri'],b = ['iguana', 'impala', 'ibis']) == True
    assert candidate(a = ['ant', 'antelope', 'antiquity'],b = ['aardvark', 'apricot', 'armadillo']) == False
    assert candidate(a = ['zebra', 'zest'],b = ['yak', 'yam']) == True
    assert candidate(a = ['antelope', 'antimony', 'antler'],b = ['antelope', 'antler', 'anvil']) == False
    assert candidate(a = ['aardvark', 'armadillo', 'antelope'],b = ['antiquity', 'ant', 'apricot']) == True
    assert candidate(a = ['panda', 'peacock', 'pelican'],b = ['ostrich', 'owl', 'panda', 'peacock', 'pelican', 'penguin', 'python', 'quail']) == False
    assert candidate(a = ['antelope', 'antiquity', 'armadillo', 'aardvark'],b = ['ant', 'apricot', 'avocado']) == False
    assert candidate(a = ['banana', 'blueberry', 'bluefish', 'boysenberry', 'cantaloupe'],b = ['apple', 'apricot', 'avocado', 'berry', 'blackberry']) == True
    assert candidate(a = ['zebra', 'yak', 'xylophone'],b = ['wolf', 'vulture', 'toucan']) == True
    assert candidate(a = ['a', 'b', 'c', 'd'],b = ['a', 'b', 'c', 'd', 'e', 'f']) == False
    assert candidate(a = ['ant', 'ape', 'arc', 'are', 'arm'],b = ['apt', 'arc', 'ard', 'art']) == False
    assert candidate(a = ['aaa', 'aaab', 'aaac'],b = ['aaad', 'aaae', 'aaaf']) == False
    assert candidate(a = ['xylophone', 'yacht', 'yak'],b = ['xylophone', 'xenon', 'xerox']) == True
    assert candidate(a = ['aaa', 'aaab', 'aaac'],b = ['aaaa', 'aab', 'aac']) == False
    assert candidate(a = ['antelope', 'antenna', 'antler'],b = ['ant', 'anteater', 'anemone']) == True
    assert candidate(a = ['turtle', 'turkey', 'toucan'],b = ['squirrel', 'tortoise', 'turkey', 'toucan', 'turtle', 'turtle', 'turtle']) == True
    assert candidate(a = ['azalea', 'azimuth'],b = ['axolotl', 'ayahuasca']) == True
    assert candidate(a = ['quail', 'quokka', 'quoll'],b = ['possum', 'quail', 'quokka', 'quoll', 'rabbit']) == False
    assert candidate(a = ['quail', 'quilt', 'quit'],b = ['quip', 'quipu', 'quipus']) == True
    assert candidate(a = ['cherry', 'citrus', 'cucumber'],b = ['berry', 'broccoli', 'cabbage', 'carrot', 'cucumber']) == False
    assert candidate(a = ['lemur', 'lemon', 'lens'],b = ['lem', 'len', 'level']) == False
    assert candidate(a = ['ananas', 'antelope', 'apricot', 'avocado'],b = ['albatross', 'anteater', 'armadillo', 'baboon', 'banana', 'babysitter']) == False
    assert candidate(a = ['kangaroo', 'kayak', 'karate'],b = ['kanal', 'kay', 'ka']) == True
    assert candidate(a = ['kiwi', 'kumquat', 'lemon', 'lime'],b = ['jackfruit', 'jujube', 'kiwi', 'kumquat', 'lemonade', 'limeade']) == False
    assert candidate(a = ['cat', 'cherry', 'citrus', 'coconut'],b = ['banana', 'berry', 'broccoli', 'cabbage', 'carrot']) == True
    assert candidate(a = ['quagga', 'quokka', 'quoll'],b = ['quagga', 'quokka', 'quoll', 'quetzal']) == True
    assert candidate(a = ['dolphin', 'dome', 'domino'],b = ['dog', 'dove', 'dragonfly']) == False
    assert candidate(a = ['panda', 'parrot', 'peacock'],b = ['panda', 'parrot', 'pelican']) == False
    assert candidate(a = ['raccoon', 'raven', 'reindeer'],b = ['raccoon', 'raven', 'reindeer', 'rhinoceros']) == False
    assert candidate(a = ['xylophone', 'yak', 'yam'],b = ['wombat', 'wolf', 'wombat', 'xenon', 'xylophone', 'yak', 'yam', 'yak', 'yak']) == True
    assert candidate(a = ['aardvark', 'aardwolf'],b = ['aalii', 'aaliyah']) == True
    assert candidate(a = ['cat', 'caterpillar', 'cathedral'],b = ['camel', 'car', 'canoe']) == True
    assert candidate(a = ['zebra', 'zoo'],b = ['yak', 'yeti', 'yodel']) == True
    assert candidate(a = ['abcd', 'abce', 'abcf'],b = ['abcc', 'abcg', 'abch']) == False
    assert candidate(a = ['flower', 'fowl', 'fox'],b = ['flour', 'frost', 'fog']) == False
    assert candidate(a = ['abacaxi', 'abacaxu', 'abacaxin', 'abacaxo'],b = ['abacax', 'abacaxos', 'abacaxi', 'abacaxio']) == True
    assert candidate(a = ['iguana', 'ice', 'iguana'],b = ['iceberg', 'ice cream', 'icy']) == True
    assert candidate(a = ['dog', 'dolphin', 'dragon'],b = ['dove', 'donkey', 'drake']) == False
    assert candidate(a = ['cat', 'caterpillar', 'catch'],b = ['car', 'cart', 'cash']) == True
    assert candidate(a = ['octopus', 'oak', 'oboe'],b = ['obe', 'obey', 'obeisance']) == True
    assert candidate(a = ['aaa', 'aab', 'aac', 'aad'],b = ['aba', 'abb', 'abc', 'abd']) == False
    assert candidate(a = ['narwhal', 'newt', 'nymph'],b = ['narwhal', 'newt', 'nyala']) == True
    assert candidate(a = ['apple', 'banana', 'cherry'],b = ['apricot', 'blueberry', 'grape']) == True
    assert candidate(a = ['apple', 'apricot', 'avocado'],b = ['apricot', 'banana', 'blueberry']) == False
    assert candidate(a = ['dog', 'dove', 'dragon'],b = ['dactyl', 'dandelion', 'darjeeling']) == True
    assert candidate(a = ['giraffe', 'gorilla', 'grizzly'],b = ['gibbon', 'gorilla', 'grizzly']) == True
    assert candidate(a = ['aardvark', 'ant', 'apricot'],b = ['antelope', 'antiquity', 'armadillo']) == False
    assert candidate(a = ['walrus', 'wasp', 'weasel'],b = ['vulture', 'wasp', 'weasel', 'whale', 'wolf', 'wombat']) == False
    assert candidate(a = ['apricot', 'avocado', 'banana'],b = ['ant', 'antelope', 'antiquity']) == True
    assert candidate(a = ['amor', 'amoroso', 'amour'],b = ['amor', 'amour', 'amour']) == False
    assert candidate(a = ['aardvark', 'aardwolf', 'aasvogel'],b = ['abacaxi', 'abalone', 'abraxas']) == False
    assert candidate(a = ['apple', 'apricot', 'avocado', 'banana', 'berry'],b = ['apex', 'banana', 'cherry', 'date']) == False
    assert candidate(a = ['zebra'],b = ['yak', 'yak', 'yak', 'yak', 'yak', 'yak', 'yak']) == True
    assert candidate(a = ['zebra', 'zucchini'],b = ['yak', 'yeti', 'yam']) == True
    assert candidate(a = ['cat', 'caterpillar', 'catering'],b = ['cab', 'car', 'cashmere']) == True
    assert candidate(a = ['bear', 'bee', 'beetle'],b = ['badger', 'bat', 'beaver']) == True
    assert candidate(a = ['aardwolf', 'aardvark', 'aardvarka'],b = ['aardvarkb', 'aardvarkc', 'aardvarkd']) == True
    assert candidate(a = ['lion', 'lynx', 'leopard'],b = ['tiger', 'tapir', 'tenrec']) == True
    assert candidate(a = ['cherry', 'cantaloupe'],b = ['cranberry', 'cucumber', 'citrus']) == False
    assert candidate(a = ['koala', 'kangaroo', 'kinkajou'],b = ['koala', 'kangaroo', 'kiwi']) == True
    assert candidate(a = ['llama', 'lemur', 'leopard'],b = ['llama', 'lemur', 'leopard', 'liger']) == True
    assert candidate(a = ['frog', 'fox', 'ferret'],b = ['giraffe', 'goat', 'gnu']) == False
    assert candidate(a = ['cat', 'cherry', 'coconut'],b = ['bear', 'bat', 'bird']) == True
    assert candidate(a = ['aardvark', 'aardwolf', 'albatross', 'alligator'],b = ['anteater', 'antelope', 'armadillo', 'baboon', 'badger']) == False
    assert candidate(a = ['fig', 'grape', 'grapefruit'],b = ['elderberry', 'ginkgo', 'guava', 'honeydew']) == False
    assert candidate(a = ['quince', 'raspberry', 'strawberry'],b = ['pomegranate', 'quincefruit', 'raspberrysauce', 'strawberryjello', 'tangerine']) == False
    assert candidate(a = ['dog', 'dolphin'],b = ['cat', 'cow', 'crane']) == True
    assert candidate(a = ['zebra'],b = ['yak', 'xylophone']) == True
    assert candidate(a = ['a', 'ab', 'abc'],b = ['a', 'ab', 'abc']) == True
    assert candidate(a = ['a', 'ab', 'abc'],b = ['ac', 'ad', 'ae']) == False
    assert candidate(a = ['antelope', 'antenna', 'antibody'],b = ['amino', 'and', 'angle', 'ankle']) == True
    assert candidate(a = ['aardvark', 'albatross', 'antelope'],b = ['baboon', 'badger', 'bat']) == False
    assert candidate(a = ['xyz', 'xyza', 'xyzab'],b = ['xyzabc', 'xyzabcd', 'xyzabcde']) == False
    assert candidate(a = ['cherry', 'coconut', 'cranberry'],b = ['blueberry', 'boysenberry', 'cantaloupe', 'chardonnay', 'clementine']) == True
    assert candidate(a = ['toucan', 'tapir', 'tarantula'],b = ['toucan', 'tapir', 'tarantula', 'tarsier']) == True
    assert candidate(a = ['antelope', 'antiquity', 'armadillo'],b = ['ant', 'apricot', 'avocado']) == False
    assert candidate(a = ['giraffe', 'goat', 'gorilla'],b = ['elephant', 'emu', 'flamingo', 'frog', 'goat', 'gorilla']) == True
    assert candidate(a = ['panda', 'panther', 'parrot'],b = ['monkey', 'meerkat', 'marmot']) == True
    assert candidate(a = ['antelope', 'apricot', 'armadillo'],b = ['aardvark', 'ant', 'antiquity']) == True
    assert candidate(a = ['aardvark', 'albatross', 'antelope', 'anteater'],b = ['aardwolf', 'alpaca', 'ant', 'armadillo']) == False
    assert candidate(a = ['grape', 'grapefruit', 'grapevine'],b = ['green', 'grey', 'grew']) == False
    assert candidate(a = ['aardvark', 'apricot', 'antiquity'],b = ['ant', 'armadillo', 'antelope']) == False
    assert candidate(a = ['jackal', 'jaguar', 'jail'],b = ['jack', 'jar', 'jaw']) == False
    assert candidate(a = ['umbrella', 'violet', 'wheat', 'xylophone', 'yellow', 'zebra'],b = ['underground', 'ufo', 'violetflower', 'watermelon', 'xylophonebox', 'yellowstone', 'zebracrossing']) == False
    assert candidate(a = ['antelope', 'ant', 'anaconda'],b = ['antelope', 'anvil', 'aphid']) == False
    assert candidate(a = ['banana', 'bandana', 'bandwidth'],b = ['bamboo', 'bandicoot', 'bandanna']) == True
    assert candidate(a = ['zebra', 'zoo'],b = ['xylophone', 'xenon', 'xylography']) == True
    assert candidate(a = ['zebra', 'zoo'],b = ['yak', 'yx', 'yw']) == True
    assert candidate(a = ['aardvark', 'albatross', 'antelope'],b = ['aardwolf', 'alpaca', 'ant']) == True
    assert candidate(a = ['aardvark', 'aardwolf', 'albatross'],b = ['aardvark', 'albatross', 'antelope']) == False
    assert candidate(a = ['aaa', 'aab', 'aac'],b = ['aaaa', 'aaab', 'aaac']) == True
    assert candidate(a = ['banana', 'blueberry', 'cherry'],b = ['apple', 'apricot', 'avocado']) == True
    assert candidate(a = ['antelope', 'antiquity', 'armadillo'],b = ['aardvark', 'ant', 'apricot']) == True
    assert candidate(a = ['dog', 'dolphin', 'donkey'],b = ['cat', 'chimpanzee', 'cow', 'crab', 'crocodile', 'crow', 'deer']) == True
    assert candidate(a = ['melon', 'mango', 'mule'],b = ['lemon', 'lichen', 'mango', 'melon', 'mule', 'muskrat']) == False
    assert candidate(a = ['iguana', 'iguanaa', 'iguanaaa'],b = ['iguanaaaaa', 'iguanaaaaaa', 'iguanaaaaaaaaa']) == False
    assert candidate(a = ['elephant', 'elbow', 'elk'],b = ['eagle', 'earth', 'egg']) == True
    assert candidate(a = ['giraffe', 'gorilla', 'guinea'],b = ['grape', 'grapefruit', 'grapevine']) == True
    assert candidate(a = ['mule', 'mongoose', 'meerkat'],b = ['mule', 'mongoose', 'marmot']) == True
    assert candidate(a = ['kiwi', 'kangaroo'],b = ['jaguar', 'jellyfish', 'kangaroo', 'koala']) == False
    assert candidate(a = ['abcd', 'abce', 'abcf'],b = ['abcd', 'abce', 'abcf', 'abcdg']) == True
    assert candidate(a = ['apple', 'apricot', 'banana', 'blueberry'],b = ['avocado', 'banana', 'blackberry', 'blueberry']) == True
    assert candidate(a = ['zebra'],b = ['yak', 'xenon', 'wombat']) == True
    assert candidate(a = ['elephant', 'emu', 'eagle'],b = ['dog', 'dolphin', 'deer']) == True
    assert candidate(a = ['cat', 'dog', 'elephant'],b = ['catfish', 'dogwood', 'elephantine']) == False
    assert candidate(a = ['antelope', 'ape', 'apricot'],b = ['ant', 'antler', 'anvil', 'ape', 'apricot', 'aquarium']) == False
    assert candidate(a = ['banana', 'berry', 'blueberry'],b = ['banana', 'berry', 'blueberry', 'blackberry']) == True
    assert candidate(a = ['apple', 'banana', 'cherry', 'date', 'elderberry'],b = ['apricot', 'blueberry', 'cranberry', 'fig', 'grape']) == True
    assert candidate(a = ['zebra', 'zoo'],b = ['yak', 'yxion']) == True
    assert candidate(a = ['ant', 'bear', 'cat'],b = ['ape', 'bat', 'canine']) == True
    assert candidate(a = ['aardvark', 'apple', 'apricot', 'avocado', 'banana', 'blueberry', 'blackberry', 'carrot'],b = ['aardwolf', 'albatross', 'ant', 'antelope', 'apricot', 'avocado', 'banana', 'blackberry', 'blueberry']) == True
    assert candidate(a = ['ocelot', 'orangutan', 'opossum'],b = ['ocelot', 'orangutan', 'ostrich']) == False
    assert candidate(a = ['orange', 'papaya', 'peach', 'pear'],b = ['orangeade', 'papayafruit', 'peachtree', 'pearfruit', 'plum']) == False
    assert candidate(a = ['heron', 'herb', 'hemlock'],b = ['hen', 'heap', 'heal']) == True
