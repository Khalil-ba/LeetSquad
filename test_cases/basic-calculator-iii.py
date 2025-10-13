# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "1-1+1") == 1
    assert candidate(s = "2*(5+5*2)/3+(6/2+8)") == 21
    assert candidate(s = "((1+2)*3)") == 9
    assert candidate(s = "100 * ( 2 + 12 ) / 14") == 100
    assert candidate(s = "1-(     5)") == -4
    assert candidate(s = "1 - (3 + (5 - 2))") == -5
    assert candidate(s = "2*(5+5*2)/3+(6/2+8)*2") == 32
    assert candidate(s = "10/3") == 3
    assert candidate(s = "(123+(456))") == 579
    assert candidate(s = "(1+(4+5+2)-3)+(6+8)") == 23
    assert candidate(s = "0") == 0
    assert candidate(s = "100 * 2 + 12") == 212
    assert candidate(s = "10 + 2 * 6") == 22
    assert candidate(s = "(0+0)") == 0
    assert candidate(s = "3+2*2") == 7
    assert candidate(s = "100*(2+12)/14") == 100
    assert candidate(s = " 3+5 / 2 ") == 5
    assert candidate(s = "1000000000-1000000000+1") == 1
    assert candidate(s = "1-(     3)") == -2
    assert candidate(s = " 3/2 ") == 1
    assert candidate(s = "10/2-1*3") == 2
    assert candidate(s = "(2+6*3+5-(3*14/7+2)*5)+3") == -12
    assert candidate(s = "3+(2*2)") == 7
    assert candidate(s = "(1)") == 1
    assert candidate(s = "0+0") == 0
    assert candidate(s = "3 + 2 * 2") == 7
    assert candidate(s = "100 * ( 2 + 12 )") == 1400
    assert candidate(s = "100*(2+12)+3*(4+5)") == 1427
    assert candidate(s = "1+1") == 2
    assert candidate(s = "(2+12)+3*(4+5)") == 41
    assert candidate(s = "3+5 / 2") == 5
    assert candidate(s = "10+5*(2+3)") == 35
    assert candidate(s = "6-4/2") == 4
    assert candidate(s = "123/45+67*(89-10)+11") == 5306
    assert candidate(s = "999/3-2*(10+20/5)+100-3*(2+5*7)") == 294
    assert candidate(s = "((3+5)*2-4)/2") == 6
    assert candidate(s = "3*(5+2*(4-1)+3)/6") == 7
    assert candidate(s = "(5+3*(4+5-2)-10)*2/((3+2)*1)+7-2*3+15/3") == 12
    assert candidate(s = "((5+6)*(7-3))/2+4*(2+3)-1") == 41
    assert candidate(s = "1000-(200*300/(400-500)+600)") == 1000
    assert candidate(s = "10+2*(6/((9+3)*3-8))") == 10
    assert candidate(s = "(1+2*(3+(4*5-6)))*7/8") == 30
    assert candidate(s = "123-((12*3)/4)+56-(78/9)") == 162
    assert candidate(s = "(1+2*(3+4*(5+6*(7+8*(9+10-11)))+12-13)*(14/2+3))-(15+16)") == 34490
    assert candidate(s = "(1+2*3)*(4-5)+6/(7+8-9)") == -6
    assert candidate(s = "((1 + 2) * 3) / 4 + (5 - 6) * 7") == -5
    assert candidate(s = "(100/25+50*2-10*(5+2))+(30-15*(2+1)*2/3)") == 34
    assert candidate(s = "(10+(3*(4-2)+5*2)/2)-((3+1)*2-5)+8") == 23
    assert candidate(s = "(100-(50+25-10)*2+30/3)-20*2+100/10") == -50
    assert candidate(s = "(2*(3+4)-5)+6/2") == 12
    assert candidate(s = "1+((2+3)*4-5)*(6+7/(8-9))") == -14
    assert candidate(s = "200/(((5+2)*3-(4*5-6))/7+8)") == 22
    assert candidate(s = "((2+3)*4+(5-6)/7)*8-9") == 151
    assert candidate(s = "(10*2+20/5-30)+40") == 34
    assert candidate(s = "(2+(3+4)*5-6)/7+8") == 12
    assert candidate(s = "(10+20*(30+40*50)-60)/(70+80*90)-100") == -95
    assert candidate(s = "1+(2*3+(4/2-1)*5)*6") == 67
    assert candidate(s = "(1*2*3*4*5*6*7*8*9)/10") == 36288
    assert candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9+(0+1)))))))))") == 46
    assert candidate(s = "(1+2*(3+4*(5+6*(7+8*(9+0))))-1)/2") == 1919
    assert candidate(s = "(10+3*(4-2)+5*2/2)*((3+1)*2-5)+8-3*2") == 65
    assert candidate(s = "((3+5)*(2-8))/4+10") == -2
    assert candidate(s = "(1+2*(3+4*(5+6)))+7") == 102
    assert candidate(s = "100+200*300/100-50") == 650
    assert candidate(s = "1000*5/25+(300+200*2)-500") == 400
    assert candidate(s = "((10+20)*30-40)+50") == 910
    assert candidate(s = "(3+5*(2-1+3)/2)-4+((7-2)*3)/2*2") == 23
    assert candidate(s = "(1+(4*(5-2)+3))/(6+(2*8))") == 0
    assert candidate(s = "((2+6*3+5-(3*14/7+2)*5)+3)") == -12
    assert candidate(s = "(10*2+(5+3*2-8/4+2*(3+2*2-1)+10/5))/3") == 14
    assert candidate(s = "(5+((1+2)*3+(4*5-6))/7)+8") == 16
    assert candidate(s = "(1*2+3*4+5*6+7*8+9*10)/(1+1*2+3*4+5*6+7*8)") == 1
    assert candidate(s = "100 / 5 + 3 * (4 - 2) - 1") == 25
    assert candidate(s = "((1+2)*3-4/(2+3)*5)+6*(7-8/2)+9") == 36
    assert candidate(s = "(10+(3*4-10)+2*(5-3))/((3+2)*1)+7") == 10
    assert candidate(s = "(2+3*(4+5)/2-1)*((3+2)*2-4)+10/2+(3-1)*5") == 99
    assert candidate(s = "10/5+2*(3-8/4)+7") == 11
    assert candidate(s = "(((1+2)*3+4)*5+6)/7-8+9*10") == 92
    assert candidate(s = "(2+3*(4+5)/2-1)*((3+2)*2-4)+10") == 94
    assert candidate(s = "(123*456+789)/(101+202*303-404*505+606)") == 0
    assert candidate(s = "(10+20+(30-(40/5+6*2-(10-5))))") == 45
    assert candidate(s = "100/25+30*2-4") == 60
    assert candidate(s = "((2+3)*4)/5") == 4
    assert candidate(s = "(9+8*7*(6+5*4-3)+2-1)/1") == 1298
    assert candidate(s = "((1+2)*(3+4)-(5+6)*(7+8))/((9+10)*(11+12)-(13+14)*(15+16))") == 0
    assert candidate(s = "(100/10-10+20*2+(30-20*2+10/1))") == 40
    assert candidate(s = "(100/10-10)*20+(30+40/5)") == 38
    assert candidate(s = "(5+3*2+1)-(3*3*3/9+7)+2*3") == 8
    assert candidate(s = "100-50/25+((20+30)*2/(5-2))+8") == 139
    assert candidate(s = "1000-((200+300)*2/(500-200))+800") == 1797
    assert candidate(s = "(1+2-3*4+5/2)*((6+7-8*9+10/3)-(11+12-13*14+15/4))") == -700
    assert candidate(s = "(((1+2)*3+4)*5+6)/7+8-9") == 9
    assert candidate(s = "100*2+12/(6-2)+3") == 206
    assert candidate(s = "(100-(50+25*(2-1)))") == 25
    assert candidate(s = "(10+(3*4-10)+2*(5-3))/((3+2)*1)+7-2*3") == 4
    assert candidate(s = "((1+2)*(3+4)/2-5)*(6-3+2*5)") == 65
    assert candidate(s = "123+456*789/100-56") == 3664
    assert candidate(s = "3*2+2*(1+5*10-20/2+100-50*(1+1))") == 88
    assert candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9))))))))") == 45
    assert candidate(s = "3*(2+(6/2+8)*(3+5))") == 270
    assert candidate(s = "(1000+2000*3/10-500)*(2+3-1)/4") == 1100
    assert candidate(s = "(5+((1+2)*3)+4)*(9-8)") == 18
    assert candidate(s = "123+456*(789-1011+1213)/1415-1617") == -1175
    assert candidate(s = "(123+456-789)*((10/2)+3*(4-2))") == -2310
    assert candidate(s = "7+6*12-4/(8+3*2)") == 79
    assert candidate(s = "1+(2+(3+(4+(5+(6+(7+(8+(9)))))))") == 45
    assert candidate(s = "(1+2*(3-4)*5+6*(7-8)*9+10)/(11+12*13-14+15*16-17)") == 0
    assert candidate(s = "30+2*(1+2*(3+4*(5+6)))-7") == 213
    assert candidate(s = "3*5-(2+3*(5-2)+2)*2+3*2/4") == -10
    assert candidate(s = "8+6*(2+(3*4-5)+7)-2/(3+1)") == 104
    assert candidate(s = "(1+1)*(2+2)*(3+3)*(4+4)*(5+5)/(10+10)") == 192
    assert candidate(s = "(12+24/(6*2)-3)+(8/2+5)") == 20
    assert candidate(s = "100*(1+100/100-100/100)+100") == 200
    assert candidate(s = "(1+2)*(3+4)*(5+6)*(7+8)*(9+10)") == 65835
    assert candidate(s = "3*(2+(3+2)*4)/2+3*5") == 48
    assert candidate(s = "(9*(8*(7+6)/5)-4)+3") == 179
    assert candidate(s = "9-5+2*3+(4-2)*3/2") == 13
    assert candidate(s = "3 + 5 / 2 * (3 + (2 * 2))") == 17
    assert candidate(s = "(1+2*(3+4*(5+6*(7+8*(9+10-11))))+12-13)/14") == 246
    assert candidate(s = "12+3*(12/4-2)+18/3") == 21
    assert candidate(s = "(5+3*2-8/4+2*(3+2*2-1)+10/5)") == 23
    assert candidate(s = "(1+2*(3+4*(5+6*(7+8*(9+10-11))))+12-13)*(14/2+3)") == 34540
    assert candidate(s = "(1+2*3-4/2+5*(6-7/2)+8-9)*(10/5+2)") == 76
    assert candidate(s = "(1+10*(2+30*(4+50*(6+70))))/(8+90*(10+100*(11+1000)))") == 0
    assert candidate(s = "(999-((888-777)*666/555)+444-333+222-111)") == 1088
    assert candidate(s = "100/((5+5)*2)+10") == 15
    assert candidate(s = "10+20/((5+5)*2)+10-(3+2)*2+5") == 16
    assert candidate(s = "(3+2*(2-1)*3)/2+1*5-(4/2+3)") == 4
    assert candidate(s = "((10 + 2) * (6 - 3)) / (4 + 2) - 5") == 1
    assert candidate(s = "(9 - (4 + 3) * 2) / 5 + 1") == 0
    assert candidate(s = "(1+(2*3+(4*(5-6))))/7+8-9") == -1
    assert candidate(s = "(10+20-30)*((2+3)*4/2-1)+50") == 50
    assert candidate(s = "100*(100/10+(10+5)*5-3*2)") == 7900
    assert candidate(s = "5 + 3 * (2 - 8 / (4 + 2))") == 8
    assert candidate(s = "(2*3+5/2*(3+5-2))-4+((7-2)*3)/2") == 21
    assert candidate(s = "((1+2)*3+(4*5-6))/7+8-9+10") == 12
    assert candidate(s = "100*2-50/(25+25/5)+50*3") == 349
    assert candidate(s = "100+50*3-20") == 230
    assert candidate(s = "1+((2+3)*4-5)+6/(7-8)") == 10
    assert candidate(s = "5+3*(2+4*2+(1+2)*3)/2") == 33
    assert candidate(s = "1000/((5*20-100)/10+(50-30))") == 50
    assert candidate(s = "(1+2)*((2+3)*(3+4)/(4+5))+(6+7*(8-9)*10)") == -55
    assert candidate(s = "100-((20+30)*2/(5-2))") == 67
    assert candidate(s = "((10+5)*2-((3*4/2)-1))") == 25
    assert candidate(s = "3*(2+2*3)+4/2-1") == 25
    assert candidate(s = "(9/((3*2)+1)*4)+2*(6/3)+1") == 9
    assert candidate(s = "(1000/100-10+5)*(50-25*(2-1)+100-50*(1+1))") == 125
    assert candidate(s = "(123+(456-789)*100)/((234-567)/89+10)") == -4739
    assert candidate(s = "1+2-3*(4/5+(6-7)*8)-9") == 18
    assert candidate(s = "(999+888*777-666+555-444*333+222)/(111+11*22-33*44+55*66-77*88+99*100)") == 96
    assert candidate(s = "100/((5*(4+3)-2*8)+1)") == 5
    assert candidate(s = "((1+2*3-4*5/2+6)*7+8-9)*(10/5+2)") == 80
    assert candidate(s = "(1+2*(3-4/(2+3)*5)+6*(7-8/2)+9)/(10/5+2)") == 8
    assert candidate(s = "(12+(15-2*3)+4*(5/2+8))-9") == 52
    assert candidate(s = "(3 * 2 - 1) + ((4 * (6 + 2) / (3 - 1)) * 2)") == 37
    assert candidate(s = "(1+2+3+4+5+6+7+8+9)*10") == 450
    assert candidate(s = "(1+2*3-4/2+5*(6-7/2)+8-9)/(10/5+2)") == 4
    assert candidate(s = "123+(456*789)/(123-456)+789") == -168
    assert candidate(s = "(12+24)/(6*(2+3))-8") == -7
    assert candidate(s = "((1+3)*5-2)/4") == 4
    assert candidate(s = "(2 + 3) * (4 - 5) + 6 / 2") == -2
    assert candidate(s = "((1+2)*3+4*(5-6))/(2+3-4)") == 5
    assert candidate(s = "(2+3*(4-5+(6/2+8)))/3") == 10
    assert candidate(s = "(3+3+3+3+3+3+3+3+3+3+3+3+3+3+3+3+3+3+3+3)/5") == 12
    assert candidate(s = "((2+6*3)+8)/((3+11)*2-10)") == 1
    assert candidate(s = "(10 - 2 * (1 + 3)) * (2 + (4 / 2))") == 8
    assert candidate(s = "((22+(2*3))-(6/3)+7)*2") == 66
    assert candidate(s = "((1+2)*(3+4)-5*(6+7)+8*(9+10))/(11*12+13*14-15*16+17*18)") == 0
    assert candidate(s = "(8-6*2)/(2+1)*(3-1)") == -2
    assert candidate(s = "(8+2*5-(3+9/3)*2)*4") == 24
    assert candidate(s = "((5+5*2)-3+(6/2+8))*2/((3+2)*1)+7") == 16
