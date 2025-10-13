# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(dict = ['apple', 'appla', 'applb', 'applc']) == True
    assert candidate(dict = ['hello', 'hallo', 'hxllo']) == True
    assert candidate(dict = ['aaaa', 'aaab', 'aaba', 'abaa']) == True
    assert candidate(dict = ['ab', 'cd', 'yz']) == False
    assert candidate(dict = ['abcd', 'abcf', 'abxg', 'abyh']) == True
    assert candidate(dict = ['aaaa', 'aaba', 'aaab', 'abaa']) == True
    assert candidate(dict = ['apple', 'apply', 'angle', 'ample']) == True
    assert candidate(dict = ['test', 'text', 'tast', 'telt']) == True
    assert candidate(dict = ['abcd', 'cccc', 'abyd', 'abab']) == True
    assert candidate(dict = ['apple', 'appla', 'appel', 'apples']) == True
    assert candidate(dict = ['abcd', 'acbd', 'aacd']) == True
    assert candidate(dict = ['kitten', 'sitten', 'bitten', 'bitton', 'bitted']) == True
    assert candidate(dict = ['abcde', 'fghij', 'klmno', 'pqrst']) == False
    assert candidate(dict = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa']) == True
    assert candidate(dict = ['test', 'text', 'tyst']) == True
    assert candidate(dict = ['apple', 'appla', 'appla']) == True
    assert candidate(dict = ['aaaa', 'abaa', 'acaa']) == True
    assert candidate(dict = ['hello', 'hallo', 'hxllo', 'hexlo']) == True
    assert candidate(dict = ['abcdefg', 'abcdeff', 'abcdegf', 'abcdehf', 'abcdeif', 'abcdejf', 'abcdekf', 'abcdelf', 'abcdelf', 'abcdelf', 'abcdelf', 'abcdelf']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghia', 'abcdefghib', 'abcdefghic']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefghi', 'abcdefgj', 'abcdefgi']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefga', 'abcdefgb', 'abcdefgc', 'abcdefgd', 'abcdefge', 'abcdefgf', 'abcdefgg', 'abcdefgh', 'abcdefgj', 'abcdefgk', 'abcdefgl', 'abcdefgm', 'abcdefgn', 'abcdefgo', 'abcdefgp', 'abcdefgq', 'abcdefgr', 'abcdefgs', 'abcdefgt', 'abcdefgu', 'abcdefgv', 'abcdefgw', 'abcdefgx', 'abcdefgy', 'abcdefgz']) == True
    assert candidate(dict = ['aabbcc', 'aabbbc', 'aabcbc', 'aabccc', 'aabccc', 'aabccc']) == True
    assert candidate(dict = ['aabbcc', 'aabbbc', 'aabccc', 'aabbcd', 'aabbcf', 'aabbdg', 'aabbch', 'aabbci', 'aabbcj', 'aabbbk', 'aabblm', 'aabbnm', 'aabbon', 'aabboq', 'aabbor', 'aabbos', 'aabbot', 'aabbpw', 'aabbpv', 'aabbur', 'aabbps', 'aabbut', 'aabpuu', 'aabpuv', 'aabpuw', 'aabpux', 'aabpuy', 'aabpuz']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == True
    assert candidate(dict = ['abcdef', 'abcfef', 'abcgef', 'abcghef', 'abchief']) == True
    assert candidate(dict = ['zxyabc', 'zxyabd', 'zxyabe', 'zxyac']) == True
    assert candidate(dict = ['xyzxyzxyz', 'xyzxyzxya', 'xyzxyzxyb', 'xyzxyzxyc']) == True
    assert candidate(dict = ['abcdefgh', 'abcdeghf', 'abcdehgf', 'abcdefhg']) == False
    assert candidate(dict = ['aabbccdd', 'aabbccde', 'aabbccdf', 'aabbccdg']) == True
    assert candidate(dict = ['abcdef', 'abcxef', 'abcxff', 'abcxfg']) == True
    assert candidate(dict = ['aaaaaaaa', 'aaaaaaab', 'aaaaaaac', 'aaaaaaad']) == True
    assert candidate(dict = ['abcdefghijk', 'abcdefghijl', 'abcdefghijm', 'abcdefghijn', 'abcdefghijo']) == True
    assert candidate(dict = ['abcdefg', 'abcdeff', 'abcdeef', 'abcdeeef']) == True
    assert candidate(dict = ['aaaaaaaaaaaa', 'aaaaaaaaabaa', 'aaaaaaaaacaa', 'aaaaaaaaadaa', 'aaaaaaaaaaaaa']) == True
    assert candidate(dict = ['zzzzzzzz', 'zzzzzzza', 'zzzzzzzb', 'zzzzzzzc']) == True
    assert candidate(dict = ['abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmno', 'abcdefghijklmnopr']) == True
    assert candidate(dict = ['abcdefghi', 'abcdefghj', 'abcdefghk', 'abcdefghl', 'abcdefghm']) == True
    assert candidate(dict = ['abcdef', 'abcdeg', 'abcdgf', 'abcdgh', 'abcdgi', 'abcdgj', 'abcdgk', 'abcdgl', 'abcdgm', 'abcdgn', 'abcdgo', 'abcdgp']) == True
    assert candidate(dict = ['abcdefghijk', 'abcdefghijl', 'abcdefghijm', 'abcdefghijn']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghif', 'abcdefghig', 'abcdefghih', 'abcdefghii', 'abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim', 'abcdefghin', 'abcdefghio', 'abcdefghip']) == True
    assert candidate(dict = ['different', 'differenr', 'differenx', 'differeny', 'differenz']) == True
    assert candidate(dict = ['mnopqr', 'mnopqs', 'mnopqt', 'mnopqu', 'mnopqv', 'mnopqw', 'mnopqx', 'mnopqy', 'mnopqz']) == True
    assert candidate(dict = ['algorithm', 'algorithn', 'algorithr', 'algoriths', 'algorithw']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim', 'abcdefghin', 'abcdefghio', 'abcdefghip', 'abcdefghiq', 'abcdefghir', 'abcdefghis', 'abcdefghit', 'abcdefghiu', 'abcdefghiv', 'abcdefghiw', 'abcdefghix', 'abcdefghiy', 'abcdefghiz']) == True
    assert candidate(dict = ['qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty']) == True
    assert candidate(dict = ['abcdefghijk', 'abcdefghijl', 'abcdefghijm', 'abcdefghijn', 'abcdefghijp']) == True
    assert candidate(dict = ['aabbcc', 'aabcbc', 'aaccbb', 'abcabc', 'abcbac']) == False
    assert candidate(dict = ['abcdefg', 'abcdegg', 'abcdhgg', 'abcdigg', 'abcdefh']) == True
    assert candidate(dict = ['abcdef', 'abcdeg', 'abcfeg', 'abcdex', 'abcdef', 'abcdfg']) == True
    assert candidate(dict = ['abcdefgh', 'abcdeghi', 'abcdefgj', 'abcdefgk']) == True
    assert candidate(dict = ['samechar', 'samechsr', 'samechars', 'samechart', 'samecharu']) == True
    assert candidate(dict = ['aaaaa', 'baaaa', 'caaaa', 'daaaa', 'eaaaa']) == True
    assert candidate(dict = ['banana', 'banana', 'banano', 'banana', 'banama']) == True
    assert candidate(dict = ['zzzzz', 'zyzzz', 'zzxzz', 'zzzvz', 'zzzzw']) == True
    assert candidate(dict = ['abcdefgh', 'abcdegfh', 'abcdefgi', 'abcdefghi']) == True
    assert candidate(dict = ['abcde', 'abfde', 'abcfe', 'abcdf', 'abced']) == True
    assert candidate(dict = ['qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuipo', 'qwertyuipl']) == True
    assert candidate(dict = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosi', 'pneumonoultramicroscopicsilicovolcanoconiose']) == True
    assert candidate(dict = ['abcabcabc', 'abcabcaba', 'abcabcaaa', 'abcabcaca']) == True
    assert candidate(dict = ['zzzzzzzz', 'zzzzzzzo', 'zzzzzzzp', 'zzzzzzzq']) == True
    assert candidate(dict = ['zzzzzzzz', 'zzzzzzzy', 'zzzzzzzx', 'zzzzzzzw']) == True
    assert candidate(dict = ['abcdefg', 'abcdegf', 'abcedgf', 'abcefgh', 'abcedgh', 'abcdehf', 'abcdegg', 'abcdegi', 'abcdega', 'abcdegb']) == True
    assert candidate(dict = ['aaaaaaaaaa', 'abaaaaaaaa', 'acaaaaaaaa', 'adaaaaaaaa', 'aeaaaaaaaa']) == True
    assert candidate(dict = ['abcdefgh', 'abcdegfh', 'abcdefgi', 'abcdefgj']) == True
    assert candidate(dict = ['same', 'sane', 'tame', 'same', 'came']) == True
    assert candidate(dict = ['abcdef', 'abcdefg', 'abcdefh', 'abcdefi']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == True
    assert candidate(dict = ['abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abcdefn', 'abcdefo', 'abcdefp']) == True
    assert candidate(dict = ['abcdef', 'abcdeg', 'abcdgf', 'abcdgh', 'abcdgi', 'abcdgj']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefga', 'abcdefgb', 'abcdefgc']) == True
    assert candidate(dict = ['monopoly', 'monopolq', 'monopols', 'monopolr']) == True
    assert candidate(dict = ['zzzzz', 'zzzza', 'zzzzb', 'zzzzc', 'zzzzd']) == True
    assert candidate(dict = ['abcdabcd', 'abcdabce', 'abcdabcd', 'abcdabcf']) == True
    assert candidate(dict = ['aaaaabaa', 'aaaaabab', 'aaaaabac', 'aaaaabad', 'aaaaabae']) == True
    assert candidate(dict = ['oneone', 'onetho', 'oneton', 'onetoo', 'oneoon']) == True
    assert candidate(dict = ['abcdefghijk', 'abcdefghijh', 'abcdefghijg', 'abcdefghijf', 'abcdefghijh', 'abcdefghiji', 'abcdefghijk', 'abcdefghijl', 'abcdefghijm', 'abcdefghijn', 'abcdefghijo', 'abcdefghijp']) == True
    assert candidate(dict = ['xyzxyz', 'xyzyzx', 'xyzxzy', 'xyzzyz']) == True
    assert candidate(dict = ['onetwothree', 'onetwothere', 'onetwothreee', 'onetwothreea']) == True
    assert candidate(dict = ['abcdefghijklmnop', 'abcdefghijklmo', 'abcdefghijklmn', 'abcdefghijklmp', 'abcdefghijklmnop', 'abcdefghijklmop', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnop', 'abcdefghijklmnop', 'abcdefghijklmnop', 'abcdefghijklmnop']) == True
    assert candidate(dict = ['abcdef', 'abcfed', 'bacdef', 'abcdef', 'acdefb']) == True
    assert candidate(dict = ['abcdefgh', 'abcfghij', 'abcdghij', 'abcdefhj', 'abcdefgi', 'abcdefghkj', 'abcdefghil', 'abcdefghim', 'abcdefghin', 'abcdefghio', 'abcdefghip', 'abcdefghiq', 'abcdefghir', 'abcdefghis', 'abcdefghit', 'abcdefghiu', 'abcdefghiv', 'abcdefghiw', 'abcdefghix', 'abcdefghiy', 'abcdefghiz']) == True
    assert candidate(dict = ['aabbccdd', 'aabbccde', 'aabbccee', 'aabbccff']) == True
    assert candidate(dict = ['qwertyui', 'qwertyuo', 'qwertyuiop', 'qwertyuipo']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim', 'abcdefghin']) == True
    assert candidate(dict = ['longstringwithcharacters', 'longstringwithcharacterts', 'longstringwithcharactery', 'longstringwithcharactert']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim']) == True
    assert candidate(dict = ['xyz', 'xyy', 'xxz', 'xzz']) == True
    assert candidate(dict = ['xylophone', 'xylophono', 'xylophane', 'xylophonee']) == True
    assert candidate(dict = ['abcdefgh', 'abcdehgh', 'abcdifgh', 'abcdihgh', 'abcdigfh', 'abcdiggh', 'abcdighh', 'abcdigfi', 'abcdigfh', 'abcdigfj']) == True
    assert candidate(dict = ['abcdefgh', 'abcdedgh', 'abcdfegh', 'abcdgegh', 'abcdefih']) == True
    assert candidate(dict = ['hello', 'hallo', 'hbllo', 'helio', 'hezlo']) == True
    assert candidate(dict = ['aabbccdd', 'aabbccde', 'aabbccdf', 'aabbccdg', 'aabbcdhe']) == True
    assert candidate(dict = ['aabbcc', 'aabbbc', 'aabccc', 'aabbcc']) == True
    assert candidate(dict = ['zzzzzz', 'zzzzzf', 'zzzzfg', 'zzzzgg', 'zzzzgh']) == True
    assert candidate(dict = ['aabbccdd', 'aabbccde', 'aabbcdee', 'aabbcdee']) == True
    assert candidate(dict = ['qwerty', 'qwertyu', 'qwertx', 'qwertv', 'qweryt']) == True
    assert candidate(dict = ['abcdefghijk', 'abcdefghijk', 'abcdefghijk', 'abcdefghijk']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefff', 'abcdeggg', 'abcdehhh']) == False
    assert candidate(dict = ['abcdef', 'axcdef', 'abcxef', 'abcdxf', 'abcdey', 'abdcxy', 'abedef', 'abcfef', 'abcgef', 'abcdgf', 'abcdeh', 'abcdei', 'abcdej', 'abcdek', 'abcdel', 'abcdem', 'abcden', 'abcdex', 'abcdex', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe', 'abcdfe']) == True
    assert candidate(dict = ['zzzzzz', 'zyzzzz', 'yxzzzz', 'xxzzzz', 'xwzzzz', 'xvzzzz', 'xuzzzz', 'xtzzzz', 'xzszzz', 'xzzzzz', 'xzzzzq', 'xzzzzr', 'xzzzzs', 'xzzzzt', 'xzzzzu', 'xzzzzv', 'xzzzzw', 'xzzzzx', 'xzzzzy', 'xzzzzz']) == True
    assert candidate(dict = ['aaaabbbb', 'aaaabbbc', 'aaaabbbd', 'aaaabbbe']) == True
    assert candidate(dict = ['abcdefg', 'abcdegf', 'abcefgd', 'abcgfed', 'abcdgef']) == False
    assert candidate(dict = ['abcdefgh', 'abcdeffg', 'abcdeggg', 'abcdefgg']) == True
    assert candidate(dict = ['xyzxyz', 'xyzyzx', 'xyzzxy', 'xyyxzz', 'xyxzzy']) == False
    assert candidate(dict = ['same', 'sane', 'scan', 'sack', 'seam']) == True
    assert candidate(dict = ['zzzzzzzzzz', 'zzzzzzzzza', 'zzzzzzzzzb', 'zzzzzzzzzc', 'zzzzzzzzzd', 'zzzzzzzzze', 'zzzzzzzzzf', 'zzzzzzzzzg', 'zzzzzzzzzh', 'zzzzzzzzzi', 'zzzzzzzzzj', 'zzzzzzzzzk', 'zzzzzzzzzl', 'zzzzzzzzzm', 'zzzzzzzzzn', 'zzzzzzzzzo', 'zzzzzzzzzp', 'zzzzzzzzqq', 'zzzzzzzzqr', 'zzzzzzzzqs', 'zzzzzzzzqt', 'zzzzzzzzqu', 'zzzzzzzzqv', 'zzzzzzzzqw', 'zzzzzzzzqx', 'zzzzzzzzqy', 'zzzzzzzzqz']) == True
    assert candidate(dict = ['abcdefghij', 'abcdefghjk', 'abcdefghil', 'abcdefghim', 'abcdefghin']) == True
    assert candidate(dict = ['abcdefgh', 'abcdefga', 'abcdefgb', 'abcdefghi']) == True
    assert candidate(dict = ['longstringhere', 'longstringhera', 'longstringherr', 'longstringhery']) == True
    assert candidate(dict = ['samestring', 'samesrting', 'samsstring', 'samstring', 'samestrinng']) == True
    assert candidate(dict = ['abcdef', 'abcefg', 'abcdgf', 'abcdhe', 'abcdif']) == True
    assert candidate(dict = ['zzzzzzzzzzzz', 'zzzzzzzzzzza', 'zzzzzzzzzzzb', 'zzzzzzzzzzzc', 'zzzzzzzzzzzd']) == True
    assert candidate(dict = ['quickbrownfoxjumpsoverthelazydog', 'quickbrownfoxjumpsoverthelazydgo', 'quickbrownfoxjumpsoverthelazydag']) == True
