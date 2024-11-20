# 파일 레벨 백업(File-Level Backup)
<br><br>
파일 레벨 백업은 대상의 파일 시스템과 운영체제를 보호합니다.   
이 백업은 포함할 파일과 제외할 파일을 선택할 수 있습니다.   

파일 레벨 백업은 물리 대상을 지원하며,   
가상머신(VM)의 경우 호스트 레벨 백업 또는 파일 레벨 백업 중 하나를 선택할 수 있습니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; • 호스트 레벨 백업 : 파일, 가상 하드웨어, 애플리케이션 데이터 모두 백업을 수행합니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; • 파일 레벨 백업 : 가상머신(VM)을 물리 대상으로 간주하고 파일 및 애플리케이션 백업을 수행합니다.
<br><br>

###### ▪ 파일 레벨 백업 요구사항
※ 파일 레벨 백업을 위해서는 대상 시스템에 Unitrends 에이전트를 설치해야 합니다.<br>
에이전트 설치 절차는 운영체제에 따라 다르므로, 자세한 내용은 [Unitrends 에이전트 설치 가이드]를 참고하세요.<br><br>
에이전트 설치 후, [에이전트 기반의 백업 대상 추가] 페이지를 참조하여 대상을 유니트렌드 어플라이언스에 추가한 다음,
백업 정책을 생성합니다.

<br><br><br>

###### ▪ 파일 백업 정책 설정 단계
(1) Jobs → +Create Job 버튼을 클릭하여 Backup을 선택합니다.<br>  
■ 사진 첨부 필요

(2) 좌측 INVENTORY 영역에서 토글을 열어 백업 대상을 선택합니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; - 백업 대상을 등록된 이름으로 찾으려면 아래 <b>Search</b> 필드를 사용하세요.<br>
&nbsp; &nbsp; &nbsp; &nbsp; - 기본적으로 유니트렌드에 등록된 대상만 나열됩니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; - <i><b>What do you want to backup?</b></i>에서 백업 유형을 선택합니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ex) File Level, Image Level, VMware, SQL 등<br>
■ 사진 첨부 필요

(3) 우측 JOB INVENTORY SETTINGS의 Edit을 눌러 포함하거나 제외할 백업 경로를 선택합니다.<br>
(대상 시스템 전체를 백업하는 경우, 이 단계는 넘어가도 됩니다.)<br><br>
&nbsp; &nbsp; &nbsp; &nbsp; • <b>Inclusion</b> : 백업받을 파일 및 폴더를 선택하는 곳입니다. 이외 경로는 자동으로 제외됩니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 기본적으로 체크되어 있는 Protected all volumes and files(recommended)를 체크 해제한 후, 활성화 된 <b>Browse</b>를 눌러 선택합니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; • <b>Exclusion</b> : 백업에서 제외할 파일 및 폴더를 선택하는 곳입니다. 이외 경로는 자동으로 포함됩니다.<br>
&nbsp; &nbsp; &nbsp; &nbsp; • <b>Advanced</b> : 추가 설정을 하는 곳이며, 보통의 경우 따로 설정할 부분은 없습니다.(Windows 대상 제외)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - 정책 대상이 Windows인 경우, <br>
■ 사진 첨부 필요

