(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('宁城县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"150429","properties":{"name":"宁城县","cp":[119.318876,41.601375],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@KCG@K@MEICCE@EBC@EAOACCEGCE@E@EDIDGBIFKDA@KDKDOBC@E@IAIBM@MBKAK@QCA@MAIAMDMBO@I@IAMBE@MBUBIDKDOFIBIBI@IAS@M@I@KDIBEDEFIFABE@GEGMGCECI@G@K@GAC@C@GAKAK@KAMDMHGFABCBCDGHEHCFADKLINEHCJAJCHDFHPBF@DADABC@G@CAEAGCEACAIAEAGAMEWGMCI@KCI@ECAIAIAMGOECIAC@IAMAKBKDMDMDGBEBKFQFONKFGDIBAAC@MBOAIAGAIAI@KAOBQ@ODO@IBC@MF@@IBI@C@G@MAOCA@C@K@A@I@GBGDGBA@EAI@GCGEEAICE@E@OAK@I@K@SAICC@K@KAMAOCGAICCAEAA@ECCG@G@ECCACEEIEGAMAIBGDIFGFKHIJEHCDIJCJ@J@H@J@JAH@J@HJJJHFFBDAFCDGDGDIDCH@DBLFPBL@JEHEHEDIHEHKJKFMDGBIDIDMFOJQBIDCH@HDDJDL@J@HBHBDFBFFJHHDFHJJJBFAFCJEJEFCNEH@J@LJLHBBDN@DBBB@@@D@@DBBBDBBB@BDBBBB@B@B@DADA@AB@B@BB@@DBB@B@D@@@B@@B@@BD@BB@BDFFBD@@@@B@BBBB@@BABB@A@@F@D@BAF@HADABAF@DCBAD@DCFBD@DAL@BBB@BBF@N@H@HBHBF@B@DA@ADBD@J@LCDBDDJHFD@FBDHDDBD@@BDB@F@HAHAF@JCD@DBBDF@DDBDBDBAH@BDBNBDBBDBBBBF@DBBFFBDBBBAD@@@D@DA@@DGDCDC@EBAB@BHFHBDDF@@B@B@D@D@DDFCFAB@F@DBBBAJ@@@B@@B@B@@B@H@@@FB@@FBBFBDDBD@F@BBDAD@B@HBD@@@DAFBBDBDLDDBFBFBB@B@D@BB@DBJFBFDFB@BH@D@@@FAFAF@FAF@D@D@DBHDFDFFBDDBB@DBBBB@D@@BDBBBFBBBDBFBF@F@B@@BA@AB@BAB@B@DBB@B@@@B@@BB@B@@@B@@BB@BBB@B@BBBB@DBD@@@@B@BBBDBB@BB@@@BCF@BBBBBBB@@@BBD@@BDB@BDBF@BBBBBFBB@BBDB@@BD@BABADABBBAD@@@B@@FBHD@@@DAHAFHD@DBFCDB@@BD@D@BB@D@B@B@BDBFDD@D@DDHFF@DBB@F@BC@CJ@NADCF@DBFDJBB@DA@@DBB@@@BA@@BA@@B@@BB@@BB@B@@@@@BB@B@BBD@B@BBBB@F@B@@B@@@BBBBBB@B@B@B@BBB@BBDDD@F@BBB@@BDBDBDBBB@BB@@@FAB@B@BBDDDBB@D@BB@BD@BAB@B@@@FDDBF@@BD@@AB@FCDAB@B@B@B@B@B@B@B@@BB@F@FABAFAD@D@D@FAD@DABABADBDBBBD@B@F@B@D@B@BDD@BBF@DBDBDDD@F@FAH@FAJAD@HABAJAF@@BB@FAF@FBD@D@D@DDD@D@D@BBDBDBD@D@B@B@D@BBDBBBDDBBBBB@FBF@JFBFBBDBFBF@D@F@DBFBHDFDDBB@@@D@FBD@DD@B@D@BBBD@D@B@JBDBBCDCBAB@@C@@@C@A@CBAB@DBB@BBD@D@D@D@D@FBCDFAD@FADADADCFEBAEACABA@ABEAAB@DCB@BBFEGA@@DCB@B@H@F@DDB@DDB@BA@AB@BADABCBABADCB@@ABAFG@AB@@@FA@@BABBD@BBB@DBDBBBHFBBB@DDBBB@BBB@@@B@BADADAB@B@D@BBDBB@B@D@B@FABA@@D@BBB@@@DADADAD@D@B@H@@@B@D@B@B@B@D@D@D@F@F@F@HBH@J@DAH@D@BAHBD@DBHDD@FBHBB@DAB@D@D@BBDBD@@BDBJBDBDAF@@ABA@@BA@CDABAHADADBB@DBB@B@B@DABADAB@FCD@D@B@@@BAD@B@FAD@D@@BFBDBL@F@DABADABAB@FCBBD@FBD@DBBBDBBB@BB@FFDBDBBADADAFAB@D@AAACCCACAAACAC@A@A@@B@@ABA@AB@AA@CAA@E@A@A@@AA@C@AAI@CCGACCAAACCCAAAC@AAAAGCAA@A@AA@AAA@AA@A@A@AAAAA@C@A@@@@@@@C@ABADEBADCDADAB@B@B@BAFABAFAD@BADABABA@AAAAA@AAA@A@AAAA@@A@CAEAAC@@@AAC@@AA@@AAACAA@AA@ABABAB@B@B@D@DBB@B@B@BABADEBABCBC@A@C@A@ACAGCEACAAAAA@@@A@AAAACAAEC@AAA@CBC@A@ABABABA@A@ABAB@@ABAAA@@AA@A@@BCDABABC@ADADEBA@C@CAAAGBC@A@@@@@CBA@CAA@AA@CAA@@AA@@A@A@A@@@A@A@@BAB@BA@ABA@@@@@AAA@AAA@A@A@@DC@@@@@A@@@A@@@ABA@A@@B@@@B@B@@@B@BB@BB@@B@@@BB@@@BBB@B@@A@@@@B@@A@@B@@B@@B@@AB@B@@@@@@@@A@@@@@@A@@@@@@AAA@@A@@A@@BADABAB@BA@@@C@A@@BADA@@B@DCDABABCBABCBAAA@@@CBAB@@@DABAB@@@@AB@BAD@B@BADADABA@@@@D@H@D@D@BAB@@@@A@@BAB@@AL@B@BA@AB@BAB@@AFED@@@H@BAB@D@B@B@B@FCDC@@F@B@JCFABA@@BADI@@@A@@@@@AC@@@A@EAC@A@@@@ABAFCBABCB@DC@C@A@A@A@@AAAAAAA@AC@@E@ABABA@ABA@CBCB@@@AAAAA@AA@CD@@@A@A@@KB@@EB@BAB@@@@A@A@A@A@@AA@A@AAA@A@A@@@A@A@@@A@AB@@ABA@@AC@A@A@A@A@A@A@AB@@A@A@@A@@@@@ADC@@BABC@AB@BC@@BA@@A@@AA@A@@@C@A@@AA@@ABA@@B@BADA@@@@@AAAA@@@@@AAA@AA@@@A@@B@@@@@B@B@BA@@BB@@B@@A@@@AAC@@@@@@B@B@B@B@BC@A@A@AB@D@D@B@@ABA@@BA@@BABAB@B@@A@@@A@@@A@@@@AA@A@A@@@A@A@A@AB@@@@@D@BB@@@A@@@@@A@A@@BBBBBB@@@@@AB@BA@@@@DBB@@@B@@@@ABA@ABA@AB@BABABABA@ABAD@@ABC@@@A@@BC@A@AA@@@A@A@A@A@C@@@A@DGDKDK@KAE@GCEAAEAMCMGKIEIAMACAI@@BAAC@@@A@AB@@ABA@@@A@A@E@AB@BAB@@A@A@A@AAAAAAAA@A@CAC@CBCBKIIEIEMAOA@@GAOCK@M@GCAABGFED@LGLCJEFCAGCICCCAAAEACCBE@CFG@@DGHKDIDICICGAEGACAEDCDCFDH@FAH@FCBE@ECCCAKAGCGCEGCMAMAGAE@I@K@KBKBKAAAA@EEACAC@C"],"encodeOffsets":[[122102,42307]]}}],"UTF8Encoding":true});}));