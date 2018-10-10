(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('罗甸县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"522728","properties":{"name":"罗甸县","cp":[106.751589,25.426173],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@AACACEAG@GEGAGEAEECEACACBEECM@GCEEGECE@@@AAA@A@@@A@AAA@@@A@A@E@A@@@A@@@A@@@A@@@@@A@A@@@A@A@@@A@@@A@ABA@@@A@A@A@A@A@@AA@@@@BAAA@@@@@A@@@A@@AA@@@AAAAAAA@EAC@A@@AA@@@A@@AA@@@@@@@CA@@AAA@A@@AA@@@@@A@@A@@@@A@EIEEACAC@AA@@@C@A@@B@B@BBDFJFHFH@@@B@@BB@B@BB@@B@@@D@@BB@@@@@@@D@@@BAB@B@B@@@BA@AB@@@@A@@B@@@BAB@@@B@@@B@@ABA@AB@@A@ABA@@@ABA@@@AB@@A@@B@@@BA@@B@BA@@@@B@@AB@B@@@B@@@B@@@B@@@B@@@@@B@BA@@@@B@@A@@B@@@@AB@@@@A@@@ABAB@B@BA@@@@@@B@BA@@B@@@B@@AB@@A@@BA@ABABAB@@@DAB@BC@C@ABA@@B@@AB@B@BAB@@AB@BAB@@ABABA@AB@BA@AB@BC@ABAB@@AB@B@B@D@BAB@BA@@BABA@A@ABAB@BABA@A@E@ABA@ABAAAA@A@C@AA@@AAAA@A@CB@@ADABABADA@@B@B@B@BAB@B@@E@AB@B@B@BB@DAFBD@D@DB@@BD@BBBB@@BB@@BB@BBBB@@BB@@BBB@PHTHBBVNRTBLIJGLAJ@F@HAJGTERAN@H@FALABEL@BIL@BADAB@@CDEJEH@@GLOLK@OAOBABA@A@ABA@A@ABA@A@AACB@@AB@B@@AB@D@BAB@B@BAB@B@DBB@B@B@B@@BB@BBJ@F@D@B@BAD@BEDDBFBHB@@BB@@@BBBB@@BBB@B@BABCB@BABAB@B@B@B@B@@AJAB@HADABADCBE@CBCDAB@@A@A@A@A@AAA@A@A@@BBB@@BB@B@B@@@@ABA@A@@@A@C@A@AAA@A@A@AAAAAAA@A@E@CBAB@@FBDBDBD@BB@@BB@BB@@B@B@BA@@@CBA@@@@B@@BB@@@BBB@@BB@BB@FABAB@BAB@B@B@B@@@BBBBB@@BB@BB@BBB@BBB@@@BBBBBBBB@@@DBBD@B@D@B@@@B@BA@@B@B@BBBADCDAD@BCBABAB@D@@ABAB@@ABC@C@AAA@AAA@AA@@A@A@@BAB@@AD@BBBBBBBBBDB@BBBBB@BABA@@BA@A@C@@AA@A@AB@B@BB@@BBB@@@BAD@BB@A@@DBDBBJ@FADB@BCDIDED@D@HDDDDB@BBB@F@D@DAF@B@D@FLLTP^@@BDDXEVARHPLLHH@BLLVTPPFR@BB@DNDJPVDR@B@FBJJDDBNFPF@@B@LJ@B@BBB@BDDBBDBD@BF@FHJF@DBDBHNBBLZBNBFDRBJDF@B@@FHHDPCPKPONQRULI@@NIFAFAL@HLDNCFAFABELKNGJAH@F@FJHLDJB@@H@HG@AJOHOFMHMHINGPEHGFIFEFAFAD@@APERONMHKBOAQ@KDMFIFEHKDERMVS@AVGTG@@NER@REXGRG@APARDJJBBJNJJJJFFBDBN@F@HAD@DDJHFHBD@DBJDFBBBBA@@VAR@@@B@PDJFPBFAD@HCBAB@DA@@B@DAHCHCLCFCFAHAHEJEHC@@@@VK@@FABADCDAHEJGFM@KEKCGACGMEGAG@C@CB@DCB@FA@@B@D@B@TF@@B@DBLBDDB@HDDBRDV@PCLCFCD@@@@ABA@A@CBA@CA@@ABC@AAAAA@AAA@A@CDEDC@A@@@ACAA@@ABA@@B@B@D@FA@@@A@@AABA@@BAB@@C@E@CCE@AACCAEEEAAAC@CAAAEAAAC@A@A@A@A@C@EAA@ABC@CAA@A@AAA@E@CA@@AAAAA@E@CAA@A@@@AA@@A@CAAAAA@@@AB@@ABA@A@A@A@AAA@AAAAA@@@ACACAA@@A@@@AAA@C@C@@@A@@AC@CAA@C@A@@@AAAAEAACA@C@A@AAC@A@@@A@ABAAAAEAAA@@@A@A@@BC@CBABA@@B@@C@ABA@C@@@A@@AA@AAACA@A@CACBCA@@AAA@AA@AC@AA@AAA@A@AB@@A@@@A@@BABABA@A@@BA@ABA@C@A@C@A@CAA@A@@@A@C@AA@@A@ABA@ABAB@FAB@B@BABA@C@A@A@C@A@A@CBC@@@A@ABA@ABA@A@A@A@A@C@AAA@C@A@A@CB@@CDA@@BC@ABA@ABABA@C@ABCBAB@@AB@D@@AB@D@@@D@D@D@B@D@B@@@B@DAD@DA@ABA@CBABE@@@C@CACAC@AAA@C@AAE@ABC@C@C@CACCG@A@AAE@C@C@AB@BE@E@ABABAB@B@@A@A@A@@CAAA@A@C@ABCBCBC@A@GBC@CA@@@@@AA@AA@AAAACAA@A@A@A@CA@@AAAAC@CCA@CAAAAAAAAA@AAA@A@C@AB@@ABABABABADC@@DABCBA@@@@@A@@@A@@AAAAA@@@A@@@C@A@A@A@AAC@CAA@AAA@CAAACAAA@@A@@BABAB@@CDQJCBIFEBG@EBGBIBG@C@GAE@EA@AEAECA@CCCCACCCAAACCC@CACAC@CAG@G@CACBC@CAA@@@CBA@E@C@C@AAC@CACCCACAAA@AACAAACAC@@@C@I@ODEDE@EBEAA@GBC@AAEAGEGAC@ECG@A@A@@@@@A@@@AB@AA@A@@@AAA@AACA@@C@AAA@KAOEKAK@A@G@KHGBADEFCBABCBAAABC@ICECCACEGEAAC@G@GEAAKICAC@A@A@A@E@KHEFEHIHIDE@C@IBGAC@A@EAMGEAGCKAEAI@KCECEEEGAGDIBM@GAEAEACEACCCA@@"],"encodeOffsets":[[109191,25730]]}}],"UTF8Encoding":true});}));