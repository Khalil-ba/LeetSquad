# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(data = [237, 130, 130, 130]) == False
    assert candidate(data = [237, 128, 128, 130, 128, 128]) == False
    assert candidate(data = [238, 130, 130]) == True
    assert candidate(data = [31, 130, 130, 130]) == False
    assert candidate(data = [237, 130, 130, 130, 130]) == False
    assert candidate(data = [228, 189, 160]) == True
    assert candidate(data = [235, 140, 4]) == False
    assert candidate(data = [240, 162, 134, 142]) == True
    assert candidate(data = [237, 130, 130, 130, 130, 130, 130]) == False
    assert candidate(data = [251, 117, 104, 101, 108, 108, 111]) == False
    assert candidate(data = [240, 162, 134, 161]) == True
    assert candidate(data = [145]) == False
    assert candidate(data = [238, 130, 69]) == False
    assert candidate(data = [228, 189, 160, 229, 165, 189]) == True
    assert candidate(data = [197, 130, 1]) == True
    assert candidate(data = [235, 140, 4]) == False
    assert candidate(data = [197, 130, 1]) == True
    assert candidate(data = [192, 128, 191, 127]) == False
    assert candidate(data = [250, 145, 145, 145]) == False
    assert candidate(data = [0]) == True
    assert candidate(data = [240, 162, 134, 140]) == True
    assert candidate(data = [255]) == False
    assert candidate(data = [65, 66, 67, 68]) == True
    assert candidate(data = [224, 184, 148, 163]) == False
    assert candidate(data = [248, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [192, 128]) == True
    assert candidate(data = [240, 162, 138, 147, 145]) == False
    assert candidate(data = [237, 130, 130, 130]) == False
    assert candidate(data = [240, 162, 134, 142, 240, 162, 134, 142, 240, 162, 134, 142]) == True
    assert candidate(data = [252, 128, 128, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]) == False
    assert candidate(data = [110, 188, 142, 224, 160, 128]) == False
    assert candidate(data = [192, 128, 192, 128, 192, 128, 192, 192]) == False
    assert candidate(data = [225, 184, 165, 225, 184, 170, 225, 184, 185, 225, 184, 190]) == True
    assert candidate(data = [224, 160, 128, 224, 160, 128, 224, 160, 128]) == True
    assert candidate(data = [240, 159, 146, 150, 240, 159, 146, 150, 240, 159, 146, 150]) == True
    assert candidate(data = [240, 184, 152, 168, 224, 164, 174, 240, 157, 151, 166]) == True
    assert candidate(data = [248, 130, 130, 130, 130]) == False
    assert candidate(data = [248, 144, 144, 144, 144, 144]) == False
    assert candidate(data = [192, 128, 192, 128, 192, 128]) == True
    assert candidate(data = [240, 144, 144, 144, 144, 144, 144, 144]) == False
    assert candidate(data = [192, 128, 224, 162, 128, 240, 144, 128]) == False
    assert candidate(data = [248, 130, 129, 128, 128, 128, 128]) == False
    assert candidate(data = [235, 140, 141, 236, 140, 141, 237, 140, 141]) == True
    assert candidate(data = [224, 168, 128, 225, 184, 141, 225, 184, 172, 225, 184, 170, 225, 185, 172, 225, 184, 162]) == True
    assert candidate(data = [192, 128, 224, 160, 128, 225, 184, 160]) == True
    assert candidate(data = [244, 160, 128, 128, 244, 160, 128, 128]) == True
    assert candidate(data = [255, 255, 255, 255]) == False
    assert candidate(data = [225, 184, 160, 225, 184, 161, 225, 184, 162]) == True
    assert candidate(data = [192, 128, 192, 128, 192, 128, 192, 128]) == True
    assert candidate(data = [248, 128, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [250, 145, 145, 145, 145]) == False
    assert candidate(data = [225, 184, 168, 225, 184, 169, 225, 184, 170]) == True
    assert candidate(data = [240, 159, 191, 191, 240, 159, 191, 191]) == True
    assert candidate(data = [224, 162, 130, 192, 128]) == True
    assert candidate(data = [192, 128, 192, 129, 192, 130, 192, 131, 192, 132, 192, 133, 192, 134, 192, 135, 192, 136, 192, 137, 192, 138, 192, 139, 192, 140, 192, 141, 192, 142, 192, 143]) == True
    assert candidate(data = [225, 184, 150, 225, 184, 185, 225, 184, 186, 225, 184, 187, 225, 184, 188]) == True
    assert candidate(data = [250, 145, 145, 145, 145, 145]) == False
    assert candidate(data = [230, 138, 142, 230, 138, 143, 230, 138, 144]) == True
    assert candidate(data = [65, 66, 67, 68, 69, 70, 71, 72]) == True
    assert candidate(data = [240, 144, 144, 144, 240, 144, 144, 144, 240, 144, 144, 144, 240, 144, 144, 144]) == True
    assert candidate(data = [239, 188, 140, 239, 188, 141, 239, 188, 142, 239, 188, 143]) == True
    assert candidate(data = [225, 186, 130, 225, 186, 130, 225, 186, 130, 225, 186, 130, 225, 186, 130, 225, 186, 130]) == True
    assert candidate(data = [224, 160, 128, 224, 160, 129, 224, 160, 130]) == True
    assert candidate(data = [240, 159, 146, 140, 224, 164, 162, 194, 161]) == True
    assert candidate(data = [240, 128, 128, 128, 224, 160, 128, 192, 128]) == True
    assert candidate(data = [253, 160, 160, 160, 160, 160, 160, 160]) == False
    assert candidate(data = [244, 141, 132, 132, 244, 141, 132, 132]) == True
    assert candidate(data = [250, 145, 130, 147, 128, 130, 147, 128]) == False
    assert candidate(data = [240, 184, 144, 144, 240, 184, 144, 144]) == True
    assert candidate(data = [239, 187, 191, 239, 187, 191, 239, 187, 191]) == True
    assert candidate(data = [128, 129, 130, 131, 132, 133, 134, 135]) == False
    assert candidate(data = [192, 128, 224, 162, 130, 240, 159, 146, 150]) == True
    assert candidate(data = [255, 192, 128, 145]) == False
    assert candidate(data = [250, 154, 141, 154, 141, 154, 141, 154]) == False
    assert candidate(data = [252, 128, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(data = [6, 239, 191, 191, 224, 160, 128, 239, 191, 191]) == True
    assert candidate(data = [224, 160, 128, 225, 184, 160, 239, 189, 191]) == True
    assert candidate(data = [225, 186, 185, 225, 186, 185, 225, 186, 185]) == True
    assert candidate(data = [224, 160, 128, 225, 184, 128, 237, 128, 128, 240, 144, 128, 128]) == True
    assert candidate(data = [250, 145, 145, 145, 145, 145, 145, 145]) == False
    assert candidate(data = [250, 145, 130, 128, 10]) == False
    assert candidate(data = [239, 187, 191, 239, 187, 191, 239, 187, 191, 239, 187, 191]) == True
    assert candidate(data = [240, 128, 128, 128, 240, 129, 129, 129]) == True
    assert candidate(data = [191, 128, 191, 128, 191, 128]) == False
    assert candidate(data = [255, 140, 140, 140]) == False
    assert candidate(data = [192, 128, 224, 162, 138, 240, 159, 146, 150]) == True
    assert candidate(data = [128, 191, 223, 239, 255, 0, 127, 192]) == False
    assert candidate(data = [240, 144, 144, 128, 240, 144, 144, 144]) == True
    assert candidate(data = [240, 159, 146, 150, 240, 159, 146, 150]) == True
    assert candidate(data = [240, 145, 129, 128, 128]) == False
    assert candidate(data = [240, 145, 145, 145, 240, 145, 145, 145]) == True
    assert candidate(data = [234, 162, 134, 235, 140, 4, 236, 128, 132]) == False
    assert candidate(data = [240, 184, 152, 149, 240, 184, 152, 150]) == True
    assert candidate(data = [192, 128, 224, 160, 128, 240, 144, 128, 128]) == True
    assert candidate(data = [192, 128, 192, 128, 192, 128, 192, 128]) == True
    assert candidate(data = [240, 145, 128, 147, 128, 130, 147, 128, 237, 128, 128, 237, 128, 128]) == False
    assert candidate(data = [240, 145, 128, 128, 240, 145, 128, 128, 240, 145, 128, 128]) == True
    assert candidate(data = [224, 160, 128, 128, 224, 160, 128, 128, 224, 160, 128, 128]) == False
    assert candidate(data = [225, 184, 165, 225, 184, 170, 225, 184, 185]) == True
    assert candidate(data = [192, 128, 192, 128, 192, 128, 128, 192]) == False
    assert candidate(data = [224, 160, 128, 224, 160, 128, 192, 128, 128]) == False
    assert candidate(data = [239, 189, 191, 239, 189, 191]) == True
    assert candidate(data = [194, 128, 224, 160, 128, 240, 176, 128, 248, 192, 128, 128]) == False
    assert candidate(data = [192, 128, 224, 162, 138, 147, 240, 144, 144, 144, 0]) == False
    assert candidate(data = [239, 188, 140, 239, 188, 141, 239, 188, 142]) == True
    assert candidate(data = [10, 192, 128, 11, 194, 191, 14, 224, 160, 128, 15, 225, 184, 160]) == True
    assert candidate(data = [194, 128, 224, 160, 128, 240, 144, 128, 128, 250, 144, 128, 128]) == False
    assert candidate(data = [0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(data = [11111000, 10000000, 10000000, 10000000, 10000000]) == False
    assert candidate(data = [224, 160, 128, 237, 130, 176, 240, 144, 144, 128]) == True
    assert candidate(data = [255, 160, 130, 145]) == False
    assert candidate(data = [225, 186, 130, 225, 186, 130, 225, 186, 130]) == True
    assert candidate(data = [128, 129, 130, 131, 132, 133, 134, 135, 136, 137]) == False
    assert candidate(data = [240, 145, 129, 128, 240, 145, 129, 128, 240, 145, 129, 128]) == True
    assert candidate(data = [228, 189, 160, 229, 165, 189, 228, 184, 173]) == True
    assert candidate(data = [224, 162, 138, 224, 162, 138]) == True
    assert candidate(data = [194, 128, 226, 128, 128, 239, 184, 141]) == True
    assert candidate(data = [248, 130, 130, 130, 130, 130, 130, 130]) == False
    assert candidate(data = [240, 159, 146, 150, 192, 128, 224, 162, 130]) == True
    assert candidate(data = [250, 145, 145, 145, 145, 145, 145]) == False
    assert candidate(data = [240, 144, 144, 144, 144]) == False
    assert candidate(data = [10, 192, 130, 224, 162, 138, 240, 144, 144, 144, 192, 130]) == True
    assert candidate(data = [248, 130, 130, 130, 130, 130, 130]) == False
    assert candidate(data = [240, 145, 130, 128, 225, 186, 130, 192, 128]) == True
    assert candidate(data = [255, 255, 255, 255]) == False
    assert candidate(data = [192, 129, 192, 130, 192, 131, 192, 132]) == True
    assert candidate(data = [240, 144, 144, 144, 240, 144, 144, 144]) == True
    assert candidate(data = [255, 128, 128, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [240, 162, 138, 147, 240, 162, 138, 147]) == True
    assert candidate(data = [250, 145, 145, 145, 145, 145, 145, 145, 145]) == False
    assert candidate(data = [248, 128, 128, 128, 128, 128]) == False
    assert candidate(data = [192, 128, 224, 162, 138, 240, 144, 144, 144]) == True
    assert candidate(data = [237, 140, 141, 142, 143, 144, 145]) == False
