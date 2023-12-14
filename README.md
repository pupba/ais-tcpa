# AIS 데이터 송신 프로그램, TCPA 계산 서버

AIS 데이터에서 RAW를 1개씩 1초마다 주선박 수신기에 전달하는 프로그램과 주선박 AIS, 타선박의 AIS를 수신하면 TCPA를 계산하여 테러대응 단계를 정하는 서버에 전송하는 서버.

## 설치 및 환경 설정

1. Git 저장소를 클론합니다.

```shell
git clone https://github.com/pupba/ais-tcpa
```

2. 필요한 종속성 설치

```shell
pip install -r requirements.txt
```

3. 서버를 실행

```shell
python otherShipAIS.py
python TCPA_server.py
```

-   현재 TCPA_server.py와 otherShipAIS.py는 Docker Container로 실행할 것을 가정하여 만들어졌습니다.
-   그냥 Python 코드로 실행 시키려면 TCPA_server.py를 수정홰주세요.
-   AIS 데이터는 선박의 식별번호를 유출 할 수 있기 때문에 제외하였습니다.
