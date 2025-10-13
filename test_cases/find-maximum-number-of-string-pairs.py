# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji']) == 5
    assert candidate(words = ['mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts']) == 4
    assert candidate(words = ['uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba']) == 4
    assert candidate(words = ['xy', 'yx', 'zw', 'wz', 'mn']) == 2
    assert candidate(words = ['xy', 'yx', 'za', 'az', 'bw', 'wb', 'cc']) == 3
    assert candidate(words = ['lm', 'ml', 'no', 'on', 'pq', 'qp', 'rs', 'sr']) == 4
    assert candidate(words = ['ef', 'fe', 'gh', 'hg', 'ij', 'ji']) == 3
    assert candidate(words = ['st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 4
    assert candidate(words = ['xy', 'yx', 'zz', 'zx', 'yx', 'xy']) == 4
    assert candidate(words = ['xy', 'yx', 'za', 'az', 'bw', 'wb']) == 3
    assert candidate(words = ['tu', 'ut', 'vw', 'wv', 'xy', 'yx', 'za', 'az']) == 4
    assert candidate(words = ['kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq']) == 4
    assert candidate(words = ['cd', 'ac', 'dc', 'ca', 'zz']) == 2
    assert candidate(words = ['de', 'ed', 'fg', 'gf', 'hi', 'ih', 'jk', 'kj']) == 4
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']) == 0
    assert candidate(words = ['aa', 'ab']) == 0
    assert candidate(words = ['mn', 'nm', 'op', 'po', 'qr', 'rq']) == 3
    assert candidate(words = ['xy', 'yx', 'za', 'az', 'bw', 'wb', 'cd', 'dc']) == 4
    assert candidate(words = ['ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk']) == 4
    assert candidate(words = ['qq', 'rr', 'ss', 'tt', 'uu']) == 0
    assert candidate(words = ['ab', 'ba', 'cc']) == 1
    assert candidate(words = ['qp', 'pq', 'rs', 'sr', 'tu', 'ut']) == 3
    assert candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz']) == 0
    assert candidate(words = ['xy', 'yx', 'zz', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2
    assert candidate(words = ['xy', 'yx', 'pq', 'qp', 'rs', 'sr', 'tu', 'ut', 'vw', 'wv', 'xy', 'yx', 'zz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 9
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgef', 'ijkl', 'lkji', 'mnop', 'ponm', 'qrst', 'tqrs', 'uvwx', 'xwvu', 'yzab', 'bazY']) == 4
    assert candidate(words = ['aabb', 'bbaa', 'ccdd', 'ddcc', 'eeff', 'ffee', 'gghh', 'hhgg', 'iijj', 'jjii', 'kkll', 'llkk', 'mmnn', 'nntt', 'oopp', 'ppoo', 'qqr', 'rqq', 'ss tt', 'ttss', 'uuvv', 'vvuu', 'wwxx', 'xxww', 'yyzz', 'zzyy', 'aacc', 'ccaa', 'ddeeff', 'ffeedd', 'gghhiijj', 'jjihhg', 'kkllmm', 'mmllkk', 'nnooppqq', 'qqpoonnn', 'rrssttuu', 'uuttsrrr', 'vvwwxx', 'xxwwvv', 'yyzzxx', 'xxzzyy']) == 16
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'h gef', 'ijkl', 'lkij', 'mnop', 'ponm', 'qrst', 't srq', 'uvwx', 'xwvu', 'yzxy', 'zyzx', 'abcd', 'dcba', 'efgh', 'h gef', 'ijkl', 'lkij', 'mnop', 'ponm', 'qrst', 't srq', 'uvwx', 'xwvu', 'yzxy', 'zyzx', 'mnop', 'ponm', 'qrst', 't srq', 'ijkl', 'lkij', 'efgh', 'h gef', 'abcd', 'dcba']) == 22
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'za', 'az', 'zb', 'bz', 'zc', 'cz', 'zd', 'dz', 'ze', 'ez', 'zf', 'fz', 'zg', 'gz', 'zh', 'hz', 'zi', 'iz', 'zj', 'jz', 'zk', 'kz', 'zl', 'lz', 'zm', 'mz', 'zn', 'nz', 'zo', 'oz', 'zp', 'pz', 'zq', 'qz', 'zr', 'rz', 'zs', 'sz', 'zt', 'tz', 'zu', 'uz', 'zv', 'vz', 'zw', 'wz', 'zx', 'xz', 'zy', 'yz']) == 25
    assert candidate(words = ['xy', 'yx', 'zz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2
    assert candidate(words = ['xy', 'yx', 'zw', 'wz', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk']) == 15
    assert candidate(words = ['xy', 'yx', 'zz', 'wz', 'zw', 'uv', 'vu', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'ab', 'ba', 'ef', 'fe']) == 16
    assert candidate(words = ['st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq']) == 13
    assert candidate(words = ['bc', 'cb', 'de', 'ed', 'fg', 'gf', 'hi', 'ih', 'jk', 'kj', 'lm', 'ml', 'no', 'on', 'pq', 'qp', 'rs', 'sr', 'tu', 'ut']) == 10
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'zzz', 'zzzz']) == 13
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgf', 'ijkl', 'lkji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvwx', 'xwvu', 'yzab', 'baz', 'mnop', 'ponm', 'qrst', 'tsrq', 'mnop', 'ponm', 'qrst', 'tsrq', 'mnop', 'ponm', 'qrst', 'tsrq', 'mnop', 'ponm', 'qrst', 'tsrq', 'mnop', 'ponm']) == 64
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgf', 'ijkl', 'lkji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvwx', 'xwvu', 'yzab', 'baz', 'mnop', 'ponm', 'qrst', 'tsrq', 'mnop', 'ponm']) == 16
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm']) == 7
    assert candidate(words = ['xy', 'yx', 'zv', 'vz', 'ws', 'sw', 'tr', 'rt', 'qu', 'uq', 'kp', 'pk', 'jo', 'oj', 'in', 'ni', 'mh', 'hm', 'lg', 'gl', 'kf', 'fk', 'je', 'ej', 'id', 'di', 'hc', 'ch', 'gb', 'bg', 'fa', 'af', 'xy', 'yx', 'zv', 'vz', 'ws', 'sw', 'tr', 'rt', 'qu', 'uq', 'kp', 'pk', 'jo', 'oj', 'in', 'ni', 'mh', 'hm', 'lg', 'gl', 'kf', 'fk', 'je', 'ej', 'id', 'di', 'hc', 'ch', 'gb', 'bg', 'fa', 'af']) == 64
    assert candidate(words = ['xy', 'yx', 'zx', 'xz', 'ay', 'ya', 'by', 'yb']) == 4
    assert candidate(words = ['qp', 'pq', 'rs', 'sr', 'tu', 'ut', 'vw', 'wv', 'xy', 'yx', 'za', 'az', 'by', 'yb', 'cx', 'xc', 'dl', 'ld', 'em', 'me', 'fn', 'nf', 'go', 'og', 'hp', 'ph', 'iq', 'qi', 'jr', 'rj', 'ks', 'sk', 'lt', 'tl', 'mu', 'um', 'nv', 'vn', 'ow', 'wo', 'px', 'xp', 'qy', 'yq', 'rz', 'zr', 'sa', 'as', 'tb', 'bt', 'uc', 'cu', 'vd', 'dv', 'we', 'ew', 'xf', 'fx', 'yg', 'gy', 'zh', 'hz']) == 31
    assert candidate(words = ['xy', 'yx', 'zxyx', 'xzzy', 'mn', 'nm', 'abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvwx', 'xwvu', 'yzab', 'bazy']) == 9
    assert candidate(words = ['ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc']) == 13
    assert candidate(words = ['ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm']) == 5
    assert candidate(words = ['aabb', 'bbaa', 'ccdd', 'ddcc', 'eefg', 'gfee', 'hhi j', 'jjih', 'kklm', 'mllk', 'nno p', 'p onn', 'qqrs', 'srqq', 'tuvw', 'xwvt', 'yzxy', 'yzzy', 'zzyz', 'xzyz', 'zyzx', 'zyzy', 'yxzx', 'zxxy', 'xyyx', 'yxyx', 'xyxy', 'yxxy', 'xyyx', 'yxyx', 'xyxy']) == 11
    assert candidate(words = ['zz', 'zz', 'zy', 'yz', 'zx', 'xz', 'zw', 'wz', 'za', 'az', 'zb', 'bz', 'zc', 'cz', 'zd', 'dz', 'ze', 'ez', 'zf', 'fz', 'zg', 'gz', 'zh', 'hz', 'zi', 'iz', 'zj', 'jz', 'zk', 'kz', 'zl', 'lz', 'zm', 'mz', 'zn', 'nz', 'zo', 'oz', 'zp', 'pz', 'zq', 'qz', 'zr', 'rz', 'zs', 'sz', 'zt', 'tz', 'zu', 'uz', 'zv', 'vz', 'zw', 'wz', 'zx', 'xz', 'zy', 'yz']) == 35
    assert candidate(words = ['xy', 'yx', 'zv', 'vz', 'ws', 'sw', 'tr', 'rt', 'qu', 'uq', 'kp', 'pk', 'jo', 'oj', 'in', 'ni', 'mh', 'hm', 'lg', 'gl', 'kf', 'fk', 'je', 'ej', 'id', 'di', 'hc', 'ch', 'gb', 'bg', 'fa', 'af']) == 16
    assert candidate(words = ['xyyx', 'yxxy', 'zwwz', 'wzzw', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvwx', 'xwvu', 'yz', 'zy', 'abcd', 'dcba', 'efgh', 'hgf', 'ijk', 'kij', 'lmn', 'nml', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm']) == 21
    assert candidate(words = ['ba', 'ab', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'zz', 'za', 'az', 'bz', 'zb', 'cz', 'zc', 'dz', 'zd']) == 17
    assert candidate(words = ['xy', 'yz', 'zx', 'wx', 'vu', 'ts', 'rq', 'po', 'nm', 'lk', 'ji', 'hg', 'fe', 'dc', 'ba', 'za', 'zb', 'zc', 'zd', 'ze', 'zf', 'zg', 'zh', 'zi', 'zj', 'zk', 'zl', 'zm', 'zn', 'zo', 'zp', 'zq', 'zr', 'zs', 'zt', 'zu', 'zv', 'zw', 'zx', 'zy', 'zz', 'az', 'bz', 'cz', 'dz', 'ez', 'fz', 'gz', 'hz', 'iz', 'jz', 'kz', 'lz', 'mz', 'nz', 'oz', 'pz', 'qz', 'rz', 'sz', 'tz', 'uz', 'vz', 'wz', 'xz', 'yy', 'xx', 'ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll', 'kk', 'jj', 'ii', 'hh', 'gg', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa']) == 26
    assert candidate(words = ['st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 25
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ac', 'ca', 'bd', 'db']) == 15
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'h gef', 'ijkl', 'lkij', 'mnop', 'ponm', 'qrst', 't srq', 'uvwx', 'xwvu', 'yzab', 'baz y', 'mnop', 'ponm', 'qrst', 't srq', 'ijkl', 'lkij', 'efgh', 'h gef', 'abcd', 'dcba']) == 9
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia', 'aj', 'ja', 'ak', 'ka', 'al', 'la', 'am', 'ma', 'an', 'na', 'ao', 'oa', 'ap', 'pa', 'aq', 'qa', 'ar', 'ra', 'as', 'sa', 'at', 'ta', 'au', 'ua', 'av', 'va', 'aw', 'wa', 'ax', 'xa', 'ay', 'ya', 'az', 'za']) == 25
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'xy', 'yx', 'zw', 'wz', 'mn', 'nm']) == 3
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 13
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 0
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 13
    assert candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz', 'za', 'zb', 'zc', 'zd', 'ze', 'zf', 'zg', 'zh', 'zi', 'zj', 'zk', 'zl', 'zm', 'zn', 'zo', 'zp', 'zq', 'zr', 'zs', 'zt', 'zu', 'zv', 'zw', 'zx', 'zy', 'zz', 'yx', 'wz', 'vz', 'uz', 'tz', 'sz', 'rz', 'qz', 'pz', 'oz', 'nz', 'mz', 'lz', 'kz', 'jz', 'iz', 'hz', 'gz', 'fz', 'ez', 'dz', 'cz', 'bz', 'az', 'ba', 'dc', 'fe', 'hg', 'ji', 'lk', 'nm', 'po', 'rq', 'st', 'vu', 'wx', 'yz']) == 35
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 52
    assert candidate(words = ['pq', 'qp', 'rs', 'sr', 'tu', 'ut', 'vw', 'wv', 'xy', 'yx', 'za', 'az']) == 6
    assert candidate(words = ['xy', 'yx', 'zw', 'wz', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy']) == 89
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji']) == 16
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia']) == 8
    assert candidate(words = ['abc', 'cba', 'bcd', 'dcb', 'cde', 'edc', 'def', 'fed', 'efg', 'gfe', 'fgh', 'hgf', 'ghi', 'ihg', 'hij', 'jih', 'ijk', 'kji', 'jkl', 'lkj', 'klm', 'mlk', 'lmn', 'nml', 'mno', 'onm', 'nop', 'pon', 'opq', 'qpo', 'pqr', 'rqp', 'qrs', 'srq', 'rst', 'tsr', 'stu', 'uts', 'tuv', 'vut', 'uvw', 'wvu', 'vwx', 'xwv', 'wxy', 'yxw', 'xyz', 'zyx']) == 24
