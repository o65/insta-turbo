import requests
import threading
import ctypes
attempt = 0
print('[+] Instagram Developer : @_m3gon')
req_banner = requests.get(f'http://artii.herokuapp.com/make?text=Insta-Turbo').text
print(req_banner)
class Instagram_Turbo():
    def endpoint_original():
        url_original = 'https://i.instagram.com'
        headers_original = {
            'Host': 'i.instagram.com',
            'User-Agent': 'Instagram 187.0.0.32.120 Android (25/7.1.2; 191dpi; 576x1024; OnePlus; A5010; A5010; intel; en_US; 289692181)',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close'
        }
        def login():
            username_login = input('[?] Enter Username Or Email To Login : ')
            password = input('[?] Enter Password : ')
            url_login = 'https://www.instagram.com/accounts/login/ajax/'
            headers_login = {
                'Host': 'www.instagram.com',
                'Cookie': 'ig_did=E1069C00-B44A-4C3C-AEC6-2EDFF828476E; mid=YFNJ-gALAAFOnl3VaylOWdyOj2VX; ig_nrcb=1; shbid="17013\054276667561\0541659931001:01f7894c18f566b4a13bf44ec754a89ab5e70b284abfdaa86e854cba543963bdad4f0657"; shbts="1628395001\054276667561\0541659931001:01f7a20b2625348db96b5a70f0b98c9da100569a029e1c074df214ebb68c27647114bb8f"; ds_user_id=280463934; csrftoken=RCAOU1Rz7MDb0qn7bLZnQkwDItWu1f12; rur="ASH\054280463934\0541659951357:01f7b87cf3b5f32846055d33c2720a189f32a1d66a9e72ca9ac6071fc1717ddbb0d09631"',
                'Content-Length': '340',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                'X-Ig-Www-Claim': 'hmac.AR0T5C4sOWM9xlkDQI4gJT47mdQ2vI9HGQz4uHlblZbZZ1OY',
                'Sec-Ch-Ua-Mobile': '?0',
                'X-Instagram-Ajax': '7db165a66390',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'X-Asbd-Id': '437806',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                'X-Csrftoken': 'RCAOU1Rz7MDb0qn7bLZnQkwDItWu1f12',
                'X-Ig-App-Id': '936619743392459',
                'Origin': 'https://www.instagram.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.instagram.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9'
            }
            data_login = f'username={username_login}&enc_password=#PWD_INSTAGRAM_BROWSER:0:1628416704:{password}&queryParams=%7B%7D&optIntoOneTap=false&stopDeletionNonce=&trustedDeviceRecords=%7B%7D'
            req_login = requests.post(url_login, headers=headers_login, data=data_login)
            if ('"authenticated":true') in req_login.text:
                print('[+] Done Login')
                sessionid = req_login.cookies['sessionid']
                MessageBox = ctypes.windll.user32.MessageBoxW
                username_target = input('[?] Enter Username Target : ')
                thread = int(input('[?] Enter Thread : '))
                cookies = {'sessionid': sessionid}
                def get_info_your_account():
                    url_info = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
                    headers_info = {
                        'Host': 'i.instagram.com',
                        'X-IG-Capabilities': '3wo=',
                        'Connection': 'close',
                        'Accept': '*/*',
                        'User-Agent': 'Instagram 10.0.0 (iPhone10,6; iOS 14_2; en_SA@calendar=gregorian; ar-SA; scale=3.00; 1125x2001) AppleWebKit/420+',
                        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-SA;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'X-IG-Connection-Type': 'WiFi'
                    }
                    cookiess = {'sessionid': sessionid}
                    req_info = requests.get(url_info, headers=headers_info, cookies=cookiess)
                    if ('user') in req_info.text:
                        email = req_info.json()['user']['email']
                        full_name = req_info.json()['user']['full_name']
                        biography = req_info.json()['user']['biography']
                        external_url = req_info.json()['user']['external_url']
                        phone_number = req_info.json()['user']['phone_number']
                        def endpoint_swap_normal():
                            url_swap = 'https://www.instagram.com/accounts/edit/'
                            headers_swap = {
                                'Host': 'www.instagram.com',
                                'Content-Length': '143',
                                'Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                'X-Ig-Www-Claim': 'hmac.AR0UHu-XW-qyqYL7XEn5SYV6Rsd4E_hONXLPiCxXCsZtQnmy',
                                'Sec-Ch-Ua-Mobile': '?0',
                                'X-Instagram-Ajax': 'f75a62fe716a',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Accept': '*/*',
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-Asbd-Id': '437806',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                                'X-Csrftoken': 's96wG0xAcwYppzkkLBJLh4osoHMrJFET',
                                'X-Ig-App-Id': '936619743392459',
                                'Origin': 'https://www.instagram.com',
                                'Sec-Fetch-Site': 'same-origin',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Dest': 'empty',
                                'Referer': 'https://www.instagram.com/accounts/edit/',
                                'Accept-Encoding': 'gzip, deflate',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Connection': 'close'
                            }
                            data_swap = f'first_name={full_name}&email={email}&username={username_target}&phone_number={phone_number}&biography={biography}&external_url={external_url}&chaining_enabled=on'
                            def get_id_username_target():
                                url_id = f'https://www.instagram.com/{username_target}/?__a=1'
                                headers_id = {
                                    'Host': 'www.instagram.com',
                                    'Pragma': 'no-cache',
                                    'Cache-Control': 'no-cache',
                                    'Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                    'Sec-Ch-Ua-Mobile': '?0',
                                    'Upgrade-Insecure-Requests': '1',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'Sec-Fetch-Site': 'none',
                                    'Sec-Fetch-Mode': 'navigate',
                                    'Sec-Fetch-User': '?1',
                                    'Sec-Fetch-Dest': 'document',
                                    'Accept-Encoding': 'gzip, deflate',
                                    'Accept-Language': 'en-US,en;q=0.9'
                                }
                                req_id = requests.get(url_id, headers=headers_id, cookies=cookies)
                                if (f'"username":"{username_target}"') in req_id.text:
                                    id_username = req_id.json()['graphql']['user']['id']
                                    def check():
                                        global attempt
                                        while 1:
                                            url_check_1 = url_original + '/api/v1/fbsearch/profile_link_search/?q=@'+username_target+'&count=20'
                                            req_check_1 = requests.get(url_check_1, headers=headers_original, cookies=cookies)
                                            if (f'username') in req_check_1.text:
                                                t788_whmy_1 = req_check_1.text.split('"pk":'+id_username+',"username":"')[1]
                                                t788_1 = t788_whmy_1.split('",')[0]
                                                if t788_1 == username_target:
                                                    attempt +=1
                                                    print(f'\r[1] Attempt : {attempt}', end='')
                                                elif t788_1 is not username_target:
                                                    url_swap_fast = 'https://www.instagram.com/accounts/edit/'
                                                    headers_swap_fast = {
                                                        'Host': 'www.instagram.com',
                                                        'Content-Length': '143',
                                                        'Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                                        'X-Ig-Www-Claim': 'hmac.AR0UHu-XW-qyqYL7XEn5SYV6Rsd4E_hONXLPiCxXCsZtQnmy',
                                                        'Sec-Ch-Ua-Mobile': '?0',
                                                        'X-Instagram-Ajax': 'f75a62fe716a',
                                                        'Content-Type': 'application/x-www-form-urlencoded',
                                                        'Accept': '*/*',
                                                        'X-Requested-With': 'XMLHttpRequest',
                                                        'X-Asbd-Id': '437806',
                                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                                                        'X-Csrftoken': 's96wG0xAcwYppzkkLBJLh4osoHMrJFET',
                                                        'X-Ig-App-Id': '936619743392459',
                                                        'Origin': 'https://www.instagram.com',
                                                        'Sec-Fetch-Site': 'same-origin',
                                                        'Sec-Fetch-Mode': 'cors',
                                                        'Sec-Fetch-Dest': 'empty',
                                                        'Referer': 'https://www.instagram.com/accounts/edit/',
                                                        'Accept-Encoding': 'gzip, deflate',
                                                        'Accept-Language': 'en-US,en;q=0.9',
                                                        'Connection': 'close'
                                                    }
                                                    data_swap_fast = f'first_name={full_name}&email={email}&username={username_target}&phone_number={phone_number}&biography={biography}&external_url={external_url}&chaining_enabled=on'
                                                    cookies_swap_fast = {'sessionid': sessionid}
                                                    req_swap_1 = requests.post(url_swap_fast, data=data_swap_fast, headers=headers_swap_fast, cookies=cookies_swap_fast).text
                                                    if ('"status":"ok"') in req_swap_1:
                                                        MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                    else:
                                                        print(req_swap_1)
                                                        input()
                                            else:
                                                def check_2():
                                                    global attempt
                                                    while 1:
                                                        url_check_2 = url_original + '/api/v1/users/search/?rank_token=12903591420_259F4009-F6C2-4217-9DCE-68E644E9173D&query='+username_target+'&is_typeahead=true&timezone_offset=10800'
                                                        req_check_2 = requests.get(url_check_2, headers=headers_original, cookies=cookies)
                                                        if (f'username') in req_check_2.text:
                                                            t788_whmy_2 = req_check_2.text.split('"pk":'+id_username+',"username":"')[1]
                                                            t788_2 = t788_whmy_2.split('",')[0]
                                                            if t788_2 == username_target:
                                                                attempt +=1
                                                                print(f'\r[2] Attempt : {attempt}', end='')
                                                            elif t788_2 is not username_target:
                                                                req_swap_2 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                if ('"status":"ok"') in req_swap_2:
                                                                    MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                else:
                                                                    print(req_swap_2)
                                                                    input()
                                                        else:
                                                            def check_3():
                                                                global attempt
                                                                while 1:
                                                                    url_check_3 = url_original + '/api/v1/direct_v2/ranked_recipients/?mode=raven&show_threads=true&query='+username_target
                                                                    req_check_3 = requests.get(url_check_3, headers=headers_original, cookies=cookies)
                                                                    if (f'username') in req_check_3.text:
                                                                        t788_whmy_3 = req_check_3.text.split('"pk":'+id_username+',"username":"')[1]
                                                                        t788_3 = t788_whmy_3.split('",')[0]
                                                                        if t788_3 == username_target:
                                                                            attempt ==1
                                                                            print(f'\r[3] Attempt : {attempt}', end='')
                                                                        elif t788_3 is not username_target:
                                                                            req_swap_3 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                            if ('"status":"ok"') in req_swap_3:
                                                                                MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                            else:
                                                                                print(req_swap_3)
                                                                    else:
                                                                        def check_4():
                                                                            global attempt
                                                                            while 1:
                                                                                url_check_4 = url_original + '/api/v1/users/search/?search_surface=comment_composer_page&query='+username_target
                                                                                req_check_4 = requests.get(url_check_4, headers=headers_original, cookies=cookies)
                                                                                if (f'username') in req_check_4.text:
                                                                                    t788_whmy_4 = req_check_4.text.split('"pk":'+id_username+',"username":"')[1]
                                                                                    t788_4 = t788_whmy_4.split('",')[0]
                                                                                    if t788_4 == username_target:
                                                                                        attempt +=1
                                                                                        print(f'\r[4] Attempt : {attempt}', end='')
                                                                                    elif t788_4 is not username_target:
                                                                                        req_swap_4 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                                        if ('"status":"ok"') in req_swap_4:
                                                                                            MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                                        else:
                                                                                            print(req_swap_4)
                                                                                else:
                                                                                    def check_5():
                                                                                        global attempt
                                                                                        while 1:
                                                                                            url_check_5 = url_original + '/api/v1/direct_v2/ranked_recipients/?mode=default_no_interop&show_threads=false&query='+username_target
                                                                                            req_check_5 = requests.get(url_check_5, headers=headers_original, cookies=cookies)
                                                                                            if ('username') in req_check_5.text:
                                                                                                t788_whmy_5 = req_check_5.text.split('"pk":'+id_username+',"username":"')[1]
                                                                                                t788_5 = t788_whmy_5.split('",')[0]
                                                                                                if t788_5 == username_target:
                                                                                                    attempt +=1
                                                                                                    print('\r[5] Attempt : {attempt}', end='')
                                                                                                elif t788_5 is not username_target:
                                                                                                    req_swap_5 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                                                    if ('"status":"ok"') in req_swap_5:
                                                                                                        MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                                                    else:
                                                                                                        print(req_swap_5)
                                                                                            else:
                                                                                                def check_7():
                                                                                                    global attempt
                                                                                                    while 1:
                                                                                                        url_check_7 = 'https://i.instagram.com/api/v1/users/'+id_username+'/info/'
                                                                                                        req_check_7 = requests.get(url_check_7, headers=headers_original, cookies=cookies)
                                                                                                        if ('username') in req_check_7.text:
                                                                                                            t788_whmy_7 = req_check_7.text.split('"pk":'+id_username+',"username":"')[1]
                                                                                                            t788_7 = t788_whmy_7.split('",')[0]
                                                                                                            if t788_7 == username_target:
                                                                                                                attempt +=1
                                                                                                                print(f'\r[6] Attempt : {attempt}', end='')
                                                                                                            elif t788_7 is not username_target:
                                                                                                                req_swap_7 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                                                                if ('"status":"ok"') in req_swap_7:
                                                                                                                    MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                                                                else:
                                                                                                                    print(req_swap_7)
                                                                                                        else:
                                                                                                            def check_8():
                                                                                                                global attempt
                                                                                                                while 1:
                                                                                                                    url_check_8 = 'https://i.instagram.com/api/v1/users/'+id_username+'/info/?from_module=direct_thread'
                                                                                                                    req_check_8 = requests.get(url_check_8, headers=headers_original, cookies=cookies)
                                                                                                                    if ('username') in req_check_8.text:
                                                                                                                        t788_whmy_8 = req_check_8.text.split('"pk":'+id_username+',"username":"')[1]
                                                                                                                        t788_8 = t788_whmy_8.split('",')[0]
                                                                                                                        if t788_8 == username_target:
                                                                                                                            attempt +=1
                                                                                                                            print(f'\r[7] Attempt : {attempt}', end='')
                                                                                                                        elif t788_8 is not username_target:
                                                                                                                            req_swap_8 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                                                                            if ('"status":"ok"') in req_swap_8:
                                                                                                                                MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                                                                            else:
                                                                                                                                print(req_swap_8)
                                                                                                                    else:
                                                                                                                        def check_9():
                                                                                                                            global attempt
                                                                                                                            while 1:
                                                                                                                                url_check_9 = url_original + '/api/v1/users/'+id_username+'/info/?from_module=direct_thread_info'
                                                                                                                                req_check_9 = requests.get(url_check_9, headers=headers_original, cookies=cookies)
                                                                                                                                if ('username') in req_check_9.text:
                                                                                                                                    t788_whmy_9 = req_check_9.text.split('"pk":'+id_username+',"username":"')[1]
                                                                                                                                    t788_9 = t788_whmy_9.split('",')[0]
                                                                                                                                    if t788_9 == username_target:
                                                                                                                                        attempt +=1
                                                                                                                                        print(f'\r[8] Attempt : {attempt}', end='')
                                                                                                                                    elif t788_9 is not username_target:
                                                                                                                                        req_swap_9 = requests.post(url_swap, data=data_swap, headers=headers_swap, cookies=cookies).text
                                                                                                                                        if ('"status":"ok"') in req_swap_9:
                                                                                                                                            MessageBox(None, f'Swapped : @{username_target}', 'Turbo Instgarm', 0)
                                                                                                                                        else:
                                                                                                                                            print(req_swap_9)
                                                                                                                                    else:
                                                                                                                                        print('\rStop]', end='')
                                                                                                                                        input()
                                                                                                                                        exit(0)
                                                                                                                                else:
                                                                                                                                    print('\r[Stop]', end='')
                                                                                                                                    input()
                                                                                                                                    exit(0)
                                                                                                                        for x15 in range(thread):
                                                                                                                            thread9 = threading.Thread(target=check_9).start()
                                                                                                                            [].append(thread9)
                                                                                                                        for x16 in []:
                                                                                                                            x16.join()
                                                                                                            for x13 in range(thread):
                                                                                                                thread8 = threading.Thread(target=check_8).start()
                                                                                                                [].append(thread8)
                                                                                                            for x14 in []:
                                                                                                                x14.join()
                                                                                                for x11 in range(thread):
                                                                                                    thread7 = threading.Thread(target=check_7).start()
                                                                                                    [].append(thread7)
                                                                                                for x12 in []:
                                                                                                    x12.join()
                                                                                    for x9 in range(thread):
                                                                                        thread5 = threading.Thread(target=check_5).start()
                                                                                        [].append(thread5)
                                                                                    for x10 in []:
                                                                                        x10.join()                                                
                                                                        for x7 in range(thread):
                                                                            thread4 = threading.Thread(target=check_4).start()
                                                                            [].append(thread4)
                                                                        for x8 in []:
                                                                            x8.join()                                                            
                                                            for x5 in range(thread):
                                                                thread3 = threading.Thread(target=check_3).start()
                                                                [].append(thread3)
                                                            for x6 in []:
                                                                x6.join()
                                                for x3 in range(thread):
                                                    thread2 = threading.Thread(target=check_2).start()
                                                    [].append(thread2)
                                                for x4 in []:
                                                    x4.join()
                                    for x1 in range(thread):
                                        thread1 = threading.Thread(target=check).start()
                                        [].append(thread1)
                                    for x2 in []:
                                        x2.join()
                                else:
                                    print('[-] Error Get Id Username Target')
                                    input()
                                    exit(0)
                            get_id_username_target()
                        endpoint_swap_normal()
                    else:
                        print('[-] Error Get Info Your Account')
                        input()
                        exit(0)
                get_info_your_account()
            else:
                print('[-] Error Login')
                input()
                exit(0)
        login()
    endpoint_original()
