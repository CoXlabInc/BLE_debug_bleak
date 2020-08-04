1. read_test.py
 => read_test.py "SERVICE_UUID" "CHARACTERISTIC_UUID"
 => ex) read_test.py "f64f0000-7fdf-4b2c-ad31-e65ca15bef6b" "f64f0100-7fdf-4b2c-ad31-e65ca15bef6b"

2. write_test.py
=> write_test.py "SERVICE_UUID" "CHARACTERISTIC_UUID" "WRITE_VALUE" NEED_RESPONSE
=> ex) write_test.py "f64f0000-7fdf-4b2c-ad31-e65ca15bef6b" "f64f0100-7fdf-4b2c-ad31-e65ca15bef6b" "Hello_World" 0

예외 상황
0. argument를 일정 개수 이상 안넣어줬을 때 : Insufficient argument!

1. discover은 끝났는데, Coxlab Inc, Inc.를 찾지 못할경우 : Sorry, There is No Coxlab, Inc.

2. Coxlab Inc를 찾았고, 연결하는데 Timeout 때문에 연결 못한 경우 or 코드상의 문제 : not Connect T.T please restart!!

3. Coxlab Inc를 찾았고, 연결하는데 해당 Service_UUID가 없는 경우 : There is No Service : Service_uuid

4. Coxlab Inc를 찾았고, 연결하는데 해당 Characteristic UUID가 없는경우 : There is No Characteristic_UUID : characteristic_UUID
