/set isize=2
/set lwgo=0
/set status_pad=
/set uciekl=**
;---------------
/set skd=*
/set kkd=Cwhite
/set szm=*
/set kzm=Cwhite
/set saw=***
/set kaw=Cwhite
/set sbm=-
/set kbm=Cwhite
/set exits=n ne se
/set specowanie=S+

/set pad=
/set sgrupapad=This is a test
/set status_height=2

/def -i status_set=\
        /eval /set padwidth=$[expr(columns()-79)]%;\
        /eval /set grupawidth=$[expr(columns())]%;\
        /set status_fields=\
          'k' skd:1:%{kkd} :1 \
          'z' szm:1:%{kzm}  :1 \
          saw:3:%{kaw} :1 \
          specowanie:3:BCcyan :1 \
          'asd':9:BCcyan :1 \
          uciekl:2:BCred :1 \
          exits:46:BCwhite \
          sbm:1:%{kbm} \
          pad:%{padwidth} \
          @clock:5 \
          sgrupapad:%{grupawidth} \

/def -hRESIZE hook_screen_resized=\
   /eval /set padwidth=$[expr(columns()-79)]%;\
   /eval /set grupawidth=$[expr(columns())]%;\
  /status_edit pad:%{padwidth}

/status_set
