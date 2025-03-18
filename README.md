# Image to ASCII art Convertor
#### Pre-requisites
- Make sure you have Pillow (built upon PIL) library installed
  - `pip install Pillow`
  - `pacman -S python-Pillow` for Arch systems
#### Run
- Run using `python path/to/ASCII.py`
- It will ask for the path to the image
  - `path/to/image.extension` and hit Enter
- It will ask what to name the .txt file which will contain the ASCII art
  - `file-name.txt` and hit Enter
- The .txt file will be created within the same directory as ASCII.py 
#### Example Output
`                                                                                          -----------------------                                                                   
                                                                                    -----|-oooooocccccccccccccoo|-----                                                              
                                                                                ---||ooooocccccccccccccccccccccccccoo|---                                                           
                                                                             --||oooooccccccccccccccccccccccccccccccccco|--                                                         
                                                                           -|ooooocccccccccccccccccccccccc::---:::::cccccc|--                                                       
                                                                        --|oooccccccccccccccccccccccccc--------------::ccccc|-                                                      
                                                                      -|ooocccccccccccccccccccccccccc----9W---WWW99?o--:::ccc|--                                                    
                                                                    -|ooocccccccccccccccccccccccccc-|?9WW||c||----|o|9|--:::ccc|-                                                   
                                                                  -|oooccccccccccccccccccccccc:::c||99W-|occ-c|-|occ||9||-:::::c|-                                                  
                                                                 |ooocccccccccccccccccccccccccccc:|99W-|ccc||-ccc--cc|-9||::::::c|                                                  
                                                               -|ooccccccccccccccccccccccccc::cc:||99|-ccc|9W|--|?|o::|99|:::::::|-                                                 
                                                        ------|oocccccccccccccccccccccccccc:::::::|-|-cc:|9W9W9?99||::|?9|::::::::|-                                                
                                                     --|?ooooocccccccccccccccccccccccccc::::::::::||-?o-|9999999999|::-||:.::::.:::|                                                
                                                   -|oooooccccccccccccccccccccccccccccc:::::::::::::|--------------|cc-|:.::.....::|-                                               
                                                  |?oooccccccccccccccccccccccccc:cc::::::ccccccccccccccccccccoooo-----:..:::.....::||                                               
                                                 |ooooccccccccccccccccccccc::::::::ccccccccccccccccccccccccccccccccccccc:::.......::|                                               
                                                 |ooocccccccccccccc:c:::::::::ccccccccc----------ccc:::::::::::::::cccc--ccc::....::|                                               
                                                |oooccccccccccc:::::::::::ccccccccccc---:::.::..-::::::::::::::.......::::::::::::::|                                               
                                                |-ooccccccccc::::::::::ccccccccccc-c-:...---- ....-ooooocccccccc::::............::::|--                                             
                                                 |----------::::::::---:-----ccccoo|.-------------|-ooooooooooooo--..    ............:|-                                            
                                                -|9-99WWW9----:::::....|??-----????---oo???????oc--|oooooooooooo|:.-----  .::..........|                                            
                                               |WWWW-----W#W||-:::::::||WWWWWW9999??????----?--o??ocooooooooooo|:--:ccc:- |c:..........|                                            
                                              |WWWW99????99WW||::::::::|WWWWWWWWWWWW99--occo--9??o???????ooooooccooooooo|-||:........:-|                                            
                                              |WWW9???9999?999|c:::::::|-WWWWWWWWWWWW|c-----c|WW9??????????ooo----?oocooocc|...------|                                              
                                              |WWW9999999???99||:::::::||WWWWWWWWWWW|c|:||||o||#WW?9999999???|---c-??ocoooo|.-|                                                     
                                              |WWW999W9?oo???99|::::::::|WWWWWWWWWW||c|.--.||||#WW9WWWWW9999|||:|c|???ooooo||||                                                     
                                              |-WW99WW???999999|::::.--|9WWWWWWWWWW||o|-:::|o|9#WW9WWWWW999|:||:|c|?9?oooooc|?|                                                     
                                              ||9WWWW99?999999W|::::||9WWWWWWWWW--W9|--occco-|WWW99WWWW9999|----|o|?9?oooo|:||| ---------------                                     
                                               |-9WWWW9999WW99W||--||WWWWWWWWW-|-|--99------9WW999WWWWW99999-------9??oooo|.||-|9W9WWWW9WWWWWW|------                               
                                                |-9WWWWW9999WWWWW--|WWWWWWWWW||...|----W999W9999WWWWWWWWWWWWWWWWWWWW99?--||.|##WWWWWWWWWWWWWWWWWWWWW|----                           
                                                 |--9WWWWWWWWWWWWW##WWWWWWWWW|......:-------WWWWWWWWWWWWWWWWWWWWWWWWWWWW99||--WWWWWWWWWWWWWWWWWWWWWWWWWW|-                          
                                                   |--99W------WWWWWWWWWWWWW||..........:-------WWWWWWW#####WWWWWWWWWWW99||.|---9999999999999999999999999|-                         
                                                     |--------||WWWWWWWWWWWWW|-...............||WWWWWWWW###WWWWWWWWWW99999|. |c---999999999999999999??????|                         
                                                        |:::::.|-WWWWWWWWWWW99|--..............|-WWWWWWWWWWWWWWWWWW99999??|. |..:|--?9999999999999????ooo?|                         
                                                       ||::..::||-WWWWWWWW999999|----..........||-WWWWWWWWWWWWWWW99999????|  |.::.|-?????9999999?????ooo??|                         
                                                ------|?|c......||-W99999999999999?o|-..........||--99WWWWWW99999999?????|.  .::::.|o????????9??????ooo??o|                         
                                            ---||ooooooooc:.--...||-99999999999999999|--..........|-----99999999??????--|--.........|????????????????o???o|                         
                                        ---|?oocccccccccc:::::...-||--9999999999999999|c.------.... .-----------?-----:--o|:........|???o????????????oooo|                          
                                     --|oooccccccccc::::::::::::::|.||--99999999999999|o:coooo--- ..  --..:---cccc:---|o-|:.........|??oo???????????????|                           
                                   -|ooocccccccccc::::::::::::::::|c:.|---??99999999999|-|---ooo----------- ---cocccoo?-|........--|???oo?????????????99|-                          
                                 -|oocccccccccccc:::::::::::::.:::||c:...----??999999999|- .:-------------:-coooooo?---:....:-----o???o?????????????????||                          
                                |oocccccccccccccc::------:::::.:::||c:::...:---????999???|--.......::::.--co?oooo?--c:..::::--o?????-----??????????ooooo|                           
                               |ooccccccccccccc-------------------||-------..:----????????|---::....----co??oo?--c:..:::---|-------|    |--------------|                            
                              |ooccccccccccc----9WWWWWWWWW9-------------------|-:c---????????o-------o?????---c:.:::---||                                                           
                              |ooccccccccc-||W##WWWWWWWWWW#########WW#####WWWW9|---:c----?????????????-----::..::--||                                                               
                              |occcccccc-||###WWWWW#################WWWWWWWWWWWWW9||-.::---------------::|...:--|                                                                   
                              |occccccc||W##WWW#############WW#######WWWWWWWWWWWWWWW|-.......:::::.......|.:-|                                                                      
                             -|ccccccc||###WW##################WWW##WWWWWWWWWWWWWW999|-:::........  .....|:||                                                                       
                          --|???occcc||###WW#########WW########WWWWWWWWWWWWWW99999999?|-::::......  ......|                                                                         
                        -|???oocccccc|W#WWW########WW########WWWWWWWWWWWWWWWW99??9999??|-----------.......|                                                                         
                      -|??oocc:----c||#WWWW##############WW###WWWWWWWW9WWWWW9999??9999??|:::::::::.::..---|                                                                         
                  ---|ccoocc----cc|-||WWWWW###############WWW###WWWWWW9?99999999???999???|.........::-|co||                                                                         
               --|?ooooooc--cccc:::|||WWW9WWWW###########WWWWWWWWWWWW99???999999??o?9???o|........|:|?ooo-|-                                                                        
              ||?ooooooc--c:ccc::::::|-W99WWWWWWWW#######WWWW99WWWWWW999?o?9999????oo?ooo:........:|o?ooco||                                                                        
             |oooooocc-c:::cc:::::::::|-999WWWWWWWWWWW##WWWW99??99W99999??o?99???ooococoo|.......|||ooooo?||                                                                        
            |ooooocc--::cccc:::::c:::::|--99999WWWWWW-WWWWW999?o?999999???ooo??oooocccooo|...... ::|----o||                                                                         
           |cooocc:|:::ccco::ccc:::::::::c----99999???-9WW99999?o--99???ooo-cooccoooooooo|....... .....||                                                                           
          |coocc::|:::cc:cc:::::::::::::::::c---99??ooo?999999??ocooooooo--|-oooooooooo-|. .......  ..|                                                                             
         |:coc::::|::c::::::::::::::::::::::..:----?oooo9999??ooo-:------.. .---------:.. ............|                                                                             
         |:cc:::::|:::::::::::::::::::::::::.....:c----------o---.......   .  .......   .. ..........|                                                                              
         |::::::::|::::::::::::::::::::::................::::::..............        .. .. ...  ....||-                                                                             
         |cc::::::|:::::::::::::::::::::............................................................::|-                                                                            
         |-cc::::||:::::::::::::::....................................................................:|-                                                                           
          |--c::::|:::::::::::::......................................    ..............................|--                                                                         
           ||-cc::|:::.:....................................................          ..................::|-      -----------                                                       
             |----c|::................................ ..-----............  ...................:.:.::::::::|-----|----9-9W-W|----                                                   
                |-----..............................----|   |---------.....................::::::::::::::::::|99?????ooo??---99W|--                                                 
                     |--........................---||               ||--...................:::::::::::::::---o--oocccccccccco---99|--                                               
                       |---................----|                       |--..........::.....:::::::::::::---:ccccccc:::cccc::::co--?9|-                                              
                          |---------------|                             ||-..........::...::::::::::.:--:::::::::::::::::::::::::c---|-                                             
                                                                          |--........::::::::::::::::--::::::::::--:::::::.........:--|-                                            
                                                                            |-........::::::::::::::|c:::::::::ccoo:::...............|||                                            
                                                                             |::..:.::.::::::::::c--c::::::::ccc|-|:........---------.||                                            
                                                                             |-::.::::::::::::::c|:cc:::::::::::::......----cccooooocc||                                            
                                                                              |-::::::::::::::c-|:cc::::::::::::.....----oo?ooocccccccc|-                                           
                                                                               |-:::::::::::::|::cc:::::::::.......---o??ooccccccccccccc|                                           
                                                                                |::::::::ccc-|:::::::::::::......--co?occcccccccccccccc|                                            
                                                                                |-::::::::--.::::::::::........--ooooccccccccccccccccc|                                             
                                                                                 |:::::---..::::::::........--cooocccccccccocccccccc-|                                              
                                                                                 |c::--:..::::::..........--coooccccccccccccccccc--|                                                
                                                                                 |:c::::::::::::.......--:cooocccccccccccccccc--|                                                   
                                                                                 |---c:::::::::::.....:co-occcccccccccccc----|                                                      
                                                                                   |?c::::::::::..---:cc::::::::::::::c-|                                                           
                                                                                   |?c::::::::.---coocc:::::::::::::--|                                                             
                                                                                   ||-c::::..--co-occcccccccccccc--||                                                               
                                                                                    ||-c::.-co--oc::cccccccccc--|                                                                   
                                                                                      |----oooc::ccccccc::---|                                                                      
                                                                                         |--c:::::::-----|                                                                          
                                                                                           |-------||                                                                               `
