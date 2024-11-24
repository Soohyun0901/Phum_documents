# Widnows 에이전트 설치

Windows 대상을 백업하려면 해당 Windows에 에이전트를 설치해야 합니다.<br>
이 에이전트는 <b>파일 백업(File-Level), 이미지 백업(Image-Level) 및 애플리케이션 백업(application)</b>을 실행하는 데 필요합니다.<br>

###### 에이전트 설치 전 요구사항
Windows 에이전트를 설치하기 전에 아래 요구사항을 충족해야 합니다.
1. Unitrends 어플라이언스와 에이전트 버전 호환성
* 10.8.1 버전부터, 에이전트 설치 프로그램보다 Unitrends 어플라이언스 버전이 더 낮을 경우 오류가 발생할 수 있습니다.
2. 관리자 권한
* 에이전트를 설치하려는 사용자는 <b>Windows 관리자 권한</b>을 가지고 있어야 합니다.<br>
3. 디스크 여유공간
* Windows 시스템 드라이브(일반적으로 C:\)에 <b>약 1100MB의 여유 공간</b>이 필요합니다.<br>
4. Windows VSS(Volume Shadow Copy Service)
* Windows VSS framework가 설치되어 있어야 합니다.<br>
5. VSS Writer 요구사항
애플리케이션 백업을 위해 다음 VSS Writer가 필요합니다.:<br>
* Exchange : VSS Exchange Writer
* SQL Server : VSS SQL Writer
* Hyper-V : VSS Hyper-V Writer