(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('阳新县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"420222","properties":{"name":"阳新县","cp":[115.215227,29.830257],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@@G@EAG@G@G@EB@@EAC@A@C@ABEDABGBCBGDMFCB@@C@E@CACAC@ABCB@BAB@B@D@BDDDBBBBH@@@B@BBB@@D@B@B@@@@@B@@BABB@@B@@@BABAB@@BBDH@D@BABCDIFCDCBA@A@AA@@AAAAAAA@A@E@C@ABCBA@AAA@@A@A@@A@CAA@A@C@A@CCAAA@A@A@A@A@A@A@A@@@ABE@@AAA@AAA@@A@@BC@ABA@CA@ACC@@A@A@A@AD@@AB@BABABC@@@CDAB@@@@A@A@A@AA@@AB@@ABCDADADAD@BC@GBA@A@@BA@ABAD@BABA@A@A@@@@AACBCACA@A@@AAAC@CAA@C@E@ABABC@A@AAEE@CAECCEAE@UBGDI@GBEHCBEBCDDT@FBF@FEBG@IBGBK@C@C@C@EBAF@HDHAFKLGJEDADAJ@F@D@DDJBLBHADABGHCDEHCJ@D@XADCF@@EHABAB@BCFA@AFADAF@@EBWDOBC@@BAB@BBJ@DCH@BCD@B@B@D@B@HEJEHABA@CBCBC@G@G@ABEBCBA@I@C@EAE@K@ABA@@@A@A@A@@C@A@@@@A@E@A@A@A@@@ABADC@A@EBA@C@A@A@C@A@A@A@@DCBCBE@CBG@AACAGA@ACBEFQLGHEFADAD@FBFJLBJBL@JFHFJ@FAFCHAFBDBLBNAP@HABC@O@I@GBCBABBL@HBDDHBHBBAHBDBJBJ@F@DBDDD@BBB@PBBBBB@PCD@JAL@FCHE@EBCDEDAFAD@FBD@BDDD@B@D@@B@LADAB@HAD@D@REJA@ABA@C@A@AJ@LCDARENALAJAZC@@TC\\ENCDCFAJAD@H@D@FAD@FBD@BBB@D@D@B@B@DBFBD@@@@BBBB@BBFBFDBBFBBF@B@DAH@@AL@D@@@B@B@@@B@B@@BB@B@@B@@@BB@@BBDB@B@@@B@@@@A@@BB@@@@D@@@B@@A@ABA@@B@@@BB@@B@B@B@D@FAHBH@DBBBDDFLHDBDBLHFFJFFDBF@DBHBFAFBHBFHFRBPDJ@L@JBDD@@B@D@FADAB@B@B@BBBDBBDDDD@BD@@@@B@@@BA@@@AAAB@@@@@D@@@D@F@@@BAB@@@D@B@@BBBD@D@@@@BBB@D@B@FEFAB@@ADAB@@@B@D@B@B@BB@@@FB@@BB@FBB@DBBB@DBDBB@@DAB@BAB@B@FDFF@BDFFFB@BBBB@BBD@B@@CBC@EBA@GFGLIPGFGLADCDCFCFADABEJ@BADAFENCJAFBFCFBH@BBB@DDDJDJDN@@@@@LAJCD@FAHCD@D@H@J@H@HAJCDCFCJAJAJBB@L@LAHBJBB@LDJFHDHFHFJJBDDFBD@DCF@D@DDDDBD@DBDBDADBB@D@H@B@DADAB@BAB@@BDBBB@@B@BAF@@B@@B@B@@DB@@@HBD@BA@@B@@A@A@ABEBC@@@AB@B@B@BBB@@B@@@@ABBB@BBBDD@@BDBBBBB@@BB@@B@B@@DBDDBDB@B@DAD@F@B@D@FAB@@@@B@@@@ADA@CBAB@B@@@BDB@@BBBD@DBDBBDAHCFAH@HANO@@BA@@BCJI@ADCBABA@@BAFGFGBAFGFGDGFI@@JMHOBIDEBI@CBG@A@G@EBA@IAG@E@G@CBEBGDGDGBADEFC@@FEFCFCHCDADCFCFCDEFCDEHMJQFIJOBAHKJGFEHCNEJEDI@GAGAGCI@KBGBENMHEHAHCHEFGFEDIDIDMFGFGFEDCFEHCHED@DCLE\\MdGLA@ACI@A@@@AAA@@@A@@@@AA@@@E@AAA@ABCBA@@@@@@ABA@ABOCEACAC@EAGCACGE@@EG@GAIAEAEBG@CCGCGCGAIAGBGFK@E@@DUCEEEGE@AGCGCEEICIEGECCCA@AEEAAGGGGGEAECCCECECCCCICGE@@@A@AGG@@@@A@@@C@AB@@AAA@EECACA@@ICAAEEMMAAAAEA@ABA@AAA@AAAAAAA@@ABCDCBA@@@CA@@A@@@ABABA@AAAACAEBC@C@OEGCCGEEA@C@AAA@AA@@A@@@ABA@@A@@@@A@@@ABCBA@C@@@@@@C@A@@A@CA@@AC@@CCA@AE@@C@A@@@AAA@CA@AEG@AA@@@A@@BA@@BEDA@@@G@EBGHADCFALBHFH@J@HAHEBGBI@MAKCMAIAGCKDIBGBK@MAO@IBGAICG@ABCBIDE@A@I@I@GBIDEFIJCJCDCFKHGFK@EAECAACEAEAE@EBCBGBAFEDCHEFAF@JAFBF@BAB@D@HCBC@A@E@CAGCC@@AAAAA@A@A@@AAAAAAA@A@A@ABC@A@A@AAC@@@A@C@@@AB@@@B@BAB@@A@AAAAAAAA@AAAA@ACE@A@ABABA@@BA@@@@@AA@AAIAGA@AA@BA@ADAB@B@DADADABAB@B@@@@@B@@@@@@@B@@@@BD@BBBBFB@BB@F@H@HBFBFBFBFAHABCB@BE@E@@@@A@A@AA@@A@@AA@@@@@AB@@@@A@@@@@A@@@@@@A@@A@@@@@GCA@AA@@AA@A@A@A@AB@@A@@@A@@@@@AA@A@@@CA@@@@@@@@@A@@@A@A@@@@BABCB@@A@@@@@E@AB@@AEIAI@AAE@I@G@IBGAGDIFI@ICCCC"],"encodeOffsets":[[117918,30219]]}}],"UTF8Encoding":true});}));