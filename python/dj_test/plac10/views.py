import requests, base64, json
from django.shortcuts import render, redirect
from django.urls import reverse




def index(request):
    return render(request,"plac10/index.html")



def auth(request):
    '''認証ページへリダイレクトさせる'''

    client_id = 'bzaJg7lYR3uk9lP7pf7VXg'
    client_secret = '2el89DlvtV1DsY8e515cVm1clsY1a3NX'

    if 'code' not in request.GET:
        print('get code')
        auth_url = 'https://zoom.us/oauth/authorize'
        response_type = 'code'
        # ngrokでlocalhostをSSL形式でアクセスできるようにする
        redirect_uri = 'https://XXXXXX.ngrok.io/zoom/auth'

        auth_href = auth_url + '?response_type=' + response_type + '&client_id=' + client_id + '&redirect_uri=' + redirect_uri
        
        return render(request, 'plac10/index.html', {
            'auth_href': auth_href
        })
    else:
        print('get token')
        auth_url = 'https://zoom.us/oauth/token'
        code = request.GET.get('code')
        grant_type = 'authorization_code'
        redirect_uri = 'https://XXXXXX.ngrok.io/zoom/auth'

        # basic認証用のコードを作成（client_ID:Client_Secretをbase64エンコード）
        client_basic = base64.b64encode('{0}:{1}'.format(client_id, client_secret).encode())

        # POST用のパラメータとカスタムヘッダを作成する
        post_payload = {
            'code': code,
            'grant_type': grant_type,
            'redirect_uri': redirect_uri
        }
        post_header = {
            'Authorization': 'Basic {0}'.format(client_basic.decode())
        }

        # # Exec POST
        response = requests.post(auth_url, data=post_payload, headers=post_header)
        response_text = json.loads(response.text)

        if 'access_token' in response_text:
            # 認証結果をセッションに保存
            request.session['zoom_access_token'] = response_text['access_token']
            request.session['zoom_token_type'] = response_text['token_type']
            request.session['zoom_refresh_token'] = response_text['refresh_token']
            request.session['zoom_expires_in'] = response_text['expires_in']
            request.session['zoom_scope'] = response_text['scope']

            return redirect('zoom_auth_complete')
        else:
            return render(request, 'plac10/index.html', {
                'auth_href': 'hoge'
            })



def auth_complete(request):
    '''認証完了ページ'''

    get_user_url = 'https://api.zoom.us/v2/users'
    access_token = request.session['zoom_access_token']

    # ユーザー情報の取得
    get_user_headers = {
        'Authorization': 'Bearer {0}'.format(access_token)
    }
    get_user_response = requests.get(get_user_url, headers=get_user_headers)
    get_user_response_text = json.loads(get_user_response.text)
    user_info = get_user_response_text['users'][0]

    # 部屋の作成
    create_meeting_url = 'https://api.zoom.us/v2/users/{0}/meetings'.format(user_info['id'])
    create_meeting_params = {
        'topic': 'Sample Meeting',
        'type': 2, # scheduled meeting
        'start_time': '2022-09-08 T 15:00:00',
        'duration': 30,
        'timezone': user_info['timezone'],
    }
    create_meeting_params_json = json.dumps(create_meeting_params).encode('utf-8')
    create_meeting_headers = {
        'Authorization': 'Bearer {0}'.format(access_token),
        'Content-Type': 'application/json'
    }
    create_meeting_response = requests.post(create_meeting_url, data=create_meeting_params_json.decode(), headers=create_meeting_headers)
    create_meeting_response_text = json.loads(create_meeting_response.text)
    
    return render(request, 'plac10/complete.html')