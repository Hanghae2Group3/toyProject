# toyProject
#### 우분투에서 작업 예시
1. 프롬프트에서 클론 받을 폴더로 디렉토리 변경 \n
$ git clone (http link)\n
$ pip install virtualenv\n
$ virtualenv (env)\n
  // (env)는 본인이 편한 가상환경 이름 선택. 보통 venv 또는 env를 사용한다.\n
$ source env/bin/activate\n
  // 이 명령어를 친 후 디렉토리 상단에 (env)가 있는지 확인\n
$ pip install > requirements.txt\n
$ python3 crawlingBooksTest.py\n
$ ./run\n
  // 서버가 정상적으로 실행 된다면 인터넷 주소창으로 localhost:5000에 접속 후 정상적으로 작동하는지 확인\n
