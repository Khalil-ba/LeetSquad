def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(features = ['cooler', 'lock', 'touch'],responses = ['i like cooler cooler', 'lock touch cool', 'locker like touch']) == ['touch', 'cooler', 'lock']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['cooler', 'lock', 'touch'],responses = ['i like cooler cooler', 'lock touch cool', 'locker like touch']) == ['touch', 'cooler', 'lock']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['a', 'aa', 'b', 'c'],responses = ['a', 'a aa', 'a a a a a', 'b a']) == ['a', 'aa', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['a', 'aa', 'b', 'c'],responses = ['a', 'a aa', 'a a a a a', 'b a']) == ['a', 'aa', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['processor', 'memory', 'storage', 'display'],responses = ['processor', 'memory processor', 'storage memory', 'display storage', 'processor memory storage display', 'memory memory memory', 'storage storage storage', 'display display display', 'processor processor', 'memory storage display', 'display memory processor', 'storage display memory', 'processor storage display memory', 'memory display storage', 'storage display memory processor']) == ['memory', 'storage', 'display', 'processor']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['processor', 'memory', 'storage', 'display'],responses = ['processor', 'memory processor', 'storage memory', 'display storage', 'processor memory storage display', 'memory memory memory', 'storage storage storage', 'display display display', 'processor processor', 'memory storage display', 'display memory processor', 'storage display memory', 'processor storage display memory', 'memory display storage', 'storage display memory processor']) == ['memory', 'storage', 'display', 'processor']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['long-lasting', 'portable', 'stylish', 'affordable'],responses = ['long-lasting battery', 'portable and stylish', 'affordable and long-lasting', 'stylish and portable', 'long-lasting and affordable', 'affordable design', 'portable battery', 'stylish battery', 'affordable battery', 'long-lasting and portable', 'stylish and long-lasting', 'affordable and stylish', 'portable and affordable', 'long-lasting portable', 'affordable stylish portable', 'long-lasting stylish', 'affordable long-lasting', 'stylish long-lasting portable', 'portable long-lasting', 'affordable and portable and stylish', 'long-lasting and affordable and portable', 'portable and affordable and stylish', 'stylish and affordable and long-lasting', 'affordable and long-lasting and portable and stylish']) == ['long-lasting', 'portable', 'affordable', 'stylish']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['long-lasting', 'portable', 'stylish', 'affordable'],responses = ['long-lasting battery', 'portable and stylish', 'affordable and long-lasting', 'stylish and portable', 'long-lasting and affordable', 'affordable design', 'portable battery', 'stylish battery', 'affordable battery', 'long-lasting and portable', 'stylish and long-lasting', 'affordable and stylish', 'portable and affordable', 'long-lasting portable', 'affordable stylish portable', 'long-lasting stylish', 'affordable long-lasting', 'stylish long-lasting portable', 'portable long-lasting', 'affordable and portable and stylish', 'long-lasting and affordable and portable', 'portable and affordable and stylish', 'stylish and affordable and long-lasting', 'affordable and long-lasting and portable and stylish']) == ['long-lasting', 'portable', 'affordable', 'stylish']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['processor', 'ram', 'storage', 'gpu'],responses = ['processor is powerful', 'ram is fast', 'storage is reliable', 'gpu is great', 'processor and ram', 'ram and storage', 'storage and gpu', 'gpu and processor', 'powerful processor', 'fast ram', 'reliable storage', 'great gpu']) == ['processor', 'ram', 'storage', 'gpu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['processor', 'ram', 'storage', 'gpu'],responses = ['processor is powerful', 'ram is fast', 'storage is reliable', 'gpu is great', 'processor and ram', 'ram and storage', 'storage and gpu', 'gpu and processor', 'powerful processor', 'fast ram', 'reliable storage', 'great gpu']) == ['processor', 'ram', 'storage', 'gpu']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3 feature4 feature5', 'feature1 feature2 feature3 feature4', 'feature1 feature2 feature3', 'feature1 feature2', 'feature1', 'feature2 feature3 feature4 feature5', 'feature3 feature4 feature5', 'feature4 feature5', 'feature5', 'feature2 feature1', 'feature3 feature2 feature1', 'feature4 feature3 feature2 feature1', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature5 feature5 feature5', 'feature4 feature4 feature4 feature4 feature4', 'feature3 feature3 feature3 feature3 feature3', 'feature2 feature2 feature2 feature2 feature2', 'feature1 feature1 feature1 feature1 feature1']) == ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3 feature4 feature5', 'feature1 feature2 feature3 feature4', 'feature1 feature2 feature3', 'feature1 feature2', 'feature1', 'feature2 feature3 feature4 feature5', 'feature3 feature4 feature5', 'feature4 feature5', 'feature5', 'feature2 feature1', 'feature3 feature2 feature1', 'feature4 feature3 feature2 feature1', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature5 feature5 feature5', 'feature4 feature4 feature4 feature4 feature4', 'feature3 feature3 feature3 feature3 feature3', 'feature2 feature2 feature2 feature2 feature2', 'feature1 feature1 feature1 feature1 feature1']) == ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2', 'feature3 feature3 feature3', 'feature4 feature4', 'feature5', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature4 feature4 feature3 feature3 feature2 feature2 feature1 feature1', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature2 feature3 feature4 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2', 'feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3', 'feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1 feature1']) == ['feature5', 'feature1', 'feature2', 'feature3', 'feature4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2', 'feature3 feature3 feature3', 'feature4 feature4', 'feature5', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature4 feature4 feature3 feature3 feature2 feature2 feature1 feature1', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature2 feature3 feature4 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2', 'feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3', 'feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1 feature1']) == ['feature5', 'feature1', 'feature2', 'feature3', 'feature4']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['performance', 'battery', 'design', 'price'],responses = ['performance is key', 'battery long life', 'design aesthetic', 'price reasonable', 'performance matters', 'battery backup', 'design modern', 'price great', 'performance great', 'battery good', 'design sleek', 'price affordable', 'performance', 'battery', 'design', 'price', 'performance', 'battery', 'design', 'price']) == ['performance', 'battery', 'design', 'price']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['performance', 'battery', 'design', 'price'],responses = ['performance is key', 'battery long life', 'design aesthetic', 'price reasonable', 'performance matters', 'battery backup', 'design modern', 'price great', 'performance great', 'battery good', 'design sleek', 'price affordable', 'performance', 'battery', 'design', 'price', 'performance', 'battery', 'design', 'price']) == ['performance', 'battery', 'design', 'price']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['camera', 'battery', 'screen', 'processor'],responses = ['battery good battery', 'screen very good', 'processor is fast', 'screen screen screen', 'camera great shot']) == ['screen', 'camera', 'battery', 'processor']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['camera', 'battery', 'screen', 'processor'],responses = ['battery good battery', 'screen very good', 'processor is fast', 'screen screen screen', 'camera great shot']) == ['screen', 'camera', 'battery', 'processor']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['fast', 'efficient', 'reliable', 'user-friendly'],responses = ['very fast and efficient', 'reliable and user-friendly', 'user-friendly design', 'fast processing', 'efficient battery', 'reliable connection', 'fast and reliable', 'user-friendly interface', 'efficient performance', 'fast and user-friendly', 'reliable and efficient']) == ['fast', 'efficient', 'reliable', 'user-friendly']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['fast', 'efficient', 'reliable', 'user-friendly'],responses = ['very fast and efficient', 'reliable and user-friendly', 'user-friendly design', 'fast processing', 'efficient battery', 'reliable connection', 'fast and reliable', 'user-friendly interface', 'efficient performance', 'fast and user-friendly', 'reliable and efficient']) == ['fast', 'efficient', 'reliable', 'user-friendly']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['color', 'material', 'size', 'weight'],responses = ['colorful design', 'material quality is great', 'size is perfect', 'weight is fine', 'color and material', 'size and weight', 'material and color', 'weight and size', 'color size weight material', 'size color weight material', 'weight material color size', 'material color size weight', 'color material size weight', 'size weight color material', 'weight color material size']) == ['material', 'size', 'weight', 'color']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['color', 'material', 'size', 'weight'],responses = ['colorful design', 'material quality is great', 'size is perfect', 'weight is fine', 'color and material', 'size and weight', 'material and color', 'weight and size', 'color size weight material', 'size color weight material', 'weight material color size', 'material color size weight', 'color material size weight', 'size weight color material', 'weight color material size']) == ['material', 'size', 'weight', 'color']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'nfc'],responses = ['wifi is important wifi', 'bluetooth for connectivity', 'nfc useful', 'wifi and bluetooth', 'wifi wifi wifi', 'nfc nfc nfc nfc']) == ['wifi', 'bluetooth', 'nfc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'nfc'],responses = ['wifi is important wifi', 'bluetooth for connectivity', 'nfc useful', 'wifi and bluetooth', 'wifi wifi wifi', 'nfc nfc nfc nfc']) == ['wifi', 'bluetooth', 'nfc']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4 feature5', 'feature1 feature4', 'feature5 feature1 feature3', 'feature3 feature4 feature5', 'feature2 feature1 feature5', 'feature4 feature2 feature1', 'feature3 feature5 feature1', 'feature5 feature4 feature3', 'feature1 feature2 feature3 feature4 feature5']) == ['feature1', 'feature3', 'feature5', 'feature4', 'feature2']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4 feature5', 'feature1 feature4', 'feature5 feature1 feature3', 'feature3 feature4 feature5', 'feature2 feature1 feature5', 'feature4 feature2 feature1', 'feature3 feature5 feature1', 'feature5 feature4 feature3', 'feature1 feature2 feature3 feature4 feature5']) == ['feature1', 'feature3', 'feature5', 'feature4', 'feature2']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['storage', 'processor', 'battery', 'design'],responses = ['storage important', 'processor fast', 'battery long', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design']) == ['storage', 'processor', 'battery', 'design']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['storage', 'processor', 'battery', 'design'],responses = ['storage important', 'processor fast', 'battery long', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design']) == ['storage', 'processor', 'battery', 'design']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['featureX', 'featureY', 'featureZ'],responses = ['featureX featureY featureZ featureX featureY featureZ', 'featureX featureY featureZ featureX featureY', 'featureX featureY featureZ', 'featureX featureY', 'featureX', 'featureY featureZ', 'featureZ', 'featureY', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ']) == ['featureY', 'featureX', 'featureZ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['featureX', 'featureY', 'featureZ'],responses = ['featureX featureY featureZ featureX featureY featureZ', 'featureX featureY featureZ featureX featureY', 'featureX featureY featureZ', 'featureX featureY', 'featureX', 'featureY featureZ', 'featureZ', 'featureY', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ']) == ['featureY', 'featureX', 'featureZ']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['touch', 'gesture', 'voice', 'face', 'fingerprint'],responses = ['touch and gesture controls are awesome', 'voice recognition is cool', 'face recognition is secure', 'fingerprint sensor is fast', 'touch and fingerprint are the best', 'gesture and voice controls are convenient', 'voice and face recognition are top', 'fingerprint is reliable', 'touch and gesture are amazing']) == ['touch', 'gesture', 'voice', 'fingerprint', 'face']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['touch', 'gesture', 'voice', 'face', 'fingerprint'],responses = ['touch and gesture controls are awesome', 'voice recognition is cool', 'face recognition is secure', 'fingerprint sensor is fast', 'touch and fingerprint are the best', 'gesture and voice controls are convenient', 'voice and face recognition are top', 'fingerprint is reliable', 'touch and gesture are amazing']) == ['touch', 'gesture', 'voice', 'fingerprint', 'face']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['fastcharging', 'waterproof', 'hdmi', 'nfc'],responses = ['fastcharging', 'waterproof hdmi', 'fastcharging nfc', 'hdmi fastcharging', 'waterproof fastcharging hdmi', 'nfc hdmi', 'fastcharging fastcharging fastcharging', 'waterproof waterproof', 'hdmi hdmi hdmi hdmi', 'nfc nfc nfc nfc nfc', 'waterproof fastcharging nfc hdmi hdmi hdmi', 'fastcharging fastcharging fastcharging fastcharging', 'waterproof waterproof waterproof fastcharging', 'hdmi fastcharging fastcharging nfc', 'nfc nfc nfc fastcharging fastcharging', 'fastcharging fastcharging fastcharging fastcharging fastcharging']) == ['fastcharging', 'hdmi', 'nfc', 'waterproof']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['fastcharging', 'waterproof', 'hdmi', 'nfc'],responses = ['fastcharging', 'waterproof hdmi', 'fastcharging nfc', 'hdmi fastcharging', 'waterproof fastcharging hdmi', 'nfc hdmi', 'fastcharging fastcharging fastcharging', 'waterproof waterproof', 'hdmi hdmi hdmi hdmi', 'nfc nfc nfc nfc nfc', 'waterproof fastcharging nfc hdmi hdmi hdmi', 'fastcharging fastcharging fastcharging fastcharging', 'waterproof waterproof waterproof fastcharging', 'hdmi fastcharging fastcharging nfc', 'nfc nfc nfc fastcharging fastcharging', 'fastcharging fastcharging fastcharging fastcharging fastcharging']) == ['fastcharging', 'hdmi', 'nfc', 'waterproof']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['performance', 'battery', 'camera', 'display'],responses = ['i love the performance and camera', 'battery is good performance', 'camera performance', 'display', 'battery battery battery', 'performance display camera', 'display and battery', 'camera and display']) == ['performance', 'camera', 'display', 'battery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['performance', 'battery', 'camera', 'display'],responses = ['i love the performance and camera', 'battery is good performance', 'camera performance', 'display', 'battery battery battery', 'performance display camera', 'display and battery', 'camera and display']) == ['performance', 'camera', 'display', 'battery']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi is great and wifi', 'bluetooth is not bad', 'battery life is good', 'camera quality is high', 'wifi and camera', 'battery and bluetooth', 'camera and wifi']) == ['wifi', 'camera', 'bluetooth', 'battery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi is great and wifi', 'bluetooth is not bad', 'battery life is good', 'camera quality is high', 'wifi and camera', 'battery and bluetooth', 'camera and wifi']) == ['wifi', 'camera', 'bluetooth', 'battery']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi battery wifi', 'bluetooth camera', 'battery wifi camera', 'battery battery battery', 'camera wifi bluetooth']) == ['wifi', 'battery', 'camera', 'bluetooth']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi battery wifi', 'bluetooth camera', 'battery wifi camera', 'battery battery battery', 'camera wifi bluetooth']) == ['wifi', 'battery', 'camera', 'bluetooth']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'battery', 'camera', 'screen'],responses = ['battery is great', 'wifi and battery', 'screen screen', 'camera and wifi', 'battery and screen', 'wifi wifi wifi', 'camera is better than screen', 'battery battery battery', 'screen and wifi', 'camera and screen', 'battery screen wifi']) == ['screen', 'wifi', 'battery', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'battery', 'camera', 'screen'],responses = ['battery is great', 'wifi and battery', 'screen screen', 'camera and wifi', 'battery and screen', 'wifi wifi wifi', 'camera is better than screen', 'battery battery battery', 'screen and wifi', 'camera and screen', 'battery screen wifi']) == ['screen', 'wifi', 'battery', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'nfc', 'usb'],responses = ['wifi', 'bluetooth wifi', 'wifi wifi wifi', 'nfc usb', 'bluetooth', 'usb nfc nfc wifi']) == ['wifi', 'bluetooth', 'nfc', 'usb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'nfc', 'usb'],responses = ['wifi', 'bluetooth wifi', 'wifi wifi wifi', 'nfc usb', 'bluetooth', 'usb nfc nfc wifi']) == ['wifi', 'bluetooth', 'nfc', 'usb']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['screen', 'battery', 'ram', 'storage'],responses = ['screen battery ram storage', 'battery storage', 'ram ram ram', 'screen screen screen', 'battery battery battery', 'storage storage', 'ram screen battery', 'screen storage ram battery', 'ram ram ram ram', 'screen battery screen battery', 'ram storage ram storage', 'battery battery ram ram', 'screen storage storage storage', 'ram ram screen screen battery battery battery', 'storage ram battery screen']) == ['battery', 'ram', 'screen', 'storage']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['screen', 'battery', 'ram', 'storage'],responses = ['screen battery ram storage', 'battery storage', 'ram ram ram', 'screen screen screen', 'battery battery battery', 'storage storage', 'ram screen battery', 'screen storage ram battery', 'ram ram ram ram', 'screen battery screen battery', 'ram storage ram storage', 'battery battery ram ram', 'screen storage storage storage', 'ram ram screen screen battery battery battery', 'storage ram battery screen']) == ['battery', 'ram', 'screen', 'storage']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['performance', 'battery', 'display', 'camera'],responses = ['battery display', 'camera performance battery', 'battery battery battery', 'display display', 'performance performance performance performance', 'camera display battery performance', 'performance battery display']) == ['battery', 'performance', 'display', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['performance', 'battery', 'display', 'camera'],responses = ['battery display', 'camera performance battery', 'battery battery battery', 'display display', 'performance performance performance performance', 'camera display battery performance', 'performance battery display']) == ['battery', 'performance', 'display', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4', 'feature3 feature4 feature5', 'feature4 feature5 feature1', 'feature5 feature1 feature2', 'feature1 feature3 feature5', 'feature2 feature4 feature1', 'feature3 feature5 feature2', 'feature4 feature1 feature3', 'feature5 feature2 feature4', 'feature1 feature2 feature4', 'feature2 feature3 feature5', 'feature3 feature1 feature4', 'feature4 feature2 feature5', 'feature5 feature3 feature1', 'feature1 feature4 feature2', 'feature2 feature5 feature3', 'feature3 feature1 feature5', 'feature4 feature3 feature2', 'feature5 feature4 feature1', 'feature1 feature5 feature2', 'feature2 feature1 feature3', 'feature3 feature2 feature4', 'feature4 feature5 feature3', 'feature5 feature4 feature2', 'feature1 feature3 feature4', 'feature2 feature4 feature5', 'feature3 feature5 feature1', 'feature4 feature1 feature2', 'feature5 feature2 feature3']) == ['feature2', 'feature3', 'feature4', 'feature5', 'feature1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4', 'feature3 feature4 feature5', 'feature4 feature5 feature1', 'feature5 feature1 feature2', 'feature1 feature3 feature5', 'feature2 feature4 feature1', 'feature3 feature5 feature2', 'feature4 feature1 feature3', 'feature5 feature2 feature4', 'feature1 feature2 feature4', 'feature2 feature3 feature5', 'feature3 feature1 feature4', 'feature4 feature2 feature5', 'feature5 feature3 feature1', 'feature1 feature4 feature2', 'feature2 feature5 feature3', 'feature3 feature1 feature5', 'feature4 feature3 feature2', 'feature5 feature4 feature1', 'feature1 feature5 feature2', 'feature2 feature1 feature3', 'feature3 feature2 feature4', 'feature4 feature5 feature3', 'feature5 feature4 feature2', 'feature1 feature3 feature4', 'feature2 feature4 feature5', 'feature3 feature5 feature1', 'feature4 feature1 feature2', 'feature5 feature2 feature3']) == ['feature2', 'feature3', 'feature4', 'feature5', 'feature1']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['abcd', 'abcde', 'abcdef', 'abcdefg'],responses = ['abcd abcde abcdef abcdefg', 'abcde abcdefg', 'abcdefg abcd', 'abcdef abcde abcd', 'abcd abcde abcd abcd', 'abcde abcde abcde', 'abcdefg abcdefg abcdefg', 'abcd abcd abcd abcd', 'abcde abcde', 'abcdef abcdef', 'abcdefg abcdefg']) == ['abcde', 'abcd', 'abcdefg', 'abcdef']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['abcd', 'abcde', 'abcdef', 'abcdefg'],responses = ['abcd abcde abcdef abcdefg', 'abcde abcdefg', 'abcdefg abcd', 'abcdef abcde abcd', 'abcd abcde abcd abcd', 'abcde abcde abcde', 'abcdefg abcdefg abcdefg', 'abcd abcd abcd abcd', 'abcde abcde', 'abcdef abcdef', 'abcdefg abcdefg']) == ['abcde', 'abcd', 'abcdefg', 'abcdef']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['usb', 'bluetooth', 'wifi', 'battery', 'camera'],responses = ['i love the camera and the usb', 'bluetooth is great', 'wifi is essential', 'battery life is good', 'i need a good camera and bluetooth', 'wifi and battery are very important', 'usb is fast']) == ['usb', 'bluetooth', 'wifi', 'battery', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['usb', 'bluetooth', 'wifi', 'battery', 'camera'],responses = ['i love the camera and the usb', 'bluetooth is great', 'wifi is essential', 'battery life is good', 'i need a good camera and bluetooth', 'wifi and battery are very important', 'usb is fast']) == ['usb', 'bluetooth', 'wifi', 'battery', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['battery', 'display', 'camera', 'processor'],responses = ['battery display', 'camera processor camera', 'processor battery battery', 'display display processor', 'battery camera processor display']) == ['processor', 'battery', 'display', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['battery', 'display', 'camera', 'processor'],responses = ['battery display', 'camera processor camera', 'processor battery battery', 'display display processor', 'battery camera processor display']) == ['processor', 'battery', 'display', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['fast', 'powerful', 'efficient'],responses = ['fast fast fast', 'powerful powerful', 'efficient fast powerful', 'efficient efficient', 'fast powerful efficient', 'powerful fast', 'efficient powerful fast', 'fast powerful', 'powerful efficient', 'efficient fast']) == ['fast', 'powerful', 'efficient']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['fast', 'powerful', 'efficient'],responses = ['fast fast fast', 'powerful powerful', 'efficient fast powerful', 'efficient efficient', 'fast powerful efficient', 'powerful fast', 'efficient powerful fast', 'fast powerful', 'powerful efficient', 'efficient fast']) == ['fast', 'powerful', 'efficient']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['voice', 'siri', 'alexa', 'google'],responses = ['voice recognition is important', 'siri is my favorite', 'alexa works well', 'google voice is great', 'voice control', 'siri siri', 'alexa alexa', 'google google', 'voice and siri', 'voice and alexa', 'voice and google', 'siri and alexa', 'siri and google', 'alexa and google']) == ['voice', 'siri', 'alexa', 'google']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['voice', 'siri', 'alexa', 'google'],responses = ['voice recognition is important', 'siri is my favorite', 'alexa works well', 'google voice is great', 'voice control', 'siri siri', 'alexa alexa', 'google google', 'voice and siri', 'voice and alexa', 'voice and google', 'siri and alexa', 'siri and google', 'alexa and google']) == ['voice', 'siri', 'alexa', 'google']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['longevity', 'performance', 'design', 'ecoFriendly'],responses = ['longevity matters', 'performance is key', 'design is crucial', 'ecoFriendly is important', 'longevity and performance', 'design and ecoFriendly', 'performance and design', 'ecoFriendly and longevity', 'longevity longevity', 'performance performance', 'design design', 'ecoFriendly ecoFriendly', 'longevity performance design ecoFriendly', 'ecoFriendly performance design longevity', 'design performance longevity ecoFriendly']) == ['longevity', 'performance', 'design', 'ecoFriendly']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['longevity', 'performance', 'design', 'ecoFriendly'],responses = ['longevity matters', 'performance is key', 'design is crucial', 'ecoFriendly is important', 'longevity and performance', 'design and ecoFriendly', 'performance and design', 'ecoFriendly and longevity', 'longevity longevity', 'performance performance', 'design design', 'ecoFriendly ecoFriendly', 'longevity performance design ecoFriendly', 'ecoFriendly performance design longevity', 'design performance longevity ecoFriendly']) == ['longevity', 'performance', 'design', 'ecoFriendly']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['waterproof', 'fast_charging', 'durable', 'water_resistant'],responses = ['waterproof is great', 'fast charging is nice', 'durable build', 'water resistant', 'waterproof and fast charging', 'fast charging and durable', 'durable and water resistant', 'water resistant and fast charging', 'fast charging', 'durable', 'waterproof', 'water resistant', 'great fast charging', 'nice durable', 'great durable', 'waterproof build']) == ['durable', 'waterproof', 'fast_charging', 'water_resistant']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['waterproof', 'fast_charging', 'durable', 'water_resistant'],responses = ['waterproof is great', 'fast charging is nice', 'durable build', 'water resistant', 'waterproof and fast charging', 'fast charging and durable', 'durable and water resistant', 'water resistant and fast charging', 'fast charging', 'durable', 'waterproof', 'water resistant', 'great fast charging', 'nice durable', 'great durable', 'waterproof build']) == ['durable', 'waterproof', 'fast_charging', 'water_resistant']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['speed', 'storage', 'battery', 'screen'],responses = ['speed is fast', 'storage is plenty', 'battery lasts long', 'screen is beautiful', 'speed and storage', 'battery and screen', 'fast speed', 'beautiful screen', 'plenty of storage']) == ['speed', 'storage', 'screen', 'battery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['speed', 'storage', 'battery', 'screen'],responses = ['speed is fast', 'storage is plenty', 'battery lasts long', 'screen is beautiful', 'speed and storage', 'battery and screen', 'fast speed', 'beautiful screen', 'plenty of storage']) == ['speed', 'storage', 'screen', 'battery']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['battery', 'display', 'camera', 'processor', 'memory'],responses = ['battery display memory', 'camera processor camera', 'processor battery', 'display display processor', 'battery camera processor', 'memory battery', 'memory processor display', 'camera battery wifi']) == ['battery', 'processor', 'display', 'camera', 'memory']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['battery', 'display', 'camera', 'processor', 'memory'],responses = ['battery display memory', 'camera processor camera', 'processor battery', 'display display processor', 'battery camera processor', 'memory battery', 'memory processor display', 'camera battery wifi']) == ['battery', 'processor', 'display', 'camera', 'memory']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'camera', 'battery'],responses = ['i love the wifi and battery', 'battery life is amazing', 'camera is awesome', 'bluetooth is not needed', 'wifi and battery are crucial', 'camera quality is top notch']) == ['battery', 'wifi', 'camera', 'bluetooth']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'camera', 'battery'],responses = ['i love the wifi and battery', 'battery life is amazing', 'camera is awesome', 'bluetooth is not needed', 'wifi and battery are crucial', 'camera quality is top notch']) == ['battery', 'wifi', 'camera', 'bluetooth']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['performance', 'price', 'design', 'durability'],responses = ['performance price', 'price design', 'durability performance', 'design and performance', 'performance price durability', 'price price price', 'design design design', 'performance and durability', 'durability', 'price and design', 'performance and design', 'performance and price', 'design performance price', 'durability and design', 'performance', 'price', 'design', 'durability', 'performance design', 'performance price durability', 'price and performance', 'design and price', 'durability and price', 'performance price design', 'performance design price', 'price design performance', 'design price performance', 'price performance design', 'performance durability', 'durability performance', 'design performance', 'price performance', 'performance price', 'price design', 'design price']) == ['performance', 'price', 'design', 'durability']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['performance', 'price', 'design', 'durability'],responses = ['performance price', 'price design', 'durability performance', 'design and performance', 'performance price durability', 'price price price', 'design design design', 'performance and durability', 'durability', 'price and design', 'performance and design', 'performance and price', 'design performance price', 'durability and design', 'performance', 'price', 'design', 'durability', 'performance design', 'performance price durability', 'price and performance', 'design and price', 'durability and price', 'performance price design', 'performance design price', 'price design performance', 'design price performance', 'price performance design', 'performance durability', 'durability performance', 'design performance', 'price performance', 'performance price', 'price design', 'design price']) == ['performance', 'price', 'design', 'durability']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['speed', 'size', 'weight', 'durability'],responses = ['speed size weight', 'size weight', 'weight durability', 'speed weight', 'size speed weight durability', 'weight weight weight', 'speed size speed', 'size size size', 'durability weight', 'speed speed speed speed', 'weight durability size', 'size speed weight', 'durability size weight', 'weight speed', 'speed durability', 'durability speed size', 'size durability weight', 'weight size durability', 'speed size', 'size weight speed durability', 'weight size speed', 'speed weight size', 'size weight speed', 'speed weight', 'size weight durability', 'weight durability speed', 'durability speed weight', 'speed weight', 'weight size durability', 'size weight speed', 'weight speed size', 'size weight speed', 'speed size weight', 'weight speed size', 'size weight speed', 'weight speed size', 'speed size weight']) == ['weight', 'speed', 'size', 'durability']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['speed', 'size', 'weight', 'durability'],responses = ['speed size weight', 'size weight', 'weight durability', 'speed weight', 'size speed weight durability', 'weight weight weight', 'speed size speed', 'size size size', 'durability weight', 'speed speed speed speed', 'weight durability size', 'size speed weight', 'durability size weight', 'weight speed', 'speed durability', 'durability speed size', 'size durability weight', 'weight size durability', 'speed size', 'size weight speed durability', 'weight size speed', 'speed weight size', 'size weight speed', 'speed weight', 'size weight durability', 'weight durability speed', 'durability speed weight', 'speed weight', 'weight size durability', 'size weight speed', 'weight speed size', 'size weight speed', 'speed size weight', 'weight speed size', 'size weight speed', 'weight speed size', 'speed size weight']) == ['weight', 'speed', 'size', 'durability']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['fast', 'lightweight', 'durable', 'portable'],responses = ['fast and lightweight', 'fast but not durable', 'lightweight and portable', 'durable and fast', 'portable and lightweight', 'portable and durable', 'fast fast fast', 'lightweight lightweight', 'durable durable', 'portable portable']) == ['fast', 'lightweight', 'durable', 'portable']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['fast', 'lightweight', 'durable', 'portable'],responses = ['fast and lightweight', 'fast but not durable', 'lightweight and portable', 'durable and fast', 'portable and lightweight', 'portable and durable', 'fast fast fast', 'lightweight lightweight', 'durable durable', 'portable portable']) == ['fast', 'lightweight', 'durable', 'portable']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD', 'featureA featureB featureC', 'featureA featureB', 'featureA']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD', 'featureA featureB featureC', 'featureA featureB', 'featureA']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['longevity', 'battery', 'screen', 'charging'],responses = ['battery life is long', 'screen is large', 'charging fast', 'longevity matters', 'battery good', 'screen vibrant', 'charging good', 'longevity long', 'charging quick', 'battery efficient']) == ['battery', 'charging', 'longevity', 'screen']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['longevity', 'battery', 'screen', 'charging'],responses = ['battery life is long', 'screen is large', 'charging fast', 'longevity matters', 'battery good', 'screen vibrant', 'charging good', 'longevity long', 'charging quick', 'battery efficient']) == ['battery', 'charging', 'longevity', 'screen']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search'],responses = ['voice recognition', 'voice control', 'voice assistant', 'voice search', 'voice recognition and control', 'voice assistant and search', 'voice control and assistant', 'voice search and recognition', 'voice assistant', 'voice control', 'voice recognition', 'voice search', 'voice assistant and control', 'voice control and search', 'voice recognition and assistant', 'voice search and control']) == ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search'],responses = ['voice recognition', 'voice control', 'voice assistant', 'voice search', 'voice recognition and control', 'voice assistant and search', 'voice control and assistant', 'voice search and recognition', 'voice assistant', 'voice control', 'voice recognition', 'voice search', 'voice assistant and control', 'voice control and search', 'voice recognition and assistant', 'voice search and control']) == ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['great wifi and bluetooth', 'camera is awesome', 'battery life is good', 'bluetooth and wifi', 'wifi wifi wifi', 'camera quality', 'battery not bad']) == ['wifi', 'bluetooth', 'battery', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['great wifi and bluetooth', 'camera is awesome', 'battery life is good', 'bluetooth and wifi', 'wifi wifi wifi', 'camera quality', 'battery not bad']) == ['wifi', 'bluetooth', 'battery', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['storage', 'ram', 'battery', 'processor', 'camera'],responses = ['storage is the most important', 'ram and battery are crucial', 'processor speed is vital', 'camera quality is great', 'storage and ram are essential', 'battery and camera are top', 'processor and design matter', 'storage and battery are key', 'ram and processor should be fast']) == ['storage', 'ram', 'battery', 'processor', 'camera']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['storage', 'ram', 'battery', 'processor', 'camera'],responses = ['storage is the most important', 'ram and battery are crucial', 'processor speed is vital', 'camera quality is great', 'storage and ram are essential', 'battery and camera are top', 'processor and design matter', 'storage and battery are key', 'ram and processor should be fast']) == ['storage', 'ram', 'battery', 'processor', 'camera']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['storage', 'speed', 'camera', 'battery'],responses = ['storage space', 'speed is important', 'camera quality', 'battery life', 'storage large', 'speed quick', 'camera resolution', 'battery good', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery']) == ['storage', 'speed', 'camera', 'battery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['storage', 'speed', 'camera', 'battery'],responses = ['storage space', 'speed is important', 'camera quality', 'battery life', 'storage large', 'speed quick', 'camera resolution', 'battery good', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery']) == ['storage', 'speed', 'camera', 'battery']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['fast', 'reliable', 'secure', 'user-friendly', 'efficient'],responses = ['fast and reliable', 'reliable and secure', 'secure and user-friendly', 'user-friendly and efficient', 'efficient and fast', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast']) == ['user-friendly', 'fast', 'efficient', 'secure', 'reliable']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['fast', 'reliable', 'secure', 'user-friendly', 'efficient'],responses = ['fast and reliable', 'reliable and secure', 'secure and user-friendly', 'user-friendly and efficient', 'efficient and fast', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast']) == ['user-friendly', 'fast', 'efficient', 'secure', 'reliable']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['waterproof', 'shockproof', 'longevity', 'performance', 'design'],responses = ['waterproof and shockproof are essential', 'longevity matters', 'performance is key', 'design should be sleek', 'waterproof and design are important', 'shockproof and longevity are crucial', 'performance and design should blend', 'waterproof and performance are top', 'shockproof and design are appealing']) == ['design', 'waterproof', 'shockproof', 'performance', 'longevity']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['waterproof', 'shockproof', 'longevity', 'performance', 'design'],responses = ['waterproof and shockproof are essential', 'longevity matters', 'performance is key', 'design should be sleek', 'waterproof and design are important', 'shockproof and longevity are crucial', 'performance and design should blend', 'waterproof and performance are top', 'shockproof and design are appealing']) == ['design', 'waterproof', 'shockproof', 'performance', 'longevity']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['alpha', 'beta', 'gamma', 'delta'],responses = ['epsilon zeta eta', 'theta iota kappa', 'lambda mu nu', 'xi omicron pi', 'rho sigma tau', 'upsilon phi chi', 'psi omega', 'alpha beta gamma delta', 'delta gamma beta alpha', 'alpha alpha alpha', 'beta beta beta', 'gamma gamma gamma', 'delta delta delta', 'alpha beta', 'beta gamma', 'gamma delta', 'delta alpha']) == ['alpha', 'beta', 'gamma', 'delta']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['alpha', 'beta', 'gamma', 'delta'],responses = ['epsilon zeta eta', 'theta iota kappa', 'lambda mu nu', 'xi omicron pi', 'rho sigma tau', 'upsilon phi chi', 'psi omega', 'alpha beta gamma delta', 'delta gamma beta alpha', 'alpha alpha alpha', 'beta beta beta', 'gamma gamma gamma', 'delta delta delta', 'alpha beta', 'beta gamma', 'gamma delta', 'delta alpha']) == ['alpha', 'beta', 'gamma', 'delta']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['speed', 'storage', 'screen', 'battery', 'design'],responses = ['speed storage', 'storage screen battery', 'battery battery battery', 'design design', 'speed speed speed speed', 'camera display battery performance', 'speed battery display', 'screen design', 'storage design', 'battery design', 'speed design', 'screen storage', 'speed storage battery', 'battery screen', 'battery screen speed', 'design speed storage battery screen', 'speed screen', 'speed storage battery screen', 'speed design battery', 'battery storage screen', 'speed storage battery', 'design speed battery', 'speed design storage battery', 'battery design speed', 'speed battery storage design']) == ['battery', 'speed', 'storage', 'design', 'screen']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['speed', 'storage', 'screen', 'battery', 'design'],responses = ['speed storage', 'storage screen battery', 'battery battery battery', 'design design', 'speed speed speed speed', 'camera display battery performance', 'speed battery display', 'screen design', 'storage design', 'battery design', 'speed design', 'screen storage', 'speed storage battery', 'battery screen', 'battery screen speed', 'design speed storage battery screen', 'speed screen', 'speed storage battery screen', 'speed design battery', 'battery storage screen', 'speed storage battery', 'design speed battery', 'speed design storage battery', 'battery design speed', 'speed battery storage design']) == ['battery', 'speed', 'storage', 'design', 'screen']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['waterproof', 'durable', 'lightweight', 'compact'],responses = ['waterproof and durable', 'lightweight and compact', 'waterproof design', 'durable build', 'lightweight and durable', 'compact and waterproof', 'waterproof and compact', 'lightweight design', 'durable and compact', 'waterproof and lightweight', 'compact and durable', 'durable and lightweight', 'lightweight and waterproof', 'compact and lightweight', 'waterproof and durable and compact', 'durable and lightweight and waterproof']) == ['waterproof', 'durable', 'lightweight', 'compact']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['waterproof', 'durable', 'lightweight', 'compact'],responses = ['waterproof and durable', 'lightweight and compact', 'waterproof design', 'durable build', 'lightweight and durable', 'compact and waterproof', 'waterproof and compact', 'lightweight design', 'durable and compact', 'waterproof and lightweight', 'compact and durable', 'durable and lightweight', 'lightweight and waterproof', 'compact and lightweight', 'waterproof and durable and compact', 'durable and lightweight and waterproof']) == ['waterproof', 'durable', 'lightweight', 'compact']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['screen', 'processor', 'ram', 'storage', 'battery'],responses = ['processor is fast', 'ram is adequate', 'storage is good', 'battery life is amazing', 'screen is beautiful', 'processor and ram are the best', 'screen and battery are top notch', 'ram is key', 'storage and processor are vital']) == ['processor', 'ram', 'screen', 'storage', 'battery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['screen', 'processor', 'ram', 'storage', 'battery'],responses = ['processor is fast', 'ram is adequate', 'storage is good', 'battery life is amazing', 'screen is beautiful', 'processor and ram are the best', 'screen and battery are top notch', 'ram is key', 'storage and processor are vital']) == ['processor', 'ram', 'screen', 'storage', 'battery']: {e}')
    
    total += 1
    try:
        result = candidate(features = ['high-res', 'hdr', 'low-light', 'night-vision'],responses = ['high-res and hdr', 'low-light performance', 'night-vision is great', 'high-res low-light', 'hdr and night-vision', 'low-light and hdr', 'high-res and night-vision', 'night-vision', 'hdr', 'low-light', 'high-res', 'high-res hdr low-light night-vision', 'hdr low-light', 'night-vision hdr', 'low-light high-res', 'high-res night-vision', 'hdr high-res', 'low-light night-vision', 'night-vision low-light', 'hdr high-res low-light']) == ['low-light', 'high-res', 'hdr', 'night-vision']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(features = ['high-res', 'hdr', 'low-light', 'night-vision'],responses = ['high-res and hdr', 'low-light performance', 'night-vision is great', 'high-res low-light', 'hdr and night-vision', 'low-light and hdr', 'high-res and night-vision', 'night-vision', 'hdr', 'low-light', 'high-res', 'high-res hdr low-light night-vision', 'hdr low-light', 'night-vision hdr', 'low-light high-res', 'high-res night-vision', 'hdr high-res', 'low-light night-vision', 'night-vision low-light', 'hdr high-res low-light']) == ['low-light', 'high-res', 'hdr', 'night-vision']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(features = ['cooler', 'lock', 'touch'],responses = ['i like cooler cooler', 'lock touch cool', 'locker like touch']) == ['touch', 'cooler', 'lock']
    assert candidate(features = ['a', 'aa', 'b', 'c'],responses = ['a', 'a aa', 'a a a a a', 'b a']) == ['a', 'aa', 'b', 'c']
    assert candidate(features = ['processor', 'memory', 'storage', 'display'],responses = ['processor', 'memory processor', 'storage memory', 'display storage', 'processor memory storage display', 'memory memory memory', 'storage storage storage', 'display display display', 'processor processor', 'memory storage display', 'display memory processor', 'storage display memory', 'processor storage display memory', 'memory display storage', 'storage display memory processor']) == ['memory', 'storage', 'display', 'processor']
    assert candidate(features = ['long-lasting', 'portable', 'stylish', 'affordable'],responses = ['long-lasting battery', 'portable and stylish', 'affordable and long-lasting', 'stylish and portable', 'long-lasting and affordable', 'affordable design', 'portable battery', 'stylish battery', 'affordable battery', 'long-lasting and portable', 'stylish and long-lasting', 'affordable and stylish', 'portable and affordable', 'long-lasting portable', 'affordable stylish portable', 'long-lasting stylish', 'affordable long-lasting', 'stylish long-lasting portable', 'portable long-lasting', 'affordable and portable and stylish', 'long-lasting and affordable and portable', 'portable and affordable and stylish', 'stylish and affordable and long-lasting', 'affordable and long-lasting and portable and stylish']) == ['long-lasting', 'portable', 'affordable', 'stylish']
    assert candidate(features = ['processor', 'ram', 'storage', 'gpu'],responses = ['processor is powerful', 'ram is fast', 'storage is reliable', 'gpu is great', 'processor and ram', 'ram and storage', 'storage and gpu', 'gpu and processor', 'powerful processor', 'fast ram', 'reliable storage', 'great gpu']) == ['processor', 'ram', 'storage', 'gpu']
    assert candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3 feature4 feature5', 'feature1 feature2 feature3 feature4', 'feature1 feature2 feature3', 'feature1 feature2', 'feature1', 'feature2 feature3 feature4 feature5', 'feature3 feature4 feature5', 'feature4 feature5', 'feature5', 'feature2 feature1', 'feature3 feature2 feature1', 'feature4 feature3 feature2 feature1', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature5 feature5 feature5', 'feature4 feature4 feature4 feature4 feature4', 'feature3 feature3 feature3 feature3 feature3', 'feature2 feature2 feature2 feature2 feature2', 'feature1 feature1 feature1 feature1 feature1']) == ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
    assert candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2', 'feature3 feature3 feature3', 'feature4 feature4', 'feature5', 'feature5 feature4 feature3 feature2 feature1', 'feature5 feature5 feature4 feature4 feature3 feature3 feature2 feature2 feature1 feature1', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature2 feature3 feature4 feature5 feature5 feature5 feature5 feature5 feature5', 'feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1 feature1', 'feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2 feature2', 'feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3 feature3', 'feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4 feature4', 'feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5 feature5', 'feature5 feature4 feature3 feature2 feature1 feature1 feature1 feature1 feature1 feature1']) == ['feature5', 'feature1', 'feature2', 'feature3', 'feature4']
    assert candidate(features = ['performance', 'battery', 'design', 'price'],responses = ['performance is key', 'battery long life', 'design aesthetic', 'price reasonable', 'performance matters', 'battery backup', 'design modern', 'price great', 'performance great', 'battery good', 'design sleek', 'price affordable', 'performance', 'battery', 'design', 'price', 'performance', 'battery', 'design', 'price']) == ['performance', 'battery', 'design', 'price']
    assert candidate(features = ['camera', 'battery', 'screen', 'processor'],responses = ['battery good battery', 'screen very good', 'processor is fast', 'screen screen screen', 'camera great shot']) == ['screen', 'camera', 'battery', 'processor']
    assert candidate(features = ['fast', 'efficient', 'reliable', 'user-friendly'],responses = ['very fast and efficient', 'reliable and user-friendly', 'user-friendly design', 'fast processing', 'efficient battery', 'reliable connection', 'fast and reliable', 'user-friendly interface', 'efficient performance', 'fast and user-friendly', 'reliable and efficient']) == ['fast', 'efficient', 'reliable', 'user-friendly']
    assert candidate(features = ['color', 'material', 'size', 'weight'],responses = ['colorful design', 'material quality is great', 'size is perfect', 'weight is fine', 'color and material', 'size and weight', 'material and color', 'weight and size', 'color size weight material', 'size color weight material', 'weight material color size', 'material color size weight', 'color material size weight', 'size weight color material', 'weight color material size']) == ['material', 'size', 'weight', 'color']
    assert candidate(features = ['wifi', 'bluetooth', 'nfc'],responses = ['wifi is important wifi', 'bluetooth for connectivity', 'nfc useful', 'wifi and bluetooth', 'wifi wifi wifi', 'nfc nfc nfc nfc']) == ['wifi', 'bluetooth', 'nfc']
    assert candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4 feature5', 'feature1 feature4', 'feature5 feature1 feature3', 'feature3 feature4 feature5', 'feature2 feature1 feature5', 'feature4 feature2 feature1', 'feature3 feature5 feature1', 'feature5 feature4 feature3', 'feature1 feature2 feature3 feature4 feature5']) == ['feature1', 'feature3', 'feature5', 'feature4', 'feature2']
    assert candidate(features = ['storage', 'processor', 'battery', 'design'],responses = ['storage important', 'processor fast', 'battery long', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design', 'storage', 'processor', 'battery', 'design']) == ['storage', 'processor', 'battery', 'design']
    assert candidate(features = ['featureX', 'featureY', 'featureZ'],responses = ['featureX featureY featureZ featureX featureY featureZ', 'featureX featureY featureZ featureX featureY', 'featureX featureY featureZ', 'featureX featureY', 'featureX', 'featureY featureZ', 'featureZ', 'featureY', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ', 'featureX featureY featureZ']) == ['featureY', 'featureX', 'featureZ']
    assert candidate(features = ['touch', 'gesture', 'voice', 'face', 'fingerprint'],responses = ['touch and gesture controls are awesome', 'voice recognition is cool', 'face recognition is secure', 'fingerprint sensor is fast', 'touch and fingerprint are the best', 'gesture and voice controls are convenient', 'voice and face recognition are top', 'fingerprint is reliable', 'touch and gesture are amazing']) == ['touch', 'gesture', 'voice', 'fingerprint', 'face']
    assert candidate(features = ['fastcharging', 'waterproof', 'hdmi', 'nfc'],responses = ['fastcharging', 'waterproof hdmi', 'fastcharging nfc', 'hdmi fastcharging', 'waterproof fastcharging hdmi', 'nfc hdmi', 'fastcharging fastcharging fastcharging', 'waterproof waterproof', 'hdmi hdmi hdmi hdmi', 'nfc nfc nfc nfc nfc', 'waterproof fastcharging nfc hdmi hdmi hdmi', 'fastcharging fastcharging fastcharging fastcharging', 'waterproof waterproof waterproof fastcharging', 'hdmi fastcharging fastcharging nfc', 'nfc nfc nfc fastcharging fastcharging', 'fastcharging fastcharging fastcharging fastcharging fastcharging']) == ['fastcharging', 'hdmi', 'nfc', 'waterproof']
    assert candidate(features = ['performance', 'battery', 'camera', 'display'],responses = ['i love the performance and camera', 'battery is good performance', 'camera performance', 'display', 'battery battery battery', 'performance display camera', 'display and battery', 'camera and display']) == ['performance', 'camera', 'display', 'battery']
    assert candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi is great and wifi', 'bluetooth is not bad', 'battery life is good', 'camera quality is high', 'wifi and camera', 'battery and bluetooth', 'camera and wifi']) == ['wifi', 'camera', 'bluetooth', 'battery']
    assert candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['wifi battery wifi', 'bluetooth camera', 'battery wifi camera', 'battery battery battery', 'camera wifi bluetooth']) == ['wifi', 'battery', 'camera', 'bluetooth']
    assert candidate(features = ['wifi', 'battery', 'camera', 'screen'],responses = ['battery is great', 'wifi and battery', 'screen screen', 'camera and wifi', 'battery and screen', 'wifi wifi wifi', 'camera is better than screen', 'battery battery battery', 'screen and wifi', 'camera and screen', 'battery screen wifi']) == ['screen', 'wifi', 'battery', 'camera']
    assert candidate(features = ['wifi', 'bluetooth', 'nfc', 'usb'],responses = ['wifi', 'bluetooth wifi', 'wifi wifi wifi', 'nfc usb', 'bluetooth', 'usb nfc nfc wifi']) == ['wifi', 'bluetooth', 'nfc', 'usb']
    assert candidate(features = ['screen', 'battery', 'ram', 'storage'],responses = ['screen battery ram storage', 'battery storage', 'ram ram ram', 'screen screen screen', 'battery battery battery', 'storage storage', 'ram screen battery', 'screen storage ram battery', 'ram ram ram ram', 'screen battery screen battery', 'ram storage ram storage', 'battery battery ram ram', 'screen storage storage storage', 'ram ram screen screen battery battery battery', 'storage ram battery screen']) == ['battery', 'ram', 'screen', 'storage']
    assert candidate(features = ['performance', 'battery', 'display', 'camera'],responses = ['battery display', 'camera performance battery', 'battery battery battery', 'display display', 'performance performance performance performance', 'camera display battery performance', 'performance battery display']) == ['battery', 'performance', 'display', 'camera']
    assert candidate(features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'],responses = ['feature1 feature2 feature3', 'feature2 feature3 feature4', 'feature3 feature4 feature5', 'feature4 feature5 feature1', 'feature5 feature1 feature2', 'feature1 feature3 feature5', 'feature2 feature4 feature1', 'feature3 feature5 feature2', 'feature4 feature1 feature3', 'feature5 feature2 feature4', 'feature1 feature2 feature4', 'feature2 feature3 feature5', 'feature3 feature1 feature4', 'feature4 feature2 feature5', 'feature5 feature3 feature1', 'feature1 feature4 feature2', 'feature2 feature5 feature3', 'feature3 feature1 feature5', 'feature4 feature3 feature2', 'feature5 feature4 feature1', 'feature1 feature5 feature2', 'feature2 feature1 feature3', 'feature3 feature2 feature4', 'feature4 feature5 feature3', 'feature5 feature4 feature2', 'feature1 feature3 feature4', 'feature2 feature4 feature5', 'feature3 feature5 feature1', 'feature4 feature1 feature2', 'feature5 feature2 feature3']) == ['feature2', 'feature3', 'feature4', 'feature5', 'feature1']
    assert candidate(features = ['abcd', 'abcde', 'abcdef', 'abcdefg'],responses = ['abcd abcde abcdef abcdefg', 'abcde abcdefg', 'abcdefg abcd', 'abcdef abcde abcd', 'abcd abcde abcd abcd', 'abcde abcde abcde', 'abcdefg abcdefg abcdefg', 'abcd abcd abcd abcd', 'abcde abcde', 'abcdef abcdef', 'abcdefg abcdefg']) == ['abcde', 'abcd', 'abcdefg', 'abcdef']
    assert candidate(features = ['usb', 'bluetooth', 'wifi', 'battery', 'camera'],responses = ['i love the camera and the usb', 'bluetooth is great', 'wifi is essential', 'battery life is good', 'i need a good camera and bluetooth', 'wifi and battery are very important', 'usb is fast']) == ['usb', 'bluetooth', 'wifi', 'battery', 'camera']
    assert candidate(features = ['battery', 'display', 'camera', 'processor'],responses = ['battery display', 'camera processor camera', 'processor battery battery', 'display display processor', 'battery camera processor display']) == ['processor', 'battery', 'display', 'camera']
    assert candidate(features = ['fast', 'powerful', 'efficient'],responses = ['fast fast fast', 'powerful powerful', 'efficient fast powerful', 'efficient efficient', 'fast powerful efficient', 'powerful fast', 'efficient powerful fast', 'fast powerful', 'powerful efficient', 'efficient fast']) == ['fast', 'powerful', 'efficient']
    assert candidate(features = ['voice', 'siri', 'alexa', 'google'],responses = ['voice recognition is important', 'siri is my favorite', 'alexa works well', 'google voice is great', 'voice control', 'siri siri', 'alexa alexa', 'google google', 'voice and siri', 'voice and alexa', 'voice and google', 'siri and alexa', 'siri and google', 'alexa and google']) == ['voice', 'siri', 'alexa', 'google']
    assert candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD featureE']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']
    assert candidate(features = ['longevity', 'performance', 'design', 'ecoFriendly'],responses = ['longevity matters', 'performance is key', 'design is crucial', 'ecoFriendly is important', 'longevity and performance', 'design and ecoFriendly', 'performance and design', 'ecoFriendly and longevity', 'longevity longevity', 'performance performance', 'design design', 'ecoFriendly ecoFriendly', 'longevity performance design ecoFriendly', 'ecoFriendly performance design longevity', 'design performance longevity ecoFriendly']) == ['longevity', 'performance', 'design', 'ecoFriendly']
    assert candidate(features = ['waterproof', 'fast_charging', 'durable', 'water_resistant'],responses = ['waterproof is great', 'fast charging is nice', 'durable build', 'water resistant', 'waterproof and fast charging', 'fast charging and durable', 'durable and water resistant', 'water resistant and fast charging', 'fast charging', 'durable', 'waterproof', 'water resistant', 'great fast charging', 'nice durable', 'great durable', 'waterproof build']) == ['durable', 'waterproof', 'fast_charging', 'water_resistant']
    assert candidate(features = ['speed', 'storage', 'battery', 'screen'],responses = ['speed is fast', 'storage is plenty', 'battery lasts long', 'screen is beautiful', 'speed and storage', 'battery and screen', 'fast speed', 'beautiful screen', 'plenty of storage']) == ['speed', 'storage', 'screen', 'battery']
    assert candidate(features = ['battery', 'display', 'camera', 'processor', 'memory'],responses = ['battery display memory', 'camera processor camera', 'processor battery', 'display display processor', 'battery camera processor', 'memory battery', 'memory processor display', 'camera battery wifi']) == ['battery', 'processor', 'display', 'camera', 'memory']
    assert candidate(features = ['wifi', 'bluetooth', 'camera', 'battery'],responses = ['i love the wifi and battery', 'battery life is amazing', 'camera is awesome', 'bluetooth is not needed', 'wifi and battery are crucial', 'camera quality is top notch']) == ['battery', 'wifi', 'camera', 'bluetooth']
    assert candidate(features = ['performance', 'price', 'design', 'durability'],responses = ['performance price', 'price design', 'durability performance', 'design and performance', 'performance price durability', 'price price price', 'design design design', 'performance and durability', 'durability', 'price and design', 'performance and design', 'performance and price', 'design performance price', 'durability and design', 'performance', 'price', 'design', 'durability', 'performance design', 'performance price durability', 'price and performance', 'design and price', 'durability and price', 'performance price design', 'performance design price', 'price design performance', 'design price performance', 'price performance design', 'performance durability', 'durability performance', 'design performance', 'price performance', 'performance price', 'price design', 'design price']) == ['performance', 'price', 'design', 'durability']
    assert candidate(features = ['speed', 'size', 'weight', 'durability'],responses = ['speed size weight', 'size weight', 'weight durability', 'speed weight', 'size speed weight durability', 'weight weight weight', 'speed size speed', 'size size size', 'durability weight', 'speed speed speed speed', 'weight durability size', 'size speed weight', 'durability size weight', 'weight speed', 'speed durability', 'durability speed size', 'size durability weight', 'weight size durability', 'speed size', 'size weight speed durability', 'weight size speed', 'speed weight size', 'size weight speed', 'speed weight', 'size weight durability', 'weight durability speed', 'durability speed weight', 'speed weight', 'weight size durability', 'size weight speed', 'weight speed size', 'size weight speed', 'speed size weight', 'weight speed size', 'size weight speed', 'weight speed size', 'speed size weight']) == ['weight', 'speed', 'size', 'durability']
    assert candidate(features = ['fast', 'lightweight', 'durable', 'portable'],responses = ['fast and lightweight', 'fast but not durable', 'lightweight and portable', 'durable and fast', 'portable and lightweight', 'portable and durable', 'fast fast fast', 'lightweight lightweight', 'durable durable', 'portable portable']) == ['fast', 'lightweight', 'durable', 'portable']
    assert candidate(features = ['featureA', 'featureB', 'featureC', 'featureD', 'featureE'],responses = ['featureA featureB featureC featureD featureE featureA featureB featureC featureD featureE', 'featureA featureB featureC featureD', 'featureA featureB featureC', 'featureA featureB', 'featureA']) == ['featureA', 'featureB', 'featureC', 'featureD', 'featureE']
    assert candidate(features = ['longevity', 'battery', 'screen', 'charging'],responses = ['battery life is long', 'screen is large', 'charging fast', 'longevity matters', 'battery good', 'screen vibrant', 'charging good', 'longevity long', 'charging quick', 'battery efficient']) == ['battery', 'charging', 'longevity', 'screen']
    assert candidate(features = ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search'],responses = ['voice recognition', 'voice control', 'voice assistant', 'voice search', 'voice recognition and control', 'voice assistant and search', 'voice control and assistant', 'voice search and recognition', 'voice assistant', 'voice control', 'voice recognition', 'voice search', 'voice assistant and control', 'voice control and search', 'voice recognition and assistant', 'voice search and control']) == ['voice_recognition', 'voice_control', 'voice_assistant', 'voice_search']
    assert candidate(features = ['wifi', 'bluetooth', 'battery', 'camera'],responses = ['great wifi and bluetooth', 'camera is awesome', 'battery life is good', 'bluetooth and wifi', 'wifi wifi wifi', 'camera quality', 'battery not bad']) == ['wifi', 'bluetooth', 'battery', 'camera']
    assert candidate(features = ['storage', 'ram', 'battery', 'processor', 'camera'],responses = ['storage is the most important', 'ram and battery are crucial', 'processor speed is vital', 'camera quality is great', 'storage and ram are essential', 'battery and camera are top', 'processor and design matter', 'storage and battery are key', 'ram and processor should be fast']) == ['storage', 'ram', 'battery', 'processor', 'camera']
    assert candidate(features = ['storage', 'speed', 'camera', 'battery'],responses = ['storage space', 'speed is important', 'camera quality', 'battery life', 'storage large', 'speed quick', 'camera resolution', 'battery good', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery', 'storage', 'speed', 'camera', 'battery']) == ['storage', 'speed', 'camera', 'battery']
    assert candidate(features = ['fast', 'reliable', 'secure', 'user-friendly', 'efficient'],responses = ['fast and reliable', 'reliable and secure', 'secure and user-friendly', 'user-friendly and efficient', 'efficient and fast', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast reliable secure', 'reliable secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast', 'efficient fast reliable', 'fast secure user-friendly', 'secure user-friendly efficient', 'user-friendly efficient fast']) == ['user-friendly', 'fast', 'efficient', 'secure', 'reliable']
    assert candidate(features = ['waterproof', 'shockproof', 'longevity', 'performance', 'design'],responses = ['waterproof and shockproof are essential', 'longevity matters', 'performance is key', 'design should be sleek', 'waterproof and design are important', 'shockproof and longevity are crucial', 'performance and design should blend', 'waterproof and performance are top', 'shockproof and design are appealing']) == ['design', 'waterproof', 'shockproof', 'performance', 'longevity']
    assert candidate(features = ['alpha', 'beta', 'gamma', 'delta'],responses = ['epsilon zeta eta', 'theta iota kappa', 'lambda mu nu', 'xi omicron pi', 'rho sigma tau', 'upsilon phi chi', 'psi omega', 'alpha beta gamma delta', 'delta gamma beta alpha', 'alpha alpha alpha', 'beta beta beta', 'gamma gamma gamma', 'delta delta delta', 'alpha beta', 'beta gamma', 'gamma delta', 'delta alpha']) == ['alpha', 'beta', 'gamma', 'delta']
    assert candidate(features = ['speed', 'storage', 'screen', 'battery', 'design'],responses = ['speed storage', 'storage screen battery', 'battery battery battery', 'design design', 'speed speed speed speed', 'camera display battery performance', 'speed battery display', 'screen design', 'storage design', 'battery design', 'speed design', 'screen storage', 'speed storage battery', 'battery screen', 'battery screen speed', 'design speed storage battery screen', 'speed screen', 'speed storage battery screen', 'speed design battery', 'battery storage screen', 'speed storage battery', 'design speed battery', 'speed design storage battery', 'battery design speed', 'speed battery storage design']) == ['battery', 'speed', 'storage', 'design', 'screen']
    assert candidate(features = ['waterproof', 'durable', 'lightweight', 'compact'],responses = ['waterproof and durable', 'lightweight and compact', 'waterproof design', 'durable build', 'lightweight and durable', 'compact and waterproof', 'waterproof and compact', 'lightweight design', 'durable and compact', 'waterproof and lightweight', 'compact and durable', 'durable and lightweight', 'lightweight and waterproof', 'compact and lightweight', 'waterproof and durable and compact', 'durable and lightweight and waterproof']) == ['waterproof', 'durable', 'lightweight', 'compact']
    assert candidate(features = ['screen', 'processor', 'ram', 'storage', 'battery'],responses = ['processor is fast', 'ram is adequate', 'storage is good', 'battery life is amazing', 'screen is beautiful', 'processor and ram are the best', 'screen and battery are top notch', 'ram is key', 'storage and processor are vital']) == ['processor', 'ram', 'screen', 'storage', 'battery']
    assert candidate(features = ['high-res', 'hdr', 'low-light', 'night-vision'],responses = ['high-res and hdr', 'low-light performance', 'night-vision is great', 'high-res low-light', 'hdr and night-vision', 'low-light and hdr', 'high-res and night-vision', 'night-vision', 'hdr', 'low-light', 'high-res', 'high-res hdr low-light night-vision', 'hdr low-light', 'night-vision hdr', 'low-light high-res', 'high-res night-vision', 'hdr high-res', 'low-light night-vision', 'night-vision low-light', 'hdr high-res low-light']) == ['low-light', 'high-res', 'hdr', 'night-vision']


