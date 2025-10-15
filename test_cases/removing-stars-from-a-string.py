def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z") == "abdeghjkmnpqstvwz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z") == "abdeghjkmnpqstvwz": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet**cod*e") == "lecoe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet**cod*e") == "lecoe": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab*cd*ef*gh*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*") == "aceg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab*cd*ef*gh*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*") == "aceg": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyza") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyza") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz") == "acegikmoqsuwyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz") == "acegikmoqsuwyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc***") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc***") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab*cd*ef*g*hi*j*") == "aceh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab*cd*ef*g*hi*j*") == "aceh": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "erase*****") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "erase*****") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd**efgh**ijkl**mnop**qrst**uvw**x**y**z") == "abefijmnqz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd**efgh**ijkl**mnop**qrst**uvw**x**y**z") == "abefijmnqz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd***eee***fffgggggghhhhiiiiijkkkkkllllmmmmnnnnoooo***pppppqqqqrrrrsssss") == "aaabbbcccfffgggggghhhhiiiiijkkkkkllllmmmmnnnnopppppqqqqrrrrsssss"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd***eee***fffgggggghhhhiiiiijkkkkkllllmmmmnnnnoooo***pppppqqqqrrrrsssss") == "aaabbbcccfffgggggghhhhiiiiijkkkkkllllmmmmnnnnopppppqqqqrrrrsssss": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde**fghij**klmno**pqrst**uvwxy**z") == "abcfghklmpqruvwz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde**fghij**klmno**pqrst**uvwxy**z") == "abcfghklmpqruvwz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuv*xyzwvutsrponmlkjihgfedcba*") == "abcdefghijklmnopqrstuxyzwvutsrponmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuv*xyzwvutsrponmlkjihgfedcba*") == "abcdefghijklmnopqrstuxyzwvutsrponmlkjihgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa*bbbbbb*cccccc*dddddd*eeeeee*ffffff*gggggg*hhhhhh*iiiiii*jjjjjj*kkkkkk*llllll*mmmmmm*nnnnnn*oooooo*pppppp*qqqqqq*rrrrrr*ssssss*tttttt*uuuuuu*vvvvvv*wwwwww*xxxxxx*yyyyyy*zzzzzz*") == "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooopppppqqqqqrrrrrssssstttttuuuuuvvvvvwwwwwxxxxxyyyyyzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa*bbbbbb*cccccc*dddddd*eeeeee*ffffff*gggggg*hhhhhh*iiiiii*jjjjjj*kkkkkk*llllll*mmmmmm*nnnnnn*oooooo*pppppp*qqqqqq*rrrrrr*ssssss*tttttt*uuuuuu*vvvvvv*wwwwww*xxxxxx*yyyyyy*zzzzzz*") == "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooopppppqqqqqrrrrrssssstttttuuuuuvvvvvwwwwwxxxxxyyyyyzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde*fghij*klmno*pqrst*uvwxy*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdfghiklmnpqrsuvwxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde*fghij*klmno*pqrst*uvwxy*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdfghiklmnpqrsuvwxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*yz*") == "abdeghjkmnpqstvwy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*yz*") == "abdeghjkmnpqstvwy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa*bbb*ccc*ddd*eee*fff*ggg*hhh*iii*jjj*kkk*lll*mmm*nnn*ooo*ppp*qqq*rrr*sss*ttt*uuu*vvv*www*xxx*yyy*zzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa*bbb*ccc*ddd*eee*fff*ggg*hhh*iii*jjj*kkk*lll*mmm*nnn*ooo*ppp*qqq*rrr*sss*ttt*uuu*vvv*www*xxx*yyy*zzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde*fg*hi*jkl*mno*pqr*stu*vwx*y*z*") == "abcdfhjkmnpqstvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde*fg*hi*jkl*mno*pqr*stu*vwx*y*z*") == "abcdfhjkmnpqstvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg***hhiijjkkllmmnn***oo***ppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz") == "aabbccddeeefffhhiijjkkllppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg***hhiijjkkllmmnn***oo***ppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz") == "aabbccddeeefffhhiijjkkllppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwx": {e}')
    
    total += 1
    try:
        result = candidate(s = "z*yz*zyxw*vyxwv*u*vwxy*ts*rq*ponm*ln*kj*i*hg*fed*cb*a*") == "yzyxvyxwvwxtrponlkhfec"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z*yz*zyxw*vyxwv*u*vwxy*ts*rq*ponm*ln*kj*i*hg*fed*cb*a*") == "yzyxvyxwvwxtrponlkhfec": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc***def**ghij***klmno**pqrstuv***wxyz") == "dgklmpqrswxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc***def**ghij***klmno**pqrstuv***wxyz") == "dgklmpqrswxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij*klmnopqrst*uvwxyz*zyxwvutsr*qp*on*m*l*k*j*i*h*g*f*e*d*c*b*a") == "abcdefghiklmnopqrsuvwxyzyxwvutsqoa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij*klmnopqrst*uvwxyz*zyxwvutsr*qp*on*m*l*k*j*i*h*g*f*e*d*c*b*a") == "abcdefghiklmnopqrsuvwxyzyxwvutsqoa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyz*") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyz*") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxy**z") == "abcdefghijklmnopqrstuvwz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxy**z") == "abcdefghijklmnopqrstuvwz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz") == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz") == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde*****fghij*****klmno*****pqrst*****uvwxy*****z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde*****fghij*****klmno*****pqrst*****uvwxy*****z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij***klmnopqrst***uvwxyz***abcd***efghij***klmno***pqrst***uvwxy***z") == "abcdefgklmnopquvwaefgklpquvz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij***klmnopqrst***uvwxyz***abcd***efghij***klmno***pqrst***uvwxy***z") == "abcdefgklmnopquvwaefgklpquvz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk***lmnopqrstuvwxyz**aaaaaaaaaabbbbbbbbbbccccccccccddddeeeeee****") == "abcdefghlmnopqrstuvwxaaaaaaaaaabbbbbbbbbbccccccccccddddee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk***lmnopqrstuvwxyz**aaaaaaaaaabbbbbbbbbbccccccccccddddeeeeee****") == "abcdefghlmnopqrstuvwxaaaaaaaaaabbbbbbbbbbccccccccccddddee": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd*efgh*ijkl*mnop*qrst*uvw*x*y*z*") == "abcefgijkmnoqrsuv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd*efgh*ijkl*mnop*qrst*uvw*x*y*z*") == "abcefgijkmnoqrsuv": {e}')
    
    total += 1
    try:
        result = candidate(s = "nested*stars*****in*string*example***") == "nesteistrinexam"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nested*stars*****in*string*example***") == "nesteistrinexam": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*bb*ccc*dddd*eeeee*ffffff*gggggg*hhhhhhh*iiiiiiii*jjjjjjjjj*kkkkkkkkk*llllllllll*mmmmmmmmmm*nnnnnnnnnnn*ooooooooooo*pppppppppppp*qqqqqqqqqqqqq*rrrrrrrrrrrrrr*sssssssssssssss*ttttttttttttttttt*uuuuuuuuuuuuuuuuuu*vvvvvvvvvvvvvvvvvvv*wwwwwwwwwwwwwwwwwwww*xxyyz**") == "bccdddeeeefffffggggghhhhhhiiiiiiijjjjjjjjkkkkkkkklllllllllmmmmmmmmmnnnnnnnnnnoooooooooopppppppppppqqqqqqqqqqqqrrrrrrrrrrrrrssssssssssssssttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwxxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*bb*ccc*dddd*eeeee*ffffff*gggggg*hhhhhhh*iiiiiiii*jjjjjjjjj*kkkkkkkkk*llllllllll*mmmmmmmmmm*nnnnnnnnnnn*ooooooooooo*pppppppppppp*qqqqqqqqqqqqq*rrrrrrrrrrrrrr*sssssssssssssss*ttttttttttttttttt*uuuuuuuuuuuuuuuuuu*vvvvvvvvvvvvvvvvvvv*wwwwwwwwwwwwwwwwwwww*xxyyz**") == "bccdddeeeefffffggggghhhhhhiiiiiiijjjjjjjjkkkkkkkklllllllllmmmmmmmmmnnnnnnnnnnoooooooooopppppppppppqqqqqqqqqqqqrrrrrrrrrrrrrssssssssssssssttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwxxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz*abcdefghijklmnopqrstuvwxyz*") == "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz*abcdefghijklmnopqrstuvwxyz*") == "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde*fg*hij*k*lmnop*qrs*tuvw*x*y*z*") == "abcdfhilmnoqrtuv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde*fg*hij*k*lmnop*qrs*tuvw*x*y*z*") == "abcdfhilmnoqrtuv": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi*jk*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z**") == "abcdefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi*jk*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z**") == "abcdefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x") == "x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x") == "x": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa*bbcc*ddcc*eeff*ffgg*hhiijj*kkll*mmnn*oopp*qqrr*sttuu*vwwxxyyzz*****") == "aabbabbcddceefffghhiijkklmmnoopqqrsttuvwwx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa*bbcc*ddcc*eeff*ffgg*hhiijj*kkll*mmnn*oopp*qqrr*sttuu*vwwxxyyzz*****") == "aabbabbcddceefffghhiijkklmmnoopqqrsttuvwwx": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc**def**ghi**jkl**mno**pqr**stu**vwx**yz**") == "adgjmpsv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc**def**ghi**jkl**mno**pqr**stu**vwx**yz**") == "adgjmpsv": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi***ipp*ss*m*i**") == "mississiip"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi***ipp*ss*m*i**") == "mississiip": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*bc*def*ghij*klmno*pqrst*uvwxy*z") == "bdeghiklmnpqrsuvwxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*bc*def*ghij*klmno*pqrst*uvwxy*z") == "bdeghiklmnpqrsuvwxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu*****vwxyz*****abcdefghi*****jklmno*****pqrst*****uvw*****xy*****z") == "mnopz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu*****vwxyz*****abcdefghi*****jklmno*****pqrst*****uvw*****xy*****z") == "mnopz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde*fgh*i*jklmno*pqrstu*v*wxyz*") == "abcdfgjklmnpqrstwxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde*fgh*i*jklmno*pqrstu*v*wxyz*") == "abcdfgjklmnpqrstwxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z**") == "abdeghjkmnpqstv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z**") == "abdeghjkmnpqstv": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxy**z*") == "abcdefghijklmnopqrstuvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxy**z*") == "abcdefghijklmnopqrstuvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "xy*z*ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz*") == "xacegikmoqsuwy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xy*z*ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz*") == "xacegikmoqsuwy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "python*is*awesome***so**is**java**") == "pythoiawesja"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python*is*awesome***so**is**java**") == "pythoiawesja": {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwith*various*characters*and*stars*through*out***") == "longstringwitvarioucharacteranstarthroug"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwith*various*characters*and*stars*through*out***") == "longstringwitvarioucharacteranstarthroug": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz*a**b**c**d**e**f**g**h**i**j**k**l**m**n**o**p**q**r**s**t**u**v**w**x**y**z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz*a**b**c**d**e**f**g**h**i**j**k**l**m**n**o**p**q**r**s**t**u**v**w**x**y**z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z") == "abdeghjkmnpqstvwz"
    assert candidate(s = "leet**cod*e") == "lecoe"
    assert candidate(s = "a*b*c*d*e*") == ""
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "ab*cd*ef*gh*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*") == "aceg"
    assert candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyza") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxyza"
    assert candidate(s = "abcdef") == "abcdef"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a") == "a"
    assert candidate(s = "ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz") == "acegikmoqsuwyz"
    assert candidate(s = "abcde") == "abcde"
    assert candidate(s = "abc***") == ""
    assert candidate(s = "ab*cd*ef*g*hi*j*") == "aceh"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
    assert candidate(s = "erase*****") == ""
    assert candidate(s = "abcd**efgh**ijkl**mnop**qrst**uvw**x**y**z") == "abefijmnqz"
    assert candidate(s = "aaabbbcccddd***eee***fffgggggghhhhiiiiijkkkkkllllmmmmnnnnoooo***pppppqqqqrrrrsssss") == "aaabbbcccfffgggggghhhhiiiiijkkkkkllllmmmmnnnnopppppqqqqrrrrsssss"
    assert candidate(s = "abcde**fghij**klmno**pqrst**uvwxy**z") == "abcfghklmpqruvwz"
    assert candidate(s = "abcdefghijklmnopqrstuv*xyzwvutsrponmlkjihgfedcba*") == "abcdefghijklmnopqrstuxyzwvutsrponmlkjihgfedcb"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
    assert candidate(s = "aaaaaa*bbbbbb*cccccc*dddddd*eeeeee*ffffff*gggggg*hhhhhh*iiiiii*jjjjjj*kkkkkk*llllll*mmmmmm*nnnnnn*oooooo*pppppp*qqqqqq*rrrrrr*ssssss*tttttt*uuuuuu*vvvvvv*wwwwww*xxxxxx*yyyyyy*zzzzzz*") == "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooopppppqqqqqrrrrrssssstttttuuuuuvvvvvwwwwwxxxxxyyyyyzzzzz"
    assert candidate(s = "abcde*fghij*klmno*pqrst*uvwxy*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdfghiklmnpqrsuvwxz"
    assert candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*yz*") == "abdeghjkmnpqstvwy"
    assert candidate(s = "aaa*bbb*ccc*ddd*eee*fff*ggg*hhh*iii*jjj*kkk*lll*mmm*nnn*ooo*ppp*qqq*rrr*sss*ttt*uuu*vvv*www*xxx*yyy*zzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "abcde*fg*hi*jkl*mno*pqr*stu*vwx*y*z*") == "abcdfhjkmnpqstvw"
    assert candidate(s = "aabbccddeeefffggg***hhiijjkkllmmnn***oo***ppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz") == "aabbccddeeefffhhiijjkkllppqqrrssttttuuuuuuuuuuvvvvvvvvwxyz"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwx"
    assert candidate(s = "z*yz*zyxw*vyxwv*u*vwxy*ts*rq*ponm*ln*kj*i*hg*fed*cb*a*") == "yzyxvyxwvwxtrponlkhfec"
    assert candidate(s = "abc***def**ghij***klmno**pqrstuv***wxyz") == "dgklmpqrswxyz"
    assert candidate(s = "abcdefghij*klmnopqrst*uvwxyz*zyxwvutsr*qp*on*m*l*k*j*i*h*g*f*e*d*c*b*a") == "abcdefghiklmnopqrsuvwxyzyxwvutsqoa"
    assert candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk*abcdefghijkl*abcdefghijklm*abcdefghijklmn*abcdefghijklmno*abcdefghijklmnop*abcdefghijklmnopq*abcdefghijklmnopqr*abcdefghijklmnopqrs*abcdefghijklmnopqrst*abcdefghijklmnopqrstu*abcdefghijklmnopqrstuv*abcdefghijklmnopqrstuvw*abcdefghijklmnopqrstuvwx*abcdefghijklmnopqrstuvwxy*abcdefghijklmnopqrstuvwxyz*") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijklabcdefghijklmabcdefghijklmnabcdefghijklmnoabcdefghijklmnopabcdefghijklmnopqabcdefghijklmnopqrabcdefghijklmnopqrsabcdefghijklmnopqrstabcdefghijklmnopqrstuabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwxabcdefghijklmnopqrstuvwxy"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz****") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxx"
    assert candidate(s = "abcdefghijklmnopqrstuvwxy**z") == "abcdefghijklmnopqrstuvwz"
    assert candidate(s = "xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz***xyz") == "xyz"
    assert candidate(s = "abcde*****fghij*****klmno*****pqrst*****uvwxy*****z") == "z"
    assert candidate(s = "abcdefghij***klmnopqrst***uvwxyz***abcd***efghij***klmno***pqrst***uvwxy***z") == "abcdefgklmnopquvwaefgklpquvz"
    assert candidate(s = "abcdefghijk***lmnopqrstuvwxyz**aaaaaaaaaabbbbbbbbbbccccccccccddddeeeeee****") == "abcdefghlmnopqrstuvwxaaaaaaaaaabbbbbbbbbbccccccccccddddee"
    assert candidate(s = "abcd*efgh*ijkl*mnop*qrst*uvw*x*y*z*") == "abcefgijkmnoqrsuv"
    assert candidate(s = "nested*stars*****in*string*example***") == "nesteistrinexam"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
    assert candidate(s = "a*bb*ccc*dddd*eeeee*ffffff*gggggg*hhhhhhh*iiiiiiii*jjjjjjjjj*kkkkkkkkk*llllllllll*mmmmmmmmmm*nnnnnnnnnnn*ooooooooooo*pppppppppppp*qqqqqqqqqqqqq*rrrrrrrrrrrrrr*sssssssssssssss*ttttttttttttttttt*uuuuuuuuuuuuuuuuuu*vvvvvvvvvvvvvvvvvvv*wwwwwwwwwwwwwwwwwwww*xxyyz**") == "bccdddeeeefffffggggghhhhhhiiiiiiijjjjjjjjkkkkkkkklllllllllmmmmmmmmmnnnnnnnnnnoooooooooopppppppppppqqqqqqqqqqqqrrrrrrrrrrrrrssssssssssssssttttttttttttttttuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwxxy"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz*abcdefghijklmnopqrstuvwxyz*") == "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy"
    assert candidate(s = "abcde*fg*hij*k*lmnop*qrs*tuvw*x*y*z*") == "abcdfhilmnoqrtuv"
    assert candidate(s = "abcdefghi*jk*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z**") == "abcdefgh"
    assert candidate(s = "x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x") == "x"
    assert candidate(s = "aabbaa*bbcc*ddcc*eeff*ffgg*hhiijj*kkll*mmnn*oopp*qqrr*sttuu*vwwxxyyzz*****") == "aabbabbcddceefffghhiijkklmmnoopqqrsttuvwwx"
    assert candidate(s = "abc**def**ghi**jkl**mno**pqr**stu**vwx**yz**") == "adgjmpsv"
    assert candidate(s = "mississippi***ipp*ss*m*i**") == "mississiip"
    assert candidate(s = "a*bc*def*ghij*klmno*pqrst*uvwxy*z") == "bdeghiklmnpqrsuvwxz"
    assert candidate(s = "mnopqrstu*****vwxyz*****abcdefghi*****jklmno*****pqrst*****uvw*****xy*****z") == "mnopz"
    assert candidate(s = "abcde*fgh*i*jklmno*pqrstu*v*wxyz*") == "abcdfgjklmnpqrstwxy"
    assert candidate(s = "abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z**") == "abdeghjkmnpqstv"
    assert candidate(s = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*") == ""
    assert candidate(s = "abcdefghijklmnopqrstuvwxy**z*") == "abcdefghijklmnopqrstuvw"
    assert candidate(s = "xy*z*ab*cd*ef*gh*ij*kl*mn*op*qr*st*uv*wx*yz*") == "xacegikmoqsuwy"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz*") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
    assert candidate(s = "python*is*awesome***so**is**java**") == "pythoiawesja"
    assert candidate(s = "longstringwith*various*characters*and*stars*through*out***") == "longstringwitvarioucharacteranstarthroug"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz*a**b**c**d**e**f**g**h**i**j**k**l**m**n**o**p**q**r**s**t**u**v**w**x**y**z") == "z"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z") == "z"
    assert candidate(s = "a*ab*abc*abcd*abcde*abcdef*abcdefg*abcdefgh*abcdefghi*abcdefghij*abcdefghijk") == "aababcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijk"
    assert candidate(s = "a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*abcdefghijklmnopqrstuvwxyz*zyxwvutsrqponmlkjihgfedcba*") == "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcb"


