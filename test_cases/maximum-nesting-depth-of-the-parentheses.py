def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(1+(2*3)+((8)/4))+1") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*3)+((8)/4))+1") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*c)+((d/e)+f))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*c)+((d/e)+f))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+b)+((c*d)+e)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+b)+((c*d)+e)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+2)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+2)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1+(2*3)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1+(2*3)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(())") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+3)*(2-4))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+3)*(2-4))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((())()())") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((())()())") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+2)*3/(4-5))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+2)*3/(4-5))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1)+((2))+(((3)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1)+((2))+(((3)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "()(())((()()))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()(())((()()))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "()") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+b+c)*(d/e/f)+((g-(h*i))+j)") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+b+c)*(d/e/f)+((g-(h*i))+j)") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((()))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((()))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)*c)+(((d+e)*f)+g)") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)*c)+(((d+e)*f)+g)") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*(((3+4)*5)+(6/(7*((8-9)+10))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*(((3+4)*5)+(6/(7*((8-9)+10))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b))))))))))))))))))))))))))") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b))))))))))))))))))))))))))") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1+2)*(3+4))-((5+6)*(7+8)))+(((9+0)*(1+2))-((3+4)*(5+6))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1+2)*(3+4))-((5+6)*(7+8)))+(((9+0)*(1+2))-((3+4)*(5+6))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b*c))+((d+e)/(f-g)))+((h*(i-j)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b*c))+((d+e)/(f-g)))+((h*(i-j)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+u))))))))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+u))))))))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "((x+y)+((z+w)*((a+b)*(c+d))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((x+y)+((z+w)*((a+b)*(c+d))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)+((c+d)*(e+f)))+((g-h)*((i+j)/(k-l))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)+((c+d)*(e+f)))+((g-h)*((i+j)/(k-l))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(((2+((3+((4+((5+((6+((7+((8+((9+(10)))))))))))))))))))") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(((2+((3+((4+((5+((6+((7+((8+((9+(10)))))))))))))))))))") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)+(c*d))+(((e-f)-(g*h)))+((i+j)*(k+l)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)+(c*d))+(((e-f)-(g*h)))+((i+j)*(k+l)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(x+(y*(z+(w/(v+(u+((t)+s))))))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(x+(y*(z+(w/(v+(u+((t)+s))))))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)+c)+((d+e)+f))+(((g+h)+i)+(j+(k+l)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)+c)+((d+e)+f))+(((g+h)+i)+(j+(k+l)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+(d/(e+f)+g)+h)+i)") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+(d/(e+f)+g)+h)+i)") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)+(c*(d+(e/(f+(g+(h+(i+(j))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)+(c*(d+(e/(f+(g+(h+(i+(j))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*(3+(4*(5+(6+(7*(8+(9*(10)))))))))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*(3+(4*(5+(6+(7*(8+(9*(10)))))))))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((((a+b)*c)+d)+e)+f)+g)+h)") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((((a+b)*c)+d)+e)+f)+g)+h)") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+(b*c))+((d+(e*f))+(g+(h*i))))+((j+(k*l))+((m+(n*o))+(p+(q+(r+(s+t))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+(b*c))+((d+(e*f))+(g+(h*i))))+((j+(k*l))+((m+(n*o))+(p+(q+(r+(s+t))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*((3+4)*(5+6)*((7+8)*(9+10))))+11)") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*((3+4)*(5+6)*((7+8)*(9+10))))+11)") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b*(c+(d*(e+f)))))+(((g-h)+(i-j))*((k-l)+(m*n))))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b*(c+(d*(e+f)))))+(((g-h)+(i-j))*((k-l)+(m*n))))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)*((c-d)+e))+((f+(g/h))-((i*j)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)*((c-d)+e))+((f+(g/h))-((i*j)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+((2+((3+((4+((5+6)+7))+8))+9))+10)+11") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+((2+((3+((4+((5+6)+7))+8))+9))+10)+11") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)*(i+j))))*(k+l)))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)*(i+j))))*(k+l)))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b*c))+(d/((e+f)*(g-h))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b*c))+(d/((e+f)*(g-h))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((x+(y*z))+(w*((a+b)*c)))+((d+e)+((f*g)+((h+i)+((j+k)*l)))))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((x+(y*z))+(w*((a+b)*c)))+((d+e)+((f*g)+((h+i)+((j+k)*l)))))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d)))+((e+f)*((g+h)*(i+j)))+(((k+l)*(m+n))+(o+(p*(q+r))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d)))+((e+f)*((g+h)*(i+j)))+(((k+l)*(m+n))+(o+(p*(q+r))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d)))+((e/f)-(g*h))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d)))+((e/f)-(g*h))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+(2*(3+(4*(5+(6*(7+(8*(9))))))))+10)") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+(2*(3+(4*(5+(6*(7+(8*(9))))))))+10)") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d))+e+(f/(g-h)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d))+e+(f/(g-h)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1+2)*3)+4)*5)+((6+(7*(8+9)))/10))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1+2)*3)+4)*5)+((6+(7*(8+9)))/10))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s)+t)+u)+v") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s)+t)+u)+v") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+b)+((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+((u+v)+((w+x)+((y+z))))))))))))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+b)+((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+((u+v)+((w+x)+((y+z))))))))))))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((a+b)+((c+d)*(e+f)))+((g+h)+((i+j)*(k+l))))+(m+(n*(o+p))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((a+b)+((c+d)*(e+f)))+((g+h)+((i+j)*(k+l))))+(m+(n*(o+p))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((a+b)*c)+((d+e)*f))+(((g+h)*i)+((j+k)*l)))+((((m+n)*o)+((p+q)*r))+(((s+t)*u)+((v+w)*x))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((a+b)*c)+((d+e)*f))+(((g+h)*i)+((j+k)*l)))+((((m+n)*o)+((p+q)*r))+(((s+t)*u)+((v+w)*x))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((1+2)*3)+((4+5)*(6/7)))+(((8+9)*((10-11)/12)))+13") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((1+2)*3)+((4+5)*(6/7)))+(((8+9)*((10-11)/12)))+13") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((x+(y*((z+w)*v)))+(((u-t)-s)+(((r-q)+(p-o))*(n-m))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((x+(y*((z+w)*v)))+(((u-t)-s)+(((r-q)+(p-o))*(n-m))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+((2*((3+4)*(5-6)))/(7+(8*(9-10)))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+((2*((3+4)*(5-6)))/(7+(8*(9-10)))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d)))+((e+f)/(g-h))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d)))+((e+f)/(g-h))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+((2+3)*(4/5)))+((6-(7+8))*(((9/10)-11)+(12*13)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+((2+3)*(4/5)))+((6-(7+8))*(((9/10)-11)+(12*13)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1)+((2)+(((3)+((4)+(5)))+(6))))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1)+((2)+(((3)+((4)+(5)))+(6))))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+2)*((3/4)-5)+((6*7)+8))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+2)*((3/4)-5)+((6*7)+8))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))+((t+(u*v))+(((w+x)*y)/z))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))+((t+(u*v))+(((w+x)*y)/z))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+2)*((3+4)*((5+6)*((7+8)*((9+0))))))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+2)*((3+4)*((5+6)*((7+8)*((9+0))))))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+((b+((c+((d+e)*f))*g))*h))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+((b+((c+((d+e)*f))*g))*h))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1+2)+3)+4)+5)+6)+7") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1+2)+3)+4)+5)+6)+7") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z*1))))))))))))))))))))))))") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z*1))))))))))))))))))))))))") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+(d*(e+(f*(g+(h*(i+(j)))))))))+(k+(l*(m+(n*(o+(p*(q+(r*(s+(t))))))))))") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+(d*(e+(f*(g+(h*(i+(j)))))))))+(k+(l*(m+(n*(o+(p*(q+(r*(s+(t))))))))))") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1+2)*3)+4)*5)+6)") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1+2)*3)+4)*5)+6)") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)+((c+d)*(e/f)))+(((g-h)+(i/j))*((k+l)*(m-n))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)+((c+d)*(e/f)))+(((g-h)+(i/j))*((k+l)*(m-n))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+((2+3)*4))+(((5-6)+7)+((8+9)*10)))+(((11+(12*13))+14)+15)") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+((2+3)*4))+(((5-6)+7)+((8+9)*10)))+(((11+(12*13))+14)+15)") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+((b+c)*(d+((e+f)*(g+(h+i)))))+((j-k)*((l-m)+((n-o)*(p+((q-r)+s)))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+((b+c)*(d+((e+f)*(g+(h+i)))))+((j-k)*((l-m)+((n-o)*(p+((q-r)+s)))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9+0))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9+0))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+2)*((3+(4*(5+(6/7))))+((8-(9*10))+((11*12)+((13/14)+15))))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+2)*((3+(4*(5+(6/7))))+((8-(9*10))+((11*12)+((13/14)+15))))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1+((2+(3*(4+5)))/6)+(((7-8)*9)/10)") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1+((2+(3*(4+5)))/6)+(((7-8)*9)/10)") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20+(21+(22+(23+(24+(25+(26+(27+(28+(29+(30)))))))))))))))))))))))))+31)+32)+33") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20+(21+(22+(23+(24+(25+(26+(27+(28+(29+(30)))))))))))))))))))))))))+31)+32)+33") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j)))))))))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j)))))))))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((a+b)+(c*d))-(e/f))*g)+(h-(i+j)))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((a+b)+(c*d))-(e/f))*g)+(h-(i+j)))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+(b*c))+((d+(e*f))+((g+(h*i))+((j+(k*l))+((m+(n*o))+((p+(q*r))+((s+(t*u))+((v+(w*x))+((y+(z*1))+2))))))))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+(b*c))+((d+(e*f))+((g+(h*i))+((j+(k*l))+((m+(n*o))+((p+(q*r))+((s+(t*u))+((v+(w*x))+((y+(z*1))+2))))))))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))))))))))))))))))))))+a)+b)+c)+d)+e)+f)+g)+h)+i)+j)+k)+l)+m)+n)+o)+p)+q)+r)+s)+t)+u)+v)+w)+x)+y)+z") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))))))))))))))))))))))+a)+b)+c)+d)+e)+f)+g)+h)+i)+j)+k)+l)+m)+n)+o)+p)+q)+r)+s)+t)+u)+v)+w)+x)+y)+z") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+((2+(3*(4/5)))+((6-(7*8))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+((2+(3*(4/5)))+((6-(7*8))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*((3+4)*(5+(6*(7+(8+9))))))+(10*((11-12)+(13*((14-15)+(16*(17+18))))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*((3+4)*(5+(6*(7+(8+9))))))+(10*((11-12)+(13*((14-15)+(16*(17+18))))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "((x+(y*z))+(u/(v-((w+x)*(y-z)))))+(a+b)-(c*d)") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((x+(y*z))+(u/(v-((w+x)*(y-z)))))+(a+b)-(c*d)") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)*(c-d))+(((e+f)*(g-h))+(((i+j)*(k-l))+(((m+n)*(o-p))+((q+r)*(s-t)))))") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)*(c-d))+(((e+f)*(g-h))+(((i+j)*(k-l))+(((m+n)*(o-p))+((q+r)*(s-t)))))") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((a+b)*((c-d)+e))-(((f+g)*h)-(i/j)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((a+b)*((c-d)+e))-(((f+g)*h)-(i/j)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1+2)*3)+((4-5)*6))+(((7/8)+9)*10)))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1+2)*3)+((4-5)*6))+(((7/8)+9)*10)))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1)+2)*3)+(((((4)+5)*6)+((7)+8))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1)+2)*3)+(((((4)+5)*6)+((7)+8))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((1+2)*((3-4)+(5/6)))+(((7*8)-9)+((10+11)*12)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((1+2)*((3-4)+(5/6)))+(((7*8)-9)+((10+11)*12)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b)))))))))))))))))))))))))") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b)))))))))))))))))))))))))") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b*c)+(d/e))-(((f+g)*(h-i))+((j/k)+(l*m))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b*c)+(d/e))-(((f+g)*(h-i))+((j/k)+(l*m))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c/(d-e))))+(((f+g)*((h-i)+j))+((k-l)/(m*(n-o))))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c/(d-e))))+(((f+g)*((h-i)+j))+((k-l)/(m*(n-o))))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))))") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))))") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d)))+((e+f)/(g-(h*i)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d)))+((e+f)/(g-(h*i)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+d)))+(((e+f)*(g-h)))+1") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+d)))+(((e+f)*(g-h)))+1") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b*(c+(d/(e+(f*(g+(h/(i+j))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b*(c+(d/(e+(f*(g+(h/(i+j))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2*(3+4)/(5-6))+((7+8)*9))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2*(3+4)/(5-6))+((7+8)*9))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((1+2)+3)+4)+5)+6)+7)+8)+9)+10)") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((1+2)+3)+4)+5)+6)+7)+8)+9)+10)") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((x*y)+z)+((a*b)+c))+(((d*e)+f)+((g*h)+i))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((x*y)+z)+((a*b)+c))+(((d*e)+f)+((g*h)+i))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))+a)+b)+c") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))+a)+b)+c") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20))))))))))))))))+21)+22)+23)+24)+25)+26") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20))))))))))))))))+21)+22)+23)+24)+25)+26") == 23: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(1+(2*3)+((8)/4))+1") == 3
    assert candidate(s = "(a+(b*c)+((d/e)+f))") == 3
    assert candidate(s = "()()()") == 1
    assert candidate(s = "(a+b)+((c*d)+e)") == 2
    assert candidate(s = "(1+2)") == 1
    assert candidate(s = "1+(2*3)") == 1
    assert candidate(s = "") == 0
    assert candidate(s = "(())") == 2
    assert candidate(s = "((1+3)*(2-4))") == 2
    assert candidate(s = "(1)") == 1
    assert candidate(s = "((())()())") == 3
    assert candidate(s = "((1+2)*3/(4-5))") == 2
    assert candidate(s = "(1)+((2))+(((3)))") == 3
    assert candidate(s = "()(())((()()))") == 3
    assert candidate(s = "()") == 1
    assert candidate(s = "(a+b+c)*(d/e/f)+((g-(h*i))+j)") == 3
    assert candidate(s = "(a)") == 1
    assert candidate(s = "((()))") == 3
    assert candidate(s = "((a+b)*c)+(((d+e)*f)+g)") == 3
    assert candidate(s = "(1+(2*(((3+4)*5)+(6/(7*((8-9)+10))))))") == 7
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b))))))))))))))))))))))))))") == 27
    assert candidate(s = "(((((1+2)*(3+4))-((5+6)*(7+8)))+(((9+0)*(1+2))-((3+4)*(5+6))))") == 5
    assert candidate(s = "((a+(b*c))+((d+e)/(f-g)))+((h*(i-j)))") == 3
    assert candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+u))))))))))") == 12
    assert candidate(s = "((x+y)+((z+w)*((a+b)*(c+d))))") == 4
    assert candidate(s = "(((a+b)+((c+d)*(e+f)))+((g-h)*((i+j)/(k-l))))") == 4
    assert candidate(s = "(1+(((2+((3+((4+((5+((6+((7+((8+((9+(10)))))))))))))))))))") == 19
    assert candidate(s = "(((a+b)+(c*d))+(((e-f)-(g*h)))+((i+j)*(k+l)))") == 4
    assert candidate(s = "(x+(y*(z+(w/(v+(u+((t)+s))))))") == 8
    assert candidate(s = "(((a+b)+c)+((d+e)+f))+(((g+h)+i)+(j+(k+l)))") == 3
    assert candidate(s = "(a+(b*(c+(d/(e+f)+g)+h)+i)") == 5
    assert candidate(s = "((a+b)+(c*(d+(e/(f+(g+(h+(i+(j))))))))") == 9
    assert candidate(s = "(1+(2*(3+(4*(5+(6+(7*(8+(9*(10)))))))))") == 10
    assert candidate(s = "(((((((a+b)*c)+d)+e)+f)+g)+h)") == 7
    assert candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9))))))))") == 9
    assert candidate(s = "(((a+(b*c))+((d+(e*f))+(g+(h*i))))+((j+(k*l))+((m+(n*o))+(p+(q+(r+(s+t))))))") == 7
    assert candidate(s = "(1+(2*((3+4)*(5+6)*((7+8)*(9+10))))+11)") == 5
    assert candidate(s = "((a+(b*(c+(d*(e+f)))))+(((g-h)+(i-j))*((k-l)+(m*n))))") == 6
    assert candidate(s = "((a+b)*((c-d)+e))+((f+(g/h))-((i*j)))") == 3
    assert candidate(s = "(1+((2+((3+((4+((5+6)+7))+8))+9))+10)+11") == 9
    assert candidate(s = "((a+b)+(((c+d)+((e+f)+((g+h)*(i+j))))*(k+l)))") == 6
    assert candidate(s = "((a+(b*c))+(d/((e+f)*(g-h))))") == 4
    assert candidate(s = "(((((x+(y*z))+(w*((a+b)*c)))+((d+e)+((f*g)+((h+i)+((j+k)*l)))))") == 8
    assert candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))") == 5
    assert candidate(s = "(a+(b*(c+d)))+((e+f)*((g+h)*(i+j)))+(((k+l)*(m+n))+(o+(p*(q+r))))") == 4
    assert candidate(s = "(a+(b*(c+d)))+((e/f)-(g*h))") == 3
    assert candidate(s = "((1+(2*(3+(4*(5+(6*(7+(8*(9))))))))+10)") == 10
    assert candidate(s = "(a+(b*(c+d))+e+(f/(g-h)))") == 3
    assert candidate(s = "(((((1+2)*3)+4)*5)+((6+(7*(8+9)))/10))") == 5
    assert candidate(s = "(((((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s)+t)+u)+v") == 19
    assert candidate(s = "((a+b)+((c+d)+((e+f)+((g+h)+((i+j)+((k+l)+((m+n)+((o+p)+((q+r)+((s+t)+((u+v)+((w+x)+((y+z))))))))))))") == 14
    assert candidate(s = "((((a+b)+((c+d)*(e+f)))+((g+h)+((i+j)*(k+l))))+(m+(n*(o+p))))") == 5
    assert candidate(s = "((((a+b)*c)+((d+e)*f))+(((g+h)*i)+((j+k)*l)))+((((m+n)*o)+((p+q)*r))+(((s+t)*u)+((v+w)*x))))") == 4
    assert candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9))))))))") == 9
    assert candidate(s = "(((1+2)*3)+((4+5)*(6/7)))+(((8+9)*((10-11)/12)))+13") == 4
    assert candidate(s = "((x+(y*((z+w)*v)))+(((u-t)-s)+(((r-q)+(p-o))*(n-m))))") == 5
    assert candidate(s = "(1+((2*((3+4)*(5-6)))/(7+(8*(9-10)))))") == 5
    assert candidate(s = "(a+(b*(c+d)))+((e+f)/(g-h))") == 3
    assert candidate(s = "(1+((2+3)*(4/5)))+((6-(7+8))*(((9/10)-11)+(12*13)))") == 4
    assert candidate(s = "((1)+((2)+(((3)+((4)+(5)))+(6))))") == 6
    assert candidate(s = "((1+2)*((3/4)-5)+((6*7)+8))") == 3
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))+q)+r)+s") == 15
    assert candidate(s = "((x+(y*z))+((u-(v*w))+(((p+q)*r)/s)))+((t+(u*v))+(((w+x)*y)/z))") == 5
    assert candidate(s = "((1+2)*((3+4)*((5+6)*((7+8)*((9+0))))))") == 6
    assert candidate(s = "(a+((b+((c+((d+e)*f))*g))*h))") == 7
    assert candidate(s = "(((((1+2)+3)+4)+5)+6)+7") == 5
    assert candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z*1))))))))))))))))))))))))") == 27
    assert candidate(s = "(a+(b*(c+(d*(e+(f*(g+(h*(i+(j)))))))))+(k+(l*(m+(n*(o+(p*(q+(r*(s+(t))))))))))") == 11
    assert candidate(s = "(((((1+2)*3)+4)*5)+6)") == 5
    assert candidate(s = "(((a+b)+((c+d)*(e/f)))+(((g-h)+(i/j))*((k+l)*(m-n))))") == 4
    assert candidate(s = "((1+((2+3)*4))+(((5-6)+7)+((8+9)*10)))+(((11+(12*13))+14)+15)") == 4
    assert candidate(s = "(a+((b+c)*(d+((e+f)*(g+(h+i)))))+((j-k)*((l-m)+((n-o)*(p+((q-r)+s)))))") == 7
    assert candidate(s = "(1+(2*(3+(4*(5+(6+(7+(8+(9+0))))))))") == 9
    assert candidate(s = "((1+2)*((3+(4*(5+(6/7))))+((8-(9*10))+((11*12)+((13/14)+15))))") == 6
    assert candidate(s = "1+((2+(3*(4+5)))/6)+(((7-8)*9)/10)") == 4
    assert candidate(s = "((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20+(21+(22+(23+(24+(25+(26+(27+(28+(29+(30)))))))))))))))))))))))))+31)+32)+33") == 31
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j)))))))))") == 10
    assert candidate(s = "(((((a+b)+(c*d))-(e/f))*g)+(h-(i+j)))") == 5
    assert candidate(s = "(((a+(b*c))+((d+(e*f))+((g+(h*i))+((j+(k*l))+((m+(n*o))+((p+(q*r))+((s+(t*u))+((v+(w*x))+((y+(z*1))+2))))))))") == 12
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+p))))))))))))))))))))))))))))))))+a)+b)+c)+d)+e)+f)+g)+h)+i)+j)+k)+l)+m)+n)+o)+p)+q)+r)+s)+t)+u)+v)+w)+x)+y)+z") == 41
    assert candidate(s = "(1+((2+(3*(4/5)))+((6-(7*8))))") == 5
    assert candidate(s = "(1+(2*((3+4)*(5+(6*(7+(8+9))))))+(10*((11-12)+(13*((14-15)+(16*(17+18))))))") == 7
    assert candidate(s = "((x+(y*z))+(u/(v-((w+x)*(y-z)))))+(a+b)-(c*d)") == 5
    assert candidate(s = "(((a+b)*(c-d))+(((e+f)*(g-h))+(((i+j)*(k-l))+(((m+n)*(o-p))+((q+r)*(s-t)))))") == 6
    assert candidate(s = "(((a+b)*((c-d)+e))-(((f+g)*h)-(i/j)))") == 4
    assert candidate(s = "(((((1+2)*3)+((4-5)*6))+(((7/8)+9)*10)))") == 5
    assert candidate(s = "(((((1)+2)*3)+(((((4)+5)*6)+((7)+8))))") == 7
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))") == 25
    assert candidate(s = "(((1+2)*((3-4)+(5/6)))+(((7*8)-9)+((10+11)*12)))") == 4
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+(z+(a+b)))))))))))))))))))))))))") == 27
    assert candidate(s = "((a+(b*c)+(d/e))-(((f+g)*(h-i))+((j/k)+(l*m))))") == 4
    assert candidate(s = "(a+(b*(c/(d-e))))+(((f+g)*((h-i)+j))+((k-l)/(m*(n-o))))") == 4
    assert candidate(s = "((a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z))))))))))))))))))))))))") == 26
    assert candidate(s = "(a+(b*(c+d)))+((e+f)/(g-(h*i)))") == 3
    assert candidate(s = "(a+(b*(c+d)))+(((e+f)*(g-h)))+1") == 3
    assert candidate(s = "(a+(b*(c+(d/(e+(f*(g+(h/(i+j))))))))") == 9
    assert candidate(s = "(1+(2*(3+4)/(5-6))+((7+8)*9))") == 3
    assert candidate(s = "((((((((((1+2)+3)+4)+5)+6)+7)+8)+9)+10)") == 10
    assert candidate(s = "(((((x*y)+z)+((a*b)+c))+(((d*e)+f)+((g*h)+i))))") == 5
    assert candidate(s = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))+a)+b)+c") == 25
    assert candidate(s = "((((1+(2+(3+(4+(5+(6+(7+(8+(9+(10+(11+(12+(13+(14+(15+(16+(17+(18+(19+(20))))))))))))))))+21)+22)+23)+24)+25)+26") == 23


