import requests

import config


def video_url(*, session_id):
    session_details = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=('olegavakimyanov_m5hIDi', 'DvmrarPx3UCnLActiPnw'),
    ).json()

    return session_details['automation_session']['video_url']

