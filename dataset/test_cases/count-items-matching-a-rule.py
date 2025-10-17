def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'green', 'lambo']],ruleKey = "color",ruleValue = "red") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'green', 'lambo']],ruleKey = "color",ruleValue = "red") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'phone'], ['phone', 'gold', 'iphone']],ruleKey = "type",ruleValue = "phone") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'phone'], ['phone', 'gold', 'iphone']],ruleKey = "type",ruleValue = "phone") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['phone', 'black', 'samsung'], ['tablet', 'black', 'ipad']],ruleKey = "color",ruleValue = "black") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['phone', 'black', 'samsung'], ['tablet', 'black', 'ipad']],ruleKey = "color",ruleValue = "black") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['phone', 'white', 'samsung'], ['tablet', 'gray', 'apple']],ruleKey = "name",ruleValue = "apple") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['phone', 'white', 'samsung'], ['tablet', 'gray', 'apple']],ruleKey = "name",ruleValue = "apple") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'white', 't-shirt'], ['pants', 'black', 'jeans'], ['shirt', 'white', 'dress-shirt']],ruleKey = "type",ruleValue = "shirt") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'white', 't-shirt'], ['pants', 'black', 'jeans'], ['shirt', 'white', 'dress-shirt']],ruleKey = "type",ruleValue = "shirt") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['tablet', 'white', 'samsung'], ['laptop', 'silver', 'macbook']],ruleKey = "name",ruleValue = "dell") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['tablet', 'white', 'samsung'], ['laptop', 'silver', 'macbook']],ruleKey = "name",ruleValue = "dell") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shoe', 'white', 'nike'], ['shirt', 'black', 'adidas'], ['shoe', 'black', 'puma']],ruleKey = "type",ruleValue = "shoe") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shoe', 'white', 'nike'], ['shirt', 'black', 'adidas'], ['shoe', 'black', 'puma']],ruleKey = "type",ruleValue = "shoe") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['notebook', 'red', 'blank']],ruleKey = "name",ruleValue = "blank") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['notebook', 'red', 'blank']],ruleKey = "name",ruleValue = "blank") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']],ruleKey = "color",ruleValue = "silver") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']],ruleKey = "color",ruleValue = "silver") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "color",ruleValue = "red") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "color",ruleValue = "red") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'brown', 'alice'], ['pen', 'blue', 'bic'], ['notebook', 'white', 'staples']],ruleKey = "type",ruleValue = "book") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'brown', 'alice'], ['pen', 'blue', 'bic'], ['notebook', 'white', 'staples']],ruleKey = "type",ruleValue = "book") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'yamaha'], ['truck', 'blue', 'ford']],ruleKey = "type",ruleValue = "red") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'yamaha'], ['truck', 'blue', 'ford']],ruleKey = "type",ruleValue = "red") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['book', 'brown', 'textbook']],ruleKey = "type",ruleValue = "book") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['book', 'brown', 'textbook']],ruleKey = "type",ruleValue = "book") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartphone', 'blue', 'samsung galaxy s20'], ['smartphone', 'black', 'iphone 12'], ['smartphone', 'red', 'huawei p30'], ['smartphone', 'black', 'google pixel 4'], ['smartphone', 'blue', 'oneplus 8t']],ruleKey = "name",ruleValue = "iphone 12") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartphone', 'blue', 'samsung galaxy s20'], ['smartphone', 'black', 'iphone 12'], ['smartphone', 'red', 'huawei p30'], ['smartphone', 'black', 'google pixel 4'], ['smartphone', 'blue', 'oneplus 8t']],ruleKey = "name",ruleValue = "iphone 12") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['camera', 'black', 'sony'], ['camera', 'gold', 'fujifilm'], ['camera', 'black', 'olympus']],ruleKey = "name",ruleValue = "sony") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['camera', 'black', 'sony'], ['camera', 'gold', 'fujifilm'], ['camera', 'black', 'olympus']],ruleKey = "name",ruleValue = "sony") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['electronics', 'black', 'headphone'], ['electronics', 'silver', 'earbuds'], ['electronics', 'white', 'speakers'], ['electronics', 'blue', 'microphone']],ruleKey = "type",ruleValue = "electronics") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['electronics', 'black', 'headphone'], ['electronics', 'silver', 'earbuds'], ['electronics', 'white', 'speakers'], ['electronics', 'blue', 'microphone']],ruleKey = "type",ruleValue = "electronics") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['toys', 'yellow', 'balloon'], ['toys', 'red', 'car'], ['toys', 'blue', 'doll'], ['toys', 'green', 'teddy'], ['toys', 'yellow', 'block']],ruleKey = "color",ruleValue = "yellow") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['toys', 'yellow', 'balloon'], ['toys', 'red', 'car'], ['toys', 'blue', 'doll'], ['toys', 'green', 'teddy'], ['toys', 'yellow', 'block']],ruleKey = "color",ruleValue = "yellow") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['computer', 'silver', 'dell'], ['computer', 'black', 'apple'], ['computer', 'silver', 'hp'], ['computer', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['computer', 'black', 'microsoft']],ruleKey = "color",ruleValue = "silver") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['computer', 'silver', 'dell'], ['computer', 'black', 'apple'], ['computer', 'silver', 'hp'], ['computer', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['computer', 'black', 'microsoft']],ruleKey = "color",ruleValue = "silver") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley'], ['car', 'blue', 'porsche'], ['bike', 'red', 'giagiua']],ruleKey = "color",ruleValue = "red") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley'], ['car', 'blue', 'porsche'], ['bike', 'red', 'giagiua']],ruleKey = "color",ruleValue = "red") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'volvo'], ['motorcycle', 'red', 'honda'], ['car', 'blue', 'tesla']],ruleKey = "color",ruleValue = "red") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'volvo'], ['motorcycle', 'red', 'honda'], ['car', 'blue', 'tesla']],ruleKey = "color",ruleValue = "red") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'blue', 'puma'], ['hat', 'blue', 'reebok'], ['shirt', 'blue', 'nike']],ruleKey = "name",ruleValue = "nike") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'blue', 'puma'], ['hat', 'blue', 'reebok'], ['shirt', 'blue', 'nike']],ruleKey = "name",ruleValue = "nike") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['electronics', 'black', 'smartphone'], ['electronics', 'blue', 'laptop'], ['electronics', 'black', 'tablet'], ['electronics', 'red', 'smartwatch'], ['electronics', 'black', 'television']],ruleKey = "type",ruleValue = "electronics") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['electronics', 'black', 'smartphone'], ['electronics', 'blue', 'laptop'], ['electronics', 'black', 'tablet'], ['electronics', 'red', 'smartwatch'], ['electronics', 'black', 'television']],ruleKey = "type",ruleValue = "electronics") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'brown', 'tolkien'], ['book', 'blue', 'harry_potter'], ['magazine', 'black', 'national_geographic'], ['book', 'blue', 'twilight'], ['magazine', 'white', 'forbes']],ruleKey = "name",ruleValue = "blue") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'brown', 'tolkien'], ['book', 'blue', 'harry_potter'], ['magazine', 'black', 'national_geographic'], ['book', 'blue', 'twilight'], ['magazine', 'white', 'forbes']],ruleKey = "name",ruleValue = "blue") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['chair', 'brown', 'ikea'], ['table', 'white', 'ikea'], ['couch', 'gray', 'ikea'], ['desk', 'black', 'ikea'], ['lamp', 'silver', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['chair', 'brown', 'ikea'], ['table', 'white', 'ikea'], ['couch', 'gray', 'ikea'], ['desk', 'black', 'ikea'], ['lamp', 'silver', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'black', 'honda'], ['car', 'red', 'tesla']],ruleKey = "type",ruleValue = "car") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'black', 'honda'], ['car', 'red', 'tesla']],ruleKey = "type",ruleValue = "car") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda']],ruleKey = "name",ruleValue = "red") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda']],ruleKey = "name",ruleValue = "red") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook']],ruleKey = "type",ruleValue = "laptop") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook']],ruleKey = "type",ruleValue = "laptop") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'blue', 'fiction'], ['book', 'red', 'nonfiction'], ['book', 'blue', 'science'], ['book', 'green', 'history'], ['book', 'blue', 'fantasy']],ruleKey = "name",ruleValue = "nonfiction") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'blue', 'fiction'], ['book', 'red', 'nonfiction'], ['book', 'blue', 'science'], ['book', 'green', 'history'], ['book', 'blue', 'fantasy']],ruleKey = "name",ruleValue = "nonfiction") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartphone', 'blue', 'samsung'], ['smartphone', 'blue', 'googlepixel'], ['smartphone', 'black', 'iphone'], ['smartphone', 'blue', 'oneplus']],ruleKey = "name",ruleValue = "googlepixel") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartphone', 'blue', 'samsung'], ['smartphone', 'blue', 'googlepixel'], ['smartphone', 'black', 'iphone'], ['smartphone', 'blue', 'oneplus']],ruleKey = "name",ruleValue = "googlepixel") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['chair', 'white', 'ikea'], ['sofa', 'brown', 'ikea'], ['table', 'brown', 'ikea'], ['lamp', 'white', 'ikea'], ['shelf', 'brown', 'ikea'], ['cabinet', 'white', 'ikea']],ruleKey = "type",ruleValue = "ikea") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['chair', 'white', 'ikea'], ['sofa', 'brown', 'ikea'], ['table', 'brown', 'ikea'], ['lamp', 'white', 'ikea'], ['shelf', 'brown', 'ikea'], ['cabinet', 'white', 'ikea']],ruleKey = "type",ruleValue = "ikea") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['television', 'black', 'samsung'], ['refrigerator', 'white', 'whirlpool'], ['microwave', 'black', 'frigidaire'], ['washer', 'stainless', 'lg']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['television', 'black', 'samsung'], ['refrigerator', 'white', 'whirlpool'], ['microwave', 'black', 'frigidaire'], ['washer', 'stainless', 'lg']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['apparel', 'black', 'jacket'], ['apparel', 'white', 'shirt'], ['apparel', 'red', 'pants'], ['apparel', 'blue', 'hat']],ruleKey = "type",ruleValue = "apparel") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['apparel', 'black', 'jacket'], ['apparel', 'white', 'shirt'], ['apparel', 'red', 'pants'], ['apparel', 'blue', 'hat']],ruleKey = "type",ruleValue = "apparel") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['camera', 'black', 'nikon'], ['camera', 'silver', 'canon'], ['camera', 'gold', 'leica'], ['camera', 'black', 'olympus'], ['camera', 'white', 'fujifilm']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['camera', 'black', 'nikon'], ['camera', 'silver', 'canon'], ['camera', 'gold', 'leica'], ['camera', 'black', 'olympus'], ['camera', 'white', 'fujifilm']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['toy', 'green', 'car'], ['toy', 'red', 'doll'], ['toy', 'blue', 'block'], ['toy', 'green', 'train'], ['toy', 'red', 'helicopter'], ['toy', 'blue', 'truck']],ruleKey = "type",ruleValue = "toy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['toy', 'green', 'car'], ['toy', 'red', 'doll'], ['toy', 'blue', 'block'], ['toy', 'green', 'train'], ['toy', 'red', 'helicopter'], ['toy', 'blue', 'truck']],ruleKey = "type",ruleValue = "toy") == 6: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'silver', 'macbook'], ['smartphone', 'gold', 'iphone'], ['tablet', 'rose gold', 'ipad'], ['watch', 'black', 'apple watch'], ['charger', 'white', 'anker']],ruleKey = "type",ruleValue = "laptop") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'silver', 'macbook'], ['smartphone', 'gold', 'iphone'], ['tablet', 'rose gold', 'ipad'], ['watch', 'black', 'apple watch'], ['charger', 'white', 'anker']],ruleKey = "type",ruleValue = "laptop") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tablet', 'black', 'samsung'], ['smartwatch', 'black', 'fitbit'], ['laptop', 'blue', 'macbook']],ruleKey = "color",ruleValue = "blue") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tablet', 'black', 'samsung'], ['smartwatch', 'black', 'fitbit'], ['laptop', 'blue', 'macbook']],ruleKey = "color",ruleValue = "blue") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola'], ['smartphone', 'blue', 'huawei'], ['smartphone', 'red', 'oppo'], ['smartphone', 'green', 'realme']],ruleKey = "name",ruleValue = "red") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola'], ['smartphone', 'blue', 'huawei'], ['smartphone', 'red', 'oppo'], ['smartphone', 'green', 'realme']],ruleKey = "name",ruleValue = "red") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook'], ['laptop', 'gray', 'asus']],ruleKey = "name",ruleValue = "laptop") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook'], ['laptop', 'gray', 'asus']],ruleKey = "name",ruleValue = "laptop") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['laptop', 'white', 'macbook'], ['smartphone', 'blue', 'googlepixel']],ruleKey = "type",ruleValue = "laptop") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['laptop', 'white', 'macbook'], ['smartphone', 'blue', 'googlepixel']],ruleKey = "type",ruleValue = "laptop") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'blue', 'harry_potter'], ['book', 'green', 'the_lord_of_the_rings'], ['book', 'blue', 'pride_and_prejudice'], ['book', 'red', 'the_hobbit'], ['book', 'blue', '1984']],ruleKey = "color",ruleValue = "blue") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'blue', 'harry_potter'], ['book', 'green', 'the_lord_of_the_rings'], ['book', 'blue', 'pride_and_prejudice'], ['book', 'red', 'the_hobbit'], ['book', 'blue', '1984']],ruleKey = "color",ruleValue = "blue") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['dress', 'pink', 'prada'], ['shoes', 'black', 'gucci'], ['bag', 'brown', 'lv'], ['jacket', 'blue', 'dolce_gabbana'], ['hat', 'black', 'versace']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['dress', 'pink', 'prada'], ['shoes', 'black', 'gucci'], ['bag', 'brown', 'lv'], ['jacket', 'blue', 'dolce_gabbana'], ['hat', 'black', 'versace']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['watch', 'black', 'rolex'], ['watch', 'white', 'omega'], ['watch', 'gold', 'patekphilippue'], ['watch', 'silver', 'seiko'], ['watch', 'black', 'titan']],ruleKey = "name",ruleValue = "seiko") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['watch', 'black', 'rolex'], ['watch', 'white', 'omega'], ['watch', 'gold', 'patekphilippue'], ['watch', 'silver', 'seiko'], ['watch', 'black', 'titan']],ruleKey = "name",ruleValue = "seiko") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['house', 'white', 'mansions'], ['house', 'blue', 'cottages'], ['apartment', 'gray', 'flats'], ['condo', 'white', 'duplex'], ['townhouse', 'blue', 'terraced'], ['house', 'white', 'bungalows'], ['apartment', 'gray', 'penthouse'], ['condo', 'blue', 'villa'], ['townhouse', 'white', 'villas'], ['house', 'gray', 'detached']],ruleKey = "type",ruleValue = "house") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['house', 'white', 'mansions'], ['house', 'blue', 'cottages'], ['apartment', 'gray', 'flats'], ['condo', 'white', 'duplex'], ['townhouse', 'blue', 'terraced'], ['house', 'white', 'bungalows'], ['apartment', 'gray', 'penthouse'], ['condo', 'blue', 'villa'], ['townhouse', 'white', 'villas'], ['house', 'gray', 'detached']],ruleKey = "type",ruleValue = "house") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'green', 'harley'], ['truck', 'black', 'ford']],ruleKey = "type",ruleValue = "car") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'green', 'harley'], ['truck', 'black', 'ford']],ruleKey = "type",ruleValue = "car") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok']],ruleKey = "color",ruleValue = "blue") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok']],ruleKey = "color",ruleValue = "blue") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'red', 'adidas'], ['hat', 'blue', 'reebok'], ['jacket', 'green', 'nike'], ['shoes', 'black', 'puma']],ruleKey = "name",ruleValue = "nike") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'red', 'adidas'], ['hat', 'blue', 'reebok'], ['jacket', 'green', 'nike'], ['shoes', 'black', 'puma']],ruleKey = "name",ruleValue = "nike") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['television', 'black', 'samsung'], ['television', 'silver', 'lg'], ['television', 'gray', 'tcl'], ['television', 'black', 'sony'], ['television', 'red', 'panasonic']],ruleKey = "type",ruleValue = "television") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['television', 'black', 'samsung'], ['television', 'silver', 'lg'], ['television', 'gray', 'tcl'], ['television', 'black', 'sony'], ['television', 'red', 'panasonic']],ruleKey = "type",ruleValue = "television") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['car', 'blue', 'ford'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'mercedes'], ['car', 'red', 'tesla']],ruleKey = "color",ruleValue = "red") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['car', 'blue', 'ford'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'mercedes'], ['car', 'red', 'tesla']],ruleKey = "color",ruleValue = "red") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['kitchenware', 'white', 'plate'], ['kitchenware', 'blue', 'spoon'], ['kitchenware', 'white', 'bowl'], ['kitchenware', 'red', 'fork'], ['kitchenware', 'white', 'knife']],ruleKey = "color",ruleValue = "white") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['kitchenware', 'white', 'plate'], ['kitchenware', 'blue', 'spoon'], ['kitchenware', 'white', 'bowl'], ['kitchenware', 'red', 'fork'], ['kitchenware', 'white', 'knife']],ruleKey = "color",ruleValue = "white") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci'], ['scarf', 'red', 'h&m'], ['glasses', 'black', 'rayban'], ['sunglasses', 'red', 'polo'], ['boots', 'blue', 'converse'], ['sandals', 'white', 'havaianas'], ['t-shirt', 'red', 'nike'], ['bag', 'black', 'louisvuitton'], ['cap', 'gray', 'nike']],ruleKey = "name",ruleValue = "nike") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci'], ['scarf', 'red', 'h&m'], ['glasses', 'black', 'rayban'], ['sunglasses', 'red', 'polo'], ['boots', 'blue', 'converse'], ['sandals', 'white', 'havaianas'], ['t-shirt', 'red', 'nike'], ['bag', 'black', 'louisvuitton'], ['cap', 'gray', 'nike']],ruleKey = "name",ruleValue = "nike") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "name",ruleValue = "nike") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "name",ruleValue = "nike") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tv', 'black', 'samsung'], ['monitor', 'silver', 'dell'], ['laptop', 'gray', 'hp'], ['phone', 'black', 'nokia'], ['tablet', 'gold', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tv', 'black', 'samsung'], ['monitor', 'silver', 'dell'], ['laptop', 'gray', 'hp'], ['phone', 'black', 'nokia'], ['tablet', 'gold', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'red', 'pride_and_prejudice'], ['book', 'blue', 'the_little_prince'], ['book', 'green', 'to_kill_a_mockingbird'], ['book', 'red', '1984'], ['book', 'yellow', 'moby_dick']],ruleKey = "color",ruleValue = "red") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'red', 'pride_and_prejudice'], ['book', 'blue', 'the_little_prince'], ['book', 'green', 'to_kill_a_mockingbird'], ['book', 'red', '1984'], ['book', 'yellow', 'moby_dick']],ruleKey = "color",ruleValue = "red") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw']],ruleKey = "color",ruleValue = "red") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw']],ruleKey = "color",ruleValue = "red") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['electronics', 'white', 'samsung'], ['electronics', 'black', 'lg'], ['electronics', 'silver', 'sony'], ['electronics', 'black', 'toshiba'], ['electronics', 'white', 'panasonic']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['electronics', 'white', 'samsung'], ['electronics', 'black', 'lg'], ['electronics', 'silver', 'sony'], ['electronics', 'black', 'toshiba'], ['electronics', 'white', 'panasonic']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "color",ruleValue = "red") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "color",ruleValue = "red") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "name",ruleValue = "dell") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "name",ruleValue = "dell") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['tv', 'black', 'samsung'], ['tv', 'white', 'lg'], ['tv', 'silver', 'sony'], ['tv', 'black', 'toshiba'], ['tv', 'white', 'vizio']],ruleKey = "color",ruleValue = "white") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['tv', 'black', 'samsung'], ['tv', 'white', 'lg'], ['tv', 'silver', 'sony'], ['tv', 'black', 'toshiba'], ['tv', 'white', 'vizio']],ruleKey = "color",ruleValue = "white") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw'], ['truck', 'black', 'chevrolet']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw'], ['truck', 'black', 'chevrolet']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'green', 'car'], ['toy', 'red', 'ball'], ['toy', 'green', 'doll'], ['toy', 'blue', 'ball']],ruleKey = "name",ruleValue = "car") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'green', 'car'], ['toy', 'red', 'ball'], ['toy', 'green', 'doll'], ['toy', 'blue', 'ball']],ruleKey = "name",ruleValue = "car") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['dog', 'black', 'labrador'], ['cat', 'white', 'siamese'], ['dog', 'brown', 'golden_retriever'], ['bird', 'blue', 'parakeet'], ['fish', 'red', 'goldfish']],ruleKey = "type",ruleValue = "dog") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['dog', 'black', 'labrador'], ['cat', 'white', 'siamese'], ['dog', 'brown', 'golden_retriever'], ['bird', 'blue', 'parakeet'], ['fish', 'red', 'goldfish']],ruleKey = "type",ruleValue = "dog") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['clothing', 'blue', 'shirt'], ['clothing', 'red', 't-shirt'], ['clothing', 'blue', 'jeans'], ['clothing', 'green', 'pants'], ['clothing', 'blue', 'jacket'], ['clothing', 'yellow', 'shorts'], ['clothing', 'blue', 'hat']],ruleKey = "color",ruleValue = "blue") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['clothing', 'blue', 'shirt'], ['clothing', 'red', 't-shirt'], ['clothing', 'blue', 'jeans'], ['clothing', 'green', 'pants'], ['clothing', 'blue', 'jacket'], ['clothing', 'yellow', 'shorts'], ['clothing', 'blue', 'hat']],ruleKey = "color",ruleValue = "blue") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['chair', 'brown', 'leather'], ['table', 'white', 'wood'], ['lamp', 'black', 'glass'], ['sofa', 'gray', 'cotton'], ['rug', 'blue', 'carpet'], ['cabinet', 'black', 'oak'], ['bed', 'white', 'sheets'], ['mirror', 'silver', 'frame'], ['shelf', 'black', 'metal']],ruleKey = "color",ruleValue = "black") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['chair', 'brown', 'leather'], ['table', 'white', 'wood'], ['lamp', 'black', 'glass'], ['sofa', 'gray', 'cotton'], ['rug', 'blue', 'carpet'], ['cabinet', 'black', 'oak'], ['bed', 'white', 'sheets'], ['mirror', 'silver', 'frame'], ['shelf', 'black', 'metal']],ruleKey = "color",ruleValue = "black") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['shirt', 'red', 'adidas'], ['shirt', 'blue', 'puma'], ['shirt', 'green', 'reebok'], ['shirt', 'blue', 'underarmour']],ruleKey = "name",ruleValue = "puma") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['shirt', 'red', 'adidas'], ['shirt', 'blue', 'puma'], ['shirt', 'green', 'reebok'], ['shirt', 'blue', 'underarmour']],ruleKey = "name",ruleValue = "puma") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'red', 'harrypotter'], ['pen', 'blue', 'bic'], ['book', 'red', 'twilight'], ['notebook', 'white', 'blank'], ['book', 'green', 'thehobbit'], ['book', 'red', 'catch22'], ['marker', 'blue', 'sharpie'], ['book', 'red', 'prideandprejudice']],ruleKey = "name",ruleValue = "red") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'red', 'harrypotter'], ['pen', 'blue', 'bic'], ['book', 'red', 'twilight'], ['notebook', 'white', 'blank'], ['book', 'green', 'thehobbit'], ['book', 'red', 'catch22'], ['marker', 'blue', 'sharpie'], ['book', 'red', 'prideandprejudice']],ruleKey = "name",ruleValue = "red") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['mouse', 'black', 'logitech'], ['mouse', 'white', 'razer'], ['mouse', 'blue', 'corsair'], ['mouse', 'black', 'microsoft'], ['mouse', 'black', 'steelseries']],ruleKey = "color",ruleValue = "black") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['mouse', 'black', 'logitech'], ['mouse', 'white', 'razer'], ['mouse', 'blue', 'corsair'], ['mouse', 'black', 'microsoft'], ['mouse', 'black', 'steelseries']],ruleKey = "color",ruleValue = "black") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'white', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'puma'], ['hat', 'white', 'reebok'], ['socks', 'blue', 'nike']],ruleKey = "color",ruleValue = "blue") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'white', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'puma'], ['hat', 'white', 'reebok'], ['socks', 'blue', 'nike']],ruleKey = "color",ruleValue = "blue") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'ducati'], ['motorcycle', 'red', 'harley_davidson'], ['scooter', 'red', 'vespa'], ['convertible', 'red', 'porsche']],ruleKey = "color",ruleValue = "red") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'ducati'], ['motorcycle', 'red', 'harley_davidson'], ['scooter', 'red', 'vespa'], ['convertible', 'red', 'porsche']],ruleKey = "color",ruleValue = "red") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['couch', 'brown', 'sofa'], ['chair', 'black', 'office'], ['table', 'brown', 'dining'], ['lamp', 'black', 'reading'], ['cabinet', 'brown', 'kitchen']],ruleKey = "color",ruleValue = "brown") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['couch', 'brown', 'sofa'], ['chair', 'black', 'office'], ['table', 'brown', 'dining'], ['lamp', 'black', 'reading'], ['cabinet', 'brown', 'kitchen']],ruleKey = "color",ruleValue = "brown") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['keyboard', 'black', 'logitech'], ['keyboard', 'white', 'razer'], ['keyboard', 'blue', 'corsair'], ['keyboard', 'black', 'microsoft'], ['keyboard', 'black', 'filco']],ruleKey = "type",ruleValue = "keyboard") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['keyboard', 'black', 'logitech'], ['keyboard', 'white', 'razer'], ['keyboard', 'blue', 'corsair'], ['keyboard', 'black', 'microsoft'], ['keyboard', 'black', 'filco']],ruleKey = "type",ruleValue = "keyboard") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci']],ruleKey = "name",ruleValue = "nike") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci']],ruleKey = "name",ruleValue = "nike") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['monitor', 'black', 'dell'], ['laptop', 'silver', 'lenovo']],ruleKey = "type",ruleValue = "laptop") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['monitor', 'black', 'dell'], ['laptop', 'silver', 'lenovo']],ruleKey = "type",ruleValue = "laptop") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "color",ruleValue = "blue") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "color",ruleValue = "blue") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['camera', 'black', 'canon'], ['smartphone', 'white', 'iphone'], ['tablet', 'gold', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'silver', 'macbook']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['camera', 'black', 'canon'], ['smartphone', 'white', 'iphone'], ['tablet', 'gold', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'silver', 'macbook']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['furniture', 'brown', 'table'], ['furniture', 'white', 'sofa'], ['furniture', 'brown', 'chair'], ['furniture', 'black', 'cabinet'], ['furniture', 'white', 'lamp'], ['furniture', 'brown', 'dresser']],ruleKey = "color",ruleValue = "brown") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['furniture', 'brown', 'table'], ['furniture', 'white', 'sofa'], ['furniture', 'brown', 'chair'], ['furniture', 'black', 'cabinet'], ['furniture', 'white', 'lamp'], ['furniture', 'brown', 'dresser']],ruleKey = "color",ruleValue = "brown") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['smartwatch', 'white', 'fitbit'], ['tablet', 'black', 'xiaomi']],ruleKey = "color",ruleValue = "white") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['smartwatch', 'white', 'fitbit'], ['tablet', 'black', 'xiaomi']],ruleKey = "color",ruleValue = "white") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['lens', 'black', 'canon'], ['camera', 'white', 'sony'], ['tripod', 'gray', 'benro'], ['camera', 'black', 'fujifilm']],ruleKey = "brand",ruleValue = "canon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['lens', 'black', 'canon'], ['camera', 'white', 'sony'], ['tripod', 'gray', 'benro'], ['camera', 'black', 'fujifilm']],ruleKey = "brand",ruleValue = "canon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['book', 'green', 'encyclopedia'], ['book', 'red', 'dictionary'], ['book', 'blue', 'novel'], ['book', 'green', 'textbook'], ['book', 'red', 'guide']],ruleKey = "color",ruleValue = "green") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['book', 'green', 'encyclopedia'], ['book', 'red', 'dictionary'], ['book', 'blue', 'novel'], ['book', 'green', 'textbook'], ['book', 'red', 'guide']],ruleKey = "color",ruleValue = "green") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley']],ruleKey = "color",ruleValue = "red") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley']],ruleKey = "color",ruleValue = "red") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['headphones', 'black', 'sony'], ['headphones', 'black', 'apple'], ['headphones', 'black', 'sennheiser'], ['headphones', 'black', 'bose'], ['headphones', 'black', 'jaybird']],ruleKey = "color",ruleValue = "black") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['headphones', 'black', 'sony'], ['headphones', 'black', 'apple'], ['headphones', 'black', 'sennheiser'], ['headphones', 'black', 'bose'], ['headphones', 'black', 'jaybird']],ruleKey = "color",ruleValue = "black") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'ford'], ['bicycle', 'green', 'giant']],ruleKey = "color",ruleValue = "red") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'ford'], ['bicycle', 'green', 'giant']],ruleKey = "color",ruleValue = "red") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'red', 'truck'], ['toy', 'yellow', 'balloon'], ['toy', 'blue', 'teddybear'], ['toy', 'red', 'firetruck']],ruleKey = "type",ruleValue = "toy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'red', 'truck'], ['toy', 'yellow', 'balloon'], ['toy', 'blue', 'teddybear'], ['toy', 'red', 'firetruck']],ruleKey = "type",ruleValue = "toy") == 6: {e}')
    
    total += 1
    try:
        result = candidate(items = [['camera', 'black', 'nikon'], ['phone', 'black', 'iphone'], ['tablet', 'black', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'black', 'macbook']],ruleKey = "color",ruleValue = "black") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['camera', 'black', 'nikon'], ['phone', 'black', 'iphone'], ['tablet', 'black', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'black', 'macbook']],ruleKey = "color",ruleValue = "black") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['sneakers', 'white', 'nike'], ['tshirt', 'blue', 'adidas'], ['jeans', 'black', 'puma'], ['hat', 'red', 'nike'], ['pants', 'blue', 'reebok']],ruleKey = "name",ruleValue = "nike") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['sneakers', 'white', 'nike'], ['tshirt', 'blue', 'adidas'], ['jeans', 'black', 'puma'], ['hat', 'red', 'nike'], ['pants', 'blue', 'reebok']],ruleKey = "name",ruleValue = "nike") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda'], ['car', 'red', 'mustang'], ['bike', 'black', 'ktm']],ruleKey = "type",ruleValue = "bike") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda'], ['car', 'red', 'mustang'], ['bike', 'black', 'ktm']],ruleKey = "type",ruleValue = "bike") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus']],ruleKey = "type",ruleValue = "computer") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus']],ruleKey = "type",ruleValue = "computer") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['monitor', 'black', 'asus'], ['monitor', 'white', 'dell'], ['monitor', 'blue', 'benq'], ['monitor', 'silver', 'acer'], ['monitor', 'black', 'lg']],ruleKey = "type",ruleValue = "monitor") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['monitor', 'black', 'asus'], ['monitor', 'white', 'dell'], ['monitor', 'blue', 'benq'], ['monitor', 'silver', 'acer'], ['monitor', 'black', 'lg']],ruleKey = "type",ruleValue = "monitor") == 5: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartphone', 'black', 'samsung'], ['smartphone', 'blue', 'iphone'], ['smartphone', 'black', 'google'], ['smartphone', 'red', 'oneplus'], ['smartphone', 'black', 'zte']],ruleKey = "color",ruleValue = "black") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartphone', 'black', 'samsung'], ['smartphone', 'blue', 'iphone'], ['smartphone', 'black', 'google'], ['smartphone', 'red', 'oneplus'], ['smartphone', 'black', 'zte']],ruleKey = "color",ruleValue = "black") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'black', 'nike'], ['jeans', 'blue', 'levis'], ['jacket', 'brown', 'adidas'], ['shoes', 'white', 'nike'], ['hat', 'black', 'nike'], ['socks', 'blue', 'addidas'], ['gloves', 'brown', 'adidas'], ['shorts', 'white', 'levis']],ruleKey = "color",ruleValue = "black") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'black', 'nike'], ['jeans', 'blue', 'levis'], ['jacket', 'brown', 'adidas'], ['shoes', 'white', 'nike'], ['hat', 'black', 'nike'], ['socks', 'blue', 'addidas'], ['gloves', 'brown', 'adidas'], ['shorts', 'white', 'levis']],ruleKey = "color",ruleValue = "black") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartphone', 'blue', 'huawei'], ['laptop', 'red', 'macbook']],ruleKey = "type",ruleValue = "smartphone") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartphone', 'blue', 'huawei'], ['laptop', 'red', 'macbook']],ruleKey = "type",ruleValue = "smartphone") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['phone', 'black', 'samsung'], ['laptop', 'gray', 'hp'], ['tablet', 'silver', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['phone', 'black', 'samsung'], ['laptop', 'gray', 'hp'], ['tablet', 'silver', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['laptop', 'black', 'lenovo'], ['desktop', 'black', 'acer']],ruleKey = "color",ruleValue = "black") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['laptop', 'black', 'lenovo'], ['desktop', 'black', 'acer']],ruleKey = "color",ruleValue = "black") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "name",ruleValue = "tesla") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "name",ruleValue = "tesla") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok'], ['shirt', 'blue', 'puma']],ruleKey = "name",ruleValue = "blue") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok'], ['shirt', 'blue', 'puma']],ruleKey = "name",ruleValue = "blue") == 0: {e}')
    
    total += 1
    try:
        result = candidate(items = [['tv', 'black', 'samsung'], ['fridge', 'white', 'lg'], ['microwave', 'black', 'whirlpool'], ['stove', 'black', 'bosch']],ruleKey = "color",ruleValue = "black") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['tv', 'black', 'samsung'], ['fridge', 'white', 'lg'], ['microwave', 'black', 'whirlpool'], ['stove', 'black', 'bosch']],ruleKey = "color",ruleValue = "black") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['vehicle', 'red', 'ferrari'], ['vehicle', 'blue', 'lamborghini'], ['vehicle', 'red', 'porsche'], ['vehicle', 'black', 'ferrari'], ['vehicle', 'red', 'mustang']],ruleKey = "name",ruleValue = "ferrari") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['vehicle', 'red', 'ferrari'], ['vehicle', 'blue', 'lamborghini'], ['vehicle', 'red', 'porsche'], ['vehicle', 'black', 'ferrari'], ['vehicle', 'red', 'mustang']],ruleKey = "name",ruleValue = "ferrari") == 2: {e}')
    
    total += 1
    try:
        result = candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['hat', 'blue', 'puma'], ['socks', 'green', 'reebok'], ['jacket', 'blue', 'the north face']],ruleKey = "color",ruleValue = "blue") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['hat', 'blue', 'puma'], ['socks', 'green', 'reebok'], ['jacket', 'blue', 'the north face']],ruleKey = "color",ruleValue = "blue") == 4: {e}')
    
    total += 1
    try:
        result = candidate(items = [['bed', 'wood', 'ikea'], ['sofa', 'leather', 'furniture_king'], ['chair', 'plastic', 'home_decor'], ['lamp', 'metal', 'ikea'], ['table', 'glass', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['bed', 'wood', 'ikea'], ['sofa', 'leather', 'furniture_king'], ['chair', 'plastic', 'home_decor'], ['lamp', 'metal', 'ikea'], ['table', 'glass', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 3: {e}')
    
    total += 1
    try:
        result = candidate(items = [['phone', 'blue', 'pixel'], ['phone', 'blue', 'galaxy'], ['phone', 'blue', 'nokia'], ['phone', 'blue', 'oneplus'], ['phone', 'blue', 'google'], ['phone', 'blue', 'xiaomi'], ['phone', 'blue', 'htc']],ruleKey = "name",ruleValue = "google") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['phone', 'blue', 'pixel'], ['phone', 'blue', 'galaxy'], ['phone', 'blue', 'nokia'], ['phone', 'blue', 'oneplus'], ['phone', 'blue', 'google'], ['phone', 'blue', 'xiaomi'], ['phone', 'blue', 'htc']],ruleKey = "name",ruleValue = "google") == 1: {e}')
    
    total += 1
    try:
        result = candidate(items = [['smartwatch', 'silver', 'apple'], ['smartwatch', 'gold', 'rolex'], ['bracelet', 'silver', 'tissot'], ['pendant', 'gold', 'omega'], ['bracelet', 'silver', 'casio']],ruleKey = "name",ruleValue = "silver") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [['smartwatch', 'silver', 'apple'], ['smartwatch', 'gold', 'rolex'], ['bracelet', 'silver', 'tissot'], ['pendant', 'gold', 'omega'], ['bracelet', 'silver', 'casio']],ruleKey = "name",ruleValue = "silver") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'green', 'lambo']],ruleKey = "color",ruleValue = "red") == 1
    assert candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'phone'], ['phone', 'gold', 'iphone']],ruleKey = "type",ruleValue = "phone") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['phone', 'black', 'samsung'], ['tablet', 'black', 'ipad']],ruleKey = "color",ruleValue = "black") == 3
    assert candidate(items = [['laptop', 'black', 'dell'], ['phone', 'white', 'samsung'], ['tablet', 'gray', 'apple']],ruleKey = "name",ruleValue = "apple") == 1
    assert candidate(items = [['shirt', 'white', 't-shirt'], ['pants', 'black', 'jeans'], ['shirt', 'white', 'dress-shirt']],ruleKey = "type",ruleValue = "shirt") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['tablet', 'white', 'samsung'], ['laptop', 'silver', 'macbook']],ruleKey = "name",ruleValue = "dell") == 1
    assert candidate(items = [['shoe', 'white', 'nike'], ['shirt', 'black', 'adidas'], ['shoe', 'black', 'puma']],ruleKey = "type",ruleValue = "shoe") == 2
    assert candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['notebook', 'red', 'blank']],ruleKey = "name",ruleValue = "blank") == 1
    assert candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']],ruleKey = "color",ruleValue = "silver") == 1
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "color",ruleValue = "red") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['book', 'brown', 'alice'], ['pen', 'blue', 'bic'], ['notebook', 'white', 'staples']],ruleKey = "type",ruleValue = "book") == 1
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'harley'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'yamaha'], ['truck', 'blue', 'ford']],ruleKey = "type",ruleValue = "red") == 0
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini']],ruleKey = "name",ruleValue = "ferrari") == 1
    assert candidate(items = [['book', 'red', 'novel'], ['pen', 'blue', 'ballpoint'], ['book', 'brown', 'textbook']],ruleKey = "type",ruleValue = "book") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['smartphone', 'blue', 'samsung galaxy s20'], ['smartphone', 'black', 'iphone 12'], ['smartphone', 'red', 'huawei p30'], ['smartphone', 'black', 'google pixel 4'], ['smartphone', 'blue', 'oneplus 8t']],ruleKey = "name",ruleValue = "iphone 12") == 1
    assert candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['camera', 'black', 'sony'], ['camera', 'gold', 'fujifilm'], ['camera', 'black', 'olympus']],ruleKey = "name",ruleValue = "sony") == 1
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['electronics', 'black', 'headphone'], ['electronics', 'silver', 'earbuds'], ['electronics', 'white', 'speakers'], ['electronics', 'blue', 'microphone']],ruleKey = "type",ruleValue = "electronics") == 4
    assert candidate(items = [['toys', 'yellow', 'balloon'], ['toys', 'red', 'car'], ['toys', 'blue', 'doll'], ['toys', 'green', 'teddy'], ['toys', 'yellow', 'block']],ruleKey = "color",ruleValue = "yellow") == 2
    assert candidate(items = [['computer', 'silver', 'dell'], ['computer', 'black', 'apple'], ['computer', 'silver', 'hp'], ['computer', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['computer', 'black', 'microsoft']],ruleKey = "color",ruleValue = "silver") == 3
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley'], ['car', 'blue', 'porsche'], ['bike', 'red', 'giagiua']],ruleKey = "color",ruleValue = "red") == 3
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'blue', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'black', 'apple'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'volvo'], ['motorcycle', 'red', 'honda'], ['car', 'blue', 'tesla']],ruleKey = "color",ruleValue = "red") == 3
    assert candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'blue', 'puma'], ['hat', 'blue', 'reebok'], ['shirt', 'blue', 'nike']],ruleKey = "name",ruleValue = "nike") == 2
    assert candidate(items = [['electronics', 'black', 'smartphone'], ['electronics', 'blue', 'laptop'], ['electronics', 'black', 'tablet'], ['electronics', 'red', 'smartwatch'], ['electronics', 'black', 'television']],ruleKey = "type",ruleValue = "electronics") == 5
    assert candidate(items = [['book', 'brown', 'tolkien'], ['book', 'blue', 'harry_potter'], ['magazine', 'black', 'national_geographic'], ['book', 'blue', 'twilight'], ['magazine', 'white', 'forbes']],ruleKey = "name",ruleValue = "blue") == 0
    assert candidate(items = [['chair', 'brown', 'ikea'], ['table', 'white', 'ikea'], ['couch', 'gray', 'ikea'], ['desk', 'black', 'ikea'], ['lamp', 'silver', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 5
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'black', 'honda'], ['car', 'red', 'tesla']],ruleKey = "type",ruleValue = "car") == 3
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "type",ruleValue = "laptop") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda']],ruleKey = "name",ruleValue = "red") == 0
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook']],ruleKey = "type",ruleValue = "laptop") == 3
    assert candidate(items = [['book', 'blue', 'fiction'], ['book', 'red', 'nonfiction'], ['book', 'blue', 'science'], ['book', 'green', 'history'], ['book', 'blue', 'fantasy']],ruleKey = "name",ruleValue = "nonfiction") == 1
    assert candidate(items = [['smartphone', 'blue', 'samsung'], ['smartphone', 'blue', 'googlepixel'], ['smartphone', 'black', 'iphone'], ['smartphone', 'blue', 'oneplus']],ruleKey = "name",ruleValue = "googlepixel") == 1
    assert candidate(items = [['chair', 'white', 'ikea'], ['sofa', 'brown', 'ikea'], ['table', 'brown', 'ikea'], ['lamp', 'white', 'ikea'], ['shelf', 'brown', 'ikea'], ['cabinet', 'white', 'ikea']],ruleKey = "type",ruleValue = "ikea") == 0
    assert candidate(items = [['television', 'black', 'samsung'], ['refrigerator', 'white', 'whirlpool'], ['microwave', 'black', 'frigidaire'], ['washer', 'stainless', 'lg']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['apparel', 'black', 'jacket'], ['apparel', 'white', 'shirt'], ['apparel', 'red', 'pants'], ['apparel', 'blue', 'hat']],ruleKey = "type",ruleValue = "apparel") == 4
    assert candidate(items = [['camera', 'black', 'nikon'], ['camera', 'silver', 'canon'], ['camera', 'gold', 'leica'], ['camera', 'black', 'olympus'], ['camera', 'white', 'fujifilm']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['toy', 'green', 'car'], ['toy', 'red', 'doll'], ['toy', 'blue', 'block'], ['toy', 'green', 'train'], ['toy', 'red', 'helicopter'], ['toy', 'blue', 'truck']],ruleKey = "type",ruleValue = "toy") == 6
    assert candidate(items = [['laptop', 'silver', 'macbook'], ['smartphone', 'gold', 'iphone'], ['tablet', 'rose gold', 'ipad'], ['watch', 'black', 'apple watch'], ['charger', 'white', 'anker']],ruleKey = "type",ruleValue = "laptop") == 1
    assert candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tablet', 'black', 'samsung'], ['smartwatch', 'black', 'fitbit'], ['laptop', 'blue', 'macbook']],ruleKey = "color",ruleValue = "blue") == 2
    assert candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola'], ['smartphone', 'blue', 'huawei'], ['smartphone', 'red', 'oppo'], ['smartphone', 'green', 'realme']],ruleKey = "name",ruleValue = "red") == 0
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp'], ['laptop', 'black', 'macbook'], ['laptop', 'gray', 'asus']],ruleKey = "name",ruleValue = "laptop") == 0
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['laptop', 'white', 'macbook'], ['smartphone', 'blue', 'googlepixel']],ruleKey = "type",ruleValue = "laptop") == 2
    assert candidate(items = [['book', 'blue', 'harry_potter'], ['book', 'green', 'the_lord_of_the_rings'], ['book', 'blue', 'pride_and_prejudice'], ['book', 'red', 'the_hobbit'], ['book', 'blue', '1984']],ruleKey = "color",ruleValue = "blue") == 3
    assert candidate(items = [['dress', 'pink', 'prada'], ['shoes', 'black', 'gucci'], ['bag', 'brown', 'lv'], ['jacket', 'blue', 'dolce_gabbana'], ['hat', 'black', 'versace']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['watch', 'black', 'rolex'], ['watch', 'white', 'omega'], ['watch', 'gold', 'patekphilippue'], ['watch', 'silver', 'seiko'], ['watch', 'black', 'titan']],ruleKey = "name",ruleValue = "seiko") == 1
    assert candidate(items = [['house', 'white', 'mansions'], ['house', 'blue', 'cottages'], ['apartment', 'gray', 'flats'], ['condo', 'white', 'duplex'], ['townhouse', 'blue', 'terraced'], ['house', 'white', 'bungalows'], ['apartment', 'gray', 'penthouse'], ['condo', 'blue', 'villa'], ['townhouse', 'white', 'villas'], ['house', 'gray', 'detached']],ruleKey = "type",ruleValue = "house") == 4
    assert candidate(items = [['smartphone', 'red', 'iphone'], ['smartphone', 'black', 'galaxy'], ['smartphone', 'white', 'nokia'], ['smartphone', 'black', 'oneplus'], ['smartphone', 'red', 'motorola']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['motorcycle', 'green', 'harley'], ['truck', 'black', 'ford']],ruleKey = "type",ruleValue = "car") == 2
    assert candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok']],ruleKey = "color",ruleValue = "blue") == 5
    assert candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'red', 'adidas'], ['hat', 'blue', 'reebok'], ['jacket', 'green', 'nike'], ['shoes', 'black', 'puma']],ruleKey = "name",ruleValue = "nike") == 2
    assert candidate(items = [['television', 'black', 'samsung'], ['television', 'silver', 'lg'], ['television', 'gray', 'tcl'], ['television', 'black', 'sony'], ['television', 'red', 'panasonic']],ruleKey = "type",ruleValue = "television") == 5
    assert candidate(items = [['car', 'red', 'ferrari'], ['car', 'blue', 'ford'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'mercedes'], ['car', 'red', 'tesla']],ruleKey = "color",ruleValue = "red") == 3
    assert candidate(items = [['kitchenware', 'white', 'plate'], ['kitchenware', 'blue', 'spoon'], ['kitchenware', 'white', 'bowl'], ['kitchenware', 'red', 'fork'], ['kitchenware', 'white', 'knife']],ruleKey = "color",ruleValue = "white") == 3
    assert candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci'], ['scarf', 'red', 'h&m'], ['glasses', 'black', 'rayban'], ['sunglasses', 'red', 'polo'], ['boots', 'blue', 'converse'], ['sandals', 'white', 'havaianas'], ['t-shirt', 'red', 'nike'], ['bag', 'black', 'louisvuitton'], ['cap', 'gray', 'nike']],ruleKey = "name",ruleValue = "nike") == 4
    assert candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "name",ruleValue = "nike") == 1
    assert candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['tv', 'black', 'samsung'], ['monitor', 'silver', 'dell'], ['laptop', 'gray', 'hp'], ['phone', 'black', 'nokia'], ['tablet', 'gold', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3
    assert candidate(items = [['book', 'red', 'pride_and_prejudice'], ['book', 'blue', 'the_little_prince'], ['book', 'green', 'to_kill_a_mockingbird'], ['book', 'red', '1984'], ['book', 'yellow', 'moby_dick']],ruleKey = "color",ruleValue = "red") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw']],ruleKey = "color",ruleValue = "red") == 3
    assert candidate(items = [['electronics', 'white', 'samsung'], ['electronics', 'black', 'lg'], ['electronics', 'silver', 'sony'], ['electronics', 'black', 'toshiba'], ['electronics', 'white', 'panasonic']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "color",ruleValue = "red") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartwatch', 'gold', 'fitbit'], ['laptop', 'gray', 'hp']],ruleKey = "name",ruleValue = "dell") == 1
    assert candidate(items = [['tv', 'black', 'samsung'], ['tv', 'white', 'lg'], ['tv', 'silver', 'sony'], ['tv', 'black', 'toshiba'], ['tv', 'white', 'vizio']],ruleKey = "color",ruleValue = "white") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla'], ['car', 'red', 'bmw'], ['truck', 'black', 'chevrolet']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'green', 'car'], ['toy', 'red', 'ball'], ['toy', 'green', 'doll'], ['toy', 'blue', 'ball']],ruleKey = "name",ruleValue = "car") == 2
    assert candidate(items = [['dog', 'black', 'labrador'], ['cat', 'white', 'siamese'], ['dog', 'brown', 'golden_retriever'], ['bird', 'blue', 'parakeet'], ['fish', 'red', 'goldfish']],ruleKey = "type",ruleValue = "dog") == 2
    assert candidate(items = [['clothing', 'blue', 'shirt'], ['clothing', 'red', 't-shirt'], ['clothing', 'blue', 'jeans'], ['clothing', 'green', 'pants'], ['clothing', 'blue', 'jacket'], ['clothing', 'yellow', 'shorts'], ['clothing', 'blue', 'hat']],ruleKey = "color",ruleValue = "blue") == 4
    assert candidate(items = [['chair', 'brown', 'leather'], ['table', 'white', 'wood'], ['lamp', 'black', 'glass'], ['sofa', 'gray', 'cotton'], ['rug', 'blue', 'carpet'], ['cabinet', 'black', 'oak'], ['bed', 'white', 'sheets'], ['mirror', 'silver', 'frame'], ['shelf', 'black', 'metal']],ruleKey = "color",ruleValue = "black") == 3
    assert candidate(items = [['shirt', 'blue', 'nike'], ['shirt', 'red', 'adidas'], ['shirt', 'blue', 'puma'], ['shirt', 'green', 'reebok'], ['shirt', 'blue', 'underarmour']],ruleKey = "name",ruleValue = "puma") == 1
    assert candidate(items = [['book', 'red', 'harrypotter'], ['pen', 'blue', 'bic'], ['book', 'red', 'twilight'], ['notebook', 'white', 'blank'], ['book', 'green', 'thehobbit'], ['book', 'red', 'catch22'], ['marker', 'blue', 'sharpie'], ['book', 'red', 'prideandprejudice']],ruleKey = "name",ruleValue = "red") == 0
    assert candidate(items = [['mouse', 'black', 'logitech'], ['mouse', 'white', 'razer'], ['mouse', 'blue', 'corsair'], ['mouse', 'black', 'microsoft'], ['mouse', 'black', 'steelseries']],ruleKey = "color",ruleValue = "black") == 3
    assert candidate(items = [['shirt', 'white', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'puma'], ['hat', 'white', 'reebok'], ['socks', 'blue', 'nike']],ruleKey = "color",ruleValue = "blue") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'red', 'ducati'], ['motorcycle', 'red', 'harley_davidson'], ['scooter', 'red', 'vespa'], ['convertible', 'red', 'porsche']],ruleKey = "color",ruleValue = "red") == 5
    assert candidate(items = [['couch', 'brown', 'sofa'], ['chair', 'black', 'office'], ['table', 'brown', 'dining'], ['lamp', 'black', 'reading'], ['cabinet', 'brown', 'kitchen']],ruleKey = "color",ruleValue = "brown") == 3
    assert candidate(items = [['keyboard', 'black', 'logitech'], ['keyboard', 'white', 'razer'], ['keyboard', 'blue', 'corsair'], ['keyboard', 'black', 'microsoft'], ['keyboard', 'black', 'filco']],ruleKey = "type",ruleValue = "keyboard") == 5
    assert candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shoes', 'black', 'reebok'], ['hat', 'red', 'nike'], ['jacket', 'blue', 'puma'], ['watch', 'silver', 'rolex'], ['belt', 'brown', 'gucci']],ruleKey = "name",ruleValue = "nike") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['monitor', 'black', 'dell'], ['laptop', 'silver', 'lenovo']],ruleKey = "type",ruleValue = "laptop") == 3
    assert candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas']],ruleKey = "color",ruleValue = "blue") == 4
    assert candidate(items = [['camera', 'black', 'canon'], ['smartphone', 'white', 'iphone'], ['tablet', 'gold', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'silver', 'macbook']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['furniture', 'brown', 'table'], ['furniture', 'white', 'sofa'], ['furniture', 'brown', 'chair'], ['furniture', 'black', 'cabinet'], ['furniture', 'white', 'lamp'], ['furniture', 'brown', 'dresser']],ruleKey = "color",ruleValue = "brown") == 3
    assert candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus'], ['computer', 'silver', 'lenovo'], ['smartwatch', 'white', 'fitbit'], ['tablet', 'black', 'xiaomi']],ruleKey = "color",ruleValue = "white") == 2
    assert candidate(items = [['camera', 'black', 'canon'], ['camera', 'silver', 'nikon'], ['lens', 'black', 'canon'], ['camera', 'white', 'sony'], ['tripod', 'gray', 'benro'], ['camera', 'black', 'fujifilm']],ruleKey = "brand",ruleValue = "canon") == 2
    assert candidate(items = [['book', 'green', 'encyclopedia'], ['book', 'red', 'dictionary'], ['book', 'blue', 'novel'], ['book', 'green', 'textbook'], ['book', 'red', 'guide']],ruleKey = "color",ruleValue = "green") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bicycle', 'black', 'trek'], ['motorcycle', 'green', 'harley']],ruleKey = "color",ruleValue = "red") == 2
    assert candidate(items = [['headphones', 'black', 'sony'], ['headphones', 'black', 'apple'], ['headphones', 'black', 'sennheiser'], ['headphones', 'black', 'bose'], ['headphones', 'black', 'jaybird']],ruleKey = "color",ruleValue = "black") == 5
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'black', 'ford'], ['bicycle', 'green', 'giant']],ruleKey = "color",ruleValue = "red") == 2
    assert candidate(items = [['toy', 'red', 'car'], ['toy', 'blue', 'doll'], ['toy', 'red', 'truck'], ['toy', 'yellow', 'balloon'], ['toy', 'blue', 'teddybear'], ['toy', 'red', 'firetruck']],ruleKey = "type",ruleValue = "toy") == 6
    assert candidate(items = [['camera', 'black', 'nikon'], ['phone', 'black', 'iphone'], ['tablet', 'black', 'ipad'], ['smartwatch', 'black', 'applewatch'], ['laptop', 'black', 'macbook']],ruleKey = "color",ruleValue = "black") == 5
    assert candidate(items = [['sneakers', 'white', 'nike'], ['tshirt', 'blue', 'adidas'], ['jeans', 'black', 'puma'], ['hat', 'red', 'nike'], ['pants', 'blue', 'reebok']],ruleKey = "name",ruleValue = "nike") == 2
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['bike', 'red', 'ducati'], ['car', 'blue', 'toyota'], ['bike', 'white', 'honda'], ['car', 'red', 'mustang'], ['bike', 'black', 'ktm']],ruleKey = "type",ruleValue = "bike") == 4
    assert candidate(items = [['computer', 'black', 'macbook'], ['smartwatch', 'silver', 'apple'], ['tablet', 'white', 'samsung'], ['laptop', 'blue', 'dell'], ['desktop', 'black', 'asus']],ruleKey = "type",ruleValue = "computer") == 1
    assert candidate(items = [['monitor', 'black', 'asus'], ['monitor', 'white', 'dell'], ['monitor', 'blue', 'benq'], ['monitor', 'silver', 'acer'], ['monitor', 'black', 'lg']],ruleKey = "type",ruleValue = "monitor") == 5
    assert candidate(items = [['smartphone', 'black', 'samsung'], ['smartphone', 'blue', 'iphone'], ['smartphone', 'black', 'google'], ['smartphone', 'red', 'oneplus'], ['smartphone', 'black', 'zte']],ruleKey = "color",ruleValue = "black") == 3
    assert candidate(items = [['shirt', 'black', 'nike'], ['jeans', 'blue', 'levis'], ['jacket', 'brown', 'adidas'], ['shoes', 'white', 'nike'], ['hat', 'black', 'nike'], ['socks', 'blue', 'addidas'], ['gloves', 'brown', 'adidas'], ['shorts', 'white', 'levis']],ruleKey = "color",ruleValue = "black") == 2
    assert candidate(items = [['laptop', 'black', 'dell'], ['smartphone', 'black', 'samsung'], ['tablet', 'silver', 'ipad'], ['smartphone', 'blue', 'huawei'], ['laptop', 'red', 'macbook']],ruleKey = "type",ruleValue = "smartphone") == 2
    assert candidate(items = [['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone'], ['phone', 'black', 'samsung'], ['laptop', 'gray', 'hp'], ['tablet', 'silver', 'ipad']],ruleKey = "type",ruleValue = "phone") == 3
    assert candidate(items = [['laptop', 'black', 'dell'], ['laptop', 'gray', 'hp'], ['desktop', 'black', 'asus'], ['laptop', 'black', 'lenovo'], ['desktop', 'black', 'acer']],ruleKey = "color",ruleValue = "black") == 4
    assert candidate(items = [['car', 'red', 'ferrari'], ['bike', 'blue', 'yamaha'], ['car', 'red', 'lamborghini'], ['truck', 'white', 'ford'], ['car', 'black', 'tesla']],ruleKey = "name",ruleValue = "tesla") == 1
    assert candidate(items = [['shirt', 'blue', 'tshirt'], ['jeans', 'blue', 'levis'], ['shirt', 'green', 'polo'], ['shorts', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['shirt', 'blue', 'reebok'], ['shirt', 'blue', 'puma']],ruleKey = "name",ruleValue = "blue") == 0
    assert candidate(items = [['tv', 'black', 'samsung'], ['fridge', 'white', 'lg'], ['microwave', 'black', 'whirlpool'], ['stove', 'black', 'bosch']],ruleKey = "color",ruleValue = "black") == 3
    assert candidate(items = [['vehicle', 'red', 'ferrari'], ['vehicle', 'blue', 'lamborghini'], ['vehicle', 'red', 'porsche'], ['vehicle', 'black', 'ferrari'], ['vehicle', 'red', 'mustang']],ruleKey = "name",ruleValue = "ferrari") == 2
    assert candidate(items = [['shirt', 'blue', 'nike'], ['pants', 'blue', 'adidas'], ['hat', 'blue', 'puma'], ['socks', 'green', 'reebok'], ['jacket', 'blue', 'the north face']],ruleKey = "color",ruleValue = "blue") == 4
    assert candidate(items = [['bed', 'wood', 'ikea'], ['sofa', 'leather', 'furniture_king'], ['chair', 'plastic', 'home_decor'], ['lamp', 'metal', 'ikea'], ['table', 'glass', 'ikea']],ruleKey = "brand",ruleValue = "ikea") == 3
    assert candidate(items = [['phone', 'blue', 'pixel'], ['phone', 'blue', 'galaxy'], ['phone', 'blue', 'nokia'], ['phone', 'blue', 'oneplus'], ['phone', 'blue', 'google'], ['phone', 'blue', 'xiaomi'], ['phone', 'blue', 'htc']],ruleKey = "name",ruleValue = "google") == 1
    assert candidate(items = [['smartwatch', 'silver', 'apple'], ['smartwatch', 'gold', 'rolex'], ['bracelet', 'silver', 'tissot'], ['pendant', 'gold', 'omega'], ['bracelet', 'silver', 'casio']],ruleKey = "name",ruleValue = "silver") == 0


