from flask import Flask, request
import math
import requests
import os
tcpa = Flask(__name__)

# 두선박간의 거리 계산
address = os.environ.get('SEND_IP')
port = os.environ.get('PORT')
# address = "localhost"
# port = "5003"


def haversine_dist(lat1, lon1, lat2, lon2):
    R = 6371  # 지구의 반경 (단위: km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def calculate_tcpa(lat1, lon1, sog1, cog1, lat2, lon2, sog2, cog2):
    # 두 선박의 거리 계산
    distance = haversine_dist(lat1, lon1, lat2, lon2)

    # COG 값을 라디안 단위로 변환
    cog1_rad = math.radians(cog1)
    cog2_rad = math.radians(cog2)

    # 두 선박의 상대 속도 계산
    relative_speed = math.sqrt(
        sog1**2 + sog2**2 - 2 * sog1 * sog2 * math.cos(cog2_rad - cog1_rad))

    # TCPA 계산
    time_to_closest_point = distance / relative_speed

    # 분 단위로 변환
    tcpa = time_to_closest_point * 60

    return tcpa


@tcpa.route('/tcpa_endpoint', methods=['POST'])
def tcpa_endpoint():
    global address
    global port
    # 주선박 서버로부터 받은 records 값을 로드
    records = request.get_json()

    # own, other 값 설정
    own = records['own']
    other = records['other']

    # TCPA 계산
    tcpa = calculate_tcpa(own['Latitude'], own['Longitude'], own['SOG'], own['COG'],
                          other['Latitude'], other['Longitude'], other['SOG'], other['COG'])

    response = requests.post(
        f"http://{address}:{port}/decision", json={'tcpa': tcpa})
    return "success"


if __name__ == '__main__':
    tcpa.run(host='0.0.0.0', port=5002, debug=True)
